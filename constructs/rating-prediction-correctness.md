---
id: rating-prediction-correctness
title: "Recommendation performance: rating prediction correctness"
aliases: [rating prediction error, numeric prediction accuracy]
page_type: construct
template_version: "0.1"
fields: [recommender-systems]

broader: [recommendation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [koren2009, cremonesi2010]
---

# Recommendation performance: rating prediction correctness

> How close a recommender's predicted ratings are to the ratings people actually gave. For continuous predictions like these, correctness means closeness, not right or wrong.

## 1. Definition
The distance between the ratings a recommender predicts and the ratings people gave, averaged over held-out ratings [koren2009].

## 2. Boundaries
Being close on average does not mean ranking the right items first [cremonesi2010]. It says nothing about items people never rated.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
RMSE and mean absolute error are the usual metrics.
<!-- generated:metrics:start -->
- [Root Mean Squared Error (RMSE)](../metrics/root-mean-squared-error.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical and weak.

## 6. How it is identified
Recommender-systems research [koren2009].

## 7. Sources
- [koren2009]: RMSE in rating prediction.
- [cremonesi2010]: rating error vs top-N quality.

## Open questions and review notes
- None yet.
