# risk-check

**Summary:** Checks an AI use case: the autonomy dial setting it should start at, the risks to handle, the standards that apply, and the modules to read.
**Options:** `risk-check <use case>`
**Examples:** `risk-check an agent that drafts replies to customer complaints` · "Is it safe to let an agent merge PRs?"
**Next:** `explain`, `explore Operate`

Learning guidance only: not a legal, compliance or security approval, and it doesn't replace the organisation's own approval process. Say this once, briefly, at the end.

## Fetch
1. Agent index (already loaded): find the modules on the autonomy dial, safe use, guardrails, security and evaluation in the module index (e.g. the AI rules module and `L4.1`).
2. The **Standards alignment** page (link in the agent index), for the current wording of each standard.
3. The **Company pack** page, for the organisation's rules placeholder.
Don't fetch module pages unless a specific flag needs more detail.

## Ask (one message; skip what the description already answers)
1. What data does it touch? (public, internal, personal, customer, financial, secrets)
2. What does the AI do: suggest only, read from systems, or act (write, send, pay, deploy)?
3. Who is affected if it's wrong, and can a mistake be undone?
4. Who reviews its work, and when?

## Answer
- **Dial setting to start at:** one of Suggest, Approve first, Act within limits, Act and report, chosen by risk and reversibility as the roadmap teaches. Anything touching money, customers or production starts at **Approve first** with a named approver. Give one line of why, and what would have to be true to move it one setting up.
- **Risks to handle** (a short table): risk, why it applies here, what to do, module to read (`ID · Title`). Consider: sensitive data exposure, prompt injection and untrusted input, excessive permissions or agency, wrong or made-up output, missing human review, no logging or monitoring, no evaluation before launch.
- **Standards:** only those on the Standards alignment page that apply, each with one line in the page's own terms (e.g. staff AI literacy, risk management, AI management system, LLM and agentic security risks).
- **Company rules:** point to the Company pack and say to check the organisation's approved tools and data rules.

End with the not-a-legal-approval line, then "Next: `explain <the top risk>`".
