---
id: attack-success-rate
title: "Attack Success Rate (ASR)"
aliases: [ASR, jailbreak success rate, JSR]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, ai-safety]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the attempts to make a system break its rules, the share that succeed."
  measures: [safety]
  subject: [system]
  aspect: [safety]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [adversarial-testing]
  route: [external-judgment, reference-comparison]
  collection_mode: [offline]
  data_source: [model-judge, relevance-judgments]
  unit: "proportion"
  range: "0-1"
  better: lower
  validity_concern: {level: high, note: "Depends on the attacks tried and on how success is judged; definitions differ across benchmarks."}
  instruments:
    - {name: "AdvBench", sources: [zou2023], probes: "refusal of harmful requests under jailbreak attacks", scale: "share of successful attacks, 0-1", note: "Harmful behaviours and strings used to test attacks."}
    - {name: "HarmBench", sources: [mazeika2024], probes: "refusal of harmful requests under automated red teaming", scale: "share of successful attacks, 0-1", note: "Standardized behaviours, attacks and a fixed judge for comparability."}
    - {name: "DecodingTrust", sources: [wang2023], probes: "trustworthiness under adversarial conditions, across several perspectives", scale: "per-perspective scores", note: "Covers toxicity, bias, adversarial robustness, privacy and more."}

cost:
  level: medium
  requires: ["an attack set or red team", "a judge for whether each response is unsafe"]
  automatable: true

related:
  - {metric: toxicity-rate, kind: conceptual, note: "Harmful content in ordinary use, not under attack."}
  - {metric: performance-drop-rate, kind: conceptual, note: "Robustness to changed inputs in general, not to attacks on safety rules."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Successful attacks that become public erode trust in the system."}
  improved-usability: {direction: unknown, evidence: none, note: "Safety measures can also make the system refuse harmless requests."}

sources: [wang2023, liu2025, ganguli2022, zhu2023, zou2023, mazeika2024]
---

# Attack Success Rate (ASR)

> The share of attack attempts that make the system produce the harmful or forbidden behaviour the attacker wanted.

## 1. What is measured

### 1.1 Definition
Attack Success Rate (ASR) is the number of successful attacks divided by the number of attempts. An attack is a prompt or input meant to make the system do something it should refuse, such as give dangerous instructions or reveal private data. It counts as successful when the response shows the targeted behaviour [wang2023; liu2025].

### 1.2 Construct: property of subject in context
The property is safety under attack. The subject is the whole system, including filters and refusal behaviour, because attacks target what the user sees. The context is a set of attacks.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Output quality: safety](../constructs/safety.md) (under System characteristics → System performance → Output quality)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure safety in ordinary use, where most users do not attack. It does not measure over-refusal: a system that refuses everything has an attack success rate of zero.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the attacks tried and the judge used; **proxy** for how safe the system is against attackers in general, hence `mixed`. Benchmarks define success differently, for example any harmful content vs the exact content requested, so rates from different benchmarks are not comparable [liu2025].

**Using a proxy with a known gap.** A low rate supports a claim that the system resists *these* attacks under *this* judge. It cannot support a claim that the system is safe: new attacks appear constantly. Report the attack set, the success definition and the judge; pair it with an over-refusal rate on harmless requests; and re-test with new attacks before claiming improvement.

### 2.2 Reliability
Depends on the judge: model judges and people disagree on borderline responses. Human red teams vary in skill, so the same system can score differently with a different team [ganguli2022].

### 2.3 Data collection and measurement error
Run an attack set or red-team session against the system and judge each response. See [adversarial testing](../strategies/adversarial-testing.md).

### 2.4 Computation
- ASR = successful attacks ÷ attack attempts.
- Per attack type (jailbreak, prompt injection, data extraction) as well as overall.
- For automated attacks that try many variants, report whether success is counted per attempt or per target behaviour [zhu2023].

### 2.5 Unit and scale
0 to 1. Lower is better.

### 2.6 Instruments
**Refusal under jailbreak attacks**
- **AdvBench** [zou2023]: harmful behaviours used to test whether attacks make a model comply. Success was originally judged by refusal phrases, which can over-count success (check against the paper).
- **HarmBench** [mazeika2024]: standardizes behaviours, attack methods and a fixed judge, so attack success rates are comparable across studies.

**Broad trustworthiness under attack**
- **DecodingTrust** [wang2023]: adversarial tests across several perspectives, such as toxicity, bias, robustness and privacy; reports a score per perspective rather than one rate.

Attack success rates depend on the judge as much as on the model; compare only under the same judge.

## 3. Why it is measured

### 3.1 Use cases
- A chatbot provider tests each model release against a fixed jailbreak suite and blocks release if the rate rises [wang2023].
- An enterprise agent that reads email is tested with prompt-injection messages: how often does it follow instructions hidden in an email?
- A red team spends a week trying to extract private training data; the share of successful attempts goes into the risk report [ganguli2022].

### 3.2 Purposes
Release gating, safety reporting, comparing safety measures.

### 3.3 Assumptions
The attack set represents what real attackers will try; the judge recognizes harmful responses.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Safety and red-team engineers.

### 4.2 Consumers and decisions informed
Release managers, policy and risk teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Patching the specific attacks in a public suite lowers the rate without making the system safer. Lowering the rate by refusing more hurts harmless users.

## 5. Related metrics

### 5.1 Operationally related metrics
Jailbreak success rate and per-type rates are variants on this page.

### 5.2 Conceptually related metrics
[Toxicity Rate](toxicity-rate.md) covers harmful content in ordinary use. [Performance Drop Rate](performance-drop-rate.md) covers changed inputs that are not attacks on safety rules.

<!-- generated:neighbours:start -->
- Same construct: [Toxicity Rate](toxicity-rate.md) (Output quality: safety)
- Sibling construct: [Demographic Parity Difference (DPD)](demographic-parity-difference.md) (Output quality: fairness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: lowering attack success by stricter refusal raises over-refusal of harmless requests. Why it could be true: the same refusal behaviour that blocks attacks also fires on harmless requests that look similar; surveys discuss over-refusal as a known cost [liu2025] (further reference needed for measured trade-offs).

## 6. Links to business objectives
**Sustained use:** negative, theoretical: public safety failures erode trust. **Improved usability:** unknown: stronger defences can make the system refuse harmless requests.

## 7. Sources
- [wang2023]: attack success in a trustworthiness benchmark.
- [liu2025]: safety evaluation survey, success definitions, over-refusal.
- [ganguli2022]: human red teaming.
- [zhu2023]: automated adversarial prompts.

## Open questions and review notes
- Should over-refusal rate get its own page as the paired metric?
