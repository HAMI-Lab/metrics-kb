---
id: verifiable-correctness
title: "Generation performance: verifiable correctness"
aliases: [functional correctness, execution correctness]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, software-engineering]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [chen2021, kulal2019, yue2025]
---

# Generation performance: verifiable correctness

> Whether generated output is right by a check that can be run: tests pass, or the answer matches a key.

## 1. Definition
Generated output, such as program code or a final answer to a math problem, is correct when an automatic check accepts it: the code passes held-out tests, or the answer equals the key [chen2021; kulal2019]. The check decides correctness without a human judge.

## 2. Boundaries
Differs from [factuality](factuality.md), which checks claims against knowledge, and from [similarity to reference](reference-similarity.md), which rewards matching wording: a program can look nothing like the reference and still pass. Correctness is only as good as the check; tests that miss cases accept wrong programs. When an agent does a whole multi-step task, completion is a system property: [autonomous task completion](autonomous-task-completion.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
pass@k is the standard metric. At small k it describes how often a single sample is right; at large k it describes what the model can solve at all if every sample is checked [yue2025].
<!-- generated:metrics:start -->
- [pass@k](../metrics/pass-at-k.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: correct generated code or answers save users work, if users can tell which outputs are correct.

## 6. How it is identified
Code-generation and reasoning benchmarks [chen2021; kulal2019; yue2025].

## 7. Sources
- [chen2021]: HumanEval and functional correctness.
- [kulal2019]: program synthesis checked by tests.
- [yue2025]: correctness at large sample budgets.

## Open questions and review notes
- None yet.
