---
id: aopc
title: "Area Over the Perturbation Curve (AOPC)"
aliases: [AOPC, deletion metric, feature removal test]
page_type: metric
template_version: "0.2"
fields: [xai, machine-learning]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much a model's output drops when the input features an explanation ranks as most important are removed first."
  measures: [explanation-faithfulness]
  subject: [system-component]
  aspect: [effectiveness, trust]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [test-collection, controlled-comparison]
  route: [difference-scoring]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "output units (often probability)"
  range: "depends on output scale"
  better: higher
  validity_concern: {level: high, note: "Removing features creates unnatural inputs, so drops may reflect the change rather than reliance (see 2.1)."}

cost:
  level: low
  requires: ["a model with scores", "explanations to test", "a removal or replacement scheme"]
  automatable: true

related:
  - {metric: accuracy, kind: conceptual, note: "Unrelated to accuracy: a faithful explanation can explain a wrong prediction."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: positive, evidence: theoretical, note: "Faithful explanations are a precondition for users to understand the model."}

sources: [samek2017, nauta2023, pawlicki2024]
---

# Area Over the Perturbation Curve (AOPC)

> Remove the most important features first, step by step, and average how much the model's output falls.

## 1. What is measured

### 1.1 Definition
The area over the perturbation curve (AOPC) tests an explanation by removing the features it ranks as most important and watching the model's output fall [samek2017]. An explanation ranks input features (pixels, words, columns) by importance. Features are removed or replaced in that order, step by step, and the output is recorded after each step. AOPC is the average drop over the steps. If the explanation is faithful, removing its top features should hurt the output quickly.

### 1.2 Construct: property of subject in context
The property is faithfulness of explanations to the model. The subject is an explanation method applied to a model. The context is a test set and a removal scheme.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Explanation performance: faithfulness](../constructs/explanation-faithfulness.md) (under Component characteristics → Component performance → Explanation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not show whether people understand or trust the explanation. A faithful explanation of a wrong prediction still scores well.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the effect of removal under the chosen scheme; **proxy** for what the model relies on. Removing features produces inputs unlike training data, so the output may drop because the input is strange, not because the feature mattered [nauta2023].

**Using a proxy with a known gap.** AOPC can rank explanation methods under one removal scheme. It cannot show that an explanation is faithful in general, and still less that users will understand it. Report the removal scheme, compare with removal in random order, and, if the choice matters, check that the ranking holds under a second scheme.

### 2.2 Reliability
Sensitive to the replacement value, step size and number of steps; report them.

### 2.3 Data collection and measurement error
For each test input: compute the explanation, then perturb the input in order of importance and record outputs.

### 2.4 Computation
- AOPC = (1 ÷ (L + 1)) × Σ_{k=0..L} [f(x) − f(x with top k features removed)], averaged over inputs [samek2017].
- Compare with removal in random order, as a baseline.

### 2.5 Unit and scale
In units of the model output, usually probability of the predicted class.

## 3. Why it is measured

### 3.1 Use cases
- A medical-imaging team compares two saliency methods by how quickly classifier confidence drops when the highlighted regions are masked.
- A credit-scoring team checks whether its feature attributions point at features the model actually uses.

### 3.2 Purposes
Choosing explanation methods; sanity checks before showing explanations to users [nauta2023].

### 3.3 Assumptions
Removing a feature removes its information without adding new signals.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
XAI researchers and ML engineers.

### 4.2 Consumers and decisions informed
Teams deciding which explanations to show.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Methods can be tuned to the removal scheme. A good AOPC can be taken as proof that explanations help users, which needs a user study.

## 5. Related metrics

### 5.1 Operationally related metrics
Insertion curves (adding features in order of importance) are a mirror variant.

### 5.2 Conceptually related metrics
[Accuracy](accuracy.md) is independent of faithfulness.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: AOPC and other faithfulness metrics can rank explanation methods differently. Why it could be true: each metric changes the input in its own way (removal, replacement, insertion), and each change creates its own unnatural inputs, so the drops measure partly different things. Whether several metrics are needed at all is the question [pawlicki2024] examines (further reference needed for the direction of the finding).

## 6. Links to business objectives
**Improved usability:** positive, theoretical. **Sustained use:** unknown.

## 7. Sources
- [samek2017]: region perturbation and AOPC.
- [nauta2023]: review of faithfulness measures.
- [pawlicki2024]: disagreement between XAI metrics.

## Open questions and review notes
- None yet.
