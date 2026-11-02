---
id: classification-correctness
title: "Classification effectiveness: correctness"
aliases: [classification accuracy]
page_type: construct
template_version: "0.1"
fields: [machine-learning]

broader: [classification-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [manning2008]
---

# Classification effectiveness: correctness

> Whether a classifier assigns items to the right classes.

## 1. Definition
The agreement between the classes a system assigns and the true classes [manning2008].

## 2. Boundaries
It treats the reference labels as truth; if they are wrong, so is the measure.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Precision and recall per class, and their combinations, are the usual metrics.
<!-- generated:metrics:start -->
- [Accuracy](../metrics/accuracy.md)
- [Area Under the ROC Curve (ROC-AUC)](../metrics/roc-auc.md)
- [F1 Score](../metrics/f1-score.md)
- [Precision (benchmark)](../metrics/precision-benchmark.md)
- [Recall (benchmark)](../metrics/recall-benchmark.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical.

## 6. How it is identified
Machine learning practice.

## 7. Sources
- [manning2008]

## Open questions and review notes
- None yet.
