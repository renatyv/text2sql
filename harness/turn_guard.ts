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
const FINAL_SQL = /(?:<ans>|```(?:sql|mysql)?\s*\n)\s*(?:SELECT|WITH|\()/i;

export default function turnGuardExtension(pi: ExtensionAPI) {
  let turnCount = 0;

  pi.on("turn_end", (event, ctx) => {
    turnCount += 1;
    if (turnCount === MAX_TURNS - 1 && event.message.stopReason === "toolUse") {
      pi.setActiveTools([]);
      pi.sendMessage({
        customType: "turn-guard",
        content: "FINAL TURN: Tools are now disabled. Return your best complete MySQL query immediately inside <ans>...</ans>. Do not explain.",
        display: false,
      }, { deliverAs: "steer" });
      return;
    }
    if (turnCount === MAX_TURNS) {
      const text = Array.isArray(event.message.content)
        ? event.message.content.filter((part) => part.type === "text").map((part) => part.text).join("")
        : "";
      if (!FINAL_SQL.test(text)) {
        pi.setActiveTools([]);
        pi.sendMessage({
          customType: "turn-guard",
          content: "FORMAT RECOVERY: Your response did not contain final SQL. Do not use tools or explain. Return the best complete MySQL query now inside <ans>...</ans>.",
          display: false,
        }, { deliverAs: "followUp", triggerTurn: true });
      }
      return;
    }
    // Failsafe: allow only the one answer-format recovery turn.
    if (turnCount > MAX_TURNS && event.message.stopReason === "toolUse") {
      try { ctx.abort(); } catch { /* ignore */ }
    }
  });
}
