---
id: calibration
title: "Classification performance: calibration"
aliases: [confidence calibration]
page_type: construct
template_version: "0.1"
fields: [machine-learning, llm-evaluation]

broader: [classification-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [guo2017, liang2022, brier1950]
---

# Classification performance: calibration

> Whether a model's stated confidence matches how often it is right.

## 1. Definition
A model is calibrated when, among predictions made with confidence *p*, about a share *p* are correct [guo2017]. More calibration means its confidence can be taken at face value, for example to decide when to defer to a person.

## 2. Boundaries
Distinct from [correctness](classification-correctness.md): a model can be accurate but overconfident, or poorly accurate but honest about it. It applies to any component that outputs a probability or confidence, including language models answering questions [liang2022].

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Expected calibration error summarizes the gap over confidence bins; the Brier score [brier1950] mixes calibration with accuracy.
<!-- generated:metrics:start -->
- [Expected Calibration Error](../metrics/expected-calibration-error.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: users and downstream components can only rely appropriately on confidence that is calibrated.

## 6. How it is identified
Probability forecasting [brier1950] and machine learning [guo2017].

## 7. Sources
- [guo2017]: calibration of modern neural networks.
- [liang2022]: calibration in language-model evaluation.
- [brier1950]: the Brier score.

## Open questions and review notes
- Is calibration a classification property only, or should it sit under component performance for any component that outputs confidence?
