---
id: numeric-prediction-performance
title: Numeric prediction performance
aliases: [regression performance, rating prediction performance]
page_type: construct
template_version: "0.1"
fields: [recommender-systems, machine-learning]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [koren2009]
---

# Numeric prediction performance

> How well a component predicts a number, such as the rating a user would give an item.

## 1. Definition
Output type (D23): the output is a number on a continuous or ordered scale, judged by its distance from the observed value [koren2009].

## 2. Boundaries
Not [classification](classification-performance.md), where the output is a label, nor [retrieval](retrieval-performance.md), where it is a ranking; recommenders can be evaluated either way, and the two can disagree.

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Numeric prediction performance: accuracy](numeric-prediction-accuracy.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect.

## 6. How it is identified
Rating prediction in recommender systems [koren2009].

## 7. Sources
- [koren2009]: rating prediction.

## Open questions and review notes
- None yet.
