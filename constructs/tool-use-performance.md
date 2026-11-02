---
id: tool-use-performance
title: Tool-use performance
aliases: [tool calling]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, agents]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [mohammadi2025]
---

# Tool-use performance

> How well an agent component chooses and calls tools.

## 1. Definition
Properties of the tool calls an agent makes: which tools it picks, with what arguments, in what order [mohammadi2025].

## 2. Boundaries
It judges the calls, not whether the overall goal was met; that is [autonomous task completion](autonomous-task-completion.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Tool-use performance: call correctness](tool-call-correctness.md)
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical, through autonomous task completion.

## 6. How it is identified
Agent evaluation surveys [mohammadi2025].

## 7. Sources
- [mohammadi2025]: agent evaluation and benchmarking.

## Open questions and review notes
- Planning quality (the sequence of steps) is a candidate sibling construct.
