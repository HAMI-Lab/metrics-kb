---
id: explanation-faithfulness
title: "Explanation performance: faithfulness"
aliases: [fidelity]
page_type: construct
template_version: "0.1"
fields: [xai]

broader: [explanation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [nauta2023, samek2017]
---

# Explanation performance: faithfulness

> Whether an explanation reflects what the model actually relies on.

## 1. Definition
An explanation is faithful when the features it marks as important are the ones that drive the model's output: removing them changes the output more than removing others [samek2017; nauta2023].

## 2. Boundaries
Faithful explanations may still be hard for people to understand, and plausible-looking explanations may be unfaithful.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
- [AOPC (deletion curve)](../metrics/aopc.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical.

## 6. How it is identified
XAI evaluation literature [nauta2023].

## 7. Sources
- [samek2017]: perturbation-based evaluation.
- [nauta2023]: review of faithfulness measures.

## Open questions and review notes
- None yet.
