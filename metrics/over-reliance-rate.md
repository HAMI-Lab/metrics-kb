---
id: over-reliance-rate
title: Over-reliance Rate
aliases: [over-reliance, automation bias rate, following wrong advice]
page_type: metric
template_version: "0.3"
fields: [human-ai-interaction, xai]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "When the system's advice is wrong, how often people follow it anyway."
  measures: [appropriate-reliance]
  subject: [user-system-team]
  aspect: [trust, effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [task-study]
  route: [reference-comparison]
  collection_mode: [in-lab, field]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: lower
  validity_concern: {level: moderate, note: "Needs enough cases where the advice is wrong (or right); the study's mix of right and wrong advice shapes the rate."}

cost:
  level: high
  requires: ["participants", "cases with known outcomes", "advice that is sometimes wrong"]
  automatable: false

related:
  - {metric: under-reliance-rate, kind: conceptual, note: "The opposite failure; the two trade off."}
  - {metric: decision-accuracy-with-ai, kind: conceptual, note: "Team accuracy; reliance rates explain its errors."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Over-reliance may keep people using a system they should question; under-reliance wastes it."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Inappropriate reliance lowers decision quality."}

sources: [schemmer2023, cabitza2023, lee2004]
---

# Over-reliance Rate

> The share of wrong recommendations that people accept.

## 1. What is measured

### 1.1 Definition
Over-reliance Rate is the share of cases with wrong advice in which the person's final decision follows that advice. It is read from a table of cases by whether the advice was right and whether the person followed it [schemmer2023; cabitza2023].

### 1.2 Construct: property of subject in context
The property is appropriateness of reliance: following the system when it is right and not when it is wrong. The subject is the person deciding with the system. The context is a set of cases with known right answers.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Reliance on AI: appropriateness](../constructs/appropriate-reliance.md) (under Task characteristics → Reliance on AI)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It says nothing about cases where the advice is right; a person who rejects all advice has zero over-reliance. Pair it with [Under-reliance Rate](under-reliance-rate.md).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the cases in the study. Following advice is not always reliance: the person may have reached the same decision alone. Designs that record a decision before and after the advice separate the two [schemmer2023].

### 2.2 Reliability
Depends on the number of cases with wrong (or right) advice; studies often have few wrong-advice cases, so the rate is noisy.

### 2.3 Data collection and measurement error
A task study in which participants decide cases with advice whose correctness is known; ideally they decide first without advice, then again with it.

### 2.4 Computation
- Over-reliance = cases where advice was wrong and followed ÷ cases where advice was wrong.
- With a decision before and after the advice: count only cases where the person switched to (or away from) the advice; relative measures of this kind are proposed by [schemmer2023] (check against the paper).

### 2.5 Unit and scale
0 to 1. Lower is better.

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A study of a sepsis-alert tool counts how often physicians accepted the alert's recommendation on cases where it was wrong.
- A content-moderation tool is tested with deliberately wrong suggestions to see how often moderators accept them.

### 3.2 Purposes
Evaluating explanation and interface designs meant to support appropriate reliance [schemmer2023].

### 3.3 Assumptions
The ground truth is known; the advice errors in the study are like those in use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
HCI and XAI researchers.

### 4.2 Consumers and decisions informed
Designers of decision-support systems; safety reviewers.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Lowering over-reliance by making people distrust everything raises under-reliance.

## 5. Related metrics

### 5.1 Operationally related metrics
The same decision table yields [Under-reliance Rate](under-reliance-rate.md).

### 5.2 Conceptually related metrics
[Decision Accuracy with AI Assistance](decision-accuracy-with-ai.md) is the overall outcome these rates explain.

<!-- generated:neighbours:start -->
- Same construct: [Under-reliance Rate](under-reliance-rate.md) (Reliance on AI: appropriateness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: interventions that reduce one kind of inappropriate reliance tend to increase the other. Why it could be true: both depend on one general tendency to accept advice, so shifting it helps one side and hurts the other unless people get better at telling right from wrong advice (further reference needed).

## 6. Links to business objectives
**Improved usability:** negative, theoretical. **Sustained use:** unknown.

## 7. Sources
- [schemmer2023]: appropriateness of reliance.
- [cabitza2023]: beneficial and detrimental reliance patterns.
- [lee2004]: trust and appropriate reliance.

## Open questions and review notes
- None yet.
