---
id: smeq
title: "Subjective Mental Effort Questionnaire (SMEQ)"
aliases: [SMEQ, Rating Scale Mental Effort, RSME]
page_type: metric
template_version: "0.2"
fields: [hci, human-factors]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much mental effort a person reports a task took."
  measures: [mental-workload]
  subject: [user]
  aspect: [workload]
  perspective: [perceived]
  quantity_form: [rating-score]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [questionnaire-survey]
  route: [self-rating]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "rating"
  range: "0-150"
  better: lower
  validity_concern: {level: low, note: "Direct for reported mental effort."}

cost:
  level: low
  requires: ["seconds after each task"]
  automatable: false

related:
  - {metric: nasa-tlx, kind: conceptual, note: "Multi-dimensional workload; SMEQ covers mental effort only."}
  - {metric: task-completion-time, kind: empirical, note: "Harder tasks usually take longer and feel more effortful."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Effortful systems are less pleasant to keep using."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Less effort for the same outcome means better usability."}

sources: [zijlstra1985, sauro2009onequestion]
---

# Subjective Mental Effort Questionnaire (SMEQ)

> A single vertical scale on which a person marks how much mental effort a task took.

## 1. What is measured

### 1.1 Definition
The Subjective Mental Effort Questionnaire (SMEQ) is one vertical line from 0 to about 150 with verbal labels along it, from "not at all hard to do" to "tremendously hard to do". After a task, the person marks how much effort it took [zijlstra1985].

### 1.2 Construct: property of subject in context
The property is mental workload as experienced. The subject is the person. The context is a task just done.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Mental workload](../constructs/mental-workload.md) (under Task characteristics → Task performance → Task efficiency; Task characteristics → Usability → Task efficiency)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It covers mental effort only, not physical demand, time pressure or frustration, which NASA-TLX also asks about.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for reported mental effort.

### 2.2 Reliability
A single item, but sensitive to differences between tasks in comparisons with other one-question measures [sauro2009onequestion] (check against the paper).

### 2.3 Data collection and measurement error
Paper or on-screen scale after each task. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
- The position marked, 0-150. Average per task across participants.

### 2.5 Unit and scale
0-150; lower is less effort.

## 3. Why it is measured

### 3.1 Use cases
- A usability test of a tax-filing app asks for SMEQ after each task to find the most effortful step.
- A study of a data-analysis assistant compares effort ratings with and without AI suggestions.

### 3.2 Purposes
Post-task effort ratings in usability tests [sauro2009onequestion].

### 3.3 Assumptions
People can judge their own effort right after the task.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers.

### 4.2 Consumers and decisions informed
Design teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Low effort is not always good: effortless use of AI suggestions may mean the person stopped checking them.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[NASA-TLX](nasa-tlx.md) is the multi-dimensional alternative; SMEQ corresponds to its mental-demand side.

<!-- generated:neighbours:start -->
- Same construct: [NASA Task Load Index (NASA-TLX)](nasa-tlx.md) (Mental workload)
- Broader construct: [Task Completion Time](task-completion-time.md) (Task efficiency)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** negative, theoretical.

## 7. Sources
- [zijlstra1985]: SMEQ.
- [sauro2009onequestion]: comparison of one-question post-task measures.

## Open questions and review notes
- ReVISit lists the year as 1985; some sources date the scale to 1993. Check the original report.
