# place-me

**Summary:** A few questions, then your role path and the level to start at.
**Options:** none
**Examples:** `place-me` · "What level am I?"
**Next:** `next`, `checkpoint`

## Fetch
Agent index only (role vocabulary, paths JSON, module index).

## Ask (one message, at most four questions; skip any you already know)
1. **Your role** (e.g. backend engineer, product manager, designer, recruiter, operations, marketing, manager).
2. **What you do with AI today** - pick the last statement that's true for you:
   a. I don't use AI at work yet, or only rarely.
   b. I use an AI assistant for everyday tasks, give it context, and check the results. (Ask)
   c. My AI tools are connected to my files, apps, data or the web, and I use that regularly. (Connect)
   d. I hand multi-step tasks to an agent that acts (for example a coding agent) and I review what it did. (Delegate)
   e. I run AI workflows that act with limits, monitoring and checks, sometimes unattended. (Operate)
3. **Checkpoints passed:** have you had a level checkpoint reviewed by a mentor or peer? Which level?
4. *(Optional)* **Time per week** you can spend.

## Decide
- **Path:** map the role to a Role ID using the role vocabulary in the agent index, then to the path that uses it. Managers and leads use the tech, product or ops labels, as the index says. If two paths fit, pick one and name the other.
- **Current level:** the highest level whose checkpoint they've passed (0 if none). This is the roadmap's rule.
- **Suggested starting level:** the level matching their answer to question 2 (a or b → Level 1, c → 2, d → 3, e → 4), but **never more than one level above their current level** and never above the path's target level.
- If the suggested starting level is above their current level, they start by attempting the checkpoint of the level below it, e.g. "start with `checkpoint 1`; if it passes review, begin Level 2". This mirrors the agent index instruction to attempt the checkpoint of the level they believe they're at.

## Answer
- Path: ID, name, target level, and the path's outcome.
- Current level and suggested starting level, each with one line of reasoning.
- The first module to open (`ID · Title`, outcome, link): the first module in their path at the starting level whose prerequisites are done, or the checkpoint to attempt.
- Say plainly that this is a starting point, not a completed level.

End with: "Next: `next`" (or "`checkpoint N`" if they should attempt one first).
