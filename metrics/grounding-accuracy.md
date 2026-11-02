---
id: grounding-accuracy
title: Grounding Accuracy
aliases: [click accuracy, GUI grounding accuracy, ScreenSpot accuracy]
page_type: metric
template_version: "0.3"
fields: [agents, human-ai-interaction]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the instructions given, the share for which the component points at the right element or region."
  measures: [grounding-accuracy]
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
  validity_concern: {level: low, note: "Direct for hitting the annotated target."}
  instruments:
    - {name: "ScreenSpot", kind: content, sources: [cheng2024], probes: "locating interface elements from instructions on mobile, desktop and web screens", scale: "proportion, 0-1", note: "Screenshots with instructions and the bounding box of the target element."}

cost:
  level: low
  requires: ["screenshots with instructions and target boxes"]
  automatable: true

related:
  - {metric: task-success-rate-benchmark, kind: conceptual, note: "Whether an agent completes the whole task, of which grounding is one step."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}
  improved-usability: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}

sources: [cheng2024]
---

# Grounding Accuracy

> The share of instructions for which the predicted point falls inside the target element.

## 1. What is measured

### 1.1 Definition
Given a screenshot and an instruction such as "open the settings", the component outputs a point or box. It counts as correct when the point falls inside the annotated target element [cheng2024].

### 1.2 Construct: property of subject in context
The property is localization accuracy. The subject is a grounding component, often the perception step of a GUI agent. The context is a set of screens with instructions.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Grounding performance: localization accuracy](../constructs/grounding-accuracy.md) (under Component characteristics → Component performance → Grounding performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Whether the agent chooses the right action, or completes the task.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for hitting the annotated target.

### 2.2 Reliability
Deterministic given predictions and annotations.

### 2.3 Data collection and measurement error
Run the component on each screenshot and instruction.

### 2.4 Computation
Hits ÷ instructions.

### 2.5 Unit and scale
A proportion from 0 to 1.

### 2.6 Instruments
**Interface elements**
- **ScreenSpot** [cheng2024]: screenshots from mobile, desktop and web interfaces with instructions; results are often reported separately for text and icon targets (check against the paper).

## 3. Why it is measured

### 3.1 Use cases
- A team building a computer-use agent compares vision models on ScreenSpot before integrating one.

### 3.2 Purposes
Choosing perception components for GUI agents.

### 3.3 Assumptions
Annotated targets are the only correct ones.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Agent engineers.

### 4.2 Consumers and decisions informed
Teams building GUI agents.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Benchmarks of clean screenshots overstate accuracy on cluttered real screens.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) measures whole tasks.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [cheng2024]: SeeClick and ScreenSpot.

## Open questions and review notes
- None yet.
