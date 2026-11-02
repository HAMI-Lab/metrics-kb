---
id: factuality
title: "Generation performance: factuality"
aliases: [factual accuracy, truthfulness]
page_type: construct
template_version: "0.1"
fields: [nlp, llm-evaluation]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [min2023, chang2024]
---

# Generation performance: factuality

> Whether the claims in generated content are true.

## 1. Definition
The share of claims in generated content that are supported by trusted knowledge, regardless of what sources the system was given [min2023; chang2024].

## 2. Boundaries
Differs from [groundedness](groundedness.md), which asks whether claims are supported by the sources given to the model, true or not. A grounded answer can repeat a false source; a factual answer can go beyond its sources.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
FActScore splits text into atomic claims and checks each against a knowledge source.
<!-- generated:metrics:start -->
- [FActScore](../metrics/factscore.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: false content erodes trust and can harm users.

## 6. How it is identified
LLM hallucination research [chang2024; min2023].

## 7. Sources
- [min2023]: FActScore.
- [chang2024]: factuality in LLM evaluation.

## Open questions and review notes
- None yet.
