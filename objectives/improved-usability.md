---
id: improved-usability
title: "Objective 2: Improved Usability"
page_type: objective
template_version: "0.1"
status: ai-draft
sources: [iso9241-11, hornbaek2007, sauro2009, kim2024, rong2022]
---

# Objective 2: Improved Usability

> The system lets its intended users reach their goals more effectively, more efficiently, and with more satisfaction.

## What it means
ISO 9241-11 defines usability as the extent to which specified users can use a system to achieve specified goals with effectiveness, efficiency, and satisfaction in a specified context of use [iso9241-11]. "Improved" means these move in the right direction between versions, without trading one away for another.

## How it can be observed
No single measure captures it. The usual practice is to measure all three parts:
- Effectiveness: task success, error rate, output quality ([Precision (test collection)](../metrics/precision-test-collection.md) for the system side).
- Efficiency: [Task Completion Time](../metrics/task-completion-time.md), effort ([NASA-TLX](../metrics/nasa-tlx.md)), waiting time ([Response Latency](../metrics/response-latency.md)).
- Satisfaction: [SUS](../metrics/system-usability-scale.md) and similar questionnaires.

These parts correlate only modestly with one another [hornbaek2007; sauro2009], so improving one does not guarantee improvement in the others.

## Metrics linked to this objective

| Metric | Direction | Evidence | Note |
|---|---|---|---|
| [Response Latency](../metrics/response-latency.md) | negative | causal (visual analytics) | |
| [SUS](../metrics/system-usability-scale.md) | positive | correlational | Measures perceived usability |
| [Task Completion Time](../metrics/task-completion-time.md) | negative | correlational | For the same outcome |
| [NASA-TLX](../metrics/nasa-tlx.md) | negative | correlational | Not at very low workload |
| [Precision (test collection)](../metrics/precision-test-collection.md) | positive | correlational | Weaker than assumed |
| [Recall (test collection)](../metrics/recall-test-collection.md) | positive | correlational | Batch gains do not always translate to users |
| [Precision (user on task)](../metrics/precision-user-task.md) | positive | theoretical | Part of effectiveness for the user's own task |
| [Accuracy](../metrics/accuracy.md) | positive | theoretical | Correct components are a precondition for effective tasks; the link to user outcomes is not measured. |
| [F1 Score](../metrics/f1-score.md) | positive | theoretical | Through output quality; not measured. |
| [Area Under the ROC Curve (ROC-AUC)](../metrics/roc-auc.md) | positive | theoretical | Through output quality; not measured. |
| [Expected Calibration Error (ECE)](../metrics/expected-calibration-error.md) | positive | theoretical | Calibrated confidence lets users decide when to rely on outputs. |
| [Normalized Discounted Cumulative Gain (nDCG)](../metrics/ndcg.md) | positive | theoretical | Better rankings are assumed to help users; offline-online links are weak. |
| [Mean Reciprocal Rank (MRR)](../metrics/reciprocal-rank.md) | positive | theoretical | When one answer suffices, finding it sooner saves effort. |
| [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](../metrics/rouge.md) | unknown | none | Too far from what users experience to say. |
| [Factual Precision in Atomicity Score (FActScore)](../metrics/factscore.md) | positive | theoretical | False content harms users' tasks. |
| [Answer Faithfulness](../metrics/answer-faithfulness.md) | positive | theoretical | Answers users can trace to sources support checking. |
| [Tool Call Accuracy](../metrics/tool-call-accuracy.md) | positive | theoretical | Through autonomous task completion; not measured. |
| [Area Over the Perturbation Curve (AOPC)](../metrics/aopc.md) | positive | theoretical | Faithful explanations are a precondition for users to understand the model. |

## Open questions
- For AI systems, should trust and appropriate reliance count as part of usability, or be treated as a third objective? Several spreadsheet sources treat them as central [kim2024; rong2022].
