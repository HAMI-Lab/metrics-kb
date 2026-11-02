---
id: task-success-rate-benchmark
title: "Task Success Rate (agent benchmark)"
aliases: [task success rate, success rate, resolution rate, "pass@k", goal completion rate]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, agents]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the tasks given to a system acting on its own, the share it completes."
  measures: [autonomous-task-completion]
  subject: [system]
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
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Benchmark tasks and automatic success checks may not match what users need done."}
  instruments:
    - {name: "SWE-bench", sources: [jimenez2023], probes: "resolving real software issues in a code repository", scale: "share resolved, 0-1", note: "GitHub issues; success when the repository's tests pass after the agent's change."}
    - {name: "GAIA", sources: [mialon2023], probes: "general assistant tasks needing browsing, tools and reasoning", scale: "share correct, 0-1", note: "Questions with short, unambiguous final answers."}
    - {name: "tau-bench", sources: [yao2024], probes: "tool use while talking with a simulated user under policies", scale: "share of successful episodes, 0-1", note: "Customer-service domains; success judged by the final database state."}

cost:
  level: medium
  requires: ["benchmark tasks with automatic success checks", "compute for agent runs"]
  automatable: true

related:
  - {metric: pass-hat-k, kind: operational, note: "pass^k extends success rate to repeated runs."}
  - {metric: task-success-rate-user, kind: operational, note: "Same computation at the task level: a person uses the system for their own goal."}
  - {metric: tool-call-accuracy, kind: conceptual, note: "Correct tool calls are a step toward success, not success itself."}
  - {metric: cost-per-task, kind: empirical, note: "Higher success often costs more per task."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Agents that complete tasks save users work."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Untested with users here."}

sources: [mohammadi2025, jimenez2023, mialon2023, chen2021, kapoor2025, yao2024]
---

# Task Success Rate (agent benchmark)

> The share of benchmark tasks that an agent completes on its own, checked automatically.

## 1. What is measured

### 1.1 Definition
Task Success Rate (agent benchmark) is the share of tasks in which an autonomous system reaches the goal, such as buying the right product, fixing a software issue, or giving the right final answer [mohammadi2025]. Success is checked automatically, by tests or a reference answer. No user takes part; when a person uses the system for their own goal, see [Task Success Rate (user on task)](task-success-rate-user.md) (D20).

### 1.2 Construct: property of subject in context
The property is autonomous task completion. The subject is the system acting alone. The context is a benchmark of tasks.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Autonomous task completion](../constructs/autonomous-task-completion.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not show how users fare with the system. It ignores cost, time and the path taken.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the benchmark's tasks and checks; **proxy** for usefulness in real work, hence `mixed`. Automatic checks can pass wrong solutions, for example a code patch that passes the tests but breaks something untested [jimenez2023].

**Using a proxy with a known gap.** The rate can compare agents on the same benchmark. It cannot show that an agent will complete the tasks users actually bring, or complete them the way users want. Check a sample of "successful" runs by hand, and report cost per task alongside [kapoor2025].

### 2.2 Reliability
Agents are non-deterministic; report the number of runs and the spread, or use [pass^k](pass-hat-k.md).

### 2.3 Data collection and measurement error
Run the agent on the benchmark tasks and apply the success checks.

### 2.4 Computation
- Success rate = tasks completed ÷ tasks attempted.
- Resolution rate (SWE-bench): issues whose tests pass after the agent's patch ÷ issues [jimenez2023].
- Quasi-exact match of final answers (GAIA) [mialon2023].
- pass@k: share of tasks solved by at least one of k samples [chen2021]. For a model generating code or answers without an agent loop, pass@k is component level and has its own page: [pass@k](pass-at-k.md) (D20).

### 2.5 Unit and scale
0 to 1.

### 2.6 Instruments
**Software engineering**
- **SWE-bench** [jimenez2023]: real issues from open-source repositories; a task counts as resolved when tests tied to the issue pass after the agent's change.

**General assistance**
- **GAIA** [mialon2023]: questions that need web browsing, tools and several reasoning steps, with short final answers checked by quasi-exact match.

**Tool use with a user in the loop**
- **tau-bench** [yao2024]: an agent serves a simulated customer through tools under written policies; success is judged by the final state of the database. Also the source of [pass^k](pass-hat-k.md).

## 3. Why it is measured

### 3.1 Use cases
- A software team compares coding agents by resolution rate on SWE-bench before choosing one to pilot [jimenez2023].
- A shopping assistant is tested on scripted purchase tasks in a simulated store.
- A research lab reports GAIA success for its general assistant [mialon2023].

### 3.2 Purposes
Comparing agents and models; leaderboards [kapoor2025].

### 3.3 Assumptions
Benchmark tasks represent real tasks; the checks recognize success.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Agent developers, benchmark maintainers.

### 4.2 Consumers and decisions informed
Teams choosing agents; leaderboard readers.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Overfitting to public benchmarks; leaderboards that ignore cost reward expensive approaches [kapoor2025].

## 5. Related metrics

### 5.1 Operationally related metrics
pass@k and resolution rate are variants on this page. [pass^k](pass-hat-k.md) extends it to repeated runs.

### 5.2 Conceptually related metrics
[Tool Call Accuracy](tool-call-accuracy.md) checks the steps rather than the outcome.

<!-- generated:neighbours:start -->
- Sibling construct: [pass^k](pass-hat-k.md) (Consistency across runs), [Judge Rating (model judge)](judge-rating.md) (Output quality), [Response Latency](response-latency.md) (System responsiveness), [Performance Drop Rate (PDR)](performance-drop-rate.md) (System robustness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Success and cost trade off: agent leaderboards plot accuracy against dollar cost, and the most accurate agents are not always worth their cost [kapoor2025] (check against the paper).

## 6. Links to business objectives
**Sustained use** and **improved usability:** positive, theoretical; untested with users here.

## 7. Sources
- [mohammadi2025]: success rate in agent evaluation.
- [jimenez2023]: SWE-bench resolution rate.
- [mialon2023]: GAIA.
- [chen2021]: pass@k.
- [kapoor2025]: cost-aware leaderboards.

## Open questions and review notes
- None yet.
