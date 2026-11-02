---
id: tool-call-correctness
title: "Tool-use performance: call correctness"
aliases: [tool selection accuracy, argument accuracy]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, agents]

broader: [tool-use-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [mohammadi2025, ragas2026]
---

# Tool-use performance: call correctness

> Whether an agent called the right tools with the right arguments.

## 1. Definition
The match between the tool calls an agent made and the calls a reference says it should have made: tool names, arguments and, where it matters, order [ragas2026; mohammadi2025].

## 2. Boundaries
Correct calls can still fail to reach the goal (the plan was wrong), and wrong calls can sometimes reach it by another route.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical.

## 6. How it is identified
Agent benchmarks and tool documentation.

## 7. Sources
- [mohammadi2025]: tool-use evaluation.
- [ragas2026]: Tool Call Accuracy and F1.

## Open questions and review notes
- None yet.
