---
id: difference-scoring
title: "Difference scoring: changes between conditions"
aliases: [difference, difference score, gap, drop, disparity, relative change, contrast]
page_type: strategy
template_version: "0.2"

layer: route
research_methods: [controlled-comparison]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [cronbach1970, barocas2021, ribeiro2020, samek2017]
---

# Difference scoring: changes between conditions

> The number is how much a score changes from one condition to another.

## 1. What it is

### 1.1 Definition
A score is computed under two or more conditions that differ in one deliberate way, and the metric is the change between them. The scores themselves come from another route, such as comparison against reference data. The change can be a plain difference (B − A), a relative change ((B − A) ÷ A), a ratio (B ÷ A), or an average over several steps, such as the area under a curve of scores as inputs are changed more and more. All of these count as differences here: a ratio is a difference on a log scale.

### 1.2 Typical pairings
Fed by controlled comparison, which sets up the conditions. The scores being compared usually come from test collections or task studies.
<!-- generated:pairings:start -->
- [Controlled comparison of conditions](controlled-comparison.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Drop under perturbation:** score on changed inputs vs on the originals, as a measure of robustness [ribeiro2020].
- **Subgroup gap:** a score in one group of people minus the same score in another, as a measure of fairness [barocas2021].
- **Degradation curve:** scores as the most important input features are removed step by step, averaged over the steps, as a test of whether an explanation is faithful [samek2017].
- **Lift over baseline:** a system's score minus a baseline's or chance's.

## 2. When to use it
Use it when the construct is itself about change: whether performance holds under changed inputs, whether it is the same for different groups, whether removing something matters. Do not use it just to compare two systems on a metric: that is a study using the metric, and the number reported is still the metric (with a test of whether the gap is real).

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
The difference is only as meaningful as the change between conditions. A perturbation that also changes the right answer, or subgroups that differ in task difficulty, produce a gap that is not the construct. Relative changes exaggerate small baselines: going from 0.02 to 0.04 is a 100% increase.

### 3.2 Reliability
A difference between two noisy scores is noisier than either score, and becomes unreliable when the two scores are highly correlated [cronbach1970]. Report the uncertainty of the difference, not only of each score. Small subgroups give unstable gaps [barocas2021].

### 3.3 Bias and gaming
The choice of conditions decides the result: a system can look robust to a weak set of perturbations, or fair on a convenient split of groups. Report which conditions were used and why.

## 4. Cost
Twice (or more) the cost of the underlying score, because every condition must be measured.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [AOPC (deletion curve)](../metrics/aopc.md)
<!-- generated:metrics:end -->

## 6. Sources
- [cronbach1970]: reliability of difference scores.
- [barocas2021]: subgroup comparisons.
- [ribeiro2020]: tests with perturbed inputs.
- [samek2017]: degradation curves for explanations.

## Open questions and review notes
- Whether a significance test on the difference belongs here or in study design. Current answer: the difference is the number; the test is analysis, out of scope (D10).
