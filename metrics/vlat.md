---
id: vlat
title: "Visualization Literacy Assessment Test (VLAT)"
aliases: [VLAT, Mini-VLAT, A-VLAT, visualization literacy score]
page_type: metric
template_version: "0.2"
fields: [visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a person can read and interpret common charts, shown by answering test questions with right answers."
  measures: [visualization-literacy]
  subject: [user]
  aspect: ["other: ability (visualization literacy)"]
  perspective: [objective]
  quantity_form: [proportion]
  context: [user-specific]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [ability-test]
  route: [reference-comparison, statistical-modeling]
  collection_mode: [in-lab, field]
  data_source: [reference-answers]
  unit: "share correct (or ability estimate)"
  range: "0-1 (or a latent scale)"
  better: higher
  validity_concern: {level: moderate, note: "Covers the chart types and tasks in the test; scores on them may not carry over to unusual charts or real dashboards."}

cost:
  level: low
  requires: ["participants", "about 5 minutes (Mini-VLAT) to much longer (full VLAT)"]
  automatable: false

related:
  - {metric: calvi, kind: conceptual, note: "Critical reading of misleading charts rather than reading well-made ones."}
  - {metric: berlin-numeracy-test, kind: conceptual, note: "Numeracy, a related ability that chart reading draws on."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: [lee2017, pandey2023, cui2024, boy2014, embretson2000, ding2023]
---

# Visualization Literacy Assessment Test (VLAT)

> A test with right answers in which people read values, find trends and compare data on common chart types.

## 1. What is measured

### 1.1 Definition
The Visualization Literacy Assessment Test (VLAT) gives people charts of common types, such as bar charts, line charts, scatterplots and maps, and asks questions that have right answers: retrieve a value, find an extreme, spot a trend, compare [lee2017]. The score is the share answered correctly. Mini-VLAT is a short form with one item per chart type [pandey2023]; A-VLAT is an adaptive form that picks each next item from earlier answers [cui2024].

### 1.2 Construct: property of subject in context
The property is visualization literacy. The subject is the person, independent of any one system. The context is the test's chart types and tasks.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Literacy: visualization literacy](../constructs/visualization-literacy.md) (under User characteristics → Literacy)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure whether a person can spot misleading charts; see [CALVI](calvi.md). It says nothing about the usability of a particular visualization tool.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the chart types and tasks it covers. As a description of general visualization literacy it has the gap of any [ability test](../strategies/ability-test.md): unusual charts, interactive dashboards and real data contexts are not in it.

**Using a proxy with a known gap.** Scores can group participants or control for literacy when comparing designs. They cannot certify that someone will read a particular product's charts correctly; test that with a task study on those charts.

### 2.2 Reliability
The full test has many items, so scores are fairly stable; the short and adaptive forms trade items for time, and the authors report how much information they keep (check against [pandey2023; cui2024]).

### 2.3 Data collection and measurement error
Given online or in a lab, often as a block in a study platform such as reVISit [ding2023]. Time limits per item are part of the protocol in some forms.

### 2.4 Computation
- Share correct, or a total with a correction for guessing in multiple-choice items (check the scoring rule for each form).
- Adaptive form: an ability estimate from an item response theory model [cui2024; embretson2000].

### 2.5 Unit and scale
Share correct (0-1), or a latent ability score for the adaptive form.

## 3. Why it is measured

### 3.1 Use cases
- A visualization study gives Mini-VLAT at the start, to check whether a new chart design helps low-literacy participants more than high-literacy ones [pandey2023].
- A public-health agency tests a sample of its audience before choosing how complex its dashboard charts can be.

### 3.2 Purposes
Describing participants; controlling for literacy in studies; comparing populations [boy2014].

### 3.3 Assumptions
Chart types in the test are the ones that matter; people try their best.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Visualization researchers.

### 4.2 Consumers and decisions informed
Researchers; designers choosing chart complexity for an audience.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Treating low scores as a fixed trait of people rather than a product of training and exposure. Items leak and can be practised.

## 5. Related metrics

### 5.1 Operationally related metrics
Mini-VLAT and A-VLAT are variants on this page.

### 5.2 Conceptually related metrics
[CALVI](calvi.md) tests critical reading of misleading charts. The [Berlin Numeracy Test](berlin-numeracy-test.md) measures a related ability.

<!-- generated:neighbours:start -->
- Narrower construct: [Critical Thinking Assessment for Literacy in Visualizations (CALVI)](calvi.md) (Literacy: critical visualization literacy)
- Sibling construct: [Berlin Numeracy Test](berlin-numeracy-test.md) (Literacy: numeracy)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: visualization literacy and numeracy scores are positively correlated. Why it could be true: reading values and comparing quantities on charts draws on number skills (further reference needed).

## 6. Links to business objectives
Not linked to the objectives directly: user characteristics describe users and explain differences in outcomes.

## 7. Sources
- [lee2017]: VLAT.
- [pandey2023]: Mini-VLAT.
- [cui2024]: adaptive VLAT.
- [boy2014]: principles of literacy tests.
- [embretson2000]: item response theory.
- [ding2023]: reVISit.

## Open questions and review notes
- Visualization literacy is an ability, not one of the aspect values; `other: ability (visualization literacy)` is used. Add an `ability` aspect for user characteristics?
