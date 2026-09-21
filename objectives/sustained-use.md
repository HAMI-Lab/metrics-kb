---
id: sustained-use
title: "Objective 1: Sustained Use Over Time"
page_type: objective
template_version: "0.1"
status: ai-draft
sources: [davis1989, bhattacherjee2001, kohavi2020, S13, S17, S18]
---

# Objective 1: Sustained Use Over Time

> People keep choosing to use the system over weeks and months, not just in a first trial.

## What it means
Continued, voluntary use by the intended users. It is observed directly only over time, through return visits, retention, frequency of use, or continued reliance on the system's outputs. It is a business objective, not a metric: several metrics can stand in for it, and none captures it fully.

## How it can be observed directly
Retention and churn rates, active users over time, frequency and recency of use, and whether users keep acting on the system's outputs. These need longitudinal logs from a deployed system. (No metric pages for these yet.)

## Why proxies are used instead
Direct measures take months, need a deployed product, and arrive too late to guide early design. So teams use earlier signals and assume they predict continued use. The spreadsheet's review of sources found that most user studies stop at intention to use rather than logged continued use [S13], and that longitudinal studies are recommended but rare [S17; S18].

## Theoretical paths
- Perceived usefulness and ease of use → intention to use (Technology Acceptance Model) [davis1989].
- Satisfaction and confirmed expectations → intention to continue (expectation-confirmation model) [bhattacherjee2001].
- For AI systems: reliability and trust → reliance → continued use (argued in several sources in the spreadsheet; not yet cited here).

## Metrics linked to this objective
This table is maintained by hand for now; a script can later generate it from each metric's `objectives` front matter.

| Metric | Direction | Evidence | Note |
|---|---|---|---|
| [Response Latency](../metrics/response-latency.md) | negative | causal (web search) | Online experiments [kohavi2020] |
| [SUS](../metrics/system-usability-scale.md) | positive | theoretical | Via TAM / satisfaction |
| [NASA-TLX](../metrics/nasa-tlx.md) | negative | theoretical | |
| [Precision](../metrics/precision.md) | positive | theoretical | Long causal chain |
| [Task Completion Time](../metrics/task-completion-time.md) | unknown | none | Could go either way |

## Open questions
- Which direct measure of sustained use should the wiki treat as the reference (for example 30-day retention)? It likely differs by system type.
