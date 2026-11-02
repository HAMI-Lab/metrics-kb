---
id: closed-answer-performance
title: Closed-answer performance
aliases: [question answering performance, short-answer performance]
page_type: construct
template_version: "0.1"
fields: [nlp, llm-evaluation]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [rajpurkar2016, liang2022]
---

# Closed-answer performance

> How well a component answers questions that each have one correct answer.

## 1. Definition
The performance of a component that takes a question and returns one answer that can be checked against a key: an option picked from those given with the question, a number, or a short span of text [rajpurkar2016; liang2022]. The output is short and constrained, but the set of possible answers changes from item to item.

## 2. Boundaries
- Not [classification](classification-performance.md). A classifier chooses from one fixed set of labels shared by every item. Here each question brings its own possible answers. A multiple-choice test belongs here, even though each item is a choice among options. Question answering and classification have long been treated as different tasks in NLP.
- Not [open-ended generation](generation-performance.md). There, many different outputs can be good, and judging them needs a reference, a judge or a check that runs.
- What a question set probes (knowledge, reasoning, math) is not a narrower construct. It depends on which questions are asked, so it belongs to the test data, which is named in prose (D19, D23).

## 3. Narrower constructs
Correctness so far. Calibration of the stated confidence is a candidate, sharing a parent with [classification calibration](calibration.md).
<!-- generated:narrower:start -->
- [Closed-answer performance: answer correctness](answer-correctness.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect, through output quality and task effectiveness.

## 6. How it is identified
Reading-comprehension and question-answering benchmarks [rajpurkar2016], and LLM benchmark suites that mix many question sets [liang2022].

## 7. Sources
- [rajpurkar2016]: extractive question answering with exact match and token-overlap F1.
- [liang2022]: question answering in LLM benchmark suites.

## Open questions and review notes
- Language models can answer the same question in free text. When the answer is extracted from free text before checking, extraction errors count against the component. Should extraction get its own note on the accuracy page?
