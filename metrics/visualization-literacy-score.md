---
id: visualization-literacy-score
title: Visualization Literacy Score (ability test)
aliases: [VLAT, Visualization Literacy Assessment Test, Mini-VLAT, A-VLAT, CALVI, Critical Thinking Assessment for Literacy in Visualizations, A-CALVI, misleading visualization test, visualization literacy test]
page_type: metric
template_version: "0.3"
fields: [visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a person can read and interpret charts, including charts designed to mislead, shown by answering test questions with right answers."
  measures: [visualization-literacy, critical-visualization-literacy]
  subject: [user]
  aspect: [ability]
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
  validity_concern: {level: moderate, note: "Covers the chart types, tasks and misleading designs in the test; scores may not carry over to unusual charts, new tricks or real dashboards."}
  instruments:
    - {name: "Visualization Literacy Assessment Test (VLAT)", sources: [lee2017], note: "Common chart types; retrieve values, find extremes, spot trends, compare. Full form."}
    - {name: "Mini-VLAT", sources: [pandey2023], note: "Short form, one item per chart type; about 5 minutes."}
    - {name: "Adaptive VLAT (A-VLAT)", sources: [cui2024], note: "Picks each next item from earlier answers; scored with item response theory."}
    - {name: "Critical Thinking Assessment for Literacy in Visualizations (CALVI)", sources: [ge2023], note: "Charts with misleading features (truncated axes, bad aggregation, missing data) mixed with normal ones."}
    - {name: "Adaptive CALVI (A-CALVI)", sources: [cui2024], note: "Adaptive form of CALVI."}

cost:
  level: low
  requires: ["participants", "about 5 minutes (Mini-VLAT) to tens of minutes (full VLAT or CALVI)"]
  automatable: false

related:
  - {metric: numeracy-score, kind: conceptual, note: "Numeracy, a related ability that chart reading draws on."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: [lee2017, pandey2023, cui2024, ge2023, boy2014, embretson2000, ding2023]
---

# Visualization Literacy Score (ability test)

> A test with right answers in which people read values, find trends and compare data on charts, or avoid being misled by charts designed to mislead.

## 1. What is measured

### 1.1 Definition
People are shown charts and answer questions that have right answers; the score is the share answered correctly, or an ability estimate from an item response theory model. VLAT uses well-made charts of common types, such as bar charts, line charts, scatterplots and maps, and asks people to retrieve a value, find an extreme, spot a trend or compare [lee2017]. CALVI uses charts with misleading features, such as truncated or inverted axes, inappropriate aggregation or missing data: a person who reads the chart critically answers correctly, and one who is misled picks the answer the design invites [ge2023]. Section 2.6 compares the instruments.

### 1.2 Construct: property of subject in context
The property is visualization literacy and its narrower part, critical visualization literacy. The subject is the person, independent of any one system. The context is the test's chart types, tasks and misleading designs.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Literacy: visualization literacy](../constructs/visualization-literacy.md) (under User characteristics → Literacy)
- [Literacy: critical visualization literacy](../constructs/critical-visualization-literacy.md) (under User characteristics → Literacy → Literacy: visualization literacy)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It says nothing about the usability of a particular visualization tool. VLAT does not measure whether a person can spot misleading charts; CALVI does not measure general chart reading on well-made charts.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the chart types, tasks and misleading designs in the test. As a description of general visualization literacy it has the gap of any [ability test](../strategies/ability-test.md): unusual charts, interactive dashboards, real data contexts and new misleading tricks are not in it. CALVI includes normal items too, so that answering "it's misleading" every time does not score well (check against [ge2023]).

**Using a proxy with a known gap.** Scores can group participants, control for literacy when comparing designs, or show whether training improves reading of the covered charts. They cannot certify that someone will read a particular product's charts correctly, or resist new or subtler misleading charts; test that with a task study on those charts.

### 2.2 Reliability
The full VLAT has many items, so scores are fairly stable; the short and adaptive forms trade items for time, and the authors report how much information they keep (check against [pandey2023; cui2024]). The CALVI authors report item analysis with item response theory (check against [ge2023]).

### 2.3 Data collection and measurement error
Given online or in a lab, often as a block in a study platform such as reVISit [ding2023]. Time limits per item are part of the protocol in some forms.

### 2.4 Computation
- Share correct, or a total with a correction for guessing in multiple-choice items (check the scoring rule for each form).
- Adaptive forms (A-VLAT, A-CALVI): an ability estimate from an item response theory model [cui2024; embretson2000].

### 2.5 Unit and scale
Share correct (0-1), or a latent ability score for the adaptive forms. Scores from different instruments are not on the same scale.

### 2.6 Instruments
- **VLAT** [lee2017]: the full test on well-made charts. Choose it when literacy is a main variable of the study.
- **Mini-VLAT** [pandey2023]: one item per chart type, about five minutes. Choose it to describe or group participants at the start of a study.
- **A-VLAT** [cui2024]: adaptive; fewer items for a similar precision.
- **CALVI** [ge2023]: critical reading of misleading charts. Choose it when being misled is the concern, for example with AI-generated or persuasive charts.
- **A-CALVI** [cui2024]: adaptive form of CALVI.

## 3. Why it is measured

### 3.1 Use cases
- A visualization study gives Mini-VLAT at the start, to check whether a new chart design helps low-literacy participants more than high-literacy ones [pandey2023].
- A public-health agency tests a sample of its audience before choosing how complex its dashboard charts can be.
- A media-literacy course gives CALVI before and after a unit on misleading charts.
- A study of AI-generated charts uses CALVI to check whether participants who score low are more often misled by the AI's chart choices.

### 3.2 Purposes
Describing participants; controlling for literacy in studies; comparing populations [boy2014]; evaluating training [ge2023].

### 3.3 Assumptions
The chart types and misleading designs in the test are the ones that matter; people try their best.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Visualization and education researchers.

### 4.2 Consumers and decisions informed
Researchers and educators; designers choosing chart complexity for an audience.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Treating low scores as a fixed trait of people rather than a product of training and exposure. Items leak and can be practised; training to a test's specific tricks.

## 5. Related metrics

### 5.1 Operationally related metrics
Mini-VLAT, A-VLAT and A-CALVI are forms of the instruments on this page.

### 5.2 Conceptually related metrics
[Numeracy Score (ability test)](numeracy-score.md) measures a related ability.

<!-- generated:neighbours:start -->
- Sibling construct: [Numeracy Score (ability test)](numeracy-score.md) (Literacy: numeracy)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: visualization literacy and numeracy scores are positively correlated. Why it could be true: reading values and comparing quantities on charts draws on number skills (further reference needed).

## 6. Links to business objectives
Not linked to the objectives directly: user characteristics describe users and explain differences in outcomes.

## 7. Sources
- [lee2017]: VLAT.
- [pandey2023]: Mini-VLAT.
- [cui2024]: adaptive VLAT and CALVI.
- [ge2023]: CALVI.
- [boy2014]: principles of literacy tests.
- [embretson2000]: item response theory.
- [ding2023]: reVISit.

## Open questions and review notes
- Merged from the former VLAT and CALVI pages (D25).
