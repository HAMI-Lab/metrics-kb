---
id: demographic-profile
title: Demographic Profile (questionnaire)
aliases: [demographics, demographic questions, participant demographics]
page_type: metric
template_version: "0.3"
fields: [hci, human-ai-interaction, visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Who a person is in terms of attributes such as age, gender, first language and country, as they report them."
  measures: [demographics]
  subject: [user]
  aspect: [background]
  perspective: [perceived]
  quantity_form: [category]
  context: [user-specific]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [questionnaire-survey]
  route: [self-report]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "category per attribute (age may be a number)"
  range: "the answer options offered"
  better: context-dependent
  validity_concern: {level: low, note: "Direct for what people report; answer options and optional questions shape what is recorded."}
  instruments: []

cost:
  level: low
  requires: ["a few questions, under a minute"]
  automatable: false

related:
  - {metric: educational-attainment, kind: conceptual, note: "The other background attribute recorded alongside demographics."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: []
---

# Demographic Profile (questionnaire)

> A few questions on a questionnaire that record who each participant is: age, gender, first language, country.

## 1. What is measured

### 1.1 Definition
Participants answer a few questions about themselves, usually at the start or end of a study. Each answer is recorded as given: a category, or a number for age.

### 1.2 Construct: property of subject in context
The property is the person's demographic attributes. The subject is the person, independent of any system. There is no task context.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Background: demographics](../constructs/demographics.md) (under User characteristics → User background)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Nothing about what the person can do or how they used the system.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for what people report. Using a demographic group as a stand-in for something else, such as experience or ability, is a proxy with a large gap; measure that thing instead.

### 2.2 Reliability
Stable for most attributes. Answer options that do not fit some people lower data quality.

### 2.3 Data collection and measurement error
A short block of questions. Make sensitive questions optional, include "prefer not to say", and collect only what the analysis needs.

### 2.4 Computation
None beyond recording the answers. Age may be grouped into ranges.

### 2.5 Unit and scale
Categories (nominal), or a number for age. There is no better or worse.

### 2.6 Instruments
None listed. Questions are usually written for each study. Reusing the wording of an established survey makes samples comparable across studies.

## 3. Why it is measured

### 3.1 Use cases
- A paper reports the age range and gender split of its participants so readers can judge whom the results apply to.
- A study checks whether an AI writing assistant helps non-native speakers more than native speakers.

### 3.2 Purposes
Describing a sample; checking whom it represents; explaining differences in outcomes between groups.

### 3.3 Assumptions
People answer truthfully, and the answer options cover them.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Study teams; under a minute per participant.

### 4.2 Consumers and decisions informed
Readers of a study, deciding whom the results apply to; designers checking that the system works for different groups of users.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Over-collecting sensitive data. Reading group differences as caused by the attribute itself rather than by things that travel with it.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[Educational Attainment (questionnaire)](educational-attainment.md) records the other background attribute.

<!-- generated:neighbours:start -->
- Sibling construct: [Educational Attainment (questionnaire)](educational-attainment.md) (Background: education)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
Not linked to the objectives directly: user characteristics describe users and explain differences in outcomes.

## 7. Sources
None yet.

## Open questions and review notes
- None yet.
