---
id: emotional-response-score
title: Emotional Response Score (questionnaire)
aliases: [Self-Assessment Manikin, SAM, pleasure-arousal-dominance rating, emotion rating]
page_type: metric
template_version: "0.3"
fields: [hci, psychology, visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How a person feels right after seeing or doing something, rated on dimensions such as pleasure, arousal and dominance."
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
  range: "1-9 per dimension (SAM, common form)"
  better: context-dependent
  validity_concern: {level: low, note: "Direct for self-reported feeling on the rated dimensions."}
  instruments:
    - {name: "Self-Assessment Manikin (SAM)", sources: [bradley1994], probes: "pleasure, arousal and dominance", scale: "1-9 per dimension (common form)", note: "Three rows of cartoon figures; pictorial, seconds per rating."}

cost:
  level: low
  requires: ["seconds per rating"]
  automatable: false

related:
  - {metric: user-experience-score, kind: conceptual, note: "Overall product experience rather than momentary emotion."}
  - {metric: visualization-aesthetics-score, kind: conceptual, note: "Aesthetic pleasure from a visualization rather than general emotion."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: unknown, evidence: none, note: ""}

sources: [bradley1994]
---

# Emotional Response Score (questionnaire)

> Quick ratings, often with pictures, of how pleased, aroused and in control a person feels right after a stimulus or task.

## 1. What is measured

### 1.1 Definition
Right after seeing or doing something, a person rates how they feel on one or more emotional dimensions. The Self-Assessment Manikin (SAM), the instrument on this page so far, shows three rows of cartoon figures; the person marks the figure, or a point between figures, that matches how they feel on pleasure (unhappy to happy), arousal (calm to excited) and dominance (controlled to in control) [bradley1994].

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
**Direct** for self-reported feeling. Being pictorial, SAM needs little reading and works across languages [bradley1994].

### 2.2 Reliability
Single items per dimension are noisy; repeated ratings over a session give more stable estimates.

### 2.3 Data collection and measurement error
Rating right after a stimulus or task. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
One score per rated dimension. Compare conditions dimension by dimension; do not sum dimensions. Each instrument's rule is in 2.6.

### 2.5 Unit and scale
A rating per dimension, treated as interval data; the range depends on the instrument (2.6). Higher is not always better: high arousal can be excitement or stress.

### 2.6 Instruments
- **Self-Assessment Manikin (SAM)** [bradley1994]: three rows of cartoon figures for pleasure (unhappy to happy), arousal (calm to excited) and dominance (controlled to in control). The person marks a figure or a point between figures.
  - *Scale:* usually 1-9 per dimension.
  - *Choose it* for repeated ratings after each stimulus; being pictorial, it needs little reading and works across languages [bradley1994].

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
[User Experience Score (questionnaire)](user-experience-score.md) covers lasting product experience. [Visualization Aesthetics Score (questionnaire)](visualization-aesthetics-score.md) covers aesthetic pleasure specifically.

<!-- generated:neighbours:start -->
- Broader construct: [User Experience Score (questionnaire)](user-experience-score.md) (User experience)
- Sibling construct: [Visualization Aesthetics Score (questionnaire)](visualization-aesthetics-score.md) (User experience: visualization aesthetics)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [bradley1994]: SAM.

## Open questions and review notes
- Renamed from the former Self-Assessment Manikin page (D25).
