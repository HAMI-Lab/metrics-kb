---
id: autonomous-task-efficiency
title: Autonomous task efficiency
aliases: [agent efficiency, action efficiency]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, agents]

broader: [system-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [arcprize2026]
---

# Autonomous task efficiency

> How few resources, such as actions, steps or time, an autonomous system needs to complete a task.

## 1. Definition
The resources an autonomous system, such as an agent, spends to complete a task without a user: actions, steps, tool calls or time. Often expressed relative to a baseline, such as people doing the same task [arcprize2026].

## 2. Boundaries
Not [autonomous task completion](autonomous-task-completion.md), which asks whether the task gets done. Not [resource cost](resource-cost.md), which counts money or compute. The task-level counterpart, a person's efficiency with the system, is [task efficiency](task-efficiency.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Metrics compare the system's actions or time with a baseline.
<!-- generated:metrics:start -->
- [Action Efficiency Relative to Humans](../metrics/action-efficiency-vs-humans.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: efficient agents finish sooner and cost less.

## 6. How it is identified
Agent benchmarks that score efficiency against people [arcprize2026].

## 7. Sources
- [arcprize2026]: ARC-AGI-3 and action efficiency.

## Open questions and review notes
- None yet.
