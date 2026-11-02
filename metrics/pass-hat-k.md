---
id: pass-hat-k
title: pass^k
aliases: [pass hat k, consistency over k trials, reliability over repeated trials]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, agents]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How likely a system is to succeed on a task every time, over k repeated tries."
  measures: [run-consistency]
  subject: [system]
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
  validity_concern: {level: low, note: "Directly counts repeated success on the same tasks."}
  instruments:
    - {name: "tau-bench", sources: [yao2024], probes: "tool use while talking with a simulated user under policies", scale: "pass^k, 0-1", note: "Customer-service domains; repeated trials of each task."}

cost:
  level: medium
  requires: ["tasks with checkable success", "k runs per task"]
  automatable: true

related:
  - {metric: task-success-rate-benchmark, kind: operational, note: "pass^1 equals the task success rate."}
  - {metric: pass-at-k, kind: conceptual, note: "Same repeated samples, opposite question: any success vs all successes."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Users stop relying on systems whose success they cannot predict."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Consistent behaviour is easier to learn."}

sources: [yao2024, mohammadi2025, chen2021]
---

# pass^k

> The chance that a system succeeds on all k independent attempts at the same task.

## 1. What is measured

### 1.1 Definition
pass^k (read "pass hat k") is the probability that a system succeeds on a task in all of k independent runs, averaged over tasks [yao2024]. It is meant for systems that do not give the same result every time, such as language-model agents. It is the strict counterpart of [pass@k](pass-at-k.md), which counts a task as solved if any one of k runs succeeds [chen2021].

### 1.2 Construct: property of subject in context
The property is consistency across runs: success that repeats. The subject is the system, often an agent. The context is a set of tasks with checkable success.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Consistency across runs](../constructs/run-consistency.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure robustness to changed inputs; the input stays the same. It does not show why runs differ.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for repeated success on the benchmark's tasks.

### 2.2 Reliability
Needs more than k runs per task to estimate well; with few runs the estimate is coarse.

### 2.3 Data collection and measurement error
Run each task n ≥ k times and record success.

### 2.4 Computation
- With c successes in n runs of a task: pass^k = C(c, k) ÷ C(n, k), averaged over tasks [yao2024].
- pass^1 is the ordinary success rate; pass^k falls as k grows unless the system always succeeds.

### 2.5 Unit and scale
0 to 1. Report k.

### 2.6 Instruments
**Tool use with a user in the loop**
- **tau-bench** [yao2024]: introduced pass^k; each task is run several times against a simulated user, and pass^k is the chance that all k runs succeed.

## 3. Why it is measured

### 3.1 Use cases
- A customer-service agent for airline bookings is run eight times on each scripted request; pass^8 shows how often it handles a request correctly every single time [yao2024].
- A coding agent's team reports pass^k next to pass@k to show the gap between best-case and dependable performance.

### 3.2 Purposes
Judging whether agents can be relied on in deployment [mohammadi2025].

### 3.3 Assumptions
Runs are independent; success is checkable.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Agent developers and evaluators.

### 4.2 Consumers and decisions informed
Teams deciding whether an agent can run without supervision.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Setting the sampling temperature to zero raises consistency without making the agent better at the task.

## 5. Related metrics

### 5.1 Operationally related metrics
pass^1 equals [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md); pass@k is on that page as a variant.

### 5.2 Conceptually related metrics
[pass@k](pass-at-k.md) asks whether any of k samples succeeds; pass^k asks whether all do.

<!-- generated:neighbours:start -->
- Sibling construct: [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (Autonomous task completion), [Judge Rating (model judge)](judge-rating.md) (Output quality), [Response Latency](response-latency.md) (System responsiveness), [Performance Drop Rate (PDR)](performance-drop-rate.md) (System robustness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
By definition pass^k ≤ pass^1 ≤ pass@k for k > 1; the gap grows with inconsistency.

## 6. Links to business objectives
**Sustained use** and **improved usability:** positive, theoretical.

## 7. Sources
- [yao2024]: pass^k in tau-bench.
- [mohammadi2025]: reliability in agent evaluation.
- [chen2021]: pass@k.

## Open questions and review notes
- Title uses the notation pass^k, which is not an acronym; is that clear enough?
