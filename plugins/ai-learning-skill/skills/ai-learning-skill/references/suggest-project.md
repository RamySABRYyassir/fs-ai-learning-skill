# suggest-project

**Summary:** Picks a practice project that fits your level, role and interests, with steps and a definition of done.
**Options:** `--no-code` (only projects that don't need coding) · `suggest-project <level>` · `suggest-project <interest>`
**Examples:** `suggest-project` · `suggest-project 3 --no-code` · "Give me a project about reporting"
**Next:** `checkpoint`, `explain`

## Needs
Level and role (from the conversation, or ask once). Interests are optional.

## Fetch
1. Candidate project IDs: from the checkpoint module of that level (`L<n>.C` lists the level's projects) or the current module's "Practice projects", and the path's signature projects in the paths JSON if present. If you don't have these, do one Notion search in the **Practice projects** database (link in the agent index) for the level.
2. Fetch at most **two** project pages: your pick and, if useful, an alternative.

## Choose
Prefer, in order: the path's signature project for that level; a project whose "For" includes the learner's role label; one matching their interest; with `--no-code`, only projects where "Needs coding" is no.

## Answer
- `ID · Title` (link), level, needs coding yes/no.
- **Problem** and **Outcome**, from the page.
- **Steps:** the page's steps, or a short sequence of 4-6 steps faithful to the page if it doesn't list them.
- **Done when:** the outcome or evidence the page gives; tie it to the level checkpoint's evidence list if it counts toward it.
- **Safety:** use synthetic or approved, non-confidential material; connect tools read-only; anything touching money, customers or production stays at Approve first. Use the roadmap's wording where the page or company pack has it.
- One line naming the alternative project.

End with: "Next: `checkpoint <level>` when you've done it."
