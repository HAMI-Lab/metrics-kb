---
id: win-rate
title: "Win Rate (pairwise comparison)"
aliases: [win rate, AlpacaEval, length-controlled win rate, Arena-Hard]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How often a system's response is preferred over a reference system's response to the same prompt."
  measures: [output-quality]
  subject: [system]
  aspect: [effectiveness]
  perspective: [objective, perceived]
  quantity_form: [proportion]
  context: [task, system-specific]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [benchmark]
  route: [comparative-judgment]
  collection_mode: [offline]
  data_source: [model-judge, relevance-judgments]
  unit: "proportion of comparisons won"
  range: "0-1"
  better: higher
  validity_concern: {level: high, note: "Depends on the judge, usually a model, and on the reference system; judges favour longer answers unless controlled."}
  instruments:
    - {name: "AlpacaEval", kind: content, sources: [dubois2024], probes: "following general user instructions", scale: "win rate, 0-1; length-controlled variant", note: "Instructions answered by the system and a reference model, compared by an LLM judge."}
    - {name: "Arena-Hard", kind: content, sources: [li2024b], probes: "hard, real user prompts", scale: "win rate, 0-1", note: "Prompts selected from Chatbot Arena, compared by an LLM judge against a baseline model."}
    - {name: "Pairwise LLM judge", kind: scorer, sources: [zheng2023, li2024], scale: "preference per pair", note: "A judge model compares two responses; order effects are controlled by swapping positions."}

cost:
  level: low
  requires: ["a prompt set", "a reference system's responses", "a judge"]
  automatable: true

related:
  - {metric: elo-rating, kind: operational, note: "Ratings fitted from many pairwise outcomes across many systems."}
  - {metric: judge-rating, kind: conceptual, note: "A judge rates each response alone rather than comparing two."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Preferred responses are assumed to keep users coming back."}
  improved-usability: {direction: unknown, evidence: none, note: "Judge preferences may not match what helps users."}

sources: [dubois2024, li2024b, zheng2023, li2024]
---

# Win Rate (pairwise comparison)

> The share of prompts on which a judge prefers the system's response to a reference system's response.

## 1. What is measured

### 1.1 Definition
For each prompt, the system and a reference system both respond, and a judge, usually a strong LLM and sometimes people, says which response is better. The win rate is the share of comparisons the system wins, with ties counted as half or set aside [dubois2024].

### 1.2 Construct: property of subject in context
The property is the quality of a system's responses relative to a reference system, as the judge sees it. The subject is the system used end to end (D28). The context is the prompt set, the reference system and the judge.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Output quality](../constructs/output-quality.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Absolute quality: a high win rate against a weak reference says little. Whether users would prefer the same responses.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy**: the judge stands in for users. Model judges prefer longer answers and can prefer a position or their own style; length-controlled win rates adjust for length [dubois2024] (check against the paper; [zheng2023]).

**Using a proxy with a known gap.** Win rates can rank systems cheaply against one reference. They cannot show what users prefer without checking the judge against human preferences on a sample. Keep the reference system and judge fixed when comparing.

### 2.2 Reliability
Depends on the judge, its prompt and the reference system. Swap the order of the two responses to control position bias. Agreement statistics for judges are on the [comparative judgment](../strategies/comparative-judgment.md) route page (D21).

### 2.3 Data collection and measurement error
Generate both systems' responses; run the judge on each pair, in both orders where possible.

### 2.4 Computation
- Win rate = wins ÷ comparisons (ties as half, or excluded; say which).
- Length-controlled: a regression adjusts the judge's preferences for the length difference [dubois2024].

### 2.5 Unit and scale
A proportion from 0 to 1; 0.5 means no difference from the reference. Not comparable across reference systems or judges.

### 2.6 Instruments
**Content: general instructions and hard user prompts**
- **AlpacaEval** [dubois2024]: general instructions; compared against a fixed reference model, with a length-controlled win rate.
- **Arena-Hard** [li2024b]: hard prompts selected from real user conversations, compared against a baseline model (check against the paper).

**Scorers**
- **Pairwise LLM judge** [zheng2023; li2024]: the judge model, its prompt and the order-swapping rule together are the scorer.

## 3. Why it is measured

### 3.1 Use cases
- A team compares fine-tuned variants of an assistant by win rate against the current production model.
- A model release reports AlpacaEval length-controlled win rate.

### 3.2 Purposes
Cheap comparison of open-ended responses where no answer key exists.

### 3.3 Assumptions
The judge's preferences match users'; the prompts represent use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML engineers; cost is the judge's inference.

### 4.2 Consumers and decisions informed
Teams choosing models and prompts for assistants.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Longer or more flattering answers can win without being better; training against the judge exploits its preferences.

## 5. Related metrics

### 5.1 Operationally related metrics
[Elo Rating (pairwise comparison)](elo-rating.md) fits ratings from many pairwise outcomes.

### 5.2 Conceptually related metrics
[Judge Rating (model judge)](judge-rating.md) scores responses one at a time.

<!-- generated:neighbours:start -->
- Same construct: [Elo Rating (pairwise comparison)](elo-rating.md) (Output quality), [Judge Rating (model judge)](judge-rating.md) (Output quality)
- Narrower construct: [Demographic Parity Difference (DPD)](demographic-parity-difference.md) (Output quality: fairness), [Attack Success Rate (ASR)](attack-success-rate.md) (Output quality: safety), [Toxicity Rate](toxicity-rate.md) (Output quality: safety)
- Sibling construct: [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (Autonomous task completion), [Action Efficiency Relative to Humans](action-efficiency-vs-humans.md) (Autonomous task efficiency), [pass^k](pass-hat-k.md) (Consistency across runs), [Response Latency](response-latency.md) (System responsiveness), [Performance Drop Rate (PDR)](performance-drop-rate.md) (System robustness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use:** positive, theoretical. **Improved usability:** unknown.

## 7. Sources
- [dubois2024]: AlpacaEval and length control.
- [li2024b]: Arena-Hard.
- [zheng2023]: pairwise LLM judging and its biases.
- [li2024]: survey of LLM judges.

## Open questions and review notes
- Win rates judged by people rather than a model belong here too, as a different scorer; none is listed yet.
