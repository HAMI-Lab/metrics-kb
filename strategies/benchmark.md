---
id: benchmark
title: Benchmarks
aliases: [test collection, test set, labeled dataset, annotated dataset, gold-standard dataset, ground-truth data, evaluation dataset, test suite, offline evaluation, batch evaluation]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [manning2008, voorhees2000, hersh2000, turpin2006, zheng2023]
---

# Benchmarks

> A fixed set of inputs, often with reference outputs, is built once and reused to run systems against, with no user present.

## 1. What it is

### 1.1 Definition
A benchmark is a fixed set of inputs, such as queries, documents, prompts or test cases, often stored with the right outputs. Each system is run on the same inputs, and its outputs are recorded. No user takes part in the run. Because the inputs stay fixed, results can be compared across systems and over time.

Fields use different names for the same concept, and the wiki treats them as one method: **test collection** in information retrieval, **benchmark** in machine learning and LLM evaluation, **labeled** or **annotated dataset**, **gold standard** or **ground truth** when the emphasis is on the reference outputs, **test set** for the held-out part of a dataset, and **test suite** in software engineering. The wiki uses "benchmark" as the canonical name (D26). Each named benchmark, such as TREC or HumanEval, is an instrument (D25).

### 1.2 Typical pairings
Most often scored by comparison against the stored reference. When outputs are judged after the run, the route is external judgment. Pass rates and run times of test suites are read directly.
<!-- generated:pairings:start -->
- [Comparison against reference data](reference-comparison.md)
- [Direct reading: timing and counting](direct-reading.md)
- [External judgment: annotators, experts, model judges, simulated users](external-judgment.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Cranfield-style collections** in information retrieval (IR): documents, queries and relevance judgments, reused to compare systems. In large collections such as TREC, judges assess only a *pool*, the top results returned by the participating systems [manning2008].
- **Held-out test splits** in machine learning: labeled examples kept apart from training data.
- **Automated test suites** with expected outputs, for software components.
- **LLM benchmarks** whose outputs are scored by a model judge instead of a stored answer [zheng2023].

## 2. When to use it
Use it for component and system constructs, when many system versions must be compared cheaply and repeatably. It does not reach task constructs on its own: gains measured on a collection do not always appear when people use the system [hersh2000; turpin2006]. Pair it with a task study or logs when the claim is about users.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
The data shows what the system outputs for the chosen inputs, not how people would use those outputs. The inputs are chosen by the collection's builders and may not resemble real use. A collection freezes a moment: content and user needs move on, but the collection does not.

### 3.2 Reliability
Small input sets give high variance, and results can depend on which inputs happened to be chosen. Report the spread across inputs, not just the mean. Judges disagree about references, although system rankings can be more stable than individual judgments [voorhees2000] (check against the paper).

### 3.3 Bias and gaming
Reuse invites overfitting: a test set used for many rounds of tuning stops being a test. Test items can leak into training data, especially for models trained on web-scale text. With pooling, judges assess only the items the original systems returned [manning2008], and items no one judged usually count as not relevant. Hypothesis: this penalizes a new system that finds relevant items outside the original pool. Why it could be true: those items were never judged, so they count as misses for the new system although they would count as hits if judged (further reference needed).

## 4. Cost
High to build: inputs, references, licensing and documentation. Once built, a re-run costs little, which is why collections are shared and reused across many studies.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Accuracy](../metrics/accuracy.md)
- [Action Efficiency Relative to Humans](../metrics/action-efficiency-vs-humans.md)
- [Answer Faithfulness](../metrics/answer-faithfulness.md)
- [Area Over the Perturbation Curve (AOPC)](../metrics/aopc.md)
- [Area Under the ROC Curve (ROC-AUC)](../metrics/roc-auc.md)
- [CLIPScore](../metrics/clipscore.md)
- [Cost per Task](../metrics/cost-per-task.md)
- [Demographic Parity Difference (DPD)](../metrics/demographic-parity-difference.md)
- [Expected Calibration Error (ECE)](../metrics/expected-calibration-error.md)
- [F1 Score](../metrics/f1-score.md)
- [Factual Precision in Atomicity Score (FActScore)](../metrics/factscore.md)
- [Grounding Accuracy](../metrics/grounding-accuracy.md)
- [Instruction-Following Accuracy](../metrics/instruction-following-accuracy.md)
- [Judge Rating (model judge)](../metrics/judge-rating.md)
- [Learned Reference-Based Score](../metrics/learned-reference-score.md)
- [Mean Average Precision (MAP)](../metrics/mean-average-precision.md)
- [Mean Reciprocal Rank (MRR)](../metrics/reciprocal-rank.md)
- [Normalized Discounted Cumulative Gain (nDCG)](../metrics/ndcg.md)
- [pass@k](../metrics/pass-at-k.md)
- [pass^k](../metrics/pass-hat-k.md)
- [Performance Drop Rate (PDR)](../metrics/performance-drop-rate.md)
- [Precision (benchmark)](../metrics/precision-benchmark.md)
- [Recall (benchmark)](../metrics/recall-benchmark.md)
- [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](../metrics/rouge.md)
- [Root Mean Squared Error (RMSE)](../metrics/root-mean-squared-error.md)
- [Saliency Map Similarity (SIM)](../metrics/saliency-map-similarity.md)
- [Task Success Rate (agent benchmark)](../metrics/task-success-rate-benchmark.md)
- [Tool Call Accuracy](../metrics/tool-call-accuracy.md)
- [Toxicity Rate](../metrics/toxicity-rate.md)
- [Win Rate (pairwise comparison)](../metrics/win-rate.md)
- [Word Error Rate (WER)](../metrics/word-error-rate.md)
<!-- generated:metrics:end -->

## 6. Sources
- [manning2008]: test collections and pooling in IR evaluation.
- [voorhees2000]: judge disagreement and its effect on system comparisons.
- [hersh2000], [turpin2006]: batch gains vs gains with users.
- [zheng2023]: LLM-as-a-judge on benchmarks.

## Open questions and review notes
- Should contamination of test items into training data get a citation and its own subsection as LLM evaluation grows?
