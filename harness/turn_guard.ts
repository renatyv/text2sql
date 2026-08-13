/**
 * turn_guard — hard agent turn-cap for the containerized BEAVER runner.
 *
 * The legacy sql_exec.ts enforced the turn budget by refusing further
 * exploration after BEAVER_MAX_TURNS. Now that the agent explores MySQL via
 * `bash` + the `mysql` CLI (no sql_exec tool), this minimal extension keeps
 * ONLY that turn-counting responsibility: it counts turn_end events and calls
 * ctx.abort() one turn past the cap so the model gets a chance to finalize
 * after its budget is exhausted.
 *
 * It registers NO tools and reads NO MySQL credentials — pure lifecycle guard.
 *
 * Env:
 *   BEAVER_MAX_TURNS   agent turn cap (default 10). Aborted at cap+1.
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const MAX_TURNS = Number(process.env.BEAVER_MAX_TURNS ?? "10");

export default function turnGuardExtension(pi: ExtensionAPI) {
  let turnCount = 0;

  pi.on("turn_end", (_event, ctx) => {
    turnCount += 1;
    // Hard stop one turn past the cap so the model gets a chance to emit its
    // final ```sql block after the budget runs out.
    if (turnCount > MAX_TURNS) {
      try { ctx.abort(); } catch { /* ignore */ }
    }
  });
}
