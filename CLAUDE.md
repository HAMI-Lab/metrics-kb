# Instructions for AI assistants working in this repo

Read `README.md` first. This file adds the rules for AI edits.

## Before editing anything
- Run `git log --oneline -20` and `git diff HEAD~5 --stat` (or since the last commit you made) to see what humans changed since your last session.
- For any page you are about to edit, run `git log -p -- <file>` and read the human changes. **Human edits are authoritative.** Do not revert, reword, or "tidy" text a human wrote or changed unless asked. If you think a human edit is wrong, say so in the page's "Open questions and review notes" section or in chat, and leave the text.
- Pages with `status: human-reviewed` or `expert-verified`: propose changes in chat or in review notes; do not edit the body unless asked.

## Writing rules
- Follow `schema/metric-template.md` exactly: same headings, same order, same front matter keys.
- Use only values from `schema/vocabulary.yaml`. If none fits, use `other: <description>` and flag it.
- `construct.statement` is the authoritative definition; tags are aids.
- Every factual claim that is not common knowledge cites a key from `references/bibliography.yaml` in the form `[key]`. Never invent a citation. If you add a reference, mark it `verified: false`, and never add details (page numbers, figures) you are not sure of; write "(check against the paper)" instead.
- State evidence strength honestly in section 6. Theoretical links must be called theoretical.
- Plain language. Short sentences. Explain jargon on first use.
- Link to other pages with relative links, e.g. `[SUS](system-usability-scale.md)`.

## Status handling
- New or AI-rewritten pages: `status: ai-draft`.
- Never raise a page's status yourself.

## After editing
- Run `python scripts/validate.py`; it must pass.
- Commit in small steps, one topic per commit, with a message that says what changed and why. Do not commit changes mixed with a human's uncommitted work; ask first if the working tree is dirty.
- Update the tables in `objectives/*.md` if you changed a page's `objectives` front matter.
