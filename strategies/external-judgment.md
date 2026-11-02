---
id: external-judgment
title: "External judgment: annotators, experts, model judges, simulated users"
aliases: [human assessment, LLM-as-a-judge, proxy user]
page_type: strategy
template_version: "0.2"

layer: route
research_methods: [test-collection, expert-inspection, simulation, logs-telemetry, adversarial-testing]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [voorhees2000, nielsen1993, zheng2023, li2024, cohen1960, fleiss1971, krippendorff2004, shrout1979]
---

# External judgment: annotators, experts, model judges, simulated users

> Someone or something other than the user judges the system's outputs or behaviour, and the judgments are counted or averaged.

## 1. What it is

### 1.1 Definition
A judge looks at an output or an interaction and assigns a label or score: relevant or not, correct or not, a quality rating. The judge can be a trained annotator, a domain expert, an LLM, or a simulated user.

### 1.2 Typical pairings
Building test collections, expert inspection, simulation, and judging samples of logged outputs.
<!-- generated:pairings:start -->
- [Test collections and benchmarks](test-collection.md)
- `expert-inspection` (no method page yet)
- `simulation` (no method page yet)
- [Interaction logs and telemetry](logs-telemetry.md)
- [Adversarial testing and red teaming](adversarial-testing.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Human relevance assessment** for test collections; assessors disagree, but system rankings are fairly stable across assessors [voorhees2000].
- **Expert inspection**, such as heuristic evaluation, where experts judge an interface against principles [nielsen1993].
- **LLM-as-a-judge**, where a language model scores or compares outputs; agreement with human preferences can be high, with known biases [zheng2023; li2024].
- **Simulated or proxy users** that act on the system so their behaviour can be measured.
- **Human corrections as judgments**: when a person edits a model's output, each edit is a judgment that the output was wrong.

## 2. When to use it
Use it when the construct is a quality of outputs that needs judgment and no reusable reference exists yet. Once judgments are stored and reused, the route becomes [comparison against reference data](reference-comparison.md).

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
Judges may not share the user's view of what matters. LLM judges show position bias, a preference for longer answers, and a preference for outputs like their own [zheng2023]. Simulated users are only as valid as their model of real behaviour.

### 3.2 Reliability
Measure agreement between judges, and between model judges and humans on a sample, before trusting differences. These statistics describe the judges, not the system, so they are reported alongside the metric rather than as metrics of their own:
- **Two judges, categories:** Cohen's kappa, which corrects raw agreement for agreement expected by chance [cohen1960].
- **Many judges, categories:** Fleiss' kappa [fleiss1971], or Krippendorff's alpha, which also handles missing judgments and ordinal or interval scales [krippendorff2004].
- **Numeric ratings:** the intraclass correlation, in the form that matches how judges were assigned [shrout1979].
- **Model judge vs humans:** Pearson correlation for scores, Spearman or Kendall correlation for rankings, and position consistency for pairwise judges (whether the verdict survives swapping the order of the two answers) [li2024].

### 3.3 Bias and gaming
Systems can be tuned to please the judge rather than the user. Judge prompts and guidelines drift over time.

## 4. Cost
Human judges: medium to high per item. LLM judges and simulators: low per item, but each needs validation against human judgments for the task.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Answer Faithfulness](../metrics/answer-faithfulness.md)
- [Attack Success Rate (ASR)](../metrics/attack-success-rate.md)
- [Factual Precision in Atomicity Score (FActScore)](../metrics/factscore.md)
- [Normalized Discounted Cumulative Gain (nDCG)](../metrics/ndcg.md)
- [Precision (test collection)](../metrics/precision-test-collection.md)
- [Recall (test collection)](../metrics/recall-test-collection.md)
- [Task Success Rate (user on task)](../metrics/task-success-rate-user.md)
- [Toxicity Rate](../metrics/toxicity-rate.md)
<!-- generated:metrics:end -->

## 6. Sources
- [voorhees2000]
- [nielsen1993]
- [zheng2023]
- [li2024]
- [cohen1960]
- [fleiss1971]
- [krippendorff2004]
- [shrout1979]

## Open questions and review notes
- Should LLM-as-a-judge and simulated users get their own pages, given how fast that practice is changing?
