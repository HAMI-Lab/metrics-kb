---
id: trust-in-automation-scale
title: Trust in Automation Scale
aliases: [Jian trust scale, checklist for trust between people and automation, trust questionnaire]
page_type: metric
template_version: "0.2"
fields: [human-factors, human-ai-interaction, xai]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much a person reports trusting (and distrusting) a particular automated system."
  measures: [trust-in-system]
  subject: [user]
  aspect: [trust]
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
  better: context-dependent
  validity_concern: {level: moderate, note: "Reported trust is an attitude; it does not show whether trust matches how trustworthy the system is."}

cost:
  level: low
  requires: ["people who used the system", "a few minutes"]
  automatable: false

related:
  - {metric: over-reliance-rate, kind: empirical, note: "Reported trust shapes reliance, but behaviour can differ from attitude."}
  - {metric: under-reliance-rate, kind: empirical, note: "Low trust can lead to rejecting right advice."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Trust affects whether people keep relying on a system."}
  improved-usability: {direction: unknown, evidence: none, note: "More trust is good only when it matches trustworthiness."}

sources: [jian2000, lee2004]
---

# Trust in Automation Scale

> A 12-item questionnaire on trust and distrust toward an automated system.

## 1. What is measured

### 1.1 Definition
The Trust in Automation Scale has 12 statements, some about trust (for example that the system is reliable) and some about distrust (for example that it is deceptive), rated on 7-point scales [jian2000].

### 1.2 Construct: property of subject in context
The property is trust in a particular system, as an attitude [lee2004]. The subject is the person. The context is having used the system.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Trust in the system](../constructs/trust-in-system.md) (under Task characteristics)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure whether people actually rely on the system, nor whether the system deserves trust. More trust is not better: the goal is trust that matches trustworthiness [lee2004].

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for reported trust. Hypothesis: trust and distrust items behave as two related factors rather than one scale. Why it could be true: the scale was built from separate trust and distrust words, and people can hold both views of a system at once (further reference needed).

### 2.2 Reliability
Multi-item, so internal consistency can be checked; report it for your sample.

### 2.3 Data collection and measurement error
Questionnaire after use. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
- Score each item 1-7; reverse-score distrust items; average. Or report trust and distrust separately (see 2.1).

### 2.5 Unit and scale
1-7 mean.

## 3. Why it is measured

### 3.1 Use cases
- An XAI study compares trust ratings for a model with and without explanations, alongside reliance rates on wrong advice.
- A driver-assistance study tracks trust after a system failure.

### 3.2 Purposes
Studying how explanations, errors and design change trust.

### 3.3 Assumptions
People can report trust; items mean the same for AI systems as for the automation they were written for.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Human factors and HCI researchers.

### 4.2 Consumers and decisions informed
Designers of automation and AI systems.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Designs that raise reported trust without raising trustworthiness can increase over-reliance.

## 5. Related metrics

### 5.1 Operationally related metrics
Separate trust and distrust subscores are a variant on this page.

### 5.2 Conceptually related metrics
Reliance behaviour is on [Over-reliance Rate](over-reliance-rate.md) and [Under-reliance Rate](under-reliance-rate.md).

<!-- generated:neighbours:start -->
- Sibling construct: [Forward-Prediction Accuracy](forward-prediction-accuracy.md) (Explanation understanding), [User Experience Questionnaire (UEQ)](ueq.md) (User experience)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: reported trust predicts reliance only partly. Why it could be true: reliance also depends on workload, time pressure and confidence in one's own judgment [lee2004] (further reference needed for measured correlations).

## 6. Links to business objectives
**Sustained use:** positive, theoretical. **Improved usability:** unknown.

## 7. Sources
- [jian2000]: the scale.
- [lee2004]: trust, trustworthiness and reliance.

## Open questions and review notes
- None yet.
