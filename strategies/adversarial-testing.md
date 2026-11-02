---
id: adversarial-testing
title: Adversarial testing and red teaming
aliases: [red teaming, jailbreak testing, attack suites, penetration testing]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [ganguli2022, liu2025, wang2023, zhu2023]
---

# Adversarial testing and red teaming

> People or programs deliberately try to make the system fail or misbehave, and the attempts and responses are recorded.

## 1. What it is

### 1.1 Definition
Testers act as attackers. They write inputs meant to make the system break its rules or fail, such as prompts that try to get a language model to produce harmful content, leak private data, or follow injected instructions [ganguli2022; liu2025]. The attempts can come from people (red teams), from fixed attack suites, or from programs that search for successful attacks [zhu2023]. The data is the set of attempts and the system's responses.

### 1.2 Typical pairings
Responses are judged as harmful or not by people or model judges, or checked against a known target behaviour.
<!-- generated:pairings:start -->
- [Comparison against reference data](reference-comparison.md)
- [External judgment: annotators, experts, model judges, simulated users](external-judgment.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Human red teaming:** people try freely to elicit harmful behaviour [ganguli2022].
- **Jailbreak and attack benchmarks:** fixed sets of attack prompts, reused across systems [wang2023; liu2025].
- **Automated attacks:** programs that generate or optimize attack prompts [zhu2023].
- **Prompt injection tests** for agents: instructions hidden in content the agent reads.

## 2. When to use it
Use it for safety and security constructs, where ordinary inputs rarely show the failure. It measures resistance to the attacks tried, not typical behaviour; use ordinary test collections or logs for that.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
A system that resists the attacks tried may fail to new ones; results are a lower bound on vulnerability, not a guarantee. What counts as success for an attack differs across benchmarks [liu2025], so results from different suites are not comparable.

### 3.2 Reliability
Human red teams vary in skill and creativity, so results depend on who tested. Fixed suites are repeatable but age quickly.

### 3.3 Bias and gaming
Public attack suites can be patched one by one without making the system safer. Systems can look safe by refusing too much, which is why over-refusal on harmless requests is measured alongside [liu2025].

## 4. Cost
Human red teaming is costly and stressful work. Fixed suites are cheap to re-run; judging the responses is the recurring cost.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
_No metric page uses it yet._
<!-- generated:metrics:end -->

## 6. Sources
- [ganguli2022]: human red teaming.
- [liu2025]: safety evaluation survey.
- [wang2023]: trustworthiness benchmark with jailbreak tests.
- [zhu2023]: adversarial prompts.

## Open questions and review notes
- None yet.
