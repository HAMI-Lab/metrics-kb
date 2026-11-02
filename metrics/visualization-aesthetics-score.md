---
id: visualization-aesthetics-score
title: Visualization Aesthetics Score (questionnaire)
aliases: [BeauVis, BeauVis Aesthetic Pleasure Scale, visualization aesthetics scale, aesthetic pleasure rating]
page_type: metric
template_version: "0.3"
fields: [visualization, hci]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How aesthetically pleasing a person finds a visualization."
  measures: [visualization-aesthetics]
  subject: [user]
  aspect: [satisfaction]
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
  unit: "scale mean"
  range: "1-7 (BeauVis)"
  better: higher
  validity_concern: {level: low, note: "Direct for reported aesthetic pleasure; BeauVis was validated as a scale by its authors."}
  instruments:
    - {name: "BeauVis Aesthetic Pleasure Scale", sources: [he2023], scale: "1-7 mean", note: "A few adjectives about aesthetic pleasure, 7-point; validated for visualizations."}

cost:
  level: low
  requires: ["seconds per visualization"]
  automatable: false

related:
  - {metric: emotional-response-score, kind: conceptual, note: "General emotional reaction rather than aesthetic pleasure."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: unknown, evidence: none, note: "Aesthetic pleasure is distinct from readability."}

sources: [he2023]
---

# Visualization Aesthetics Score (questionnaire)

> A short questionnaire rating of how pleasing a visualization looks.

## 1. What is measured

### 1.1 Definition
After viewing a visualization, a person rates it on a few adjectives about aesthetic pleasure, and the score is the mean. BeauVis, the instrument on this page so far, was built and validated for visual representations of data [he2023].

### 1.2 Construct: property of subject in context
The property is aesthetic pleasure. The subject is the person viewing a visualization. The context is viewing it, usually in a study.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [User experience: visualization aesthetics](../constructs/visualization-aesthetics.md) (under Task characteristics → User experience)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure whether the chart is easy to read or correct.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for reported aesthetic pleasure; the BeauVis authors report a validation of the scale (check against [he2023]).

### 2.2 Reliability
Multi-item scales allow internal consistency to be checked. Figures for each instrument are in 2.6.

### 2.3 Data collection and measurement error
Rating after viewing each visualization. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
The mean of the item ratings for each visualization, averaged across viewers. Each instrument's rule is in 2.6.

### 2.5 Unit and scale
A mean rating, treated as interval data, on the instrument's range (2.6). Higher is more pleasing, which is not the same as easier to read.

### 2.6 Instruments
- **BeauVis Aesthetic Pleasure Scale** [he2023]: a few adjectives about aesthetic pleasure on 7-point scales; the score is the mean, 1-7 (check the exact items and scale against the paper). The authors report a validation of the scale. Seconds per visualization, so it suits rating many visualizations in one study.

## 3. Why it is measured

### 3.1 Use cases
- A newsroom graphics team compares reader ratings of two chart styles for the same story.
- A dashboard vendor checks whether a new theme is rated more pleasing without hurting readability.

### 3.2 Purposes
Comparing visual designs on aesthetics.

### 3.3 Assumptions
Aesthetic pleasure can be reported directly.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Visualization researchers and designers.

### 4.2 Consumers and decisions informed
Design teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing beauty at the cost of accuracy.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[Emotional Response Score (questionnaire)](emotional-response-score.md) captures general emotion. Perceived readability (PREVis) is a candidate sibling metric.

<!-- generated:neighbours:start -->
- Broader construct: [User Experience Score (questionnaire)](user-experience-score.md) (User experience)
- Sibling construct: [Emotional Response Score (questionnaire)](emotional-response-score.md) (User experience: emotional response)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [he2023]: BeauVis.

## Open questions and review notes
- Renamed from the former BeauVis page (D25), which settles that page's question about being titled after an instrument.
