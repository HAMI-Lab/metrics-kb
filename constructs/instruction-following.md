---
id: instruction-following
title: "Generation performance: instruction following"
aliases: [instruction adherence, constraint following]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [zhou2023]
---

# Generation performance: instruction following

> Whether generated output does what the input instructed, such as respecting a format, a length or a required keyword.

## 1. Definition
The extent to which a generated output meets the instructions stated in its input. Instructions can be checkable by a program ("answer in under 100 words", "use JSON", "mention X twice") or need judgment ("be formal", "focus on the risks") [zhou2023].

## 2. Boundaries
Not [answer correctness](answer-correctness.md): an output can follow every instruction and still be wrong, or be right while ignoring the format asked for. Not [content adequacy](content-adequacy.md), which asks whether the right content is there. It applies to any output type; it sits under generation for now, and other parents can be added when a metric needs them (D23, D28).

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Checkable instructions are scored automatically; instructions that need judgment need a human or model judge.
<!-- generated:metrics:start -->
- [Instruction-Following Accuracy](../metrics/instruction-following-accuracy.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: outputs that follow instructions need less rework from users.

## 6. How it is identified
LLM evaluation, where following user instructions is a core expected behaviour [zhou2023].

## 7. Sources
- [zhou2023]: IFEval and verifiable instructions.

## Open questions and review notes
- Instructions that need judgment have no metric page yet; IFEval covers only checkable ones.
