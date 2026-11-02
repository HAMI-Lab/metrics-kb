---
id: precision-user-task
title: Precision (user on task)
aliases: [precision, user-judged precision, interactive precision, click precision]
page_type: metric
template_version: "0.2"
fields: [information-retrieval, recommender-systems, hci]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the items a system returned to a user doing their own task, the share that the user found relevant to that task."
  measures: [situational-relevance]
  subject: [user-system-team]
  aspect: [effectiveness]
  perspective: [objective, perceived]
  quantity_form: [proportion]
  context: [task, session]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [task-study, logs-telemetry]
  route: [self-rating, statistical-modeling]
  collection_mode: [in-lab, field, online]
  data_source: [relevance-judgments, interaction-logs]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: high, note: "Explicit judgments change how people search; clicks are biased by rank and presentation and are not judgments (see 2.1)."}

cost:
  level: high
  requires: ["participants doing real or realistic tasks who mark results, or a deployed system with logs and a click model"]
  automatable: false

related:
  - {metric: precision-test-collection, kind: operational, note: "Same computation at the component level, on fixed queries and assessor judgments."}
  - {metric: precision-test-collection, kind: empirical, note: "Higher test-collection precision does not reliably give higher precision for users on their own tasks."}
  - {metric: task-completion-time, kind: conceptual, note: "Effectiveness and efficiency of the same task."}
  - {metric: system-usability-scale, kind: empirical, note: "Result quality is expected to feed perceived usability; not measured here."}

objectives:
  improved-usability: {direction: positive, evidence: theoretical, note: "Part of effectiveness for the user's own task."}
  sustained-use: {direction: positive, evidence: theoretical, note: "Results that help with real tasks make the system worth returning to."}

sources: [saracevic2007, barry1998, hersh2000, turpin2006, kelly2009, hofmann2016, chuklin2015, webb1966]
---

# Precision (user on task)

> The fraction of what the system showed a user, for the user's own task, that the user found relevant.

## 1. What is measured

### 1.1 Definition
Precision = items the user found relevant ÷ items returned (or the top *k* shown). The formula is the same as [Precision (test collection)](precision-test-collection.md). What differs is where the parts come from: the queries are the ones the user issued, and relevance is decided by the user, for their task, either explicitly or as inferred from behaviour.

### 1.2 Construct: property of subject in context
The property is **situational relevance** of the results: whether they help this user with this task [saracevic2007]. The subject is the user and system together. The context is a task the user is doing, in a study or in real use.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Task effectiveness: situational relevance](../constructs/situational-relevance.md) (under Task characteristics → Task performance → Task effectiveness; Task characteristics → Usability → Task effectiveness)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure the component on its own: the user's queries and judgments are part of the number, so a change in precision may come from the user, the interface, or the retriever. It ignores what the user never saw or never found (task-level recall is harder still, because nobody knows the full set of items relevant to a user's task). It says nothing about effort or satisfaction.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** when users mark each result as relevant to their task, though only for the results they look at. **Proxy** when relevance is inferred from clicks, saves or dwell time: a click shows interest in a snippet, not that the item helped [chuklin2015]. Users judge by more than topic, such as novelty and reliability [barry1998], so their judgments and an assessor's can differ for the same item. Hence `measure_type: mixed`.

### 2.2 Reliability
Judgments of one user on one task are not repeatable in the way assessor judgments are: the same person may judge differently later, once they know more. Compare systems with many users and tasks, and report the spread.

### 2.3 Data collection and measurement error
- **Task study:** participants search for their own or assigned realistic tasks and mark results as relevant, or save the ones they would use [kelly2009]. Asking for judgments changes behaviour: people read more carefully than they otherwise would [webb1966].
- **Logs:** relevance is inferred from clicks or other signals in real use, and corrected for position bias with a click model [chuklin2015; hofmann2016].
- **Mixed:** in some interactive studies, users choose and save items, and assessors judge the saved items afterwards [hersh2000]. The queries and choices are the user's; the judgments are not, so state which.

### 2.4 Computation
- Per task or session: user-relevant results ÷ results shown, or over the top *k* the user saw.
- Averaged over tasks and users: report macro or micro averaging, and the number of users and tasks.
- With inferred relevance: state the signal (click, save, dwell above a threshold) and the correction model.

### 2.5 Unit and scale
A proportion from 0 to 1. Comparable only across conditions with similar users, tasks and judgment instructions; it is not comparable with test-collection precision on the same system.

## 3. Why it is measured

### 3.1 Use cases
- A streaming service A/B tests two "recommended for you" ranking models, comparing precision@10 against what listeners actually played versus skipped.
- A hospital's sepsis-alert system is audited monthly: of the alerts it fired, how many did clinicians confirm versus dismiss as false alarms?
- A library tests a new discovery interface: students do their own coursework searches and mark which results they would cite.

### 3.2 Purposes
Checking whether a component improvement reaches users; comparing interfaces or systems in user studies; monitoring result quality in deployed systems.

### 3.3 Assumptions
The user's judgment, or the signal used in its place, is taken as the truth about relevance for the task. Every result the user looked at is assumed to have been judged. The tasks and users in the study represent real use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
User researchers and IR researchers running studies; product analysts working from logs. Studies are costly per data point; logs are cheap once instrumented but need a click model to be trusted.

### 4.2 Consumers and decisions informed
Product teams deciding whether a ranking change helps users; researchers testing whether offline gains hold up with people.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Treating clicks as judgments rewards attractive snippets rather than useful items. Reporting the test-collection number as if it were this one hides the gap described in 5.3.

## 5. Related metrics

### 5.1 Operationally related metrics
[Precision (test collection)](precision-test-collection.md) is the same computation at the component level, on fixed queries and assessor judgments.

### 5.2 Conceptually related metrics
[Task Completion Time](task-completion-time.md) measures the efficiency of the same task; task success measures its outcome. [SUS](system-usability-scale.md) measures how usable the system felt.

<!-- generated:neighbours:start -->
- Broader construct: [Task Success Rate (user on task)](task-success-rate-user.md) (Task effectiveness)
- Sibling construct: [Decision Accuracy with AI Assistance](decision-accuracy-with-ai.md) (Task effectiveness: decision correctness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
The test-collection version is cheap and repeatable, so builders optimize it; users experience this one. In controlled studies, large differences in test-collection precision produced small or no differences in what users achieved [hersh2000; turpin2006]. A builder optimizing the first should check the second before claiming a user benefit.

## 6. Links to business objectives
**Improved usability:** positive, theoretical: it is part of effectiveness for the user's task.

**Sustained use:** positive, theoretical: results that help with real tasks make the system worth returning to.

## 7. Sources
- [saracevic2007], [barry1998]: situational relevance and users' relevance criteria.
- [kelly2009]: interactive IR studies with users.
- [hersh2000], [turpin2006]: test-collection gains vs user outcomes.
- [chuklin2015], [hofmann2016]: relevance inferred from clicks, and position bias.
- [webb1966]: reactive measurement.

## Open questions and review notes
- Should a Recall (user on task) page follow? Interactive studies have used recall computed on users' saved items [hersh2000] (check against the paper).
- `route` lists self-rating for explicit judgments. A user marking items as relevant is closer to judgment than to rating; is self-rating the right route, or does external judgment by the user fit better?
