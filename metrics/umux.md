---
id: umux
title: "Usability Metric for User Experience (UMUX)"
aliases: [UMUX, UMUX-LITE]
page_type: metric
template_version: "0.2"
fields: [hci]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How usable people judge a system to be, from a short questionnaire."
  measures: [perceived-usability]
  subject: [user]
  aspect: [ease-of-use, effectiveness, satisfaction]
  perspective: [perceived]
  quantity_form: [rating-score]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [questionnaire-survey]
  route: [self-rating]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "score"
  range: "0-100"
  better: higher
  validity_concern: {level: low, note: "Direct for perceived usability as reported; a proxy for usability as performance."}

cost:
  level: low
  requires: ["people who have used the system", "under a minute"]
  automatable: false

related:
  - {metric: system-usability-scale, kind: conceptual, note: "Longer instrument for the same construct; UMUX was designed to track it."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Via satisfaction and continued use."}
  improved-usability: {direction: positive, evidence: correlational, note: "Measures perceived usability."}

sources: [finstad2010, lewis2013, lewis2018]
---

# Usability Metric for User Experience (UMUX)

> A four-item (or two-item, UMUX-LITE) questionnaire score of perceived usability, on a 0-100 scale.

## 1. What is measured

### 1.1 Definition
The Usability Metric for User Experience (UMUX) is a four-item questionnaire about how well a system meets the person's needs, how frustrating and how easy it is, and how much time it takes to correct things, scored on a 0-100 scale [finstad2010]. UMUX-LITE keeps the two positively worded items [lewis2013].

### 1.2 Construct: property of subject in context
The property is perceived usability. The subject is the person's judgment of the system. The context is use of the system for their tasks.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Usability: perceived usability](../constructs/perceived-usability.md) (under Task characteristics → Usability)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure performance; people can rate a system highly while failing tasks. It is too short to diagnose specific problems.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for perceived usability as reported; **proxy** for usability in the ISO sense, as for [SUS](system-usability-scale.md).

### 2.2 Reliability
Reported internal consistency is acceptable for a short scale (check against [finstad2010]). UMUX-LITE trades reliability for brevity.

### 2.3 Data collection and measurement error
Post-study or post-use questionnaire. See [self-rating](../strategies/self-rating.md).

### 2.4 Computation
- UMUX: 7-point items, odd items scored as response − 1 and even items as 7 − response, summed and rescaled to 0-100 [finstad2010] (check against the paper).
- UMUX-LITE: two items, rescaled to 0-100; a regression adjustment to align with SUS has been proposed [lewis2013] (check against the paper).

### 2.5 Unit and scale
0-100.

## 3. Why it is measured

### 3.1 Use cases
- A SaaS team adds UMUX-LITE to an in-app survey because SUS is too long for a pop-up [lewis2013].
- A university IT team compares two learning-management systems with UMUX after a pilot term.

### 3.2 Purposes
Tracking perceived usability where questionnaire space is short [lewis2018].

### 3.3 Assumptions
Respondents used the system enough to judge it.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers and product teams.

### 4.2 Consumers and decisions informed
Product teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
As for any self-report: friendly samples and timing inflate scores.

## 5. Related metrics

### 5.1 Operationally related metrics
UMUX-LITE is a variant on this page.

### 5.2 Conceptually related metrics
[SUS](system-usability-scale.md) is the longer substitute; UMUX scores were designed to correspond closely to SUS scores [finstad2010] (check against the paper).

<!-- generated:neighbours:start -->
- Same construct: [System Usability Scale (SUS)](system-usability-scale.md) (Usability: perceived usability)
- Sibling construct: [Task Success Rate (user on task)](task-success-rate-user.md) (Task effectiveness), [Task Completion Time](task-completion-time.md) (Task efficiency)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded beyond its correspondence with SUS.

## 6. Links to business objectives
**Improved usability:** positive, correlational. **Sustained use:** positive, theoretical.

## 7. Sources
- [finstad2010]: UMUX.
- [lewis2013]: UMUX-LITE.
- [lewis2018]: the SUS family and short alternatives.

## Open questions and review notes
- None yet.
