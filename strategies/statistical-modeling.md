---
id: statistical-modeling
title: Statistical and latent-variable modeling
aliases: [latent measurement, model-based measurement, inferred metrics]
page_type: strategy
template_version: "0.1"

research_methods: [questionnaire-survey, logs-telemetry]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [embretson2000, bollen1991, chuklin2015]
---

# Statistical and latent-variable modeling

> The number is estimated by a statistical model from many observed indicators, not read or judged directly.

## 1. What it is

### 1.1 Definition
A model links observed data (item responses, clicks, behaviours) to an unobserved quantity, and the metric is the model's estimate of that quantity.

### 1.2 Typical research methods
Questionnaires with many items, and large logs of behaviour.

### 1.3 Named practices
- **Psychometric scaling** with factor analysis or item response theory [embretson2000].
- **Reflective vs formative composites**: items that all reflect one construct, versus parts that together define it [bollen1991].
- **Click models** that infer relevance or satisfaction from click patterns [chuklin2015].
- **Predicted satisfaction or success** from behavioural features, trained on a labeled sample.

## 2. When to use it
Use it when the construct is not observable but has many noisy indicators, or to turn cheap behavioural data into an estimate of something that would otherwise need asking or judging.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
The estimate is valid only if the model's assumptions hold. Predictive models trained on one population or system version may not transfer. The model can hide what actually drives the score.

### 3.2 Reliability
Report estimation uncertainty and model fit; recheck when the system or population changes.

### 3.3 Bias and gaming
Indicators the model relies on can be gamed (for example, inducing clicks). Training data biases carry into the estimate.

## 4. Cost
Needs statistical expertise and data to fit; cheap to apply once fitted.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
_No metric page uses it yet._
<!-- generated:metrics:end -->

## 6. Sources
- [embretson2000]
- [bollen1991]
- [chuklin2015]

## Open questions and review notes
- None yet.
