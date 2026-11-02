---
id: grounding-correctness
title: "Grounding performance: localization correctness"
aliases: [click accuracy, localization accuracy]
page_type: construct
template_version: "0.1"
fields: [agents, human-ai-interaction]

broader: [grounding-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [cheng2024]
---

# Grounding performance: localization correctness

> Whether the predicted location falls on the right target.

## 1. Definition
The share of instructions for which the predicted point or box falls on the target element or region [cheng2024].

## 2. Boundaries
A hit on the right element does not mean the action was right in context.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Grounding accuracy is the share of hits.
<!-- generated:metrics:start -->
- [Grounding Accuracy](../metrics/grounding-accuracy.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical.

## 6. How it is identified
GUI agent benchmarks [cheng2024].

## 7. Sources
- [cheng2024]: ScreenSpot.

## Open questions and review notes
- None yet.
