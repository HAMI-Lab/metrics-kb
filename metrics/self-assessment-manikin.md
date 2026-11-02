---
id: self-assessment-manikin
title: "Self-Assessment Manikin (SAM)"
aliases: [SAM, pleasure-arousal-dominance rating]
page_type: metric
template_version: "0.2"
fields: [hci, psychology, visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How a person feels right now, in pleasure, arousal and dominance, rated with pictures."
  measures: [emotional-response]
  subject: [user]
  aspect: [satisfaction]
  perspective: [perceived]
  quantity_form: [rating-score]
  context: [task, session]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [questionnaire-survey]
  route: [self-rating]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "rating per dimension"
  range: "1-9 (common form)"
  better: context-dependent
  validity_concern: {level: low, note: "Direct for self-reported feeling on three dimensions."}

cost:
  level: low
  requires: ["seconds per rating"]
  automatable: false

related:
  - {metric: ueq, kind: conceptual, note: "Overall product experience rather than momentary emotion."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: unknown, evidence: none, note: ""}

sources: [bradley1994]
---

# Self-Assessment Manikin (SAM)

> Three picture scales on which a person marks how pleased, aroused and in control they feel.

## 1. What is measured

### 1.1 Definition
The Self-Assessment Manikin (SAM) shows three rows of cartoon figures. The person marks the figure, or a point between figures, that matches how they feel on pleasure (unhappy to happy), arousal (calm to excited) and dominance (controlled to in control) [bradley1994].

### 1.2 Construct: property of subject in context
The property is emotional response to something just seen or done. The subject is the person. The context is a moment in an interaction or study.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [User experience: emotional response](../constructs/emotional-response.md) (under Task characteristics → User experience)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure lasting attitudes such as trust or satisfaction with a product. Higher is not always better: high arousal can be excitement or stress.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for self-reported feeling. Being pictorial, it needs little reading and works across languages [bradley1994].

### 2.2 Reliability
Single items per dimension; repeated ratings over a session give more stable estimates.

### 2.3 Data collection and measurement error
Rating right after a stimulus or task. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
- One score per dimension, usually 1-9.
- Compare conditions; do not sum dimensions.

### 2.5 Unit and scale
Rating per dimension, commonly 1-9.

## 3. Why it is measured

### 3.1 Use cases
- A visualization study asks participants for SAM ratings after each chart, to compare emotional reactions to different encodings of the same data.
- A game-like tutoring app checks arousal and pleasure after each lesson type.

### 3.2 Purposes
Measuring emotional reactions to stimuli and interactions quickly.

### 3.3 Assumptions
People can report their feelings; pictures are read the same way across cultures.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
HCI and psychology researchers.

### 4.2 Consumers and decisions informed
Researchers; designers of emotionally sensitive content.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Treating higher pleasure as better design without considering the task.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[UEQ](ueq.md) covers lasting product experience.

<!-- generated:neighbours:start -->
- Broader construct: [User Experience Questionnaire (UEQ)](ueq.md) (User experience)
- Sibling construct: [BeauVis Aesthetic Pleasure Scale](beauvis.md) (User experience: visualization aesthetics)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [bradley1994]: SAM.

## Open questions and review notes
- None yet.
