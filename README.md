# AI Learning Coach

A Claude skill that turns the **AI & Agentic AI Learning Roadmap** in Notion into a personal coach. Instead of reading 40-plus modules on your own, you ask: *"What level am I?"*, *"Explain prompt injection"*, *"What should I do next?"*, *"Test me on Level 2"*. The coach answers from the roadmap and links you to the exact page.

The roadmap is company-neutral. It covers four levels of working with AI:

| Level | You give AI… | In short |
|---|---|---|
| 1 · **Ask** | context | Use AI on everyday tasks and check every result |
| 2 · **Connect** | access | Connect AI, read-only, to the systems where answers live |
| 3 · **Delegate** | a goal | An agent plans, uses tools and stops at the checkpoints you set |
| 4 · **Operate** | rules & limits | AI runs on a trigger inside enforced limits, with logs, evals and a person approving anything consequential |

*(Level names and descriptions come from the roadmap; the coach always reads the current wording from Notion.)*

## What it can do

| Command | What it does | Try |
|---|---|---|
| `about` | What the roadmap is, what's inside, how to use it, why it's worth it (`--full` for detail) | `about` |
| `help` | Lists commands; `help <command>` explains one | `help checkpoint` |
| `place-me` | A few questions, then your role path and starting level | `place-me` |
| `explore` | Browse by level, role path or topic | `explore Delegate` |
| `explain` | A topic, concept or term in plain language, with the module that teaches it (`--deep` for technical) | `explain context window` |
| `next` | Your next one or two modules, with practice and "done when" | `next` |
| `suggest-project` | A practice project for your level and role (`--no-code` available) | `suggest-project --no-code` |
| `checkpoint` | Knowledge check plus evidence review for a level | `checkpoint 1` |
| `risk-check` | Autonomy dial setting, risks, standards and modules for an AI use case | `risk-check an agent that refunds customers` |

You don't have to type commands. Plain questions work too: "what can you do?", "where do I start?", "is it safe to use AI for X?".

**Coming later:** `search`, `compare`, `plan`, `resources`, `review-my-work`, `flashcards`, `team-plan`, `workshop-followup`, `progress`.

## Requirements

- **Claude** with skills enabled (claude.ai, the desktop app or Claude Code).
- **The Notion connector**, connected in Claude.
- **Access to the roadmap** in Notion: you must be able to open the hub page set in `config.json`.

Notion is required on purpose: the coach reads the roadmap live, so it's always current and nothing is copied into the skill. Only `help` works without it.

## Install

Pick one of two ways. Either way, start a chat afterwards and type `about`.

### A. From GitHub, as a plugin (no download)

This repository is also a plugin marketplace.

- **Claude desktop app:** **Customize → Plugins → Add → Add marketplace → Add from a repository**, enter `ramysabryali/ai-learning-skill`, then install **ai-learning-skill**.
- **Claude Code:**
  ```
  /plugin marketplace add ramysabryali/ai-learning-skill
  /plugin install ai-learning-skill@ai-learning
  ```

Plugins need a Pro, Max, Team or Enterprise plan. If your organisation restricts marketplaces, an owner has to allow this repository.

### B. As a skill zip

1. Build the zip:
   ```bash
   ./scripts/package.sh        # creates dist/ai-learning-skill-<version>.zip
   ```
2. In Claude: **Customize → Skills → + → Create skill → Upload a skill**, and choose the zip.
3. *(Team and Enterprise)* Share it from the skill's **⋯** menu, or **Publish to org**. People you share with get each new upload automatically; published skills go through your organisation's review again.

Claude Code without the marketplace: copy `plugins/ai-learning-skill/skills/ai-learning-skill/` into `~/.claude/skills/`.

## Update

Most roadmap changes need **no skill update**: new modules, resources, glossary terms or projects in Notion show up straight away, because the coach reads them live.

Update the skill only when its behaviour changes (a new command, a changed method):

1. Edit the files under `plugins/ai-learning-skill/skills/ai-learning-skill/`.
2. Bump `skill_version` in `config.json` and add an entry at the top of `CHANGELOG.md` (the coach shows it as "What's new").
3. Run `./scripts/package.sh`. It validates first and refuses to build if something is inconsistent.
4. Commit and push.
   - **Plugin installs** pick up the new commit: on the next update for people who turned on auto-update for the marketplace (Customize → Plugins, or **Marketplaces** in `/plugin` in Claude Code), or when they run `/plugin marketplace update ai-learning`. `plugin.json` deliberately has no `version`, so every pushed commit counts as a new version.
   - **Zip installs:** re-upload the new zip. Colleagues you shared it with get it automatically.

If the roadmap moves to another Notion page, change only the hub URL in `config.json`.

## How it works

```
You ──▶ Claude + this skill
          1. reads config.json (the roadmap hub link)
          2. finds the "AI agent index" under the hub and fetches it once per chat
             (ID scheme, role vocabulary, module index, paths, links)
          3. fetches one module, project or glossary page only when a command needs it
          4. answers with IDs, titles and links back to Notion
```

Keeping token use low is part of the design: one index fetch per chat, single pages on demand, never a whole database. `about` and `help` barely touch Notion.

**Ground rules the coach follows:** read-only (never edits Notion); answers from the roadmap and says when something isn't covered; never invents IDs or counts; never marks a level complete (checkpoints need a mentor or peer review); never suggests putting customer data, personal data or secrets into unapproved tools; `risk-check` is learning guidance, not a legal or compliance approval; it doesn't save anything about you.

## What's hard-coded, and what isn't

| Fixed in the skill | Read live from Notion |
|---|---|
| The command table, and each command's method (`references/`) | Levels, modules, checkpoints, outcomes and order |
| Ground rules and answer style | Role paths, practice projects, glossary, resources |
| Version and changelog | Counts, links, standards wording, program phases, company pack |
| The Notion hub URL (`config.json`) | |

## Repository layout

```
ai-learning-skill/
├── README.md
├── .claude-plugin/marketplace.json        ← makes the repo an installable marketplace
├── plugins/ai-learning-skill/
│   ├── .claude-plugin/plugin.json         ← plugin manifest (no version: installs track commits)
│   └── skills/ai-learning-skill/          ← the skill (this folder is what gets zipped)
│       ├── SKILL.md                       ← rules, data loading, command table, routing
│       ├── config.json                    ← Notion URLs and display version
│       ├── CHANGELOG.md
│       └── references/                    ← one file per command, loaded only when used
│           ├── about.md  help.md  place-me.md  explore.md  explain.md
│           └── next.md  suggest-project.md  checkpoint.md  risk-check.md
└── scripts/
    ├── validate.py                        ← consistency checks (skill + manifests)
    └── package.sh                         ← validate + build dist/*.zip
```

## Adding a command

1. Add a row to the command table in `SKILL.md` with status `v1` (or move a `coming soon` row to `v1`).
2. Create `references/<command>.md` starting with the four header lines `help` reads: **Summary**, **Options**, **Examples**, **Next**. Then say what to fetch, what to ask, and how to answer.
3. Add the command to the table in this README, bump the version, and run `./scripts/package.sh`.
