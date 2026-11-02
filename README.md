# Interactive Systems Evaluation Metrics Wiki

A wiki of evaluation metrics for human-facing interactive systems (HCI, human-AI interaction, information retrieval, recommender systems, visualization, and related fields). Each metric has one page that answers the same set of questions, so researchers can decide which metrics to use and what the caveats are.

The questions come from the "EvalOps - Metric Dimensions" slides (24 Aug 2026): **what** is measured, **how**, **why**, **who** is involved, and **which metrics are related**. Each page also records how the metric links to two business objectives: **sustained use over time** and **improved usability**.

## Layout

The wiki has three first-class page types:

- **Constructs** are what we want to know about: abstract concepts such as relevance, perceived usability, or mental workload ("concept" is a plain-language synonym). They form a DAG (directed acyclic graph): a construct can have several broader constructs.
- **Metrics** are operationalizations: procedures that turn observations into a number. One page per operationalization; variants that differ only in a parameter (precision@k) stay on the same page. Each metric links to one or more constructs it measures.
- **Strategies** are the reusable methodology behind metrics, in two layers (`layer` in front matter). *Routes* say how data becomes a number (direct reading, self-rating, external judgment, comparison against reference data, comparative judgment, difference scoring, coding qualitative data, statistical modeling). *Methods* say how the data is gathered (test collections, logs and telemetry, questionnaires, task studies, ability tests, adversarial testing, controlled comparison, and others in `research_method` in the vocabulary). Their pages hold the caveats every metric using them inherits.

| Folder | Contents |
|---|---|
| `constructs/` | One page per construct; `dag.yaml` (the DAG, hand-editable); `index.md` (generated diagram and tree). |
| `metrics/` | One page per metric. |
| `strategies/` | One page per route, and one per research method that has a page so far. |
| `objectives/` | One page per business objective, with the evidence linking metrics to it. |
| `schema/` | Templates for the three page types, `vocabulary.yaml` (allowed tag values), `page-guide.md` (generated: what every section answers), `DECISIONS.md` (schema decisions and their reasons). |
| `references/` | `bibliography.yaml`: every source that pages may cite. |
| `migration/` | Notes on moving content from the original spreadsheet. |
| `scripts/` | `validate.py` (checks everything), `build.py` (regenerates derived content), `sync_constructs.py` (keeps `dag.yaml` and construct pages in sync). |

Page types planned but not started: tasks (e.g. "document search and summarization") and decision guides.

## How a page is structured

Each page has two parts:
1. **Front matter** (the YAML block at the top): short, comparable facts. On metric pages: the construct statement and the constructs it measures, direct vs. proxy, research method and route, how much validity deserves attention, cost, related metrics, and links to objectives. Scripts use these to build tables and lists.
2. **Body**: one section per question, with the same headings on every page of that type. [`schema/page-guide.md`](schema/page-guide.md) lists every heading and the question it answers.

On metric pages, the construct is described as *property of subject in context*, tagged with five facets: `subject`, `aspect`, `perspective`, `quantity_form`, and `context`. The free-text `construct.statement` is the authoritative definition, written at the level of the "spirit" of the measurement; different fields' uses of the same computation go in section 3.1. See `schema/vocabulary.yaml` for how the facets map onto the slides.

Related metrics (section 5) are grouped as operationally related (shared computation), conceptually related (same or related construct), and empirical co-movements (evidence of moving together).

### Generated content

Some content is generated and must not be edited by hand: blocks between `<!-- generated:...:start -->` and `<!-- generated:...:end -->` markers, `constructs/index.md`, and `schema/page-guide.md`. Run `python scripts/build.py` after changing front matter or templates.

### Editing the construct DAG

Edit structure (title, `broader`) either in a construct page or in `constructs/dag.yaml`, then run `python scripts/sync_constructs.py`. It compares both with the last synced state and copies the change across. If both sides changed the same construct differently, or a construct was removed from the YAML, it stops without writing anything and says what to fix by hand; it never deletes a page. To rename, change the id in the YAML and add `renamed_from: <old id>`.

## Status and trust

Every page carries a `status`: `ai-draft` → `human-edited` → `human-reviewed` → `expert-verified`. Treat `ai-draft` pages as unchecked. References added by AI are marked `verified: false` in the bibliography until someone checks them.

## Adding or editing a page

1. Copy the template from `schema/` (`metric-template.md`, `construct-template.md`, or `strategy-template.md`) to the matching folder as `<id>.md`. For a new construct, adding an entry to `constructs/dag.yaml` and syncing creates the stub for you.
2. Fill in the front matter using values from `schema/vocabulary.yaml`.
3. Cite only keys that exist in `references/bibliography.yaml`; add new sources there first.
4. Run `python scripts/sync_constructs.py` (if constructs changed), then `python scripts/build.py`, then `python scripts/validate.py`, and fix what it reports.

## Viewing

The pages read fine on GitHub. For a searchable site for readers who do not use GitHub, the plan is to publish with MkDocs Material (not set up yet).
