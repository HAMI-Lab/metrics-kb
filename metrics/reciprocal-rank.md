---
id: reciprocal-rank
title: "Mean Reciprocal Rank (MRR)"
aliases: [MRR, reciprocal rank, "RR@k"]
page_type: metric
template_version: "0.3"
fields: [information-retrieval, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How near the top the first useful result appears."
  measures: [topical-relevance]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [benchmark]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [relevance-judgments, reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: low, note: "Direct for the position of the first relevant item; a fair proxy when one answer is enough."}

cost:
  level: low
  requires: ["relevance judgments or a known correct item per query"]
  automatable: true

related:
  - {metric: ndcg, kind: conceptual, note: "nDCG credits every relevant item, not only the first."}
  - {metric: precision-benchmark, kind: conceptual, note: "Precision@k counts relevant items regardless of order."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain."}
  improved-usability: {direction: positive, evidence: theoretical, note: "When one answer suffices, finding it sooner saves effort."}

sources: [voorhees1999, liang2022, mohammadi2025]
---

# Mean Reciprocal Rank (MRR)

> One divided by the rank of the first relevant result, averaged over queries.

## 1. What is measured

### 1.1 Definition
For each query, find the position of the first relevant result and take one divided by it: 1 if it is first, 0.5 if second, and so on. The mean over queries is the mean reciprocal rank (MRR) [voorhees1999].

### 1.2 Construct: property of subject in context
The property is how quickly a ranking reaches a relevant item. The subject is a ranker. The context is queries with a known correct item or judgments, often in question answering.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Retrieval effectiveness: topical relevance](../constructs/topical-relevance.md) (under Component characteristics → Component performance → Retrieval performance → Retrieval effectiveness → Retrieval effectiveness: relevance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It ignores every relevant item after the first, so it is a poor fit when users need several.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the position of the first relevant item; a reasonable proxy for effort when one answer is enough, such as finding a known page or answer.

### 2.2 Reliability
High variance per query (it jumps from 1 to 0.5); needs many queries.

### 2.3 Data collection and measurement error
A test collection with at least one known relevant item per query.

### 2.4 Computation
- RR = 1 ÷ rank of the first relevant item (0 if none in the top k).
- MRR = mean of RR over queries; RR@k cuts off at k [liang2022].

### 2.5 Unit and scale
0 to 1.

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A QA system's passage ranker is scored by MRR@10 on question-passage pairs.
- An agent's tool retriever is checked with MRR: how high does the right tool appear among candidates [mohammadi2025]?

### 3.2 Purposes
Evaluating known-item search and question answering.

### 3.3 Assumptions
The user stops at the first relevant item.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
IR engineers.

### 4.2 Consumers and decisions informed
Ranking and QA teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing MRR can push one strong result up while hurting the rest of the ranking.

## 5. Related metrics

### 5.1 Operationally related metrics
RR@k is a variant on this page.

### 5.2 Conceptually related metrics
[nDCG](ndcg.md) credits all relevant items with grades; [Precision (benchmark)](precision-benchmark.md) ignores order.

<!-- generated:neighbours:start -->
- Same construct: [F1 Score](f1-score.md) (Retrieval effectiveness: topical relevance), [Precision (benchmark)](precision-benchmark.md) (Retrieval effectiveness: topical relevance), [Recall (benchmark)](recall-benchmark.md) (Retrieval effectiveness: topical relevance)
- Broader construct: [Normalized Discounted Cumulative Gain (nDCG)](ndcg.md) (Retrieval effectiveness: relevance)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical.

## 7. Sources
- [voorhees1999]: MRR in the TREC QA track.
- [liang2022]: RR@k in retrieval benchmarks.
- [mohammadi2025]: MRR for tool ranking.

## Open questions and review notes
- None yet.
