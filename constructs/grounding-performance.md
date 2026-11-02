---
id: grounding-performance
title: Grounding performance
aliases: [visual grounding performance, GUI grounding performance]
page_type: construct
template_version: "0.1"
fields: [agents, human-ai-interaction]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [cheng2024]
---

# Grounding performance

> How well a component finds the place in an image or interface that an instruction refers to.

## 1. Definition
Output type (D23): the input is an image or screen plus an instruction, and the output is a location, such as a point or a box [cheng2024].

## 2. Boundaries
Not [visual attention prediction](visual-attention-prediction-performance.md), which outputs a value for every location. Whether an agent then completes the task is [autonomous task completion](autonomous-task-completion.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Grounding performance: localization correctness](grounding-correctness.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect, through agents that act on interfaces.

## 6. How it is identified
GUI agents [cheng2024].

## 7. Sources
- [cheng2024]: GUI grounding.

## Open questions and review notes
- None yet.
