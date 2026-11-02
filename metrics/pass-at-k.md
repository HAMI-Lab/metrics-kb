---
id: pass-at-k
title: pass@k
aliases: [pass at k, "pass@1", functional correctness rate]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, software-engineering]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How likely it is that at least one of k outputs a model generates for a problem passes an automatic check."
  measures: [functional-correctness, answer-correctness]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [test-collection]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "At k > 1 it assumes someone can pick the right sample out of k; and the tests can accept wrong programs."}

cost:
  level: medium
  requires: ["problems with unit tests or answer keys", "n >= k samples per problem"]
  automatable: true

related:
  - {metric: pass-hat-k, kind: conceptual, note: "Same samples, opposite question: pass^k asks whether all k succeed; pass@k asks whether any does."}
  - {metric: task-success-rate-benchmark, kind: conceptual, note: "Agent benchmarks report pass@k for whole multi-step tasks; that use is system level (D20)."}
  - {metric: accuracy, kind: operational, note: "pass@1 is accuracy of one sample against the check."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Through useful generated code or answers; not measured."}
  improved-usability: {direction: unknown, evidence: none, note: "Users see one output at a time and often cannot check it, so large-k scores say little about their experience."}

sources: [kulal2019, chen2021, yue2025, hariri2025]
---

# pass@k

> The chance that at least one of k generated samples for a problem passes its tests or matches its answer key.

## 1. What is measured

### 1.1 Definition
pass@k is the probability that at least one of k outputs sampled from a model for a problem is correct, where correct means passing held-out unit tests (for code) or matching the answer key (for math and other problems with checkable answers). It is averaged over problems. It came from program synthesis, where a problem counted as solved if any candidate program within a budget passed the tests [kulal2019], and spread with the HumanEval code benchmark [chen2021].

### 1.2 Construct: property of subject in context
The property is correctness checked automatically: functional correctness for code (tests pass) and answer correctness for problems with a key, such as math. The subject is the generating model, a component. The context is a benchmark of problems with automatic checks.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Generation performance: functional correctness](../constructs/functional-correctness.md) (under Component characteristics → Component performance → Generation performance)
- [Closed-answer performance: answer correctness](../constructs/answer-correctness.md) (under Component characteristics → Component performance → Closed-answer performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure consistency: pass@k rises with k even if the model is right only occasionally; [pass^k](pass-hat-k.md) asks the opposite question. It does not measure code quality beyond the tests (readability, security, efficiency). When an agent does a whole task and pass@k is reported, it describes the system, not this component.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the check at the chosen k; **proxy** for usefulness, hence `mixed`. Two gaps:

- At k > 1 the number assumes an oracle that recognizes the correct sample among k. Users usually see one output and often cannot tell whether it is right.
- The check defines correctness. Tests that miss cases accept wrong programs, so pass@k overstates correctness when the tests are thin.

**Using a proxy with a known gap.** pass@1 can compare models on how often a single answer is right. Large-k pass@k can compare what models can solve at all, which is how [yue2025] used it to argue that reinforcement learning narrows what a model can solve while making correct answers more likely at small k. Neither supports a claim about what users will get. Report pass@1 next to any larger k, report n and k, and check a sample of passing outputs by hand.

### 2.2 Reliability
With few samples per problem, pass@k estimates and model rankings are unstable [hariri2025]. Draw n well above k and report intervals.

### 2.3 Data collection and measurement error
Sample n outputs per problem from the model and run the checks on each.

### 2.4 Computation
- Unbiased estimator: with c correct out of n samples, pass@k = 1 − C(n − c, k) ÷ C(n, k), averaged over problems [chen2021].
- The naive formula 1 − (1 − pass@1)^k is biased; avoid it.
- pass@1 with greedy decoding (one deterministic sample) is a common variant; report the decoding settings.

### 2.5 Unit and scale
0 to 1. Always report k (and n).

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A team choosing a code model for an IDE assistant compares pass@1 on HumanEval-style problems, because the assistant shows one suggestion at a time [chen2021].
- A research group compares a base model with its reinforcement-learning-tuned version at k from 1 to 256 on math problems, to see whether tuning expanded or narrowed what the model can solve [yue2025].
- A tutoring product checks pass@1 of worked solutions against an answer key before release.

### 3.2 Purposes
Comparing code and reasoning models; studying what training changes [yue2025].

### 3.3 Assumptions
Problems and tests represent the target use; samples are independent; at k > 1, someone or something can pick out the correct sample.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML researchers and engineers.

### 4.2 Consumers and decisions informed
Teams choosing models; researchers comparing training methods.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Reporting a large k makes models look far better than what users get from one try. Benchmark problems and solutions leak into training data. Rankings from few samples can flip [hariri2025].

## 5. Related metrics

### 5.1 Operationally related metrics
pass@1 is [Accuracy](accuracy.md) of a single sample against the check. The agent-level use of pass@k is a variant on [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md).

### 5.2 Conceptually related metrics
[pass^k](pass-hat-k.md) uses the same repeated samples to ask whether all k succeed: a measure of consistency rather than of possible success.

<!-- generated:neighbours:start -->
- Same construct: [Accuracy](accuracy.md) (Closed-answer performance: answer correctness), [F1 Score](f1-score.md) (Closed-answer performance: answer correctness)
- Sibling construct: [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](rouge.md) (Generation performance: content adequacy), [Factual Precision in Atomicity Score (FActScore)](factscore.md) (Generation performance: factuality), [Answer Faithfulness](answer-faithfulness.md) (Generation performance: groundedness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
By definition pass^k ≤ pass@1 ≤ pass@k for k > 1. Reinforcement-learning tuning reportedly raises pass@1 but can lower pass@k at large k relative to the base model [yue2025] (check against the paper).

## 6. Links to business objectives
**Sustained use:** positive, theoretical. **Improved usability:** unknown: users see one output at a time and often cannot check it.

## 7. Sources
- [kulal2019]: program synthesis with a budget of candidates.
- [chen2021]: HumanEval and the unbiased estimator.
- [yue2025]: pass@k at large k as a capability boundary.
- [hariri2025]: instability with few samples.

## Open questions and review notes
- None yet.
