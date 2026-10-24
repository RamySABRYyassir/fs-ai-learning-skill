# next

**Summary:** Your next one or two modules, with what to practise and the evidence that shows you're done.
**Options:** `next <n>` for up to three modules
**Examples:** `next` · "What should I learn next? I've done L1.1 to L1.4."
**Next:** `suggest-project`, `checkpoint`

## Needs
The learner's path (or role), and which modules they've finished or their current level. If unknown, ask once in one line ("Which role, and which modules or checkpoints have you done?") or suggest `place-me`.

## Fetch
Agent index (paths JSON and module index), then the chosen module page(s) for practice, evidence, terms and resources. At most two module pages unless they asked for three.

## Decide
Follow the agent index instructions:
- Take the modules of their path in order.
- Skip modules they've finished. If they gave only a level, treat every module at or below their current level as done.
- Recommend the first module whose prerequisites are all done. If two are available in parallel (the index's "Next" can list several), offer both and say they can pick either.
- If every module at a level is done, the next step is that level's checkpoint.

## Answer
For each module: `ID · Title` (link), level, minutes, outcome, the practice task, and "Done when" (evidence). List its key terms by name so they can `explain` them. Mention linked resources only by title, and only those linked from the module.

End with: "Next: `suggest-project`" or "`checkpoint N`" if a checkpoint is due.
