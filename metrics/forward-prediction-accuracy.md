---
id: forward-prediction-accuracy
title: Forward-Prediction Accuracy
aliases: [simulatability, forward simulation accuracy, explanation comprehension accuracy]
page_type: metric
template_version: "0.2"
fields: [xai, human-ai-interaction]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How often people can correctly predict what a model will output for a new input."
  measures: [explanation-understanding]
  subject: [user]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [task-study, controlled-comparison]
  route: [reference-comparison]
  collection_mode: [in-lab]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Predicting outputs is one sign of understanding; it may not reflect understanding of why the model behaves as it does."}

cost:
  level: medium
  requires: ["participants", "a model and explanations to test"]
  automatable: false

related:
  - {metric: aopc, kind: conceptual, note: "Faithfulness of explanations judged without people."}
  - {metric: over-reliance-rate, kind: empirical, note: "Understanding the model is expected to support appropriate reliance."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: positive, evidence: theoretical, note: "Understanding supports appropriate use of the system."}

sources: [doshivelez2017, hase2020, kim2024]
---

# Forward-Prediction Accuracy

> The share of new inputs for which a person, after seeing explanations, correctly predicts the model's output.

## 1. What is measured

### 1.1 Definition
Forward-Prediction Accuracy is the share of new inputs for which a person correctly predicts what the model will output. People first study the model's outputs, with or without explanations, then predict its outputs on inputs they have not seen [doshivelez2017; hase2020].

### 1.2 Construct: property of subject in context
The property is understanding of the model, shown by being able to simulate it. The subject is the person who saw the explanations. The context is a model, a set of explanations and a set of test inputs.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Explanation understanding](../constructs/explanation-understanding.md) (under Task characteristics)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not check whether the person agrees with or trusts the model. It does not show whether explanations are faithful; see [AOPC](aopc.md).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the ability to predict outputs; **proxy** for understanding, hence `mixed`. People can learn surface patterns that predict outputs without understanding the reasons [kim2024].

**Using a proxy with a known gap.** It can compare explanation methods by how much they improve prediction over no explanation. It cannot show that people understand the model in a way that helps their real decisions. Compare with and without explanations, and pair it with a decision outcome such as [Decision Accuracy with AI Assistance](decision-accuracy-with-ai.md).

### 2.2 Reliability
Depends on the number of test inputs per person and on balance between inputs the model gets right and wrong.

### 2.3 Data collection and measurement error
A task study with a training phase and a test phase; often a controlled comparison of explanation conditions [hase2020].

### 2.4 Computation
- Accuracy = correct predictions ÷ predictions.
- Gain from explanations = accuracy with explanations − accuracy without [hase2020].

### 2.5 Unit and scale
0 to 1.

## 3. Why it is measured

### 3.1 Use cases
- An XAI team compares two attribution methods by how much each improves participants' predictions of a sentiment model [hase2020].
- A clinical team checks whether physicians, after a training session with explanations, can anticipate when a risk model will flag a patient.

### 3.2 Purposes
Comparing explanation methods with people [doshivelez2017; kim2024].

### 3.3 Assumptions
Predicting outputs reflects understanding; test inputs represent use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
XAI and HCI researchers.

### 4.2 Consumers and decisions informed
Teams choosing explanation designs.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Explanations tuned to make outputs easy to predict may simplify the model misleadingly.

## 5. Related metrics

### 5.1 Operationally related metrics
The gain from explanations is a variant on this page.

### 5.2 Conceptually related metrics
[AOPC](aopc.md) judges faithfulness without people.

<!-- generated:neighbours:start -->
- Sibling construct: [Trust in Automation Scale](trust-in-automation-scale.md) (Trust in the system), [User Experience Questionnaire (UEQ)](ueq.md) (User experience)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: higher forward-prediction accuracy goes with lower over-reliance. Why it could be true: people who can anticipate the model can also anticipate its errors (further reference needed).

## 6. Links to business objectives
**Improved usability:** positive, theoretical. **Sustained use:** unknown.

## 7. Sources
- [doshivelez2017]: forward simulation.
- [hase2020]: simulatability tests.
- [kim2024]: human-centered XAI evaluation.

## Open questions and review notes
- None yet.
