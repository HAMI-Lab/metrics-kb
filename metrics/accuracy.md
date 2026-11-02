---
id: accuracy
title: Accuracy
aliases: [classification accuracy, exact match, EM, quasi-exact match]
page_type: metric
template_version: "0.3"
fields: [machine-learning, llm-evaluation, nlp]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of all the cases a component answers or labels, the share it gets exactly right."
  measures: [classification-correctness, answer-correctness]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [benchmark]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Direct for agreement with the labels; misleading when classes are imbalanced or the label set is wrong (see 2.1)."}
  instruments:
    - {name: "Massive Multitask Language Understanding (MMLU)", sources: [hendrycks2021, gema2024], probes: "knowledge across academic and professional subjects", scale: "proportion, 0-1", note: "Four-option multiple-choice questions in 57 subjects."}
    - {name: "Grade School Math 8K (GSM8K)", sources: [cobbe2021, zhang2024], probes: "multi-step math reasoning", scale: "proportion, 0-1", note: "Math word problems with a numeric final answer, checked by exact match."}
    - {name: "HellaSwag", sources: [zellers2019], probes: "commonsense reasoning about everyday situations", scale: "proportion, 0-1", note: "Choose the most plausible continuation of a scene among four."}
    - {name: "TruthfulQA (multiple-choice)", sources: [lin2022], probes: "avoiding common misconceptions", scale: "proportion, 0-1", note: "Questions written so that a popular false answer is tempting."}
    - {name: "Stanford Question Answering Dataset (SQuAD)", sources: [rajpurkar2016], probes: "reading comprehension", scale: "proportion, 0-1 (exact match)", note: "Answer spans extracted from Wikipedia paragraphs."}
    - {name: "Holistic Evaluation of Language Models (HELM)", sources: [liang2022], probes: "many scenarios at once", scale: "aggregates of per-scenario scores", note: "A suite of scenarios and metrics; reports per-scenario results and aggregates."}

cost:
  level: low
  requires: ["a labeled test set"]
  automatable: true

related:
  - {metric: f1-score, kind: conceptual, note: "Balances precision and recall; preferred when classes are imbalanced."}
  - {metric: precision-benchmark, kind: conceptual, note: "Looks only at predicted positives."}
  - {metric: roc-auc, kind: conceptual, note: "Judges ranking across all thresholds instead of one decision."}
  - {metric: expected-calibration-error, kind: conceptual, note: "Whether confidence matches accuracy."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain through output quality."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Correct components are a precondition for effective tasks; the link to user outcomes is not measured."}

sources: [liang2022, rajpurkar2016, chang2024, nastoska2025, guo2017, hendrycks2021, gema2024, cobbe2021, zhang2024, zellers2019, lin2022, batzner2026]
---

# Accuracy

> The share of cases a component gets exactly right, compared with reference answers.

## 1. What is measured

### 1.1 Definition
Accuracy is the number of correct answers or labels divided by the number of cases. For generated answers it is usually called **exact match**: the answer counts as correct only if it equals the reference after normalization, such as lower-casing and removing punctuation [rajpurkar2016; liang2022].

### 1.2 Construct: property of subject in context
The property is correctness of single outputs. The subject is a component such as a classifier (one label set for all items) or a model answering closed questions (each question has its own correct answer: an option, a number, a short span). The context is a labeled test set.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Classification effectiveness: correctness](../constructs/classification-correctness.md) (under Component characteristics → Component performance → Classification performance)
- [Closed-answer performance: answer correctness](../constructs/answer-correctness.md) (under Component characteristics → Component performance → Closed-answer performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It gives no partial credit, so a nearly right answer counts the same as a wrong one (token-overlap F1 gives partial credit). It does not say which classes the errors fall in. It is not decision accuracy of a person using the component; that is a task-level metric.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for agreement with the labels. With imbalanced classes, a component that always predicts the common class can score high while missing every rare case [nastoska2025]. For generated answers, exact match counts a correct answer phrased differently as wrong, so normalization rules matter [liang2022].

### 2.2 Reliability
Stable once the test set is fixed. Small test sets give wide intervals; report them.

### 2.3 Data collection and measurement error
Run the component on a benchmark with reference labels or answers. Errors in the labels count against the component.

### 2.4 Computation
- Accuracy = correct ÷ all cases.
- Exact match: correct after the stated normalization; quasi-exact match uses looser normalization rules [liang2022].
- Balanced accuracy: the mean of per-class accuracy, for imbalanced classes.

### 2.5 Unit and scale
A proportion from 0 to 1. Compare with the accuracy of always predicting the most common class.

### 2.6 Instruments
Representative benchmarks, grouped by what they probe (D27). All report accuracy as a proportion from 0 to 1, but accuracy on one benchmark is not comparable with accuracy on another.

**Knowledge**
- **MMLU** [hendrycks2021]: four-option multiple-choice questions in 57 academic and professional subjects. Chance is 0.25. Some questions and answer keys are wrong, which caps the attainable score and blurs differences between strong models [gema2024] (check against the paper).

**Math reasoning**
- **GSM8K** [cobbe2021]: grade-school math word problems that need several steps; the final number is compared with the key after extraction from the model's text. Some models score markedly lower on a freshly written set of similar problems, which suggests contamination of the original set [zhang2024] (check against the paper).

**Commonsense reasoning**
- **HellaSwag** [zellers2019]: choose the most plausible continuation of a described situation among four, with wrong options chosen to fool models.

**Truthfulness**
- **TruthfulQA** [lin2022], multiple-choice form: questions where a common misconception gives a tempting wrong answer. It probes whether a model repeats popular falsehoods, not general knowledge.

**Reading comprehension**
- **SQuAD** [rajpurkar2016]: answer a question with a span from a given Wikipedia paragraph; scored by exact match after normalization (and by token-overlap [F1](f1-score.md)).

**Suites (aggregates over benchmarks)**
- **HELM** [liang2022]: runs many scenarios, each with its own benchmark, and reports per-scenario results alongside aggregates.

**Caution: an average over benchmarks measures no single construct (D30).** It mixes different demands, scales and chance levels, a change can come from any one member, and the weights are the suite authors' choice. Read the member scores before drawing a conclusion from the average.

The full catalog of benchmarks is far larger; registries such as the one behind Every Eval Ever list them [batzner2026].

## 3. Why it is measured

### 3.1 Use cases
- A bank's intent classifier routes customer messages; the team checks accuracy on last month's hand-labeled messages before each model update.
- An LLM team reports exact match on a short-answer question set to compare two prompt formats.
- A sentiment model for product reviews is compared with the accuracy of always predicting "positive", which is high because most reviews are positive.

### 3.2 Purposes
Model selection, regression testing, benchmark reporting [liang2022; chang2024].

### 3.3 Assumptions
Every error costs the same, and the labels are right. The test set represents the cases the component will see.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML engineers and researchers.

### 4.2 Consumers and decisions informed
Teams choosing between models and deciding whether a model is good enough to ship.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
High accuracy on imbalanced data hides failure on rare cases. Benchmarks reused for tuning overstate accuracy on new data.

## 5. Related metrics

### 5.1 Operationally related metrics
Exact match and balanced accuracy are variants on this page. [F1](f1-score.md) is computed from the same confusion table.

### 5.2 Conceptually related metrics
[F1](f1-score.md) and [Precision (benchmark)](precision-benchmark.md) are substitutes when classes are imbalanced. [ROC-AUC](roc-auc.md) complements it by ignoring the threshold.

<!-- generated:neighbours:start -->
- Same construct: [Area Under the ROC Curve (ROC-AUC)](roc-auc.md) (Classification effectiveness: correctness), [F1 Score](f1-score.md) (Classification effectiveness: correctness), [Precision (benchmark)](precision-benchmark.md) (Classification effectiveness: correctness), [Recall (benchmark)](recall-benchmark.md) (Classification effectiveness: correctness), [pass@k](pass-at-k.md) (Closed-answer performance: answer correctness)
- Sibling construct: [Expected Calibration Error (ECE)](expected-calibration-error.md) (Classification performance: calibration)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Accuracy and calibration can move apart: more accurate models are not necessarily better calibrated (check against [guo2017]).

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical, through output quality. No direct evidence recorded here.

## 7. Sources
- [liang2022]: exact match and accuracy in LLM benchmarks.
- [rajpurkar2016]: exact match for question answering.
- [chang2024]: accuracy in LLM evaluation.
- [nastoska2025]: class imbalance.

## Open questions and review notes
- Accuracy of a whole system on end-to-end tasks would be system-level under D20. Is a separate page needed, or is that Task Success Rate (autonomous)?
