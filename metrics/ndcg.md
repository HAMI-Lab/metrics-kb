---
id: ndcg
title: nDCG
aliases: [normalized discounted cumulative gain, "nDCG@k", DCG]
page_type: metric
template_version: "0.2"
fields: [information-retrieval, recommender-systems]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much useful material a ranking puts near the top, compared with the best possible ranking."
  measures: [relevance]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [test-collection]
  route: [reference-comparison, external-judgment]
  collection_mode: [offline]
  data_source: [relevance-judgments]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Assumes a particular model of how users scan a ranking; the gain values and discount are choices."}

cost:
  level: medium
  requires: ["graded relevance judgments"]
  automatable: true

related:
  - {metric: precision-test-collection, kind: conceptual, note: "Precision@k ignores order and grades within the top k."}
  - {metric: reciprocal-rank, kind: conceptual, note: "Looks only at the first relevant item."}
  - {metric: precision-user-task, kind: empirical, note: "Offline ranking gains need checking with users."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Better rankings are assumed to help users; offline-online links are weak."}

sources: [jarvelin2002, manning2008, liang2022, turpin2006]
---

# nDCG

> Graded relevance summed down a ranking, discounted by position, and scaled by the best possible ranking.

## 1. What is measured

### 1.1 Definition
Each result gets a gain for how relevant it is (for example 0, 1, 2, 3). Gains are summed down the ranking, with lower positions counting less. The sum is divided by the sum for an ideal ranking of the same items, so a perfect ranking scores 1 [jarvelin2002].

### 1.2 Construct: property of subject in context
The property is graded relevance of a ranking, weighted toward the top. The subject is a ranking component such as a search engine's ranker or a recommender. The context is a test collection with graded judgments [liang2022].

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Retrieval effectiveness: relevance](../constructs/relevance.md) (under Component characteristics → Component performance → Retrieval performance → Retrieval effectiveness)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not judge items the judges never saw. It does not measure whether users found what they needed, or diversity and novelty of results.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the stated gain-and-discount model; **proxy** for user satisfaction with the ranking. The logarithmic discount encodes an assumed user who reads down the list with declining attention [jarvelin2002].

### 2.2 Reliability
Stable rankings of systems with many queries; small query sets give large variance [manning2008].

### 2.3 Data collection and measurement error
Needs graded relevance judgments, usually from assessors on a test collection.

### 2.4 Computation
- DCG@k = Σ_{i=1..k} gain_i ÷ log₂(i + 1).
- nDCG@k = DCG@k ÷ ideal DCG@k.
- Some versions use gain 2^rel − 1 to weight highly relevant items more; report which.

### 2.5 Unit and scale
0 to 1. Comparable only with the same k, gain scale and judgments.

## 3. Why it is measured

### 3.1 Use cases
- A web search team reports nDCG@10 on its graded query set for each ranking release.
- A passage retriever for a RAG product is compared with nDCG@10 on MS MARCO-style judgments [liang2022].
- A music app compares two recommenders with nDCG using graded ratings.

### 3.2 Purposes
Comparing rankers with graded judgments; benchmark reporting.

### 3.3 Assumptions
Users scan from the top with declining attention; relevance of each item is independent of the others.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
IR and recommender engineers.

### 4.2 Consumers and decisions informed
Ranking teams; benchmark readers.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Gains in nDCG on a fixed collection can come from overfitting. Treating nDCG gains as user gains without checking [turpin2006].

## 5. Related metrics

### 5.1 Operationally related metrics
nDCG@k at different k, and the gain variants, are on this page.

### 5.2 Conceptually related metrics
[Precision (test collection)](precision-test-collection.md) ignores order and grades within the top k; [Reciprocal Rank](reciprocal-rank.md) looks only at the first relevant item.

<!-- generated:neighbours:start -->
- Narrower construct: [F1 Score](f1-score.md) (Retrieval effectiveness: topical relevance), [Precision (test collection)](precision-test-collection.md) (Retrieval effectiveness: topical relevance), [Recall (test collection)](recall-test-collection.md) (Retrieval effectiveness: topical relevance), [Reciprocal Rank (MRR)](reciprocal-rank.md) (Retrieval effectiveness: topical relevance)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: as with precision [turpin2006], gains in nDCG on a test collection may show small effects on what users achieve. Why it could be true: nDCG shares precision's fixed queries and assessor judgments, and users adapt by reformulating queries and reading further down. Evidence for nDCG specifically (further reference needed).

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical.

## 7. Sources
- [jarvelin2002]: cumulated gain.
- [manning2008]: IR evaluation.
- [liang2022]: nDCG in LLM retrieval benchmarks.
- [turpin2006]: offline measures vs user performance.

## Open questions and review notes
- Is nDCG a measure of relevance (graded) or of topical relevance? Linked to relevance for now because grades can encode more than topic.
