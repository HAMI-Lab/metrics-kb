---
id: run-consistency
title: Consistency across runs
aliases: [reliability across trials, repeatability]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, agents]

broader: [system-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [yao2024, mohammadi2025]
---

# Consistency across runs

> Whether the system gives the same quality of result when the same task is run again.

## 1. Definition
Non-deterministic systems such as language-model agents can succeed on one run and fail on the next with the same input. Consistency is the extent to which success repeats [yao2024].

## 2. Boundaries
Differs from [robustness](robustness.md), where inputs change. Differs from average performance: two systems with the same mean success can differ greatly in consistency.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: users who cannot predict whether a run will work stop relying on it.

## 6. How it is identified
Agent benchmarks [yao2024; mohammadi2025].

## 7. Sources
- [yao2024]: pass^k.
- [mohammadi2025]: reliability in agent evaluation.

## Open questions and review notes
- None yet.
