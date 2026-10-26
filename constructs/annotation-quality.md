---
id: annotation-quality
title: Annotation quality
aliases: [label quality, ground-truth quality]
page_type: construct
template_version: "0.1"
fields: [data-annotation]

broader: [output-quality]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Annotation quality

> How good the labels produced by people, models, or both are as ground truth.

## 1. Definition
The fitness of annotations (labels, boxes, tracks) to serve as ground truth, usually for training or evaluating models.

## 2. Boundaries
It is about the labels, whoever produced them. The labeler's effort belongs under [efficiency](efficiency.md).

## 3. Narrower constructs
Completeness, correctness of pre-annotations, and correct placement in time are separate parts.
<!-- generated:narrower:start -->
- [Annotation quality: completeness](label-completeness.md)
- [Annotation quality: pre-annotation quality](pre-annotation-quality.md)
- [Annotation tool: temporal alignment](temporal-alignment.md)
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
