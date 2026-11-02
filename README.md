# Interactive Systems Evaluation Metrics Wiki

A wiki of evaluation metrics for human-facing intelligent and interactive systems: human-AI interaction, information retrieval, recommender systems, visualization, LLM and agent evaluation, and related fields. It helps researchers and practitioners decide which metrics to use, what each one actually measures, and what can go wrong when they rely on it.

Every metric page answers the same questions: **what** is measured, **how**, **why**, **who** is involved, and **which metrics are related**. Each page also records how the metric links to two objectives: **sustained use over time** and **improved usability**.

**Start here:** the [wiki map](docs/wiki-map.md) links every page from one place, grouped by root, by strategy layer, and by objective. The [construct DAG](constructs/index.md) shows the same structure as a diagram.

## Design philosophy

The short version: a metric is where a question about something (a **construct**) meets a reusable way of measuring (a **strategy**). The wiki keeps the two apart, so that each metric page can say exactly which question it answers and how, and so that what is shared across metrics is written once.

The reasons for each decision are in [`schema/DECISIONS.md`](schema/DECISIONS.md); the numbers below (D1, D20 …) point there.

### 1. Constructs, strategies and metrics, read like a research project
Think of how an empirical study is put together:

| In a study | In the wiki | How many |
|---|---|---|
| The variables a research question asks about | **Constructs**: what we want to know about, such as relevance, perceived usability or trust | Open-ended: there is no end to what one can ask about |
| The methodology | **Strategies**: how data is gathered and turned into a number | Few, and heavily reused, often renamed or rediscovered across fields, like popular software libraries |
| The measures defined to answer the question | **Metrics**: one page per operationalization | Many: every study defines or reuses some |

Metrics are the meeting points. A metric page names the constructs it measures and the method and route it uses, and inherits the caveats on those strategy pages instead of repeating them (D1, D10).

What follows from the cardinalities:
- **The construct DAG is curated, not complete.** It should have enough depth and breadth to show the structure, but it will never contain every possible construct. Constructs are added when a metric needs one.
- **Strategy pages are where care pays off most**, because one good page serves many metrics.
- **Metric pages should be cheap to write**, because they lean on the other two.

### 2. Constructs form a DAG with four roots
Constructs are arranged from broad to narrow. A construct can have several broader constructs (a DAG, not a tree), so a concept like trustworthiness can sit under both retrieval relevance and output quality without being duplicated (D3). Metrics have no hierarchy of their own: what looks like one is usually variants, parts or derivations, which the metric pages record as relations (D4).

The four roots are sorted by **what you need in order to measure the construct** (D12–D15):

| Root | What it covers | Measured with |
|---|---|---|
| [Component characteristics](constructs/component-characteristics.md) | One component judged on its own: a retriever, a classifier, a generator, a tool-calling module, an explanation method | Test data, no user |
| [System characteristics](constructs/system-characteristics.md) | What the whole system delivers: output quality, safety, fairness, robustness, responsiveness, cost | The system, no user pursuing a goal |
| [Task characteristics](constructs/task-characteristics.md) | A user using the system to reach a goal: effectiveness, efficiency, usability, experience, trust, reliance | People doing tasks |
| [User characteristics](constructs/user-characteristics.md) | The person alone, independent of any system: literacy, numeracy, background such as education | Tests of the person, or questions about them |

The roots also differ in **who controls the variable** (D24). Builders design and change components and systems. Task characteristics are outcomes of use. User characteristics are attributes no one controls: a study can only select or sample people, and uses these variables to explain differences in outcomes. That is why latent abilities such as numeracy are constructs for people, while machine capabilities such as math or reasoning are not (D23).

**Inside the component root**, constructs are typed by what the component takes in and puts out: classification (a label from a fixed set), closed answers (one correct answer per item), retrieval, generation, tool use and explanation. What the test data probes, such as knowledge or reasoning, is not a construct in the DAG; it belongs to the test data and is named in prose (D23).

The split exists because **gains at one level do not automatically carry over to the next**. Errors pile up between components, and a better system does not guarantee better outcomes for users. Effects that cross levels, such as faster responses shortening tasks, are recorded as empirical links on metric pages, not as edges in the DAG.

### 3. One metric page per computation per root
A page describes one operationalization. Variants that differ only in a parameter (precision@k, macro vs micro averaging) stay on the same page, and uses of the same computation in different fields go in section 3.1 (D5). A page can measure several constructs, as long as they sit under the same root (D6, D20).

When the same formula measures constructs under **different roots**, it gets one page per root, with titles qualified by how the number is obtained (D20). The canonical example is precision:

- [Precision (benchmark)](metrics/precision-benchmark.md): fixed queries and assessor judgments; measures a retrieval component's topical relevance.
- [Precision (user on task)](metrics/precision-user-task.md): the user's own queries and judgments; measures situational relevance of results for the user's task.

Only the formula is shared. Who sets the inputs, who judges, the construct, and the method all differ. The gap between them is a principal-agent problem: builders optimize the cheap benchmark number, users experience the task-level one, and the two are linked only empirically and weakly. Two pages let that link be stated as evidence. Method changes within a root (explicit judgments vs clicks) do not make a new page. The validator enforces the rule.

**Instruments are grouped, not paged** (D25). A standardized questionnaire or test is an instantiation of a metric. Instruments that measure the same construct with the same method share one page, titled by construct and method: [Perceived Usability Score (questionnaire)](metrics/perceived-usability-score.md) holds SUS, UMUX and UMUX-LITE. Each page lists its instruments in front matter and compares them in section 2.6; instrument names stay searchable as aliases.

**A metric page is a class; instruments are its objects** (D27). The page fixes what every instrument shares: construct, method, route, the computation with its parameters, and the caveats. An instrument fixes the content: the items, or the benchmark's inputs and references. What an instrument probes, such as math reasoning for GSM8K, belongs to the instrument, so the 2.6 lists are grouped by it. The lists are representative, not complete.

### 4. Strategies have two layers
- **Methods** say how data is gathered: benchmarks (also called test collections or labeled datasets), logs and telemetry, questionnaires, task studies, ability tests, adversarial testing, controlled comparison. The full list is `research_method` in the vocabulary; not every method has a page yet (D18).
- **Routes** say how data becomes a number: direct reading, self-rating, external judgment, comparison against reference data, comparative judgment, difference scoring, coding qualitative data, statistical modeling (D10).

Keeping the layers apart matters because the same data can be scored in different ways (questionnaire answers can be self-ratings, coded text or test answers scored against a key), and each layer carries its own caveats: sampling and recording on method pages, scoring on route pages.

**Comparisons.** When a metric *is* a difference between conditions, such as a drop under perturbed inputs or a gap between groups, the method is [controlled comparison](strategies/controlled-comparison.md) and the route is [difference scoring](strategies/difference-scoring.md). When a comparison only tests whether a metric differs (an A/B test on task time), that is study design and stays out of scope; so does the significance test itself, which is analysis rather than measurement (D21).

**Agreement statistics** such as Cohen's kappa, Krippendorff's alpha and the intraclass correlation describe the judges, not the system, task or user. They live in the reliability sections of route pages, not on metric pages (D21).

### 5. What the wiki deliberately does not model
- **Instrument details.** Instruments are listed and compared on metric pages (D25), but they get no pages of their own. The exact wording and layout of a questionnaire, or the code of an evaluation tool, stay with their authors and are cited.
- **Individual studies.** There are no records per paper and no map of construct-to-construct relationships; evidence is cited on metric pages and objective pages (D22).

### 6. Validity: light on the page, deep in conversation
Pages carry just enough validity content: whether the number is a direct or proxy measure (2.1), how reliable it is (2.2), what happens when people optimize it (4.3), and a `validity_concern` flag (low, moderate, high). The full set of validity questions belongs to an interactive interview, which asks them when they matter (D11).

When a metric is **a proxy with a known gap**, its page says so in plain terms: which decisions the number can support, which it cannot, and what to check before relying on it.

### 7. Honesty about evidence
- Every claim that is not common knowledge cites a source in [`references/bibliography.yaml`](references/bibliography.yaml), using author-year keys such as `[jarvelin2002]`. Citations are never invented.
- **Findings and hypotheses are kept apart.** A finding attributed to a paper whose details have not been checked is marked "(check against the paper)". A claim that no known source states is written as "Hypothesis:", followed by why it could be true and "(further reference needed)".
- Evidence strength for links to objectives is stated as causal, correlational, theoretical or none; theoretical links are called theoretical.
- References added by AI are marked `verified: false` until a person checks them.

### 8. Writing for readers
Plain language and short sentences, with jargon explained on first use. A metric known by an acronym is titled "Full Name (ACRONYM)", such as [Normalized Discounted Cumulative Gain (nDCG)](metrics/ndcg.md), and the full name appears again in its definition. Every heading in every template carries a note on the question it answers, collected in the [page guide](schema/page-guide.md) (D8).

## Layout

| Folder | Contents |
|---|---|
| [`docs/`](docs/wiki-map.md) | `wiki-map.md` (generated): every page linked from one place. |
| [`constructs/`](constructs/index.md) | One page per construct; `dag.yaml` (the DAG, hand-editable); `index.md` (generated diagram and tree). |
| `metrics/` | One page per metric. |
| `strategies/` | One page per route, and one per research method that has a page so far. |
| `objectives/` | One page per objective ([sustained use](objectives/sustained-use.md), [improved usability](objectives/improved-usability.md)), with the evidence linking metrics to it. |
| `schema/` | Templates for the three page types, `vocabulary.yaml` (allowed tag values), `page-guide.md` (generated), `DECISIONS.md` (decisions and their reasons). |
| `references/` | `bibliography.yaml`: every source that pages may cite. |
| `scripts/` | `validate.py` (checks everything), `build.py` (regenerates derived content), `sync_constructs.py` (keeps `dag.yaml` and construct pages in sync). |

Page types considered for later: task pages (for example "document search and summarization") and decision guides.

## How a page is structured

Each page has two parts:
1. **Front matter** (the YAML block at the top): short, comparable facts. On metric pages: the construct statement and the constructs it measures, direct vs proxy, research method and route, named instruments, how much validity deserves attention, cost, related metrics, and links to objectives. Scripts use these to build tables and lists.
2. **Body**: one section per question, with the same headings on every page of that type. The [page guide](schema/page-guide.md) lists every heading and the question it answers.

On metric pages, the construct is described as *property of subject in context*, tagged with five facets: `subject`, `aspect`, `perspective`, `quantity_form` and `context`. The free-text `construct.statement` is the authoritative definition, written at the level of the "spirit" of the measurement; tags are aids.

Related metrics (section 5) come in three kinds: operationally related (shared computation), conceptually related (same or related construct), and empirical co-movements (evidence of moving together), kept apart because evidence often contradicts what concepts suggest (D7).

### Generated content

Some content is generated and must not be edited by hand: blocks between `<!-- generated:...:start -->` and `<!-- generated:...:end -->` markers, `constructs/index.md`, `schema/page-guide.md` and `docs/wiki-map.md`. Run `python scripts/build.py` after changing front matter or templates.

### Editing the construct DAG

Edit structure (title, `broader`) either in a construct page or in `constructs/dag.yaml`, then run `python scripts/sync_constructs.py`. It compares both with the last synced state and copies the change across (D9). If both sides changed the same construct differently, or a construct was removed from the YAML, it stops without writing anything and says what to fix by hand; it never deletes a page. To rename, change the id in the YAML and add `renamed_from: <old id>`.

## Status and trust

Every page carries a `status`: `ai-draft` → `human-edited` → `human-reviewed` → `expert-verified`. Treat `ai-draft` pages as unchecked. Human edits are authoritative; AI assistants follow the rules in [`CLAUDE.md`](CLAUDE.md).

## Adding or editing a page

1. Copy the template from `schema/` (`metric-template.md`, `construct-template.md` or `strategy-template.md`) to the matching folder as `<id>.md`. For a new construct, adding an entry to `constructs/dag.yaml` and syncing creates the stub for you.
2. Fill in the front matter using values from `schema/vocabulary.yaml`.
3. Cite only keys that exist in `references/bibliography.yaml`; add new sources there first.
4. Run `python scripts/sync_constructs.py` (if constructs changed), then `python scripts/build.py`, then `python scripts/validate.py`, and fix what it reports.

## Viewing

The pages read well on GitHub, including the Mermaid diagrams. For a searchable site for readers who do not use GitHub, the plan is to publish with MkDocs Material (not set up yet).
