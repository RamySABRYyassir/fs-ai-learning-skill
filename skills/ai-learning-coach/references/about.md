# about

**Summary:** What the roadmap is, what's inside, how to use it, and why it's worth your time.
**Options:** `--full` adds a paragraph per section.
**Examples:** `about` · "What is this roadmap?"
**Next:** `place-me`, `help`

## Fetch
- Default: the agent index (already loaded) and the hub page (`notion.hub`).
- `--full`: also the "Start here" page (link in the agent index).

## Default answer (aim for under 250 words, readable in two minutes)
1. **What this is.** One or two sentences: a company-neutral roadmap for learning AI and agentic AI, organised into four levels. Give each level a few words on what you hand over to AI at that level, using the level descriptions from the roadmap.
2. **What's inside.** One line per part, each linked: modules and checkpoints, role paths, practice projects, glossary, resources, standards alignment, program roadmap (for organisations), company pack, AI agent index. Use counts only where the fetched pages state them or you can count them exactly from the agent index (modules, checkpoints and paths are in the index).
3. **How to use it.** Three ways in:
   - Learner: `place-me`, follow your role path, do one practice project per level, prepare the checkpoint with `checkpoint`, then get it reviewed.
   - Manager or lead: the program roadmap phases and their outcomes and KPIs; `risk-check` before approving AI use cases.
   - Just curious: `explore` and `explain`.
4. **Why it's worth it.**
   - Learners: a clear order instead of scattered tutorials, practice on real work, skills that carry over to any company or tool.
   - Managers: shared levels and vocabulary to measure progress, outcomes and KPIs per phase.
   - Organisations: supports staff AI literacy and follows recognised frameworks. Name the frameworks from the roadmap's standards list; don't describe legal obligations beyond what the standards page says.

## --full
Same four parts, plus a short paragraph per part of "What's inside" (what it contains and when to use it), drawn from the hub and Start here pages.

## Footer
- "Skill version X · What's new: …" (version from `config.json`, the newest entry in `CHANGELOG.md`).
- "Run `place-me` to find your level. `help` lists every command."
