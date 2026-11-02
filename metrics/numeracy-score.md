---
id: numeracy-score
title: Numeracy Score (ability test)
aliases: [Berlin Numeracy Test, BNT, risk literacy test, statistical numeracy test, numeracy test]
page_type: metric
template_version: "0.3"
fields: [psychology, health]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well a person understands numbers, probabilities and risk, shown by solving short word problems with right answers."
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
  range: "0-4 (Berlin Numeracy Test, four-item form)"
  better: higher
  validity_concern: {level: low, note: "Direct for statistical numeracy as the test defines it; the Berlin test was designed for educated populations."}
  instruments:
    - {name: "Berlin Numeracy Test", sources: [cokely2012], probes: "statistical numeracy and risk literacy", scale: "number correct 0-4, or quartile 1-4", note: "Probability and risk word problems; four-item, one-item and adaptive forms."}

cost:
  level: low
  requires: ["about 2-3 minutes"]
  automatable: false

related:
  - {metric: visualization-literacy-score, kind: conceptual, note: "Visualization literacy draws on related skills."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}
  improved-usability: {direction: unknown, evidence: none, note: "Describes users; used to explain or control for differences in outcomes, not as a target."}

sources: [cokely2012, ding2023]
---

# Numeracy Score (ability test)

> A short test of word problems about numbers, probabilities and risk, such as the Berlin Numeracy Test.

## 1. What is measured

### 1.1 Definition
People solve short word problems with right answers, such as the chance of an outcome given some information. The score is the number correct, often turned into a level of numeracy. The Berlin Numeracy Test is the instrument on this page so far [cokely2012]; section 2.6 describes its forms.

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
**Direct** for statistical numeracy as the test defines it. The Berlin Numeracy Test was designed to tell apart people in educated populations, so it may not separate people well at the low end (check against [cokely2012]).

### 2.2 Reliability
Short tests give coarse scores; more items give finer distinctions. Figures for each instrument are in 2.6.

### 2.3 Data collection and measurement error
Paper or online, often in study platforms such as reVISit [ding2023]. See [ability tests](../strategies/ability-test.md).

### 2.4 Computation
Number of problems answered correctly, often turned into a level (quartile) of numeracy. Adaptive forms assign a level from fewer items. Each instrument's rule is in 2.6.

### 2.5 Unit and scale
Number correct (ratio) or level (ordinal), depending on the instrument and form (2.6). Higher is better.

### 2.6 Instruments
- **Berlin Numeracy Test** [cokely2012]: short word problems about probabilities and risks.
  - *Forms and scoring:* a four-item paper form scored as number correct (0-4), often reported as quartiles; a one-item form; and a computer-adaptive form that assigns a quartile from two or three answers.
  - *Reliability:* the authors report reliability and validity across countries (check against the paper). The one-item form is coarse. Designed to tell apart people in educated populations, so it may not separate people well at the low end (check against the paper).
  - *Choose* the adaptive or one-item form when time is short and coarse groups are enough.

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
Using a test outside the populations it was designed for.

## 5. Related metrics

### 5.1 Operationally related metrics
The forms of the Berlin Numeracy Test are on this page.

### 5.2 Conceptually related metrics
[Visualization Literacy Score (ability test)](visualization-literacy-score.md) measures a related literacy.

<!-- generated:neighbours:start -->
- Sibling construct: [Visualization Literacy Score (ability test)](visualization-literacy-score.md) (Literacy: visualization literacy)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
See the hypothesis on the [visualization literacy](visualization-literacy-score.md) page about correlation with visualization literacy.

## 6. Links to business objectives
Not linked to the objectives directly: user characteristics describe users and explain differences in outcomes.

## 7. Sources
- [cokely2012]: the Berlin Numeracy Test.
- [ding2023]: reVISit.

## Open questions and review notes
- Renamed from the former Berlin Numeracy Test page (D25).
- Other numeracy tests, such as older general numeracy scales, are candidates for 2.6; add them with verified sources.
