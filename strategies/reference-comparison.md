---
id: reference-comparison
title: Comparison against reference data
aliases: [gold-standard evaluation, test-collection evaluation, Cranfield paradigm]
page_type: strategy
template_version: "0.2"

layer: route
research_methods: [test-collection, task-study, ability-test, adversarial-testing]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [manning2008, voorhees2000, ratner2017]
---

# Comparison against reference data

> System output is compared with stored reference answers or labels, and agreement is computed.

## 1. What it is

### 1.1 Definition
A reference set says what the right output is for each input. The system is run on the inputs, and its outputs are scored against the reference, usually automatically.

### 1.2 Typical pairings
Test collections, benchmarks, labeled datasets, and automated test suites.
<!-- generated:pairings:start -->
- [Test collections and benchmarks](test-collection.md)
- [Task studies with people](task-study.md)
- [Ability tests](ability-test.md)
- [Adversarial testing and red teaming](adversarial-testing.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Cranfield-style test collections** in IR: documents, queries, and relevance judgments, reused to compare systems [manning2008].
- **Gold labels** in machine learning, made by careful human annotation.
- **Silver or synthetic labels**: references produced by models, heuristics, or weak supervision, cheaper but noisier [ratner2017].
- **Automated test suites** with expected outputs.

## 2. When to use it
Use it to compare many system versions cheaply and repeatably. It needs a reference that matches what users care about.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
The number is only as valid as the reference. Human references contain disagreement [voorhees2000] and gaps (unjudged items are usually counted as wrong). Synthetic references inherit the errors of the model that made them and may favour systems that resemble it.

### 3.2 Reliability
Stable once the reference is fixed, but small test sets give high variance, and results depend on the reference's coverage.

### 3.3 Bias and gaming
Systems overfit to a fixed benchmark. A reference made with the same tool or model as the system under test shares its blind spots.

## 4. Cost
High to build the reference (usually by [external judgment](external-judgment.md)), then near zero per re-run.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Accuracy](../metrics/accuracy.md)
- [Area Under the ROC Curve (ROC-AUC)](../metrics/roc-auc.md)
- [Attack Success Rate (ASR)](../metrics/attack-success-rate.md)
- [Decision Accuracy with AI Assistance](../metrics/decision-accuracy-with-ai.md)
- [Expected Calibration Error (ECE)](../metrics/expected-calibration-error.md)
- [F1 Score](../metrics/f1-score.md)
- [Factual Precision in Atomicity Score (FActScore)](../metrics/factscore.md)
- [Forward-Prediction Accuracy](../metrics/forward-prediction-accuracy.md)
- [Mean Reciprocal Rank (MRR)](../metrics/reciprocal-rank.md)
- [Normalized Discounted Cumulative Gain (nDCG)](../metrics/ndcg.md)
- [Over-reliance Rate](../metrics/over-reliance-rate.md)
- [pass@k](../metrics/pass-at-k.md)
- [pass^k](../metrics/pass-hat-k.md)
- [Precision (test collection)](../metrics/precision-test-collection.md)
- [Recall (test collection)](../metrics/recall-test-collection.md)
- [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](../metrics/rouge.md)
- [Task Success Rate (agent benchmark)](../metrics/task-success-rate-benchmark.md)
- [Task Success Rate (user on task)](../metrics/task-success-rate-user.md)
- [Tool Call Accuracy](../metrics/tool-call-accuracy.md)
- [Under-reliance Rate](../metrics/under-reliance-rate.md)
<!-- generated:metrics:end -->

## 6. Sources
- [manning2008]
- [voorhees2000]
- [ratner2017]

## Open questions and review notes
- Should synthetic and weak references be a separate route, given how differently they fail?
