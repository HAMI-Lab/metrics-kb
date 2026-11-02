---
id: task-success-rate-user
title: "Task Success Rate (user on task)"
aliases: [task success rate, task completion rate, completion rate, effectiveness]
page_type: metric
template_version: "0.3"
fields: [hci, human-ai-interaction]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the tasks people attempt with a system, the share they complete correctly."
  measures: [task-effectiveness]
  subject: [user-system-team]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [task-study, logs-telemetry]
  route: [reference-comparison, external-judgment]
  collection_mode: [in-lab, field]
  data_source: [observation, reference-answers, interaction-logs]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: low, note: "Directly counts completed tasks; the definition of success must be set before the study."}

cost:
  level: high
  requires: ["participants", "tasks with clear success criteria"]
  automatable: false

related:
  - {metric: task-success-rate-benchmark, kind: operational, note: "Same computation at the system level: an agent acting alone on benchmark tasks."}
  - {metric: task-completion-time, kind: conceptual, note: "Efficiency of the same tasks; report the two together."}
  - {metric: perceived-usability-score, kind: empirical, note: "Success and perceived usability are correlated, but only modestly."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "People keep using systems with which they get their tasks done."}
  improved-usability: {direction: positive, evidence: correlational, note: "Effectiveness is part of usability by definition; correlations with other usability measures are modest."}

sources: [sauro2016, nielsen1993, hornbaek2006, sauro2009, iso9241-11, lazar2017, hornbaek2007]
---

# Task Success Rate (user on task)

> The share of tasks that people complete correctly when they use the system.

## 1. What is measured

### 1.1 Definition
Task Success Rate (user on task) is the number of tasks people complete correctly divided by the number they attempt. Success is set in advance for each task: a right answer, a reached end state, or criteria an observer checks [sauro2016]. A person does the task with the system; when an agent does the task alone, see [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (D20).

### 1.2 Construct: property of subject in context
The property is task effectiveness: whether people reach their goals with the system [iso9241-11]. The subject is the person and system together. The context is a set of tasks in a study or in real use.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Task effectiveness](../constructs/task-effectiveness.md) (under Task characteristics → Task performance; Task characteristics → Usability)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It ignores how long tasks took and how hard they felt. A binary success hides partial success; some studies score levels of success instead.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the success criteria used. The criteria must match what users actually need; success on set tasks may not carry over to the tasks people bring themselves [hornbaek2006].

### 2.2 Reliability
Small samples give wide intervals: 8 out of 10 participants succeeding is compatible with a wide range of true rates. Use intervals suited to small samples [sauro2016].

### 2.3 Data collection and measurement error
In a task study, observers or the system record whether each task ended in success. In real use, success can sometimes be read from logs (a completed purchase, a submitted form), but the person's goal is usually unknown.

### 2.4 Computation
- Success rate = tasks completed successfully ÷ tasks attempted.
- Report per task and overall; give a confidence interval [sauro2016].
- Levels of success (full, partial, failed) are a variant; state the scoring.

### 2.5 Unit and scale
0 to 1.

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A hospital's patient portal is tested with 12 patients: can they find their latest lab result and book a follow-up?
- A team testing an AI writing assistant counts how many participants produce a cover letter that meets set criteria within the session.
- An e-commerce site tracks completed checkouts per started checkout as a field success rate.

### 3.2 Purposes
Usability testing; comparing designs; release criteria [nielsen1993].

### 3.3 Assumptions
The set tasks represent real goals; success can be judged consistently.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers.

### 4.2 Consumers and decisions informed
Design and product teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Easy tasks inflate the rate. Counting "completed" without checking correctness overstates success.

## 5. Related metrics

### 5.1 Operationally related metrics
The same computation at the system level is [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md).

### 5.2 Conceptually related metrics
[Task Completion Time](task-completion-time.md) is the efficiency counterpart; [SUS](perceived-usability-score.md) the perceived one.

<!-- generated:neighbours:start -->
- Narrower construct: [Decision Accuracy with AI Assistance](decision-accuracy-with-ai.md) (Task effectiveness: decision correctness), [Precision (user on task)](precision-user-task.md) (Task effectiveness: situational relevance)
- Sibling construct: [Task Completion Time](task-completion-time.md) (Task efficiency), [Perceived Usability Score (questionnaire)](perceived-usability-score.md) (Usability: perceived usability)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Correlations between success, time and satisfaction across usability studies are modest [hornbaek2007; sauro2009] (check against the papers for figures).

## 6. Links to business objectives
**Improved usability:** positive, correlational. **Sustained use:** positive, theoretical.

## 7. Sources
- [sauro2016]: measuring and reporting success rates.
- [nielsen1993]: usability testing.
- [hornbaek2006]: measurement practice.
- [sauro2009], [hornbaek2007]: correlations among usability measures.
- [iso9241-11]: effectiveness.
- [lazar2017]: research methods.

## Open questions and review notes
- None yet.
