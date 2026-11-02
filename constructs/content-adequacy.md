---
id: content-adequacy
title: "Generation performance: content adequacy"
aliases: [adequacy, content coverage, similarity to reference, overlap with reference]
page_type: construct
template_version: "0.1"
fields: [nlp]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [lin2004, papineni2002, chang2024]
---

# Generation performance: content adequacy

> Whether generated text conveys the content it should, such as the meaning of the source in a translation or the key points in a summary.

## 1. Definition
The extent to which generated text carries the content that a good output for this input would carry. Human-written references are one way to pin that content down. Overlap with references, in words, n-grams or meaning, is the usual automatic way to estimate it [lin2004; papineni2002].

## 2. Boundaries
- This construct used to be called "similarity to reference" (id `reference-similarity`). That named how it is scored, not what is measured, so it was renamed (D23). Similarity to a reference is now treated as a proxy for adequacy.
- Adequacy is not [factuality](factuality.md): a summary can cover the right points and still state something false. A correct output worded differently from the reference also scores low on overlap [chang2024].
- When there is one checkable answer, use [answer correctness](answer-correctness.md) instead.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
ROUGE and BLEU count n-gram overlap; embedding-based scores such as BERTScore compare meaning. All estimate adequacy through references.
<!-- generated:metrics:start -->
- [Learned Reference-Based Score](../metrics/learned-reference-score.md)
- [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](../metrics/rouge.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical and weak: it is far from what users care about.

## 6. How it is identified
Machine translation and summarization evaluation [papineni2002; lin2004].

## 7. Sources
- [lin2004]: ROUGE.
- [papineni2002]: BLEU.
- [chang2024]: limits for open-ended generation.

## Open questions and review notes
- Fluency, the usual partner of adequacy in translation evaluation, has no construct yet.
