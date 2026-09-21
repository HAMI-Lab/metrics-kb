# Interactive Systems Evaluation Metrics Wiki

A wiki of evaluation metrics for human-facing interactive systems (HCI, human-AI interaction, information retrieval, recommender systems, visualization, and related fields). Each metric has one page that answers the same set of questions, so researchers can decide which metrics to use and what the caveats are.

The questions come from the "EvalOps - Metric Dimensions" slides (24 Aug 2026): **what** is measured, **how**, **why**, **who** is involved, and **which metrics are related**. Each page also records how the metric links to two business objectives: **sustained use over time** and **improved usability**.

## Layout

| Folder | Contents |
|---|---|
| `metrics/` | One page per metric. |
| `objectives/` | One page per business objective, with the evidence linking metrics to it. |
| `schema/` | `metric-template.md` (copy this to start a page) and `vocabulary.yaml` (allowed values for tags). |
| `references/` | `bibliography.yaml`: every source that pages may cite. |
| `migration/` | Notes on moving content from the original spreadsheet. |
| `scripts/` | `validate.py`: checks pages against the template and vocabulary. |

Page types planned but not started: tasks (e.g. "document search and summarization"), constructs (created once groups of metrics with shared tags emerge), and decision guides.

## How a page is structured

Each page has two parts:
1. **Front matter** (the YAML block at the top): short, comparable facts such as the construct tags, direct vs. proxy, cost, related metrics, and links to objectives. Scripts use these to build tables and find related metrics.
2. **Body**: one section per question, with the same headings on every page.

The construct is described as *property of subject in context*, tagged with five facets: `subject`, `aspect`, `perspective`, `quantity_form`, and `context`. The free-text `construct.statement` is the authoritative definition; the tags are provisional aids for finding related metrics. See `schema/vocabulary.yaml` for how these map onto the facets in the slides.

## Status and trust

Every page carries a `status`: `ai-draft` → `human-edited` → `human-reviewed` → `expert-verified`. Treat `ai-draft` pages as unchecked. References added by AI are marked `verified: false` in the bibliography until someone checks them.

## Adding or editing a page

1. Copy `schema/metric-template.md` to `metrics/<id>.md`.
2. Fill in the front matter using values from `schema/vocabulary.yaml`.
3. Cite only keys that exist in `references/bibliography.yaml`; add new sources there first.
4. Run `python scripts/validate.py` and fix what it reports.

## Viewing

The pages read fine on GitHub. For a searchable site for readers who do not use GitHub, the plan is to publish with MkDocs Material (not set up yet).
