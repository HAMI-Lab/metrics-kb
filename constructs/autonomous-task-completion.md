---
id: autonomous-task-completion
title: Autonomous task completion
aliases: [agent task success]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, agents]

broader: [system-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [mohammadi2025, jimenez2023, mialon2023]
---

# Autonomous task completion

> Whether the system, acting alone, reaches the goal of a task.

## 1. Definition
The extent to which an autonomous system, such as an agent, completes multi-step tasks without a user taking part [mohammadi2025].

## 2. Boundaries
Here no user pursues the goal, so this is a system characteristic. When a person uses the system to reach their own goal, the outcome is [task effectiveness](task-effectiveness.md), measured on a separate page (D20).

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
- [Task Success Rate (agent benchmark)](../metrics/task-success-rate-benchmark.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: agents that complete tasks are expected to save users work, but this needs checking with users.

## 6. How it is identified
Agent benchmarks such as SWE-bench and GAIA [jimenez2023; mialon2023].

## 7. Sources
- [mohammadi2025]: agent evaluation.
- [jimenez2023]: SWE-bench.
- [mialon2023]: GAIA.

## Open questions and review notes
- None yet.
