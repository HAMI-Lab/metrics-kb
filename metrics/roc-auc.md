---
id: roc-auc
title: "Area Under the ROC Curve (ROC-AUC)"
aliases: [ROC-AUC, AUC, AUROC, area under the ROC curve, c-statistic]
page_type: metric
template_version: "0.3"
fields: [machine-learning, healthcare]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a component's scores separate positive cases from negative ones, across all decision thresholds."
  measures: [classification-correctness]
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
  data_source: [reference-answers]
  unit: "probability"
  range: "0-1 (0.5 = chance)"
  better: higher
  validity_concern: {level: moderate, note: "Summarizes all thresholds, including ones nobody would use; optimistic under heavy class imbalance."}
  instruments: []

cost:
  level: low
  requires: ["a labeled test set", "scores, not just labels"]
  automatable: true

related:
  - {metric: accuracy, kind: conceptual, note: "Accuracy judges one threshold; AUC judges the ranking."}
  - {metric: expected-calibration-error, kind: conceptual, note: "AUC ignores whether scores are calibrated."}
  - {metric: precision-benchmark, kind: conceptual, note: "Precision-recall curves are preferred when positives are rare."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Through output quality; not measured."}

sources: [fawcett2006, guo2023, nastoska2025]
---

# Area Under the ROC Curve (ROC-AUC)

> The probability that the component scores a random positive case above a random negative one.

## 1. What is measured

### 1.1 Definition
The receiver operating characteristic (ROC) curve plots the true-positive rate against the false-positive rate as the decision threshold moves. ROC-AUC is the area under it, which equals the chance that a randomly chosen positive case gets a higher score than a randomly chosen negative case [fawcett2006].

### 1.2 Construct: property of subject in context
The property is how well the component's scores rank positives above negatives. The subject is a scoring classifier. The context is a labeled test set.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Classification effectiveness: correctness](../constructs/classification-correctness.md) (under Component characteristics → Component performance → Classification performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not judge any single decision threshold, which is what users actually experience. It ignores whether scores are calibrated probabilities.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for ranking quality; **proxy** for performance at the threshold that will be used, hence `mixed`. With very rare positives, AUC can look high while precision at useful thresholds is poor; precision-recall curves show this better [nastoska2025].

### 2.2 Reliability
Stable with many cases of each class; with few positives, intervals are wide.

### 2.3 Data collection and measurement error
Needs scores for each case, not only labels, on a labeled test set.

### 2.4 Computation
- Sort cases by score; AUC = share of positive-negative pairs ranked correctly (ties count half).
- Equivalent to the normalized Mann-Whitney U statistic [fawcett2006].
- PR-AUC (area under the precision-recall curve) is a related metric, not a variant.

### 2.5 Unit and scale
0 to 1, where 0.5 is chance and 1 is perfect separation.

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A hospital compares two sepsis-risk models by AUC on last year's admissions before choosing one to pilot.
- A content-moderation team reports AUC of an implicit hate-speech detector across thresholds while it is still deciding where to set the cut-off [guo2023].

### 3.2 Purposes
Comparing scoring models before a threshold is chosen; clinical prediction model reporting.

### 3.3 Assumptions
All thresholds matter equally; false positives and false negatives are weighed only through the threshold chosen later.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML engineers, clinical data scientists.

### 4.2 Consumers and decisions informed
Teams choosing models; reviewers of clinical prediction models.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
A high AUC is often read as "the model is accurate", though performance at the chosen threshold may be poor.

## 5. Related metrics

### 5.1 Operationally related metrics
Computed from the same scores as precision and recall at each threshold.

### 5.2 Conceptually related metrics
[Accuracy](accuracy.md) and [F1](f1-score.md) judge one threshold. [Expected Calibration Error](expected-calibration-error.md) judges the scores as probabilities, which AUC ignores.

<!-- generated:neighbours:start -->
- Same construct: [Accuracy](accuracy.md) (Classification effectiveness: correctness), [F1 Score](f1-score.md) (Classification effectiveness: correctness), [Precision (benchmark)](precision-benchmark.md) (Classification effectiveness: correctness), [Recall (benchmark)](recall-benchmark.md) (Classification effectiveness: correctness)
- Sibling construct: [Expected Calibration Error (ECE)](expected-calibration-error.md) (Classification performance: calibration)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
A model can improve AUC while getting worse calibrated, because AUC depends only on the order of scores.

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical, through output quality.

## 7. Sources
- [fawcett2006]: ROC analysis.
- [guo2023]: AUC in classification studies.
- [nastoska2025]: limits under class imbalance.

## Open questions and review notes
- None yet.
