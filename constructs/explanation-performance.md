---
id: explanation-performance
title: Explanation performance
aliases: [explanation quality (algorithmic)]
page_type: construct
template_version: "0.1"
fields: [xai]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [nauta2023, pawlicki2024]
---

# Explanation performance

> How good the explanations an explanation component produces are, judged without users.

## 1. Definition
Properties of explanations (feature attributions, highlighted regions, rationales) computed against the model they explain, without asking people [nauta2023].

## 2. Boundaries
Whether people understand or benefit from the explanations is a task characteristic: [explanation understanding](explanation-understanding.md).

## 3. Narrower constructs
Faithfulness is the main narrower construct; others proposed in the literature include robustness of explanations and their compactness [nauta2023; pawlicki2024].
<!-- generated:narrower:start -->
- [Explanation performance: faithfulness](explanation-faithfulness.md)
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: unfaithful explanations can mislead users.

## 6. How it is identified
Systematic reviews of XAI evaluation [nauta2023; pawlicki2024].

## 7. Sources
- [nauta2023]: quantitative XAI evaluation methods.
- [pawlicki2024]: whether multiple XAI metrics are needed.

## Open questions and review notes
- None yet.
