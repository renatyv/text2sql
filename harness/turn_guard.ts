/**
 * turn_guard — hard agent turn-cap for the containerized BEAVER runner.
 *
 * The legacy sql_exec.ts enforced the turn budget by refusing further
 * exploration after BEAVER_MAX_TURNS. Now that the agent explores MySQL via
 * `bash` + the `mysql` CLI (no sql_exec tool), this minimal extension keeps
 * ONLY that turn-counting responsibility: it counts turn_end events and calls
 * ctx.abort() at the cap. If the final allowed turn is another tool call rather
 * than final SQL, the run has exhausted its evaluation budget.
 *
 * It registers NO tools and reads NO MySQL credentials — pure lifecycle guard.
 *
 * Env:
 *   BEAVER_MAX_TURNS   agent turn cap (default 6). Aborted at the cap.
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const MAX_TURNS = Number(process.env.BEAVER_MAX_TURNS ?? "6");

export default function turnGuardExtension(pi: ExtensionAPI) {
  let turnCount = 0;

  pi.on("turn_end", (event, ctx) => {
    turnCount += 1;
    // A normal final response ends by itself. Abort only when the last allowed
    // turn asks for another tool round-trip.
    if (turnCount >= MAX_TURNS && event.message.stopReason === "toolUse") {
      try { ctx.abort(); } catch { /* ignore */ }
    }
  });
}
