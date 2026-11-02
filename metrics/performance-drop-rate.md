---
id: performance-drop-rate
title: "Performance Drop Rate (PDR)"
aliases: [PDR, robustness gap, relative performance drop]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, machine-learning, nlp]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much of its performance a system loses when inputs are changed in ways that should not matter."
  measures: [robustness]
  subject: [system]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [controlled-comparison, benchmark]
  route: [difference-scoring]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion of baseline performance"
  range: "usually 0-1; negative if performance improves"
  better: lower
  validity_concern: {level: moderate, note: "Depends on which changes are applied; a change that alters the right answer makes the drop meaningless."}
  instruments:
    - {name: "PromptBench", sources: [zhu2023], probes: "robustness to adversarial changes in prompts", scale: "relative drop, usually 0-1", note: "Adversarial prompts at character, word, sentence and meaning levels, applied to standard tasks."}

cost:
  level: low
  requires: ["a test set", "a perturbation method"]
  automatable: true

related:
  - {metric: accuracy, kind: operational, note: "Usually computed from accuracy on original and changed inputs."}
  - {metric: attack-success-rate, kind: conceptual, note: "Attacks target safety rules rather than task performance."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Systems that break on small input changes frustrate users."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Users rarely phrase inputs the way benchmarks do."}

sources: [zhu2023, chang2024, liang2022, ribeiro2020, cronbach1970]
---

# Performance Drop Rate (PDR)

> The relative fall in a performance score when the same tasks are given with perturbed inputs.

## 1. What is measured

### 1.1 Definition
Performance Drop Rate (PDR) compares a performance score, such as accuracy, on original inputs with the same score on perturbed inputs: typos, paraphrases, distracting text, or adversarial edits. PDR is the drop divided by the original score [zhu2023; chang2024].

### 1.2 Construct: property of subject in context
The property is robustness to input changes that should not change the right answer. The subject is the system. The context is a test set and a set of perturbations [liang2022].

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [System robustness](../constructs/robustness.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure performance itself: a system that is bad on both versions has a small drop. It covers only the perturbations tried.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the chosen perturbations; **proxy** for robustness to the variety of real inputs, hence `mixed`.

**Using a proxy with a known gap.** PDR can show that a system is fragile to a particular kind of change, or compare systems under the same changes. It cannot show that a system is robust in general. Check that perturbed inputs keep their right answer (by sampling them), report PDR with the original score, and test several kinds of perturbation [ribeiro2020].

### 2.2 Reliability
A difference of two noisy scores is noisier than either [cronbach1970]; report intervals, and use enough items.

### 2.3 Data collection and measurement error
Score the system on a test set and on perturbed copies of it. See [controlled comparison](../strategies/controlled-comparison.md).

### 2.4 Computation
- PDR = (score on original − score on perturbed) ÷ score on original [zhu2023].
- Report per perturbation type and averaged.
- Absolute drop (no division) is a variant; state which.

### 2.5 Unit and scale
A proportion of the original score. 0 means no drop.

### 2.6 Instruments
**Prompt robustness**
- **PromptBench** [zhu2023]: perturbs task prompts at several levels (characters, words, sentences, meaning) and reports the drop in performance on standard tasks; the source of this metric's usual definition (check against the paper).

## 3. Why it is measured

### 3.1 Use cases
- An LLM classification service is tested with typo-ridden and paraphrased versions of its test prompts before release [zhu2023].
- A medical QA assistant is checked with questions rephrased in lay language: how much accuracy is lost?

### 3.2 Purposes
Robustness testing; comparing models and prompts [chang2024].

### 3.3 Assumptions
Perturbations do not change the right answer; the original test set is a fair baseline.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML and LLM evaluation engineers.

### 4.2 Consumers and decisions informed
Teams choosing models for noisy real-world inputs.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Training on the perturbation set lowers PDR on it without broader robustness.

## 5. Related metrics

### 5.1 Operationally related metrics
Computed from [Accuracy](accuracy.md) or another score on two versions of the inputs.

### 5.2 Conceptually related metrics
[Attack Success Rate](attack-success-rate.md) measures resistance to attacks on safety rules.

<!-- generated:neighbours:start -->
- Sibling construct: [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (Autonomous task completion), [pass^k](pass-hat-k.md) (Consistency across runs), [Response Latency](response-latency.md) (System responsiveness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** negative, theoretical: fragile systems frustrate users whose inputs differ from the benchmark's.

## 7. Sources
- [zhu2023]: PDR under adversarial prompts.
- [chang2024]: PDR in LLM evaluation.
- [liang2022]: robustness to perturbations.
- [ribeiro2020]: perturbation tests.
- [cronbach1970]: reliability of difference scores.

## Open questions and review notes
- None yet.
