---
id: visual-attention-prediction-performance
title: Visual attention prediction performance
aliases: [saliency prediction performance, attention map prediction performance, map prediction performance]
page_type: construct
template_version: "0.1"
fields: [visualization, computer-vision]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [bylinskii2019]
---

# Visual attention prediction performance

> How well a component predicts where people will look in an image or display.

## 1. Definition
Output type (D23): the output is an attention (saliency) map, a value for every location of an image or display giving how likely people are to look there [bylinskii2019]. Named for what is predicted, since "map" alone could be read as a geographic map.

## 2. Boundaries
Not [grounding](grounding-performance.md), which outputs one location for one instruction. Not about geographic maps.

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Visual attention prediction performance: accuracy](attention-prediction-accuracy.md)
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
