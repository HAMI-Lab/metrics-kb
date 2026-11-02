---
id: tool-call-accuracy
title: Tool Call Accuracy
aliases: [tool selection accuracy, tool call F1, argument accuracy]
page_type: metric
template_version: "0.2"
fields: [llm-evaluation, agents]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Whether an agent called the tools, with the arguments, that the task required."
  measures: [tool-call-correctness]
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
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Assumes one right sequence of calls; agents that reach the goal another way are scored as wrong."}

cost:
  level: low
  requires: ["tasks with reference tool calls"]
  automatable: true

related:
  - {metric: f1-score, kind: operational, note: "Tool Call F1 is F1 over calls."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Long causal chain."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Through autonomous task completion; not measured."}

sources: [ragas2026, mohammadi2025]
---

# Tool Call Accuracy

> Compare an agent's tool calls (names, arguments, order) with the calls a reference expects.

## 1. What is measured

### 1.1 Definition
For each test task, a reference lists the tool calls an agent should make. The agent's actual calls are compared with it: right tool names, right arguments, and, if required, right order [ragas2026; mohammadi2025].

### 1.2 Construct: property of subject in context
The property is correctness of tool calls. The subject is the tool-using part of an agent. The context is a set of tasks with reference calls.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Tool-use performance: call correctness](../constructs/tool-call-correctness.md) (under Component characteristics → Component performance → Tool-use performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not show whether the task was completed; see Task Success Rate (autonomous), on the system branch (page not yet written). It says nothing about efficiency (extra calls).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for match with the reference. Where several call sequences are valid, a single reference punishes correct alternatives.

### 2.2 Reliability
Deterministic given the reference and the matching rules (exact vs fuzzy argument matching).

### 2.3 Data collection and measurement error
Run the agent on tasks with reference calls; log calls and arguments.

### 2.4 Computation
- Tool Call Accuracy: share of tasks (or calls) where names and arguments match, with optional order checking [ragas2026].
- Tool Call F1: precision and recall of calls against the reference.
- Tool selection accuracy: only the tool name is checked [mohammadi2025].

### 2.5 Unit and scale
0 to 1.

## 3. Why it is measured

### 3.1 Use cases
- A travel-booking agent is tested on scripted requests: does it call the flight search with the right dates and airports?
- A cloud-operations agent is checked for choosing the right diagnostic command for each alert type.

### 3.2 Purposes
Debugging agents; regression tests for tool definitions and prompts.

### 3.3 Assumptions
The reference calls are the right ones; argument formats are comparable.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Agent developers.

### 4.2 Consumers and decisions informed
Agent teams deciding whether a change broke tool use.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Agents tuned to match references can lose the ability to find alternative routes.

## 5. Related metrics

### 5.1 Operationally related metrics
Tool Call F1 and tool selection accuracy are variants on this page.

### 5.2 Conceptually related metrics
Task Success Rate (autonomous), on the system branch (page not yet written) judges the outcome instead of the calls.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical.

## 7. Sources
- [ragas2026]: Tool Call Accuracy and F1.
- [mohammadi2025]: tool-use evaluation in agent surveys.

## Open questions and review notes
- Normalized edit distance between call sequences [mohammadi2025] is a candidate variant for order-sensitive tasks.
