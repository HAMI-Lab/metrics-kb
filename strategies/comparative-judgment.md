---
id: comparative-judgment
title: "Comparative judgment: preferences and interleaving"
aliases: [pairwise preference, side-by-side, interleaving]
page_type: strategy
template_version: "0.2"

layer: route
research_methods: [task-study, logs-telemetry, questionnaire-survey]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [chapelle2012, hofmann2016, bradley1952, zheng2023, li2024]
---

# Comparative judgment: preferences and interleaving

> Instead of scoring one system, people (or judges) choose between alternatives, and the choices are aggregated into a ranking.

## 1. What it is

### 1.1 Definition
Two or more outputs or systems are shown together, and the judge or the user's behaviour indicates which is better. Many such comparisons are combined into relative scores.

### 1.2 Typical pairings
Side-by-side studies, online experiments with real users, and preference questions.
<!-- generated:pairings:start -->
- [Task studies with people](task-study.md)
- [Interaction logs and telemetry](logs-telemetry.md)
- [Questionnaires and surveys](questionnaire-survey.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Interleaving** in online search: results from two rankers are mixed in one list, and clicks show which ranker users prefer [chapelle2012; hofmann2016].
- **Pairwise preference** by people or LLM judges, aggregated with models such as Bradley-Terry [bradley1952].
- **Arena-style leaderboards**, where many pairwise votes rank models [zheng2023].

## 2. When to use it
Use it when absolute scores are unreliable but people can tell which of two is better, or when sensitivity matters more than an absolute number.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
Results are relative: they say A beats B, not whether either is good enough. Preference may track style more than task success.

### 3.2 Reliability
Needs many comparisons; rankings depend on which pairs were compared. With model judges, check position consistency: whether the preferred answer stays the same when the two answers swap places [li2024]. Interleaving is reported to detect differences with fewer observations than absolute online metrics (check against [chapelle2012]).

### 3.3 Bias and gaming
Position bias (the first or left option is favoured) and length or style bias. Systems can be tuned to win comparisons without improving outcomes.

## 4. Cost
Low to medium per judgment; online interleaving is cheap once a ranking system supports it.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
_No metric page uses it yet._
<!-- generated:metrics:end -->

## 6. Sources
- [chapelle2012]
- [hofmann2016]
- [bradley1952]
- [zheng2023]
- [li2024]

## Open questions and review notes
- None yet.
