/**
 * turn_guard — hard agent turn-cap for the containerized BEAVER runner.
 *
 * The legacy sql_exec.ts enforced the turn budget by refusing further
 * exploration after BEAVER_MAX_TURNS. Now that the agent explores MySQL via
 * `bash` + the `mysql` CLI (no sql_exec tool), this minimal extension keeps
 * ONLY that turn-counting responsibility: after the penultimate turn it removes
 * tools and tells the model to use its final turn for SQL, with abort as a
 * failsafe if the model somehow still emits a tool call at the cap.
 *
 * It registers NO tools and reads NO MySQL credentials — pure lifecycle guard.
 *
 * Env:
 *   BEAVER_MAX_TURNS   agent turn cap (default 6). Last turn is answer-only.
 */
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const MAX_TURNS = Number(process.env.BEAVER_MAX_TURNS ?? "6");

export default function turnGuardExtension(pi: ExtensionAPI) {
  let turnCount = 0;

  pi.on("turn_end", (event, ctx) => {
    turnCount += 1;
    if (turnCount === MAX_TURNS - 1 && event.message.stopReason === "toolUse") {
      pi.setActiveTools([]);
      pi.sendMessage({
        customType: "turn-guard",
        content: "FINAL TURN: Tools are now disabled. Return your best complete MySQL query immediately in one ```sql block. Do not explain.",
        display: false,
      }, { deliverAs: "steer" });
      return;
    }
    // Failsafe: the final turn has no tools, so this should be unreachable.
    if (turnCount >= MAX_TURNS && event.message.stopReason === "toolUse") {
      try { ctx.abort(); } catch { /* ignore */ }
    }
  });
}
