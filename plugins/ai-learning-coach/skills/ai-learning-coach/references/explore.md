# explore

**Summary:** Browse the roadmap by level, role path or topic.
**Options:** `explore <level>` (1-4 or Ask/Connect/Delegate/Operate) · `explore <path or role>` · `explore <topic>` · add `--full` for the level page's detail
**Examples:** `explore` · `explore Delegate` · `explore engineers` · `explore evaluation`
**Next:** `explain`, `next`

## Fetch
Agent index only, except:
- `--full` on a level: also that level's page (link in the agent index).
- A topic with no match in the module index: one Notion search restricted to the hub page (`notion.hub`).

## Answers
- **No argument:** the four levels, one line each (name, what you hand over to AI, checkpoint ID), then the role paths (ID, name, target level). Suggest `explore <level>` or `explore <path>`.
- **Level:** every module at that level from the module index, in order: `ID · Title` and a one-line outcome (shorten if needed), with Everyone vs role-specific marked. Finish with the checkpoint and what it asks for.
- **Path or role:** the path's modules from the paths JSON, grouped by level, `ID · Title` only, plus the target level and outcome. If they gave a role, map it to the path first.
- **Topic:** modules whose title or outcome matches the topic (show up to six), each with a one-line reason. If none match, use the Notion search; if still nothing, say the roadmap doesn't cover it and name the closest module.

Keep it to a scannable list; no paragraphs of commentary. End with one suggested command, usually `explain <something from the list>` or `next`.
