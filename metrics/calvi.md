---
id: calvi
title: "Critical Thinking Assessment for Literacy in Visualizations (CALVI)"
aliases: [CALVI, A-CALVI, misleading visualization test]
page_type: metric
template_version: "0.2"
fields: [visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a person avoids being misled by charts whose design invites a wrong conclusion."
  measures: [critical-visualization-literacy]
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
  validity_concern: {level: moderate, note: "Covers the kinds of misleading design in the test; new tricks are not covered."}

cost:
  level: low
  requires: ["participants", "tens of minutes for the full form"]
  automatable: false

related:
  - {metric: vlat, kind: conceptual, note: "Reading well-made charts rather than misleading ones."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: [ge2023, cui2024, ding2023]
---

# Critical Thinking Assessment for Literacy in Visualizations (CALVI)

> A test of whether people reach the right answer from charts designed to mislead, such as truncated axes.

## 1. What is measured

### 1.1 Definition
Critical Thinking Assessment for Literacy in Visualizations (CALVI) shows people charts, many built with misleading features such as truncated or inverted axes, inappropriate aggregation or missing data, and asks questions with right answers [ge2023]. A person who reads the chart critically answers correctly; one who is misled picks the answer the design invites. The score is the share correct. An adaptive form, A-CALVI, exists [cui2024].

### 1.2 Construct: property of subject in context
The property is critical visualization literacy. The subject is the person. The context is the test's set of misleading designs.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Literacy: critical visualization literacy](../constructs/critical-visualization-literacy.md) (under User characteristics → Literacy → Literacy: visualization literacy)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure general chart reading on well-made charts; see [VLAT](vlat.md).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the kinds of misleading design in the test. It includes normal items too, so that answering "it's misleading" every time does not score well (check against [ge2023]).

**Using a proxy with a known gap.** Scores can compare groups or show whether training improves critical reading of the covered designs. They cannot show that people will resist new or subtler misleading charts outside the test.

### 2.2 Reliability
The authors report item analysis with item response theory (check against [ge2023]).

### 2.3 Data collection and measurement error
As for other [ability tests](../strategies/ability-test.md); available in study platforms such as reVISit [ding2023].

### 2.4 Computation
- Share correct; or an ability estimate from an item response theory model, used for the adaptive form [cui2024].

### 2.5 Unit and scale
Share correct (0-1), or a latent ability score.

## 3. Why it is measured

### 3.1 Use cases
- A media-literacy course gives CALVI before and after a unit on misleading charts.
- A study of AI-generated charts uses CALVI to check whether participants who score low are more often misled by the AI's chart choices.

### 3.2 Purposes
Describing participants; evaluating training [ge2023].

### 3.3 Assumptions
The misleading designs in the test represent those people meet.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Visualization and education researchers.

### 4.2 Consumers and decisions informed
Researchers, educators.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Training to the test's specific tricks.

## 5. Related metrics

### 5.1 Operationally related metrics
A-CALVI is a variant on this page.

### 5.2 Conceptually related metrics
[VLAT](vlat.md) measures the broader construct on well-made charts.

<!-- generated:neighbours:start -->
- Broader construct: [Visualization Literacy Assessment Test (VLAT)](vlat.md) (Literacy: visualization literacy)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
Not linked to the objectives directly.

## 7. Sources
- [ge2023]: CALVI.
- [cui2024]: adaptive form.
- [ding2023]: reVISit.

## Open questions and review notes
- None yet.
