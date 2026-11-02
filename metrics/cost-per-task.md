---
id: cost-per-task
title: Cost per Task
aliases: [dollar cost per task, token cost, inference cost]
page_type: metric
template_version: "0.2"
fields: [llm-evaluation, agents, systems]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much money and compute a system spends to handle one task."
  measures: [resource-cost]
  subject: [system]
  aspect: [resource-cost]
  perspective: [objective]
  quantity_form: ["other: monetary amount or token count"]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [test-collection, logs-telemetry]
  route: [direct-reading]
  collection_mode: [offline, online]
  data_source: [system-telemetry]
  unit: "US dollars (or tokens) per task"
  range: "> 0"
  better: lower
  validity_concern: {level: low, note: "Direct reading of spend; prices change over time, so comparisons need a fixed price table."}

cost:
  level: low
  requires: ["usage records with token counts and prices"]
  automatable: true

related:
  - {metric: task-success-rate-benchmark, kind: empirical, note: "Higher success often costs more."}
  - {metric: response-latency, kind: conceptual, note: "Time is another resource the system uses."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Costly systems are harder to offer at a price users accept."}
  improved-usability: {direction: unknown, evidence: none, note: "Cost is not something users experience directly."}

sources: [kapoor2025, patterson2021]
---

# Cost per Task

> The money (or tokens) a system spends to handle one task, including every model and tool call.

## 1. What is measured

### 1.1 Definition
Cost per Task adds up what the system spends on one task: tokens in and out of each model call, tool and API fees, and compute, converted to money with a stated price table [kapoor2025].

### 1.2 Construct: property of subject in context
The property is resource cost. The subject is the system. The context is a set of tasks.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Resource cost](../constructs/resource-cost.md) (under System characteristics)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not include energy or emissions, which depend on hardware and location [patterson2021]. It does not account for the value of the output.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for spend under the stated prices.

### 2.2 Reliability
Stable for fixed tasks and prices; agents vary in the number of steps per run, so report the spread.

### 2.3 Data collection and measurement error
From API usage records or the provider's billing, per task.

### 2.4 Computation
- Cost = Σ over calls (input tokens × input price + output tokens × output price) + tool fees.
- Report token counts as well, since prices change.
- Per successful task: total cost ÷ successful tasks.

### 2.5 Unit and scale
Dollars (or tokens) per task. Lower is better at equal quality.

## 3. Why it is measured

### 3.1 Use cases
- An agent leaderboard plots accuracy against dollar cost per task so readers can see which gains are worth paying for [kapoor2025].
- A support team compares the cost per resolved ticket of two LLM configurations.

### 3.2 Purposes
Comparing systems at equal quality; budgeting; choosing models.

### 3.3 Assumptions
The price table reflects what the operator pays.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Engineering and finance.

### 4.2 Consumers and decisions informed
Product owners deciding whether a system is affordable at scale.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Cutting cost by cutting quality; comparing costs under different price tables.

## 5. Related metrics

### 5.1 Operationally related metrics
Cost per successful task is a variant on this page.

### 5.2 Conceptually related metrics
[Response Latency](response-latency.md) measures time, another resource.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Trades off with [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) [kapoor2025] (check against the paper).

## 6. Links to business objectives
**Sustained use:** negative, theoretical. **Improved usability:** unknown.

## 7. Sources
- [kapoor2025]: cost in agent leaderboards.
- [patterson2021]: energy and emissions.

## Open questions and review notes
- `quantity_form` has no value for money; `other: monetary amount or token count` is used. Add a value?
- Energy per task and emissions are candidate sibling metrics.
