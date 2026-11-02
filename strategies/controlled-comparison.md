---
id: controlled-comparison
title: Controlled comparison of conditions
aliases: [comparison design, method of difference, ablation, perturbation testing, stress testing, disaggregated evaluation]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [ribeiro2020, barocas2021, samek2017, zhu2023, chang2024]
---

# Controlled comparison of conditions

> The same measurement is taken under conditions that differ in one deliberate way, with everything else held fixed.

## 1. What it is

### 1.1 Definition
The data comes from running the same measurement more than once: on the original and on a deliberately changed version of the inputs, the system, or the population. Because only one thing differs between conditions, a change in the score can be attributed to it. This is the logic of experimental design. The conditions are usually built on top of another method, such as a test collection or a task study.

### 1.2 Typical pairings
The difference-scoring route turns the paired scores into one number.
<!-- generated:pairings:start -->
- [Difference scoring: changes between conditions](difference-scoring.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Baseline comparison:** against a previous version, a simple baseline, or chance.
- **Ablation:** the same system with one part removed.
- **Perturbation or stress testing:** inputs changed in ways that should not change the right answer (typos, paraphrases, reordering) or should change it in a known direction [ribeiro2020]. Adversarial perturbation searches for changes that hurt most [zhu2023].
- **Counterfactual testing:** a sensitive attribute in the input is swapped, such as a name or pronoun, with everything else kept [chang2024].
- **Disaggregated evaluation:** the same score computed separately for groups of people or inputs [barocas2021].
- **Feature removal:** inputs are changed by removing the features an explanation marks as important [samek2017].
- **Hypothesis testing:** a statistical test of whether the difference between conditions could be due to chance. It decides whether a difference is real; it does not produce the metric, so it is analysis rather than measurement.

## 2. When to use it
Use it when the construct is about how a score depends on something: robustness, fairness, the contribution of a component, the faithfulness of an explanation. When the aim is only to compare two systems on an existing metric, the comparison is a study design and the metric's own page applies.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
The comparison isolates one factor only if nothing else changed. Perturbed inputs can become unnatural, so a drop may reflect strange inputs rather than fragility. Subgroups can differ in more than the attribute of interest, for example in task difficulty [barocas2021].

### 3.2 Reliability
Each condition needs enough data on its own; small subgroups and few perturbations give unstable comparisons.

### 3.3 Bias and gaming
The set of conditions is chosen by the evaluator, and a convenient choice can make a system look robust or fair. Fixed public perturbation sets can be overfit like any benchmark.

## 4. Cost
At least the cost of the underlying measurement per condition, plus the work of constructing the conditions (perturbation generators, group labels, ablated versions).

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Area Over the Perturbation Curve (AOPC)](../metrics/aopc.md)
<!-- generated:metrics:end -->

## 6. Sources
- [ribeiro2020]: behavioral testing with perturbed inputs.
- [zhu2023]: adversarial prompt perturbation.
- [chang2024]: counterfactual tests in LLM evaluation.
- [barocas2021]: disaggregated evaluation.
- [samek2017]: feature removal for explanations.

## Open questions and review notes
- D10 put study design out of scope. This method is in scope only when the comparison produces the metric itself. Is that boundary clear enough on metric pages?
