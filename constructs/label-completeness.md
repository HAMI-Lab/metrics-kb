---
id: label-completeness
title: "Annotation quality: completeness"
aliases: [coverage]
page_type: construct
template_version: "0.1"
fields: [data-annotation, computer-vision]

broader: [annotation-quality]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Annotation quality: completeness

> Whether every object of interest is labeled, wherever it appears.

## 1. Definition
The share of things that should be labeled that actually are.

## 2. Boundaries
It is a property of the labels produced in the annotation task, so it inherits task effectiveness through [annotation quality](annotation-quality.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Needs a gold reference to know what was missed.
<!-- generated:metrics:start -->
- [Object-Track Completeness](../metrics/object-track-completeness.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical.

## 6. How it is identified
The InfinityPool team's stated success criterion: "all objects should be tracked" (interview, 2026-10-19).

## 7. Sources
- None yet.

## Open questions and review notes
- None yet.
