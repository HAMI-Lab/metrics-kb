---
id: generation-performance
title: Generation performance
aliases: [text generation quality, generation quality]
page_type: construct
template_version: "0.1"
fields: [nlp, llm-evaluation]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [liang2022, chang2024]
---

# Generation performance

> How good the content a generative component produces is, judged on its own.

## 1. Definition
Properties of text (or other content) produced by a generative component, such as a language model, judged without a user doing a task with it [liang2022; chang2024]. Generation is a component because it can come from a backend without fixing how the interface renders it (D15).

## 2. Boundaries
It judges the component's output. The end-to-end quality of what the whole system delivers is [output quality](output-quality.md); what users achieve with it is [task effectiveness](task-effectiveness.md).

## 3. Narrower constructs
The narrower constructs cover different questions about the same output: does it match a reference, is it true, and is it supported by the given sources.
<!-- generated:narrower:start -->
- [Generation performance: factuality](factuality.md)
- [Generation performance: groundedness](groundedness.md)
- [Generation performance: similarity to reference](reference-similarity.md)
- [Generation performance: verifiable correctness](verifiable-correctness.md)
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical, through output quality and task effectiveness.

## 6. How it is identified
LLM evaluation frameworks and surveys [liang2022; chang2024].

## 7. Sources
- [liang2022], [chang2024]: dimensions of LLM evaluation.

## Open questions and review notes
- Fluency and coherence are candidates for further narrower constructs.
