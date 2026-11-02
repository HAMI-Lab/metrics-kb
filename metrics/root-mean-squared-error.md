---
id: root-mean-squared-error
title: "Root Mean Squared Error (RMSE)"
aliases: [RMSE, MSE, mean squared error, MAE, mean absolute error]
page_type: metric
template_version: "0.3"
fields: [recommender-systems, machine-learning]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How far a recommender's predicted ratings are from the ratings people gave, with large errors weighted more."
  measures: [rating-prediction-accuracy]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: ["other: error in the target's units"]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [benchmark]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers, interaction-logs]
  unit: "units of the predicted value (for example rating points)"
  range: "0 upward"
  better: lower
  validity_concern: {level: moderate, note: "Direct for prediction error; a weak proxy for recommendation quality, since accurate ratings do not guarantee good top-N lists."}
  instruments:
    - {name: "Netflix Prize data", kind: content, sources: [koren2009], probes: "predicting users' movie ratings", scale: "RMSE in rating points", note: "Movie ratings; RMSE was the competition measure."}
    - {name: "MovieLens", kind: content, sources: [harper2015], probes: "predicting users' movie ratings", scale: "RMSE or MAE in rating points", note: "Several public rating data sets of different sizes."}

cost:
  level: low
  requires: ["held-out observed values"]
  automatable: true

related:
  - {metric: ndcg, kind: empirical, note: "Rating-prediction error and ranking quality can disagree."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}
  improved-usability: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}

sources: [koren2009, harper2015, cremonesi2010]
---

# Root Mean Squared Error (RMSE)

> The square root of the mean squared difference between predicted and observed values.

## 1. What is measured

### 1.1 Definition
Root Mean Squared Error (RMSE) is the square root of the average squared difference between predicted and observed values. Mean squared error (MSE) omits the square root; mean absolute error (MAE) averages absolute differences. In recommender systems it measures how well a model predicts the ratings users give items [koren2009].

### 1.2 Construct: property of subject in context
The property is rating prediction accuracy. The subject is a recommender component. The context is held-out ratings. The same formula is used for other numeric predictions; within this wiki's scope, rating prediction is its main use (D29).

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Recommendation performance: rating prediction accuracy](../constructs/rating-prediction-accuracy.md) (under Component characteristics → Component performance → Recommendation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Whether the best items end up at the top of a recommendation list; whether users like the recommendations.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for prediction error; **proxy** for recommendation quality, hence `mixed`. Lower rating error does not reliably give better top-N recommendations [cremonesi2010] (check against the paper).

**Using a proxy with a known gap.** RMSE can compare rating predictors on the same data. It cannot show that recommendation lists improve; check with a ranking metric such as [nDCG](ndcg.md) and, ideally, with users.

### 2.2 Reliability
Stable on large held-out sets; sensitive to outliers because errors are squared.

### 2.3 Data collection and measurement error
Hold out observed values; predict them; compare.

### 2.4 Computation
- RMSE = √(mean of (prediction − observed)²).
- MSE: without the square root. MAE: mean of |prediction − observed|.

### 2.5 Unit and scale
In the units of the predicted value; 0 is perfect. Only comparable on the same data and scale.

### 2.6 Instruments
**Predicting users' ratings**
- **Netflix Prize data** [koren2009]: movie ratings; RMSE was the competition measure.
- **MovieLens** [harper2015]: public movie-rating data sets of several sizes.

## 3. Why it is measured

### 3.1 Use cases
- A recommender team compares rating models on MovieLens before testing ranking quality.

### 3.2 Purposes
Comparing numeric predictors; regression testing.

### 3.3 Assumptions
Errors of the same size matter equally everywhere on the scale.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML and recommender engineers.

### 4.2 Consumers and decisions informed
Teams choosing prediction models.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing RMSE favours predicting average ratings well over finding the few items a user would love.

## 5. Related metrics

### 5.1 Operationally related metrics
MSE and MAE are variants on this page.

### 5.2 Conceptually related metrics
[nDCG](ndcg.md) measures ranking quality instead.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
RMSE and top-N ranking quality can disagree [cremonesi2010] (check against the paper).

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [koren2009]: rating prediction and RMSE.
- [harper2015]: MovieLens.
- [cremonesi2010]: rating error vs top-N quality.

## Open questions and review notes
- `quantity_form` uses `other: error in the target's units`; should the vocabulary gain an error value?
