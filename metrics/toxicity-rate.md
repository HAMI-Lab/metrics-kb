---
id: toxicity-rate
title: Toxicity Rate
aliases: [toxicity score, expected maximum toxicity, toxic generation rate]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, ai-safety, nlp]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How often a system's outputs contain rude, hateful or otherwise toxic language."
  measures: [safety]
  subject: [system]
  aspect: [safety]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [benchmark, logs-telemetry]
  route: [external-judgment]
  collection_mode: [offline, online]
  data_source: [model-judge]
  unit: "proportion"
  range: "0-1"
  better: lower
  validity_concern: {level: high, note: "A classifier decides what is toxic; its errors and biases become the metric's."}
  instruments:
    - {name: "RealToxicityPrompts", sources: [gehman2020], probes: "toxic continuations of ordinary web text", scale: "share of toxic outputs, or expected maximum toxicity, 0-1", note: "Sentence prefixes from web text, continued by the model and scored by a toxicity classifier."}

cost:
  level: low
  requires: ["a prompt set or logged outputs", "a toxicity classifier"]
  automatable: true

related:
  - {metric: attack-success-rate, kind: conceptual, note: "Harm under attack rather than in ordinary use."}
  - {metric: demographic-parity-difference, kind: conceptual, note: "Toxicity can also be compared across groups mentioned in prompts."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Toxic outputs drive users away and damage reputation."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Toxic outputs make the system unpleasant to use."}

sources: [gehman2020, liang2022, liu2025]
---

# Toxicity Rate

> The share of generated outputs that a toxicity classifier flags as toxic.

## 1. What is measured

### 1.1 Definition
Toxicity Rate is the share of a system's outputs that a toxicity classifier scores above a threshold. Prompts come from a benchmark, some designed to provoke toxic continuations, or from real use [gehman2020; liang2022].

### 1.2 Construct: property of subject in context
The property is safety in the sense of avoiding toxic language. The subject is the system as users see it. The context is a prompt set or a period of real use.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Output quality: safety](../constructs/safety.md) (under System characteristics → System performance → Output quality)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not cover other harms, such as dangerous instructions or misinformation. It does not say whether toxic content was provoked by the user.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy**: the classifier's judgment stands in for people's. Hypothesis: classifiers flag some harmless text, such as mentions of identity groups or certain dialects, more often than other harmless text. Why it could be true: classifiers learn from training labels in which such words co-occurred with toxic posts (further reference needed).

**Using a proxy with a known gap.** The rate can track whether a change made outputs more or less toxic *according to this classifier*. It cannot support claims about how offensive outputs are to the people who read them, or that the system is fair across groups. Report the classifier and threshold; check a sample of flagged and unflagged outputs by hand; and check whether flags cluster on prompts about particular groups.

### 2.2 Reliability
Stable for one classifier; changes when the classifier is updated, so keep the version fixed when comparing over time.

### 2.3 Data collection and measurement error
Generate outputs for a prompt set such as RealToxicityPrompts [gehman2020], or sample logged outputs, and score each with a classifier.

### 2.4 Computation
- Toxicity rate = outputs scored above the threshold ÷ all outputs.
- Expected maximum toxicity: for each prompt, the highest toxicity among several generations, averaged over prompts [gehman2020].
- Report the classifier, its version, and the threshold.

### 2.5 Unit and scale
0 to 1. Lower is better.

### 2.6 Instruments
**Toxic degeneration**
- **RealToxicityPrompts** [gehman2020]: prompts taken from web text, including many that are not toxic themselves; the model continues each one and a toxicity classifier scores the output. Reported as the share of toxic continuations and as expected maximum toxicity over several samples. Results depend on the classifier and its version.

## 3. Why it is measured

### 3.1 Use cases
- A team training a customer-service model compares toxicity rates on a provocation prompt set before and after safety fine-tuning [gehman2020].
- A social app with an AI reply assistant monitors the weekly toxicity rate of suggested replies in production.

### 3.2 Purposes
Comparing models and safety training; monitoring deployed systems [liang2022].

### 3.3 Assumptions
The classifier's notion of toxicity matches that of the users; the prompt set represents use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Safety and trust-and-safety teams.

### 4.2 Consumers and decisions informed
Model teams, policy teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Models can learn to avoid the words the classifier reacts to while staying offensive. Filtering on the classifier can silence harmless content about some groups.

## 5. Related metrics

### 5.1 Operationally related metrics
Expected maximum toxicity is a variant on this page.

### 5.2 Conceptually related metrics
[Attack Success Rate](attack-success-rate.md) measures harm under attack.

<!-- generated:neighbours:start -->
- Same construct: [Attack Success Rate (ASR)](attack-success-rate.md) (Output quality: safety)
- Sibling construct: [Demographic Parity Difference (DPD)](demographic-parity-difference.md) (Output quality: fairness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** negative, theoretical.

## 7. Sources
- [gehman2020]: RealToxicityPrompts and expected maximum toxicity.
- [liang2022]: toxicity in LLM benchmarks.
- [liu2025]: toxicity in safety evaluation.

## Open questions and review notes
- None yet.
