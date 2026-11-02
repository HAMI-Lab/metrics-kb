---
id: f1-score
title: F1 Score
aliases: [F1, F-measure, F-score, token-overlap F1, F-beta]
page_type: metric
template_version: "0.2"
fields: [machine-learning, information-retrieval, nlp, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "A single score that is high only when a component's positive outputs are both correct and complete."
  measures: [classification-correctness, topical-relevance, answer-correctness]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [test-collection]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers, relevance-judgments]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Hides which of precision or recall is weak; equal weighting is a choice, not a fact."}

cost:
  level: low
  requires: ["a labeled test set or reference answers"]
  automatable: true

related:
  - {metric: precision-test-collection, kind: operational, note: "F1 is the harmonic mean of precision and recall."}
  - {metric: recall-test-collection, kind: operational, note: "F1 is the harmonic mean of precision and recall."}
  - {metric: accuracy, kind: conceptual, note: "Preferred over accuracy when classes are imbalanced."}
  - {metric: rouge, kind: conceptual, note: "Token-overlap F1 and ROUGE both count overlap with a reference."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Through output quality; not measured."}

sources: [vanrijsbergen1979, rajpurkar2016, liang2022, guo2023]
---

# F1 Score

> The harmonic mean of precision and recall: high only when both are high.

## 1. What is measured

### 1.1 Definition
F1 combines [precision](precision-test-collection.md) and [recall](recall-test-collection.md) into one number, their harmonic mean [vanrijsbergen1979]. The same formula is used on different units: predicted labels in classification, retrieved items in search, and words in generated answers compared with a reference answer (token-overlap F1) [rajpurkar2016; liang2022].

### 1.2 Construct: property of subject in context
The property is correctness and completeness of a component's positive outputs together. The subject is a classifier, retriever, or answer generator. The context is a test set with references.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Classification effectiveness: correctness](../constructs/classification-correctness.md) (under Component characteristics → Component performance → Classification performance)
- [Retrieval effectiveness: topical relevance](../constructs/topical-relevance.md) (under Component characteristics → Component performance → Retrieval performance → Retrieval effectiveness → Retrieval effectiveness: relevance)
- [Closed-answer performance: answer correctness](../constructs/answer-correctness.md) (under Component characteristics → Component performance → Closed-answer performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not say which of precision or recall is the problem. It ignores true negatives, so it says nothing about how well the component rejects negatives. Token-overlap F1 rewards shared words, not correct meaning.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the combined criterion. Equal weight on precision and recall is a choice; F-beta weights recall *beta* times as much [vanrijsbergen1979]. Token-overlap F1 for answers gives partial credit but can reward wordy answers that share words with the reference [guo2023].

### 2.2 Reliability
As stable as precision and recall on the same set.

### 2.3 Data collection and measurement error
As for [precision](precision-test-collection.md): run on a test collection and compare with references.

### 2.4 Computation
- F1 = 2 × precision × recall ÷ (precision + recall).
- F-beta = (1 + β²) × P × R ÷ (β² × P + R).
- Macro F1: the mean of per-class F1; micro F1: F1 on pooled counts.
- Token-overlap F1: precision and recall over the words shared by answer and reference, averaged over questions [rajpurkar2016].

### 2.5 Unit and scale
A proportion from 0 to 1. Report the averaging (macro or micro) and the unit counted.

## 3. Why it is measured

### 3.1 Use cases
- A hate-speech classifier for a social platform is compared across models with macro F1, because hateful posts are rare [guo2023].
- A reading-comprehension benchmark scores short answers with token-overlap F1 so that partly right answers earn partial credit [rajpurkar2016].
- A clinical NLP team reports F1 for extracting medication names from discharge notes.

### 3.2 Purposes
Model comparison, especially with imbalanced classes; benchmark reporting.

### 3.3 Assumptions
Precision and recall matter equally unless beta says otherwise. The references are complete and correct.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML and IR engineers and researchers.

### 4.2 Consumers and decisions informed
Teams comparing models; benchmark readers.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
A model can be tuned to the threshold that maximizes F1 on the test set, which overstates it on new data. Reporting F1 alone hides a precision-recall trade-off that users care about.

## 5. Related metrics

### 5.1 Operationally related metrics
Built from [Precision (test collection)](precision-test-collection.md) and [Recall (test collection)](recall-test-collection.md). F-beta and macro/micro averages are variants on this page.

### 5.2 Conceptually related metrics
[Accuracy](accuracy.md) is a simpler alternative when classes are balanced. [ROUGE](rouge.md) also counts overlap with a reference, for longer texts.

<!-- generated:neighbours:start -->
- Same construct: [Accuracy](accuracy.md) (Classification effectiveness: correctness), [Area Under the ROC Curve (ROC-AUC)](roc-auc.md) (Classification effectiveness: correctness), [Precision (test collection)](precision-test-collection.md) (Classification effectiveness: correctness), [Recall (test collection)](recall-test-collection.md) (Classification effectiveness: correctness), [Mean Reciprocal Rank (MRR)](reciprocal-rank.md) (Retrieval effectiveness: topical relevance), [pass@k](pass-at-k.md) (Closed-answer performance: answer correctness)
- Broader construct: [Normalized Discounted Cumulative Gain (nDCG)](ndcg.md) (Retrieval effectiveness: relevance)
- Sibling construct: [Expected Calibration Error (ECE)](expected-calibration-error.md) (Classification performance: calibration)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Moves with whichever of precision or recall is lower, because the harmonic mean is pulled toward the smaller value.

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical, through output quality.

## 7. Sources
- [vanrijsbergen1979]: the F-measure.
- [rajpurkar2016]: token-overlap F1.
- [liang2022]: F1 in LLM benchmarks.
- [guo2023]: F1 in classification surveys.

## Open questions and review notes
- Token-overlap F1 gives partial credit for closed answers (answer correctness), while classification F1 measures label correctness. Both are component level, so D20 keeps them on one page. Is that the right call, or does the unit change enough to split (D5)?
