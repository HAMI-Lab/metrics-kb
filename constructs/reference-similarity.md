---
id: reference-similarity
title: "Generation performance: similarity to reference"
aliases: [overlap with reference]
page_type: construct
template_version: "0.1"
fields: [nlp]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [lin2004, papineni2002, chang2024]
---

# Generation performance: similarity to reference

> How closely generated text matches one or more reference texts.

## 1. Definition
The overlap between generated text and human-written references, in words, n-grams or meaning [lin2004; papineni2002].

## 2. Boundaries
Similarity to a reference is not correctness: a correct answer worded differently scores low, and a fluent wrong one can score high [chang2024]. It is a stand-in for quality when references exist.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
ROUGE and BLEU count n-gram overlap; embedding-based scores such as BERTScore compare meaning.
<!-- generated:metrics:start -->
- [F1 Score](../metrics/f1-score.md)
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
- None yet.
