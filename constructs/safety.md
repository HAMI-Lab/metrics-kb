---
id: safety
title: "Output quality: safety"
aliases: [harmlessness]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, ai-safety]

broader: [output-quality]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [liu2025, wang2023, huang2024b]
---

# Output quality: safety

> Whether the system avoids producing harmful outputs, including under attack.

## 1. Definition
The extent to which a system's outputs avoid harm: toxic or hateful content, dangerous instructions, and unsafe behaviour when users try to elicit it [liu2025; wang2023].

## 2. Boundaries
Part of [output quality](output-quality.md) at the system level, because safety measures usually cover the whole system, including filters. Over-refusal (refusing benign requests) is the opposite failure and also belongs here.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Attack success rate measures resistance to adversarial prompts; toxicity rate measures harmful content in ordinary use.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: unsafe outputs harm users and trust.

## 6. How it is identified
Safety evaluation surveys and trustworthiness benchmarks [liu2025; wang2023; huang2024b].

## 7. Sources
- [liu2025]: safety evaluation of LLMs.
- [wang2023], [huang2024b]: trustworthiness benchmarks.

## Open questions and review notes
- None yet.
