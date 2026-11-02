---
id: logs-telemetry
title: Interaction logs and telemetry
aliases: [log analysis, usage data, instrumentation, online evaluation data]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [webb1966, hornbaek2006, kohavi2020, chapelle2012, hofmann2016, chuklin2015, dean2013]
---

# Interaction logs and telemetry

> A running system records what users and the system did: queries, clicks, errors, timings.

## 1. What it is

### 1.1 Definition
Logs are records written by a system while people use it in the normal way. Client logs record user actions such as queries, clicks, scrolls and edits. Server telemetry records what the system did, such as response times, errors and resource use. Nobody is asked anything, and recording happens whether or not a study is running.

### 1.2 Typical pairings
Counts, durations and rates are read directly. Statistical models infer quantities that are not logged, such as relevance from clicks. Logs also hold the outcomes of side-by-side comparisons on live traffic, and samples of logged outputs can be sent to judges.
<!-- generated:pairings:start -->
- [Comparative judgment: preferences and interleaving](comparative-judgment.md)
- [Direct reading: timing and counting](direct-reading.md)
- [External judgment: annotators, experts, model judges, simulated users](external-judgment.md)
- [Statistical and latent-variable modeling](statistical-modeling.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Online controlled experiments (A/B tests)**: users are split between versions and logged outcomes are compared [kohavi2020]. The split is study design, which is out of scope here; the logs are the data.
- **Interleaving**: results from two rankers are mixed in one list, and clicks show which one users prefer [chapelle2012; hofmann2016].
- **Click models**: statistical models that separate how relevant a result is from how likely it is to be seen [chuklin2015].
- **Latency telemetry**: response times reported as percentiles, because the slowest requests matter most at scale [dean2013].

## 2. When to use it
Use it when the construct is behaviour or system performance in real use, at scale, and when the measurement should not change behaviour: logs are non-reactive [webb1966]. Prefer another method when the question is why people acted, how they felt, or whether they reached their goal.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
Logs record actions, not intentions or outcomes. A click is not a relevant result, and a long session can mean engagement or struggle. Where a task starts and ends is often unclear [hornbaek2006]. Only what was instrumented exists, and only people who kept using the system are in the data: those who gave up early are mostly absent.

### 3.2 Reliability
Logging code changes between releases, which can break comparisons over time. Bots, test traffic and dropped events add noise. Checks include A/A tests, where both groups get the same version and should not differ, and checks on totals that should not change [kohavi2020].

### 3.3 Bias and gaming
Users click higher-ranked results more often regardless of quality, so raw clicks favour whatever is already on top [chuklin2015]. Numbers from logs are easy to push directly: designs can raise clicks or time on site without helping anyone. Privacy rules limit what can be logged and kept, which shapes what can be measured.

## 4. Cost
Low per measurement once instrumented. The costs are engineering time to add and maintain logging, storage, and privacy review. It needs a deployed system with enough traffic.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Cost per Task](../metrics/cost-per-task.md)
- [Demographic Parity Difference (DPD)](../metrics/demographic-parity-difference.md)
- [Precision (user on task)](../metrics/precision-user-task.md)
- [Response Latency](../metrics/response-latency.md)
- [Task Completion Time](../metrics/task-completion-time.md)
- [Toxicity Rate](../metrics/toxicity-rate.md)
<!-- generated:metrics:end -->

## 6. Sources
- [webb1966]: non-reactive measures.
- [hornbaek2006]: ambiguity of task boundaries in usability measurement.
- [kohavi2020]: online controlled experiments, A/A tests and data checks.
- [chapelle2012], [hofmann2016]: interleaving and online evaluation in IR.
- [chuklin2015]: click models and position bias.
- [dean2013]: tail latency at scale.

## Open questions and review notes
- Client logs and server telemetry share one vocabulary value. Split them if their caveats keep diverging.
