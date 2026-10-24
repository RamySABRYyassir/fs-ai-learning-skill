# explain

**Summary:** Explains a topic, concept or term in plain language, with the module that teaches it.
**Options:** `--deep` adds a technical explanation · `--short` gives one line only
**Examples:** `explain context window` · `explain the autonomy dial --deep` · "What is MCP?"
**Next:** `explore`, `next`

## Fetch
1. Find the term in the **Glossary** database (link in the agent index): one Notion search restricted to that database or to the hub, using the term and common synonyms (e.g. "RAG" → retrieval-augmented generation). Fetch the matching glossary entry only if the search result doesn't include its definition and "Taught in" module.
2. If it's a broader topic rather than a term, match it to modules in the module index instead.
3. Fetch the module page (the "Taught in" module, or the best-matching module) only for `--deep`, or when the definition alone is too thin to explain the concept.

## Answer
- **One line:** the roadmap's definition, in its own words where possible.
- **Plain explanation** (default, 3-5 sentences): what it is, why it matters at work, a small everyday example. Use the learner's role for the example if you know it.
- **Technical** (`--deep` only): how it works, common pitfalls, how it connects to other roadmap terms (name them so the learner can `explain` them next).
- **Where it's taught:** `ID · Title` with link, and its level.

If the roadmap doesn't have the term: say so, give a short general explanation labelled "not from the roadmap", and point to the closest module.

End with: "Next: `explain <related term>`" or "`explore <level>`".
