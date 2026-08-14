/**
 * sql_exec — MySQL exploration tool for the BEAVER text-to-SQL experiment.
 *
 * Loaded by the orchestrator on the host or mounted read-only in the container.
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

/** Run `mysql` CLI, capture stdout/stderr, kill after QUERY_TIMEOUT seconds. */
function runMysql(sql: string): Promise<{ stdout: string; stderr: string; code: number | null; timedOut: boolean }> {
  return new Promise((resolve) => {
    const env = { ...process.env, MYSQL_PWD: PWD };
    // --batch --raw => tab-separated output with a header row and no escaping.
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
  pi.registerTool({
    name: "sql_exec",
    label: "SQL Exec",
    description:
      "Run SQL against the target MySQL database and return the complete result as tab-separated text. " +
      "Each call has a " + QUERY_TIMEOUT + "s timeout.",
    promptSnippet:
      "Run SQL against the target MySQL DB to explore schema and data.",
    parameters: Type.Object({
      sql: Type.String({ description: "SQL to execute." }),
    }),
    async execute(_toolCallId, params) {
      const sql = String(params.sql ?? "").trim();
      const res = await runMysql(sql);
      if (res.timedOut) {
        return {
          content: [{ type: "text", text: "Error: query exceeded the " + QUERY_TIMEOUT + "s timeout and was killed. Simplify or add LIMIT." }],
          details: { ok: false, timedOut: true },
        };
      }
      const text = [res.stdout, res.stderr].filter(Boolean).join("\n") || "OK (no output).";
      return { content: [{ type: "text", text }], details: { code: res.code } };
    },
  });
}
