---
id: annotation-quality
title: Annotation quality
aliases: [label quality, ground-truth quality]
page_type: construct
template_version: "0.1"
fields: [data-annotation]

broader: [task-effectiveness]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Annotation quality

> How good the labels produced in an annotation task are as ground truth.

## 1. Definition
The fitness of annotations (labels, boxes, tracks) to serve as ground truth, usually for training or evaluating models.

## 2. Boundaries
It is the outcome of an annotation task: people working with a system (its interface, interaction design, and any machine pre-annotation), so it sits under [task effectiveness](task-effectiveness.md). The quality of the machine's proposals alone is a component characteristic, [machine pre-annotation quality](machine-pre-annotation-quality.md). The labeler's effort belongs under [task efficiency](task-efficiency.md).

## 3. Narrower constructs
Completeness is the first part with a page. Machine pre-annotation quality (a component characteristic) and system reliability feed it, linked by evidence rather than by the DAG.
<!-- generated:narrower:start -->
- [Annotation quality: completeness](label-completeness.md)
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: teams keep using tools whose labels they trust.

## 6. How it is identified
Added from the InfinityPool metric-chat interview (2026-10-19).

## 7. Sources
- None yet.

## Open questions and review notes
- Add box accuracy (localization) and identity consistency as narrower constructs?
