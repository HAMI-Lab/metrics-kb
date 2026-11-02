# Instructions for AI assistants working in this repo

Read `README.md` first. This file adds the rules for AI edits.

## Before editing anything
- Run `git log --oneline -20` and `git diff HEAD~5 --stat` (or since the last commit you made) to see what humans changed since your last session.
- For any page you are about to edit, run `git log -p -- <file>` and read the human changes. **Human edits are authoritative.** Do not revert, reword, or "tidy" text a human wrote or changed unless asked. If you think a human edit is wrong, say so in the page's "Open questions and review notes" section or in chat, and leave the text.
- Pages with `status: human-reviewed` or `expert-verified`: propose changes in chat or in review notes; do not edit the body unless asked.

## Writing rules
- Follow the template for the page type exactly (`schema/metric-template.md`, `construct-template.md`, `strategy-template.md`): same headings, same order, same front matter keys.
- One metric page per operationalization, and one per computation per root: all of a page's `construct.measures` must sit under the same root of the construct DAG (D20). Qualify the title when the same name exists under another root, e.g. "Precision (benchmark)" and "Precision (user on task)". Method changes within a root do not make a new page.
- Do not make a page for a standardized questionnaire or test (D25). Put it on the page for its construct and method, e.g. "Perceived Usability Score (questionnaire)": list it in `operationalization.instruments`, describe it in section 2.6, give its scoring in 2.4, and add its name to `aliases`.
- Write `construct.statement` at the level of the "spirit" of the measurement; put field-specific uses in 3.1, not in separate pages or separate statements.
- Every metric links to at least one construct (`construct.measures`) and one strategy (`operationalization.route`). If no construct fits, add one (in `constructs/dag.yaml` or a new page) and say so in chat.
- Set `validity_concern` honestly. Use `high` when the number is a proxy that is easy to game or when judges (human or model) go unchecked.
- Never edit between `<!-- generated:...:start -->` and `<!-- generated:...:end -->` markers, `constructs/index.md`, `schema/page-guide.md`, or `docs/wiki-map.md`; run `python scripts/build.py` instead.
- Change the construct DAG through `scripts/sync_constructs.py` (after editing `constructs/dag.yaml` or a page's `broader`). If sync reports a conflict or a removal, ask a person; do not delete construct pages yourself.
- Record schema changes, with reasons and alternatives, in `schema/DECISIONS.md`.
- Use only values from `schema/vocabulary.yaml`. If none fits, use `other: <description>` and flag it.
- `construct.statement` is the authoritative definition; tags are aids.
- Every factual claim that is not common knowledge cites a key from `references/bibliography.yaml` in the form `[key]`. Never invent a citation. If you add a reference, mark it `verified: false`, and never add details (page numbers, figures) you are not sure of; write "(check against the paper)" instead.
- Tell findings from hypotheses. Use "(check against the paper)" only for a finding you attribute to a cited source but whose details you have not verified. If a claim is a hypothesis (plausible, but no source you know states it), say so: write "Hypothesis:", give the reasoning for why it could be true, and end with "(further reference needed)". Never dress a hypothesis as a reported finding.
- When a metric is a proxy with a known gap (`measure_type` proxy or mixed, `validity_concern` moderate or high), say in 2.1 under "**Using a proxy with a known gap.**" which decisions the number can support, which it cannot, and what check to run before relying on it.
- State evidence strength honestly in section 6. Theoretical links must be called theoretical.
- Plain language. Short sentences. Explain jargon on first use.
- A metric known by an acronym gets the title "Full Name (ACRONYM)", e.g. "Normalized Discounted Cumulative Gain (nDCG)", and its full name is spelled out again in the first sentence of 1.1. Keep the acronym in `aliases`.
- Link to other pages with relative links, e.g. `[SUS](perceived-usability-score.md)`.

## Status handling
- New or AI-rewritten pages: `status: ai-draft`.
- Never raise a page's status yourself.

## After editing
- Run `python scripts/sync_constructs.py` (if constructs changed), `python scripts/build.py`, then `python scripts/validate.py`; it must pass.
- Commit in small steps, one topic per commit, with a message that says what changed and why. Do not commit changes mixed with a human's uncommitted work; ask first if the working tree is dirty.
- Update the tables in `objectives/*.md` if you changed a page's `objectives` front matter.
