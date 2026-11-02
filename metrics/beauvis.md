---
id: beauvis
title: BeauVis Aesthetic Pleasure Scale
aliases: [BeauVis, visualization aesthetics scale]
page_type: metric
template_version: "0.2"
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
  range: "1-7"
  better: higher
  validity_concern: {level: low, note: "Direct for reported aesthetic pleasure; validated as a scale by its authors."}

cost:
  level: low
  requires: ["seconds per visualization"]
  automatable: false

related:
  - {metric: self-assessment-manikin, kind: conceptual, note: "General emotional reaction rather than aesthetic pleasure."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: unknown, evidence: none, note: "Aesthetic pleasure is distinct from readability."}

sources: [he2023]
---

# BeauVis Aesthetic Pleasure Scale

> A short validated questionnaire on how pleasing a visualization looks.

## 1. What is measured

### 1.1 Definition
BeauVis is a short questionnaire in which people rate a visualization on a few adjectives about its aesthetic pleasure, on 7-point scales; the score is the mean [he2023]. It was built and validated for visual representations of data.

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
**Direct** for reported aesthetic pleasure; the authors report a validation of the scale (check against [he2023]).

### 2.2 Reliability
Multi-item, so internal consistency can be checked; see the validation in [he2023].

### 2.3 Data collection and measurement error
Rating after viewing each visualization. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
- Score = mean of the item ratings [he2023] (check the exact items and scale against the paper).

### 2.5 Unit and scale
1-7 mean.

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
[SAM](self-assessment-manikin.md) captures general emotion. Perceived readability (PREVis) is a candidate sibling metric.

<!-- generated:neighbours:start -->
- Broader construct: [User Experience Questionnaire (UEQ)](ueq.md) (User experience)
- Sibling construct: [Self-Assessment Manikin (SAM)](self-assessment-manikin.md) (User experience: emotional response)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [he2023]: BeauVis.

## Open questions and review notes
- The title is the instrument's own name, which is not an acronym; is that acceptable under D19?
