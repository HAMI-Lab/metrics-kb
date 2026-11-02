---
id: expected-calibration-error
title: Expected Calibration Error
aliases: [ECE, calibration error]
page_type: metric
template_version: "0.2"
fields: [machine-learning, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How far a component's stated confidence is from how often it is actually right."
  measures: [calibration]
  subject: [system-component]
  aspect: [effectiveness, trust]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [test-collection]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: lower
  validity_concern: {level: moderate, note: "Depends on the binning; a low value can hide large errors at rare confidence levels."}

cost:
  level: low
  requires: ["a labeled test set", "confidence scores"]
  automatable: true

related:
  - {metric: accuracy, kind: conceptual, note: "Calibration is judged against accuracy within each confidence bin."}
  - {metric: roc-auc, kind: conceptual, note: "AUC ignores calibration."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Users who are misled by confident errors may stop relying on the system."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Calibrated confidence lets users decide when to rely on outputs."}

sources: [guo2017, liang2022, brier1950]
---

# Expected Calibration Error

> The average gap between confidence and accuracy, over bins of predictions with similar confidence.

## 1. What is measured

### 1.1 Definition
Predictions are grouped by confidence, for example 0.0–0.1, 0.1–0.2 and so on. In each group, the average confidence is compared with the share of correct predictions. ECE is the average gap, weighted by how many predictions fall in each group [guo2017].

### 1.2 Construct: property of subject in context
The property is calibration: whether confidence can be taken at face value. The subject is a component that outputs confidence, such as a classifier or a language model answering questions [liang2022]. The context is a labeled test set.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Classification performance: calibration](../constructs/calibration.md) (under Component characteristics → Component performance → Classification performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure accuracy: a model that is always 60% confident and 60% right is perfectly calibrated and mediocre. It does not say whether people use the confidence well.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for average calibration. The number depends on the number and kind of bins, and averaging hides bins where the model is badly overconfident.

### 2.2 Reliability
Sensitive to bin choice and sample size: with few predictions per bin, the gaps are noisy.

### 2.3 Data collection and measurement error
Needs a confidence score per prediction. For language models, confidence may come from token probabilities or from asking the model, which give different results [liang2022].

### 2.4 Computation
- ECE = Σ over bins (n_bin ÷ n) × |accuracy_bin − confidence_bin| [guo2017].
- Maximum calibration error: the largest bin gap instead of the average.
- Equal-width or equal-mass bins; report which and how many.

### 2.5 Unit and scale
0 to 1 (often reported as a percentage). Lower is better.

## 3. Why it is measured

### 3.1 Use cases
- A medical-imaging team checks ECE before showing model confidence to radiologists, so that "90% confident" means something.
- An LLM team compares ECE of answers on a QA benchmark before and after fine-tuning, which often makes models more confident [liang2022].

### 3.2 Purposes
Deciding whether confidence can be shown to users or used to route cases to people; model comparison.

### 3.3 Assumptions
Confidence scores are meant to be probabilities. The test set represents the cases where confidence will be used.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML engineers and researchers.

### 4.2 Consumers and decisions informed
Teams deciding whether to show confidence or use it for deferral.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Post-hoc rescaling can lower ECE on the test set without making the model more useful.

## 5. Related metrics

### 5.1 Operationally related metrics
Maximum calibration error is a variant on this page.

### 5.2 Conceptually related metrics
The Brier score [brier1950] combines calibration and accuracy in one number. [Accuracy](accuracy.md) and [ROC-AUC](roc-auc.md) are complements.

<!-- generated:neighbours:start -->
- Sibling construct: [Accuracy](accuracy.md) (Classification effectiveness: correctness), [F1 Score](f1-score.md) (Classification effectiveness: correctness), [Precision (test collection)](precision-test-collection.md) (Classification effectiveness: correctness), [Recall (test collection)](recall-test-collection.md) (Classification effectiveness: correctness), [ROC-AUC](roc-auc.md) (Classification effectiveness: correctness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Modern neural networks are reported to be more accurate but worse calibrated than older ones (check against [guo2017]).

## 6. Links to business objectives
**Improved usability:** positive, theoretical: calibrated confidence supports appropriate reliance. **Sustained use:** positive, theoretical.

## 7. Sources
- [guo2017]: ECE and calibration of neural networks.
- [liang2022]: calibration in LLM evaluation.
- [brier1950]: the Brier score.

## Open questions and review notes
- Should the Brier score get its own page?
