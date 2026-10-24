# help

**Summary:** Lists every command, or explains one.
**Options:** `help <command>`
**Examples:** `help` · `help explain` · "What can you do?"
**Next:** `about`, `place-me`

Works without Notion. Build everything from the command table in `SKILL.md`; never type the list out from memory.

## `help` (no argument)
- Group the **v1** commands by the table's Group column, in table order. One line each: command, what it does, example.
- Then a short **Coming soon** line listing the planned commands by name only.
- Footer: skill version from `config.json` and "Start with `about` or `place-me`."

Format as a compact code block or table so the columns line up.

## `help <command>`
Read that command's reference file and show its header: Summary, Options, Examples, Next. Add one sentence on what the learner should have ready (e.g. for `checkpoint`: the level and, if they have it, their evidence). For a coming-soon command, say it's planned and name the closest v1 command. For an unknown name, show the full list.
