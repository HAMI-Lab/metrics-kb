---
id: map-prediction-performance
title: Map prediction performance
aliases: [dense prediction performance]
page_type: construct
template_version: "0.1"
fields: [visualization, computer-vision]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [bylinskii2019]
---

# Map prediction performance

> How well a component predicts a map over an image, such as where people will look.

## 1. Definition
Output type (D23): the output is a value for every location of an image or display, such as a probability that people look there [bylinskii2019].

## 2. Boundaries
Not [grounding](grounding-performance.md), which outputs one location for one instruction.

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Map prediction performance: saliency prediction accuracy](saliency-prediction-accuracy.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect.

## 6. How it is identified
Saliency modelling [bylinskii2019].

## 7. Sources
- [bylinskii2019]: saliency metrics.

## Open questions and review notes
- None yet.
