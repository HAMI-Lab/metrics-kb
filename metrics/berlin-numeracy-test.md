---
id: berlin-numeracy-test
title: Berlin Numeracy Test
aliases: [BNT, risk literacy test, statistical numeracy test]
page_type: metric
template_version: "0.2"
fields: [psychology, health]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a person understands numbers, probabilities and risk, shown by solving short word problems."
  measures: [numeracy]
  subject: [user]
  aspect: [ability]
  perspective: [objective]
  quantity_form: [count]
  context: [user-specific]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [ability-test]
  route: [reference-comparison]
  collection_mode: [in-lab, field]
  data_source: [reference-answers]
  unit: "number correct (or quartile)"
  range: "0-4 (four-item form)"
  better: higher
  validity_concern: {level: low, note: "Direct for statistical numeracy as the test defines it; designed for educated populations."}

cost:
  level: low
  requires: ["about 2-3 minutes"]
  automatable: false

related:
  - {metric: vlat, kind: conceptual, note: "Visualization literacy draws on related skills."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: [cokely2012, ding2023]
---

# Berlin Numeracy Test

> A short test of probability and risk word problems, in one-item, four-item and adaptive forms.

## 1. What is measured

### 1.1 Definition
The Berlin Numeracy Test asks short word problems about probabilities and risks, such as the chance of an outcome given some information. It has a four-item paper form, a one-item form, and a computer-adaptive form that uses two or three items depending on earlier answers [cokely2012]. Scores place people into four levels of numeracy.

### 1.2 Construct: property of subject in context
The property is numeracy, especially statistical numeracy and risk literacy. The subject is the person. The context is the test's problems.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Literacy: numeracy](../constructs/numeracy.md) (under User characteristics → Literacy)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure everyday arithmetic in general, or how people feel about numbers.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for statistical numeracy as the test defines it. It was designed to tell apart people in educated populations, so it may not separate people well at the low end (check against [cokely2012]).

### 2.2 Reliability
The authors report reliability and validity across countries (check against [cokely2012]). The one-item form is coarse.

### 2.3 Data collection and measurement error
Paper or online, often in study platforms such as reVISit [ding2023]. See [ability tests](../strategies/ability-test.md).

### 2.4 Computation
- Four-item form: number correct (0-4), often reported as quartiles.
- Adaptive form: assigns a quartile from two or three answers [cokely2012].

### 2.5 Unit and scale
Number correct or quartile (1-4).

## 3. Why it is measured

### 3.1 Use cases
- A study of risk communication in a patient app checks whether a new chart of side-effect risks helps low-numeracy patients.
- A visualization study controls for numeracy when comparing uncertainty displays.

### 3.2 Purposes
Describing participants; controlling for numeracy; tailoring risk communication [cokely2012].

### 3.3 Assumptions
Participants are not using calculators or looking up answers, unless allowed.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Psychology, health and visualization researchers.

### 4.2 Consumers and decisions informed
Researchers, designers of risk communication.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Using it outside the populations it was designed for.

## 5. Related metrics

### 5.1 Operationally related metrics
The one-item, four-item and adaptive forms are on this page.

### 5.2 Conceptually related metrics
[VLAT](vlat.md) measures a related literacy.

<!-- generated:neighbours:start -->
- Sibling construct: [Visualization Literacy Assessment Test (VLAT)](vlat.md) (Literacy: visualization literacy)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
See the hypothesis on the [VLAT](vlat.md) page about correlation with visualization literacy.

## 6. Links to business objectives
Not linked to the objectives directly.

## 7. Sources
- [cokely2012]: the Berlin Numeracy Test.
- [ding2023]: reVISit.

## Open questions and review notes
- None yet.
