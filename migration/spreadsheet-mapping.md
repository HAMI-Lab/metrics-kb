# Migrating the spreadsheet into the wiki

Notes on how the three spreadsheet tabs (exported 21 Sept 2026) map onto this repo, what is missing, and data problems to fix. Rows are identified by their "Goal" text because the CSV has multi-line cells, so line numbers are unreliable.

## Key finding: the Metrics tab is organized by evaluation goal, not by metric

The "Metric name(s)" column is empty in every row. Each row instead describes an **evaluation goal studied by a group of sources** (for example "Assess calibration / uncertainty quality", with sources 4, 5, 6). One row usually covers several metrics, and one metric (for example accuracy or LLM-as-judge scores) appears in several rows.

So the migration is many-to-many, not one row to one page:
1. Extract candidate metrics from the "Strategy" and "Algorithm / model" columns (list below).
2. For each metric page, pull in the row text as raw material for the matching sections.
3. The rows themselves are closer to **aspects or constructs** (calibration, robustness, fairness, groundedness). They could seed construct pages later, or new values in the `aspect` vocabulary.

## Column mapping: Metrics tab → metric page

| Spreadsheet column | Goes to |
|---|---|
| Source | front matter `sources` (as `S<n>`) |
| Metric name(s) | (empty; see above) |
| Context (what was the system intended to DO?) | 1.2 context; 3.1 purposes |
| User context (WHO was it designed for?) | 3.2 assumed population; 4.2 consumers |
| Goal (what the authors WANT to understand) | `construct.statement`; 1.2 |
| Strategy (HOW they plan to measure it) | 2.4 computation |
| DIRECT or PROXY | `operationalization.measure_type`; 2.1 |
| ONLINE or OFFLINE | `operationalization.collection_mode`; 2.3 |
| DATA used | `operationalization.data_source`; 2.3 |
| ALGORITHM / MODEL | 2.4 computation |
| COMPONENT instrumented | `construct.subject` |

Slide questions with **no spreadsheet column**, which will need new drafting: 1.3 what it does not measure; 2.2 reliability; 2.5 unit; 3.2 assumptions (anchor for the unit, assumed user model); 4.1 cost; 4.3 misuse, gaming, Goodhart's law; 5.1 and 5.2 related metrics.

## Column mapping: Human vs. System tab → objective pages

This tab is organized **per source**, not per metric. Its columns are evidence about how each paper connects measurements to the business objectives:

| Spreadsheet column | Goes to |
|---|---|
| Specific metrics mentioned | which metric pages should cite this source |
| Proxy layer / Intermediate construct / Causal path | section 6 of those metric pages; "Theoretical paths" on objective pages |
| Alignment with Obj1 / Obj2 | objective pages, and `objectives` front matter of the relevant metrics |
| Longitudinal component? | evidence strength (longitudinal evidence is stronger for sustained use) |
| Strengths / Limitations | could become short source-note pages later (`references/notes/S13.md`) |

## Candidate metrics found in the spreadsheet

Pilot pages already written are marked ✓.

| Candidate metric | Spreadsheet sources |
|---|---|
| Precision ✓, Recall, F1, AUC-ROC | S24 |
| Accuracy / exact match | S4, S5, S6, S7, S22, S26 |
| ROUGE, BLEU, BERTScore, perplexity | S4, S6 |
| Expected calibration error | S4, S5, S6 |
| Attack success rate (jailbreak) | S8, S10 |
| Toxicity score | S5, S6, S8, S10, S37, S42 |
| Task success rate; pass@k | S10, S30, S31, S32, S36, S38 |
| Tool-call accuracy | S10, S30, S32 |
| Faithfulness / answer relevance (RAG) | S34 |
| Explanation faithfulness (AOPC, sufficiency, comprehensiveness) | S1, S14, S15, S16 |
| LLM-judge agreement with humans | S9, S25 |
| Response Latency ✓, throughput, token cost | S4, S5, S10, S31 |
| Energy use, CO2e | S39, S31 |
| Trust scales; reliance behavior | S13, S15, S17, S18 |
| SUS ✓ | S13 |
| NASA-TLX ✓ | S13, S15, S18 |
| TAM perceived usefulness / ease of use | S13 |
| User Engagement Scale | S13 |
| Task Completion Time ✓ (time-on-task, time-to-diagnosis) | S13, S15, S17, S18, S19, S20, S21 |
| Clinical decision accuracy with AI | S19, S20, S21 |
| Communication graph metrics (multi-agent) | S35 |

Observation: the spreadsheet leans heavily toward LLM, agent, and XAI evaluation. Classic interactive-systems metrics from IR, recommender systems, and visualization (for example nDCG, click-through rate, dwell time, retention, insight-based measures) are mostly absent and would need new sources.

## Data problems to fix

**Sources tab**
- S2 is an empty row (type "book", no name or link).
- S27 has stray line breaks in its name (cleaned in the bibliography).

**Human vs. System tab**
- 6 of the 10 filled rows have no Source ID, although several give it in the paper text ("Source 29", "Source 31", "Source 35", "Source 37"). Patterson et al. 2021 matches S39.
- "Humer et al., 2024" has the same arXiv link (2502.09849) as "Gambetti et al." (S18). One of the two links is probably wrong.
- "Gambetti et al., 2026" is cited with a 2025 arXiv number; check which version and year to cite.
- Several empty rows between entries.

**Metrics tab**
- "Metric name(s)" is empty throughout.
- The first three rows (helpfulness; high school math; user search completion time) have no source.
- Two rows have no DIRECT/PROXY value (the correctness/helpfulness/coherence row and the agent observability row).
- The "benchmark performance and evaluation coverage" row (S22, S26) lists "accuracy, VQA score, SPICE" as its algorithm, apparently copied from the multimodal row; HellaSwag is text-only.
- Typos in several cells ("qualuty", "sysetm", "correctnedss").
