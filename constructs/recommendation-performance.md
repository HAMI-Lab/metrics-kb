---
id: recommendation-performance
title: Recommendation performance
aliases: [recommender performance, numeric prediction performance]
page_type: construct
template_version: "0.1"
fields: [recommender-systems]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [koren2009, cremonesi2010]
---

# Recommendation performance

> How well a recommender component predicts which items a person will like, and how much.

## 1. Definition
The performance of a recommender as a component: given a person and a set of items, it predicts how much the person would like each item, as a rating or a score, or ranks the items for them [koren2009]. Recommendation components were deferred in D15; this lifts the deferral for rating prediction (D31).

## 2. Boundaries
Ranking items for a person overlaps with [retrieval](retrieval-performance.md), and ranking metrics such as nDCG are used for both. Predicting ratings well does not guarantee good ranked lists [cremonesi2010]. Whether people like and use the recommendations is a task characteristic.

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Recommendation performance: rating prediction correctness](rating-prediction-correctness.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect, through the recommendations people see.

## 6. How it is identified
Recommender-systems research, including the Netflix Prize [koren2009].

## 7. Sources
- [koren2009]: rating prediction.
- [cremonesi2010]: rating prediction vs top-N ranking.

## Open questions and review notes
- None yet.
