---
id: task-study
title: Task studies with people
aliases: [user study, usability test, lab study, controlled experiment task, reader study]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [lazar2017, kelly2009, sauro2016, nielsen1993, bansal2021, webb1966]
---

# Task studies with people

> People do defined tasks with the system while what they do and achieve is recorded.

## 1. What it is

### 1.1 Definition
Participants use the system to do tasks set by the researcher or chosen by themselves, in a lab or in their own setting [lazar2017]. The study records what they do (actions, time, errors), what they achieve (answers, decisions, outputs), and often what they report afterwards. It is the main method for task-level constructs, because it puts a user, a system and a goal together.

### 1.2 Typical pairings
Outcomes are compared with the right answers; times and errors are read directly; ratings collected after tasks are self-reports; preferences between versions are comparative judgments.
<!-- generated:pairings:start -->
- [Comparative judgment: preferences and interleaving](comparative-judgment.md)
- [Comparison against reference data](reference-comparison.md)
- [Direct reading: timing and counting](direct-reading.md)
- [Self-report: ratings and answers about oneself](self-report.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Usability tests:** a few participants do realistic tasks while observers note successes, errors and problems [nielsen1993].
- **Interactive IR studies:** participants search for given or own information needs; the queries, results seen and items saved are logged [kelly2009].
- **Human-AI decision studies:** participants make decisions with and without AI advice, so the effect of the advice can be estimated [bansal2021].
- **Reader studies** in medical imaging: clinicians read cases with and without AI support, and their diagnoses are scored against confirmed outcomes.

## 2. When to use it
Use it for task characteristics: effectiveness, efficiency, reliance, understanding, and experience of a user with a system. It is too costly for routine monitoring of a deployed system, where logs are the usual choice.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
Set tasks may not be the tasks people actually have, and participants may not be the real users. People behave differently when observed [webb1966]. A lab study cannot show long-term effects such as learning or abandonment.

### 3.2 Reliability
Samples are small, so results vary from study to study; report intervals, not only means [sauro2016]. Task order and fatigue affect results; balance the order across participants.

### 3.3 Bias and gaming
Easy tasks or friendly participants inflate results. Participants try to please the researcher, which favours whatever system they think is the new one.

## 4. Cost
High per data point: recruiting, paying and running participants, and designing tasks with known right answers. Remote, unmoderated studies are cheaper but give less control.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Decision Accuracy with AI Assistance](../metrics/decision-accuracy-with-ai.md)
- [Forward-Prediction Accuracy](../metrics/forward-prediction-accuracy.md)
- [Over-reliance Rate](../metrics/over-reliance-rate.md)
- [Precision (user on task)](../metrics/precision-user-task.md)
- [Task Completion Time](../metrics/task-completion-time.md)
- [Task Success Rate (user on task)](../metrics/task-success-rate-user.md)
- [Under-reliance Rate](../metrics/under-reliance-rate.md)
<!-- generated:metrics:end -->

## 6. Sources
- [lazar2017]: research methods in HCI.
- [kelly2009]: interactive IR studies.
- [sauro2016]: statistics for small user studies.
- [nielsen1993]: usability testing.
- [bansal2021]: human-AI decision studies.
- [webb1966]: reactive measurement.

## Open questions and review notes
- None yet.
