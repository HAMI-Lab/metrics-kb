---
id: task-completion-time
title: Task Completion Time
aliases: [time on task, task time, time-to-completion]
page_type: metric
template_version: "0.1"
fields: [hci, information-retrieval, visualization, human-ai-interaction]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How long a person, working with the system, takes to finish a defined task."
  subject: [user-system-team]
  aspect: [efficiency]
  perspective: [objective]
  quantity_form: [duration]
  context: [task, user-specific]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [in-lab, field, online]
  data_source: [timing, interaction-logs, observation]
  unit: "seconds"
  range: "> 0"
  better: context-dependent

cost:
  level: medium
  requires: [participants or real users, "a clear task definition with start and end points"]
  automatable: true

related:
  - {metric: response-latency, relation: component-of, note: "System waiting time is part of task time."}
  - {metric: nasa-tlx, relation: correlated, note: "Faster is not better if it costs much more effort."}
  - {metric: system-usability-scale, relation: complementary, note: "Objective efficiency vs. perceived usability; modest correlation."}
  - {metric: precision, relation: correlated, note: "Better results are expected to shorten search tasks; evidence is mixed."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Shorter task time could mean a better tool or a less engaging one; depends on the task."}
  improved-usability: {direction: negative, evidence: correlational, note: "Efficiency is one of the three parts of the ISO usability definition; lower time for the same outcome is better."}

sources: [iso9241-11, hornbaek2006, hornbaek2007, sauro2009, sauro2010, sauro2016, card1983, S19, S20, S21]
---

# Task Completion Time

> How long it takes a person using the system to finish a defined task, from a clear start point to a clear end point.

## 1. What is measured

### 1.1 Definition
The time elapsed between the start of a task and its completion, for a person using a system. Measured per task and per participant, then summarized across participants.

### 1.2 Construct: property of subject in context
The property is **efficiency** (time spent to achieve an outcome). The subject is the **user and system together**: both the person's skill and the system's speed and design shape it. The context is a specific **task**, which must be defined carefully; the same system gives very different times for different tasks and different users.

### 1.3 What it does not measure
It does not measure whether the outcome was right, so it must be paired with task success or accuracy. It does not distinguish time spent thinking from time spent waiting for the system or fighting the interface. It does not measure perceived speed.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for "how long the task took." **Proxy** for efficiency in the ISO sense, which is resources spent *relative to* the outcome achieved [iso9241-11]; time is only one resource and ignores effort. Hence `measure_type: mixed`.

### 2.2 Reliability
Task times vary widely between people and are right-skewed (a few very slow participants). Reliability of the mean depends heavily on sample size and on how well the task is specified [sauro2016].

### 2.3 Data collection and measurement error
Lab studies: timer or software log with defined start and end events. Field and online: inferred from logs, where start and end are often ambiguous and people multitask. Think-aloud protocols slow people down, so times from think-aloud sessions are not comparable to silent sessions. Decide in advance how to handle abandoned tasks and time limits.

### 2.4 Computation
- Decide which attempts count: successful tasks only, or all (and state it). Hornbæk's review found reporting practice inconsistent [hornbaek2006].
- Because times are skewed, for small samples the geometric mean has been recommended over the arithmetic mean, or log-transform before analysis [sauro2010].
- Report per task, with confidence intervals; avoid averaging across unrelated tasks.
- Expected expert times can be predicted without users using keystroke-level or GOMS models [card1983].

### 2.5 Unit and scale
Seconds (ratio scale). Only comparable within the same task definition.

## 3. Why it is measured

### 3.1 Purposes
Comparing designs or AI-assistance conditions; benchmarking against a competitor or earlier version; finding tasks that are unexpectedly slow. The spreadsheet's Metrics tab lists time-to-diagnosis logs for clinical decision-support evaluation [S19; S20; S21]; which of these sources actually reports it needs checking.

### 3.2 Assumptions
That lower time is better, which fits routine and goal-directed tasks but not exploration, learning, or reading, where more time may mean more engagement or care. That the task is equally meaningful for all participants. That participants are motivated to be fast in the same way real users would be.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers in studies (needs participants); data teams from logs (cheap once instrumented, but the task boundaries are fuzzy).

### 4.2 Consumers and decisions informed
Designers and product teams choosing between alternatives; operations teams estimating labour cost; researchers testing whether assistance speeds people up.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing for speed can reduce accuracy or careful checking, including checking AI outputs. Using it without success rate hides failures (a quick give-up looks efficient). Comparing across tasks of different difficulty.

## 5. Related metrics

### 5.1 Static relationships
Same aspect, other resource: [NASA-TLX](nasa-tlx.md) (effort). Component: [Response Latency](response-latency.md) is part of task time. Complementary: task success rate, [SUS](system-usability-scale.md). Predicted time from models [card1983] is a cheap substitute early in design; measured time with users is costlier but real.

### 5.2 Dynamic relationships
Correlations between efficiency, effectiveness, and satisfaction measures are generally low to modest across studies [hornbaek2007], though higher at the task level in some datasets [sauro2009]. So time cannot stand in for the others. Speed-accuracy trade-offs mean time and error rate can move in opposite directions.

## 6. Links to business objectives
**Improved usability:** lower time for the same outcome is better; efficiency is part of the ISO definition [iso9241-11]. Evidence: correlational.

**Sustained use:** unclear. Faster completion could make the tool more worth returning to, or could reflect less engagement. No evidence recorded; treat as open.

## 7. Sources
- [iso9241-11]: efficiency in the usability definition.
- [hornbaek2006], [hornbaek2007], [sauro2009]: practice and correlations.
- [sauro2010], [sauro2016]: summarizing task times.
- [card1983]: predicted task times.
- [S19], [S20], [S21]: time-to-diagnosis in clinical AI evaluation (per spreadsheet; unverified).

## Open questions and review notes
- Should task success rate be a required companion field on this page?
- The spreadsheet Metrics tab has a row "user search completion time" with no source; which paper was it from?
