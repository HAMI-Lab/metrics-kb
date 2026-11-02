---
id: mean-average-precision
title: Mean Average Precision (MAP)
aliases: [MAP, mAP, average precision, AP, "MAP@k"]
page_type: metric
template_version: "0.3"
fields: [information-retrieval, recommender-systems]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a ranking places all the relevant items near the top, averaged over queries."
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
  route: [reference-comparison, external-judgment]
  collection_mode: [offline]
  data_source: [relevance-judgments]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Direct for binary relevance judgments on a ranking; a weak proxy for whether results help users' tasks, like precision."}
  instruments:
    - {name: "TREC ad hoc collections", kind: content, sources: [manning2008], probes: "topical relevance for ad hoc search", scale: "MAP, 0-1", note: "Queries, documents and pooled binary judgments; MAP was the main measure for many years."}

cost:
  level: medium
  requires: ["relevance judgments (costly to create once, cheap to reuse)"]
  automatable: true

related:
  - {metric: precision-benchmark, kind: operational, note: "Average precision averages precision at the rank of each relevant item."}
  - {metric: recall-benchmark, kind: operational, note: "Rewards finding all relevant items, so it depends on recall too."}
  - {metric: ndcg, kind: conceptual, note: "Uses graded rather than binary relevance."}
  - {metric: reciprocal-rank, kind: conceptual, note: "Looks only at the first relevant item."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain through better rankings."}
  improved-usability: {direction: positive, evidence: correlational, note: "Batch effectiveness gains do not always reach users' tasks."}

sources: [manning2008, turpin2006]
---

# Mean Average Precision (MAP)

> The mean, over queries, of the average of precision values taken at the rank of each relevant item.

## 1. What is measured

### 1.1 Definition
Mean Average Precision (MAP) summarizes a ranking's quality over all relevant items. For one query, average precision (AP) is the mean of the precision values at the rank of each relevant item, with relevant items never retrieved counting as zero. MAP is the mean of AP over queries [manning2008].

### 1.2 Construct: property of subject in context
The property is topical relevance of a ranking, rewarding relevant items found early and found at all. The subject is a ranking component. The context is a benchmark with binary relevance judgments.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Retrieval effectiveness: topical relevance](../constructs/topical-relevance.md) (under Component characteristics → Component performance → Retrieval performance → Retrieval effectiveness → Retrieval effectiveness: relevance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Graded relevance (see [nDCG](ndcg.md)). How results are presented or used.

Not to be confused with **mAP in object detection**, a different computation over bounding boxes; it is outside the wiki's scope (D29).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the ranking against binary judgments; a weak proxy for whether results help users, as with [precision](precision-benchmark.md) [turpin2006].

**Using a proxy with a known gap.** MAP can compare retrieval components on the same benchmark. It cannot show that users will finish search tasks faster or better; check that with a task study.

### 2.2 Reliability
Averaging over many queries gives stable system rankings on the same collection (check against [manning2008]).

### 2.3 Data collection and measurement error
Run the system on the benchmark's queries. Unjudged documents in pooled collections count as non-relevant, which penalizes systems unlike the pooled ones.

### 2.4 Computation
- AP for one query: mean of precision@*r* over the ranks *r* of the relevant items; unretrieved relevant items contribute 0.
- MAP = mean of AP over queries.
- MAP@k cuts the ranking at *k*.

### 2.5 Unit and scale
A proportion from 0 to 1. Comparable only within one collection and judgment set.

### 2.6 Instruments
**Ad hoc search**
- **TREC ad hoc collections** [manning2008]: queries, documents and pooled binary judgments; MAP was a main reported measure.

## 3. Why it is measured

### 3.1 Use cases
- A search team compares two retrieval models on a TREC collection before an online test.
- A recommender team reports MAP@10 on held-out interactions.

### 3.2 Purposes
Comparing ranking components; regression testing.

### 3.3 Assumptions
Binary relevance is enough; all relevant items matter to the user.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
IR and recommender researchers and engineers.

### 4.2 Consumers and decisions informed
Teams choosing ranking components.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Overfitting to a fixed collection. Treating gains as user-experienced gains.

## 5. Related metrics

### 5.1 Operationally related metrics
Built from [Precision (benchmark)](precision-benchmark.md) at the rank of each relevant item; depends on [Recall (benchmark)](recall-benchmark.md).

### 5.2 Conceptually related metrics
[nDCG](ndcg.md) uses graded relevance; [MRR](reciprocal-rank.md) looks only at the first relevant item.

<!-- generated:neighbours:start -->
- Same construct: [F1 Score](f1-score.md) (Retrieval effectiveness: topical relevance), [Mean Reciprocal Rank (MRR)](reciprocal-rank.md) (Retrieval effectiveness: topical relevance), [Precision (benchmark)](precision-benchmark.md) (Retrieval effectiveness: topical relevance), [Recall (benchmark)](recall-benchmark.md) (Retrieval effectiveness: topical relevance)
- Broader construct: [Normalized Discounted Cumulative Gain (nDCG)](ndcg.md) (Retrieval effectiveness: relevance)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: as with precision [turpin2006], MAP gains may show small effects on what users achieve. Why it could be true: MAP shares precision's fixed queries and assessor judgments (further reference needed).

## 6. Links to business objectives
**Improved usability:** positive, correlational and weak. **Sustained use:** positive, theoretical.

## 7. Sources
- [manning2008]: definition; TREC.
- [turpin2006]: batch effectiveness vs user outcomes.

## Open questions and review notes
- None yet.
