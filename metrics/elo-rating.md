---
id: elo-rating
title: "Elo Rating (pairwise comparison)"
aliases: [Elo, Arena score, Bradley-Terry rating, Chatbot Arena rating]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "A rating for each system, fitted from many pairwise preferences, that predicts how often it would be preferred over each other system."
  measures: [output-quality]
  subject: [system]
  aspect: [effectiveness]
  perspective: [perceived]
  quantity_form: ["other: latent rating from a statistical model"]
  context: [system-specific, user-specific]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [logs-telemetry]
  route: [comparative-judgment, statistical-modeling]
  collection_mode: [online, field]
  data_source: [interaction-logs]
  unit: "rating points"
  range: "unbounded; only differences matter"
  better: higher
  validity_concern: {level: high, note: "Reflects the preferences of the people who vote on the prompts they choose; differences between close ratings are within noise."}
  instruments:
    - {name: "Chatbot Arena", kind: content, sources: [chiang2024], probes: "preferences of platform users on their own prompts", scale: "Bradley-Terry ratings on an Elo-like scale, with confidence intervals", note: "Users chat with two anonymous models and vote for the better answer."}

cost:
  level: high
  requires: ["a platform with many voting users", "many comparisons per system"]
  automatable: false

related:
  - {metric: win-rate, kind: operational, note: "Pairwise outcomes summarized against one reference rather than fitted across all systems."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Preferred systems are assumed to be used more."}
  improved-usability: {direction: unknown, evidence: none, note: "Preference in a side-by-side vote is not the same as task success."}

sources: [elo1978, bradley1952, chiang2024, zheng2023]
---

# Elo Rating (pairwise comparison)

> A rating for each system, fitted from pairwise votes, such that differences in rating predict how often one system is preferred over another.

## 1. What is measured

### 1.1 Definition
People, or a judge, compare responses from two systems and pick the better one. Over many comparisons across many systems, a statistical model assigns each system a rating; the difference between two ratings predicts the probability that one is preferred. The Elo system updates ratings after each comparison [elo1978]; the Bradley-Terry model fits all comparisons at once [bradley1952]. Chatbot Arena reports Bradley-Terry ratings on an Elo-like scale [chiang2024].

### 1.2 Construct: property of subject in context
The property is the quality of systems' responses as preferred by the voters, relative to each other. The subject is the system used end to end (D28). The context is the population of voters and the prompts they choose.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Output quality](../constructs/output-quality.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Absolute quality, or quality for a particular user group or task, unless votes are filtered to it.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy**: votes stand in for users' preferences in general. Voters choose their own prompts and differ from the general user population; style and length can sway votes (check against [chiang2024]).

**Using a proxy with a known gap.** Ratings can rank many systems by the preferences of the platform's voters. They cannot show which system is best for a particular task or user group, or settle differences within the confidence intervals. Check the intervals, and the ratings for the relevant category of prompts, before relying on a ranking.

### 2.2 Reliability
Depends on the number of votes per system; report confidence intervals, often from bootstrapping [chiang2024].

### 2.3 Data collection and measurement error
Collect pairwise votes on a running platform; remove duplicate or abusive votes.

### 2.4 Computation
- Elo: after each comparison, the winner gains and the loser loses points in proportion to how unexpected the result was [elo1978].
- Bradley-Terry: fit a strength per system by maximum likelihood over all comparisons [bradley1952]; report on an Elo-like scale.

### 2.5 Unit and scale
Rating points; only differences are meaningful, and a fixed difference corresponds to a fixed preference probability. Not comparable across platforms.

### 2.6 Instruments
**Preferences of platform users**
- **Chatbot Arena** [chiang2024]: users chat with two anonymous models side by side and vote; ratings with confidence intervals, also by prompt category.

## 3. Why it is measured

### 3.1 Use cases
- A team checks where its released model ranks on Chatbot Arena, overall and for coding prompts.
- A company running two assistants internally collects side-by-side votes from employees and fits ratings.

### 3.2 Purposes
Ranking many systems by human preference without a fixed test set.

### 3.3 Assumptions
Preferences are consistent enough to be summarized by one number per system; voters represent the users of interest.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Platform operators; costly to run, free to read.

### 4.2 Consumers and decisions informed
Model builders and buyers comparing models.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Tuning style to win votes; reading small rating differences as real.

## 5. Related metrics

### 5.1 Operationally related metrics
[Win Rate (pairwise comparison)](win-rate.md) summarizes pairwise outcomes against one reference.

### 5.2 Conceptually related metrics
[Judge Rating (model judge)](judge-rating.md) rates responses one at a time.

<!-- generated:neighbours:start -->
- Same construct: [Judge Rating (model judge)](judge-rating.md) (Output quality), [Win Rate (pairwise comparison)](win-rate.md) (Output quality)
- Narrower construct: [Demographic Parity Difference (DPD)](demographic-parity-difference.md) (Output quality: fairness), [Attack Success Rate (ASR)](attack-success-rate.md) (Output quality: safety), [Toxicity Rate](toxicity-rate.md) (Output quality: safety)
- Sibling construct: [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (Autonomous task completion), [Action Efficiency Relative to Humans](action-efficiency-vs-humans.md) (Autonomous task efficiency), [pass^k](pass-hat-k.md) (Consistency across runs), [Response Latency](response-latency.md) (System responsiveness), [Performance Drop Rate (PDR)](performance-drop-rate.md) (System robustness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: arena ratings and benchmark accuracies agree only partly. Why it could be true: votes reward style and helpfulness on users' own prompts, which benchmarks with answer keys do not measure (further reference needed).

## 6. Links to business objectives
**Sustained use:** positive, theoretical. **Improved usability:** unknown.

## 7. Sources
- [elo1978]: the Elo system.
- [bradley1952]: the Bradley-Terry model.
- [chiang2024]: Chatbot Arena.
- [zheng2023]: human preference and LLM judging.

## Open questions and review notes
- Arena voters choose their own prompts and judge the answers, which D20 would usually place at the task root; the page sits at the system root because voters judge output quality rather than pursue a goal. Is that right?
- `quantity_form` uses `other: latent rating`; should the vocabulary gain a value for ratings fitted by a model?
