/**
 * sql_exec — read-only MySQL exploration tool for the BEAVER text-to-SQL experiment.
 *
 * Loaded by the orchestrator via `pi -e harness/pi_extension/sql_exec.ts`.
 * Connection details and caps are injected through environment variables so the
 * agent (which only sees the tool's text results) never touches the repo.
 *
 * Env (set by the Python runner before spawning pi; MYSQL_* are the .env names
 * used by data/build_local.py and are read as fallbacks so the tool also works
 * when the extension is run directly with only .env sourced):
 *   BEAVER_MYSQL_HOST / MYSQL_HOST       default 127.0.0.1
 *   BEAVER_MYSQL_PORT / MYSQL_PORT       default 3307
 *   BEAVER_MYSQL_USER / MYSQL_USER       default beaver
 *   BEAVER_MYSQL_PWD  / MYSQL_PASSWORD   (no default; passed via env, never argv)
 *   BEAVER_DB                            target database name
 *   BEAVER_QUERY_TIMEOUT                 per-query wall-clock kill, seconds (default 10)
 *   BEAVER_MAX_TURNS                     agent turn cap (default 10). After this many turns the
 *                                        tool refuses further exploration and asks the model to
 *                                        finalize, and the run is aborted at cap+1.
 *   BEAVER_EXPLORE_ROW_CAP               rows returned per exploration call (default 100)
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";
import { spawn } from "node:child_process";

const HOST = process.env.BEAVER_MYSQL_HOST ?? process.env.MYSQL_HOST ?? "127.0.0.1";
const PORT = process.env.BEAVER_MYSQL_PORT ?? process.env.MYSQL_PORT ?? "3307";
const USER = process.env.BEAVER_MYSQL_USER ?? process.env.MYSQL_USER ?? "beaver";
const PWD = process.env.BEAVER_MYSQL_PWD ?? process.env.MYSQL_PASSWORD ?? "";
const DB = process.env.BEAVER_DB ?? "";
const QUERY_TIMEOUT = Number(process.env.BEAVER_QUERY_TIMEOUT ?? "10");
const MAX_TURNS = Number(process.env.BEAVER_MAX_TURNS ?? "10");
const ROW_CAP = Number(process.env.BEAVER_EXPLORE_ROW_CAP ?? "100");

/** Only allow a single read-only statement — the agent must never mutate the benchmark DB. */
function isReadOnly(sql: string): boolean {
  const s = sql.replace(/;+\s*$/, "").trim();
  if (!s) return false;
  // Reject stacked queries (the mysql CLI would execute each one).
  if (s.includes(";")) return false;
  const head = s.slice(0, 40).toUpperCase();
  return (
    /^(SELECT|WITH|SHOW|DESCRIBE|DESC|EXPLAIN)\b/.test(head) ||
    /^\(\s*SELECT/i.test(head)
  );
}

/** Run `mysql` CLI, capture stdout/stderr, kill after QUERY_TIMEOUT seconds. */
function runMysql(sql: string): Promise<{ stdout: string; stderr: string; code: number | null; timedOut: boolean }> {
  return new Promise((resolve) => {
    const env = { ...process.env, MYSQL_PWD: PWD };
    // --batch --raw => tab-separated, no escaping; --silent skips the header so we
    // prefix the column list ourselves from information_schema when needed.
    const args = [
      `-h${HOST}`, `-P${PORT}`, `-u${USER}`,
      "--batch", "--raw", "--unbuffered",
      `-D${DB}`,
      "-e", sql,
    ];
    const child = spawn("mysql", args, { env });
    let stdout = "";
    let stderr = "";
    let timedOut = false;
    const timer = setTimeout(() => {
      timedOut = true;
      child.kill("SIGKILL");
    }, QUERY_TIMEOUT * 1000);
    child.stdout.on("data", (d) => { stdout += d.toString(); });
    child.stderr.on("data", (d) => { stderr += d.toString(); });
    child.on("error", (err) => {
      clearTimeout(timer);
      resolve({ stdout, stderr: stderr + `\n[spawn error: ${err.message}]`, code: -1, timedOut });
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      resolve({ stdout, stderr, code, timedOut });
    });
  });
}

export default function sqlExecExtension(pi: ExtensionAPI) {
  let turnCount = 0;

  pi.on("turn_end", (_event, ctx) => {
    turnCount += 1;
    // Hard stop one turn past the cap so the model gets a chance to finalize
    // after the tool started refusing exploration.
    if (turnCount > MAX_TURNS) {
      try { ctx.abort(); } catch { /* ignore */ }
    }
  });

  pi.registerTool({
    name: "sql_exec",
    label: "SQL Exec",
    description:
      "Run a READ-ONLY SQL statement (SELECT / WITH / SHOW / DESCRIBE / EXPLAIN) against " +
      "the target MySQL database and return up to " + ROW_CAP + " rows as tab-separated text. " +
      "Use it to inspect schema (SHOW TABLES, SHOW CREATE TABLE, DESCRIBE <t>) and sample data. " +
      "Write queries are rejected. Each call has a " + QUERY_TIMEOUT + "s timeout.",
    promptSnippet:
      "Run read-only SQL against the target MySQL DB to explore schema and data.",
    promptGuidelines: [
      "Prefer SHOW TABLES / SHOW CREATE TABLE / DESCRIBE to learn the schema before writing queries.",
      "Always LIMIT exploratory SELECTs (e.g. LIMIT 5) to keep output small.",
      "sql_exec is read-only; never attempt INSERT/UPDATE/DELETE/DROP/etc.",
    ],
    parameters: Type.Object({
      sql: Type.String({ description: "A single read-only SQL statement." }),
    }),
    async execute(_toolCallId, params) {
      const sql = String(params.sql ?? "").trim();
      if (!sql) {
        return { content: [{ type: "text", text: "Error: empty SQL." }], details: { ok: false } };
      }
      if (!DB) {
        return { content: [{ type: "text", text: "Error: no database configured (BEAVER_DB unset)." }], details: { ok: false } };
      }
      if (!isReadOnly(sql)) {
        return {
          content: [{ type: "text", text: "Rejected: only read-only statements (SELECT/WITH/SHOW/DESCRIBE/EXPLAIN) are allowed." }],
          details: { ok: false, rejected: true },
        };
      }
      if (turnCount >= MAX_TURNS) {
        return {
          content: [{
            type: "text",
            text: "TURNCAP_REACHED: You have used your exploration turn budget (" + MAX_TURNS +
              "). Do NOT call any more tools. Output your FINAL SQL query now in a single ```sql block and stop.",
          }],
          details: { ok: false, turncapped: true },
        };
      }
      const res = await runMysql(sql);
      if (res.timedOut) {
        return {
          content: [{ type: "text", text: "Error: query exceeded the " + QUERY_TIMEOUT + "s timeout and was killed. Simplify or add LIMIT." }],
          details: { ok: false, timedOut: true },
        };
      }
      if (res.code !== 0) {
        const msg = (res.stderr || "unknown mysql error").split("\n").filter((l) => !/using a password on the command line/i.test(l)).join("\n").trim();
        return { content: [{ type: "text", text: "MySQL error (exit " + res.code + "):\n" + msg }], details: { ok: false } };
      }
      const raw = res.stdout;
      if (!raw) {
        return { content: [{ type: "text", text: "OK (no rows / empty result set)." }], details: { ok: true, rows: 0 } };
      }
      const lines = raw.replace(/\r\n/g, "\n").split("\n");
      if (lines.length && lines[lines.length - 1] === "") lines.pop();
      const totalRows = lines.length - 1; // first line is the header row in --batch
      let truncated = false;
      let body = raw;
      if (totalRows > ROW_CAP) {
        body = lines.slice(0, ROW_CAP + 1).join("\n");
        truncated = true;
      }
      const text = body + (truncated ? `\n... [${totalRows - ROW_CAP} more rows truncated; ${ROW_CAP}/${totalRows} shown]` : "") +
        `\n[rows: ${Math.min(totalRows, ROW_CAP)}${truncated ? ` of ${totalRows}` : ""}]`;
      return { content: [{ type: "text", text }], details: { ok: true, rows: totalRows, truncated } };
    },
  });
}
