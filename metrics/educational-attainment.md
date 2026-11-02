---
id: educational-attainment
title: Educational Attainment (questionnaire)
aliases: [education level, highest degree, education background, field of study]
page_type: metric
template_version: "0.3"
fields: [hci, human-ai-interaction, visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "The highest level of formal education a person has completed, and optionally their field of study, as they report them."
  measures: [educational-background]
  subject: [user]
  aspect: [background]
  perspective: [perceived]
  quantity_form: [category]
  context: [user-specific]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [questionnaire-survey]
  route: [direct-reading]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "level (ordered category); field of study (category)"
  range: "the answer options offered"
  better: context-dependent
  validity_concern: {level: low, note: "Direct for completed schooling; a weak proxy for knowledge or skill, which literacy tests measure."}
  instruments: []

cost:
  level: low
  requires: ["one or two questions"]
  automatable: false

related:
  - {metric: demographic-profile, kind: conceptual, note: "The other background attribute recorded alongside education."}
  - {metric: numeracy-score, kind: conceptual, note: "An ability test; education is sometimes used in its place, with a large gap."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: []
---

# Educational Attainment (questionnaire)

> One or two questions on a questionnaire that record a participant's highest completed level of education and field of study.

## 1. What is measured

### 1.1 Definition
Participants choose their highest completed level of education from a list, and sometimes name their field of study. The answers are recorded as given.

### 1.2 Construct: property of subject in context
The property is the person's formal education. The subject is the person, independent of any system. There is no task context.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Background: education](../constructs/educational-background.md) (under User characteristics → User background)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure what the person knows or can do: two people with the same degree can differ widely in [numeracy](numeracy-score.md) or [visualization literacy](visualization-literacy-score.md).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for completed schooling as reported.

**Using a proxy with a known gap.** Education can describe a sample and serve as a rough grouping variable. It cannot stand in for an ability that matters to the task, such as numeracy; if the ability matters, test it.

### 2.2 Reliability
Stable. Level names differ across countries, so international samples need a mapping between systems.

### 2.3 Data collection and measurement error
One question with ordered levels, plus an optional open or listed question on field of study.

### 2.4 Computation
None beyond recording the answers. Levels may be merged into fewer groups for analysis.

### 2.5 Unit and scale
Ordered categories for level; nominal categories for field. There is no better or worse.

### 2.6 Instruments
None listed. Questions are usually written for each study. Reusing an established classification of education levels makes samples comparable across countries and studies.

## 3. Why it is measured

### 3.1 Use cases
- A paper reports that most participants hold a university degree, so readers can judge how far the results carry.
- A study of a statistics chatbot compares participants with and without training in a quantitative field.

### 3.2 Purposes
Describing a sample; explaining differences in outcomes between groups.

### 3.3 Assumptions
The answer options fit the education systems participants come from.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Study teams; seconds per participant.

### 4.2 Consumers and decisions informed
Readers of a study, deciding whom the results apply to.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Using education as a stand-in for ability. Samples skewed toward highly educated participants, common in university studies, limit how far results carry.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[Demographic Profile (questionnaire)](demographic-profile.md) records the other background attributes. [Numeracy Score (ability test)](numeracy-score.md) measures an ability that education is sometimes wrongly used for.

<!-- generated:neighbours:start -->
- Sibling construct: [Demographic Profile (questionnaire)](demographic-profile.md) (Background: demographics)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
Not linked to the objectives directly: user characteristics describe users and explain differences in outcomes.

## 7. Sources
None yet.

## Open questions and review notes
- The route is `direct-reading` because answers are recorded as given. Neither existing route fits a self-reported fact exactly; is a "self-report" route needed?
