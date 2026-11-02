---
id: classification-performance
title: Classification performance
aliases: [classifier performance]
page_type: construct
template_version: "0.1"
fields: [machine-learning]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [manning2008]
---

# Classification performance

> How well a classification component or functionality assigns items to classes, and at what cost.

## 1. Definition
The performance of a classifier as a component: how correctly it assigns classes [manning2008] and, in future pages, how efficiently.

## 2. Boundaries
A component or system functionality, judged on reference labels; whether users act better on its outputs is a task characteristic.

## 3. Narrower constructs
Correctness so far; efficiency (latency, cost per item) and calibration of its confidence scores are candidates.
<!-- generated:narrower:start -->
- [Classification effectiveness: correctness](classification-correctness.md)
- [Classification performance: calibration](calibration.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect.

## 6. How it is identified
Added on 2026-10-26: classification is a component or system functionality, like retrieval.

## 7. Sources
- [manning2008]

## Open questions and review notes
- Add classification efficiency and calibration as narrower constructs?
