---
id: robustness
title: System robustness
aliases: [stability under perturbation]
page_type: construct
template_version: "0.1"
fields: [machine-learning, llm-evaluation]

broader: [system-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [liang2022, chang2024, ribeiro2020]
---

# System robustness

> Whether the system keeps performing when its inputs are changed in ways that should not matter.

## 1. Definition
The extent to which performance holds up under input changes such as typos, paraphrases, formatting changes or adversarial edits [liang2022; ribeiro2020].

## 2. Boundaries
Robustness is defined relative to a set of changes; a system robust to typos may not be robust to paraphrases. It differs from [consistency across runs](run-consistency.md), where the input is the same.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Performance drop rate compares scores on original and changed inputs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: real users rarely type the way benchmarks do.

## 6. How it is identified
LLM evaluation frameworks [liang2022; chang2024] and behavioral testing [ribeiro2020].

## 7. Sources
- [liang2022], [chang2024]: robustness evaluation.
- [ribeiro2020]: invariance tests.

## Open questions and review notes
- Generalization to new domains (out-of-distribution performance) is a related construct; add as a sibling?
