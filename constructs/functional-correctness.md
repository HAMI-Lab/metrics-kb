---
id: functional-correctness
title: "Generation performance: functional correctness"
aliases: [execution correctness, verifiable correctness]
page_type: construct
template_version: "0.1"
fields: [llm-evaluation, software-engineering]

broader: [generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [chen2021, kulal2019, yue2025]
---

# Generation performance: functional correctness

> Whether generated code does what it should when it runs.

## 1. Definition
A generated program is functionally correct when it behaves as specified, which in practice means it passes held-out tests [chen2021; kulal2019]. Running the program decides correctness, without a human judge.

## 2. Boundaries
- This construct used to be called "verifiable correctness" (id `verifiable-correctness`). That named how it is checked, not what is measured, so it was renamed (D23). Final answers to math problems, which the old page also covered, are now under [answer correctness](answer-correctness.md).
- It differs from [factuality](factuality.md), which checks claims against knowledge, and from [content adequacy](content-adequacy.md), where overlap with a reference is the usual check: a program can look nothing like the reference and still pass.
- Correctness is only as good as the tests: tests that miss cases accept wrong programs.
- When an agent does a whole multi-step task, completion is a system property: [autonomous task completion](autonomous-task-completion.md).

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
Theoretical: correct generated code saves users work, if users can tell which outputs are correct.

## 6. How it is identified
Code-generation benchmarks [chen2021; kulal2019].

## 7. Sources
- [chen2021]: HumanEval and functional correctness.
- [kulal2019]: program synthesis checked by tests.
- [yue2025]: correctness at large sample budgets.

## Open questions and review notes
- Code generation may deserve its own type under component performance (output: an executable program), next to open-ended generation. Not done yet.
