---
id: groundedness
title: "Generation performance: groundedness"
aliases: [faithfulness to context, attribution]
page_type: construct
template_version: "0.1"
fields: [nlp, llm-evaluation]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [es2023, ragas2026]
---

# Generation performance: groundedness

> Whether generated content is supported by the sources the system was given.

## 1. Definition
In retrieval-augmented generation, an answer is grounded when its claims can be inferred from the retrieved context [es2023].

## 2. Boundaries
Differs from [factuality](factuality.md): it checks support by the given context, not truth. Differs from [retrieval relevance](relevance.md), which judges the context itself.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
RAGAS Faithfulness is the common metric; other tools use similar claim-by-claim checks [ragas2026].
<!-- generated:metrics:start -->
- [Answer Faithfulness](../metrics/answer-faithfulness.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: grounded answers let users check claims against sources.

## 6. How it is identified
RAG evaluation [es2023].

## 7. Sources
- [es2023]: RAGAS.
- [ragas2026]: metric documentation.

## Open questions and review notes
- None yet.
