---
id: numeric-prediction-accuracy
title: "Numeric prediction performance: accuracy"
aliases: [prediction error, rating prediction accuracy]
page_type: construct
template_version: "0.1"
fields: [recommender-systems, machine-learning]

broader: [numeric-prediction-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [koren2009]
---

# Numeric prediction performance: accuracy

> How close predicted numbers are to the observed ones.

## 1. Definition
The distance between predicted and observed values, usually averaged over items [koren2009].

## 2. Boundaries
Being close on average does not mean ranking the right items first.

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
Recommender systems and regression [koren2009].

## 7. Sources
- [koren2009]: RMSE in rating prediction.

## Open questions and review notes
- None yet.
