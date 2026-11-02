---
id: answer-correctness
title: "Closed-answer performance: answer correctness"
aliases: [exact-match correctness, answer accuracy]
page_type: construct
template_version: "0.1"
fields: [nlp, llm-evaluation]

broader: [closed-answer-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [rajpurkar2016, liang2022]
---

# Closed-answer performance: answer correctness

> Whether the component's answer matches the correct answer.

## 1. Definition
An answer is correct when it equals the key after the stated normalization, such as lower-casing or removing punctuation, or, with partial credit, by how much it overlaps the key [rajpurkar2016; liang2022].

## 2. Boundaries
- It differs from [classification correctness](classification-correctness.md) in the output space: per-item answers, not one shared label set.
- It differs from [functional correctness](functional-correctness.md), where the output is a program and running it decides correctness.
- A correct answer phrased differently from the key can be scored wrong. That is a weakness of the check, not of the construct.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Accuracy (exact match) gives no partial credit. Token-overlap F1 gives partial credit for answers that share words with the key. pass@k counts a problem as solved if any of k sampled answers is right.
<!-- generated:metrics:start -->
- [Accuracy](../metrics/accuracy.md)
- [F1 Score](../metrics/f1-score.md)
- [pass@k](../metrics/pass-at-k.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: correct answers save users work, if users can tell which answers are correct.

## 6. How it is identified
Question-answering benchmarks [rajpurkar2016] and LLM benchmark suites [liang2022].

## 7. Sources
- [rajpurkar2016]: exact match and token-overlap F1.
- [liang2022]: exact match and quasi-exact match in LLM benchmarks.

## Open questions and review notes
- None yet.
