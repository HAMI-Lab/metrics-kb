---
id: decision-accuracy-with-ai
title: Decision Accuracy with AI Assistance
aliases: [human-AI team accuracy, assisted decision accuracy, diagnostic accuracy with AI]
page_type: metric
template_version: "0.2"
fields: [human-ai-interaction, xai, healthcare]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How often people make the right decision when a system advises them."
  measures: [decision-correctness]
  subject: [user-system-team]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [task-study, controlled-comparison]
  route: [reference-comparison]
  collection_mode: [in-lab, field]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Depends on the ground truth and on how representative the cases and the advice quality are."}

cost:
  level: high
  requires: ["participants with the right expertise", "cases with known outcomes"]
  automatable: false

related:
  - {metric: accuracy, kind: conceptual, note: "The AI's own accuracy on the same cases; the team can be better or worse."}
  - {metric: over-reliance-rate, kind: conceptual, note: "Explains team errors that follow wrong advice."}
  - {metric: under-reliance-rate, kind: conceptual, note: "Explains team errors that ignore right advice."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Decision support is kept if it improves decisions."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Effectiveness of the person and system together."}

sources: [bansal2021, gambetti2025, schemmer2023]
---

# Decision Accuracy with AI Assistance

> The share of decisions people get right with the system's advice, compared with the right answers.

## 1. What is measured

### 1.1 Definition
Decision Accuracy with AI Assistance is the share of cases in which a person who sees a system's advice, such as a diagnosis suggestion or a risk score, makes the correct final decision [bansal2021]. It is usually compared with the person deciding alone and the AI alone.

### 1.2 Construct: property of subject in context
The property is decision correctness of the person and system together. The subject is the human-AI team. The context is a set of cases with known right answers [gambetti2025].

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Task effectiveness: decision correctness](../constructs/decision-correctness.md) (under Task characteristics → Task performance → Task effectiveness; Task characteristics → Usability → Task effectiveness)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It is not the AI's accuracy. It does not show why the team erred: following wrong advice and ignoring right advice need the reliance metrics.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the cases and ground truth used. The result depends on how good the advice is in the study; teams can look better or worse than in practice if the AI's accuracy in the study differs from deployment.

### 2.2 Reliability
Expert participants are few, so samples are small; cases vary in difficulty, so balance them across conditions.

### 2.3 Data collection and measurement error
In a task study, participants decide each case with advice (and often without, as a baseline). Decisions are compared with confirmed outcomes. See [controlled comparison](../strategies/controlled-comparison.md) for the with/without design.

### 2.4 Computation
- Accuracy = correct decisions ÷ decisions.
- Complementarity: team accuracy minus the better of human-alone and AI-alone accuracy [bansal2021].
- Sensitivity and specificity instead of accuracy when the decision is a diagnosis.

### 2.5 Unit and scale
0 to 1.

## 3. Why it is measured

### 3.1 Use cases
- A reader study: radiologists read fracture X-rays with and without a model's highlighted regions, and their diagnoses are scored against confirmed outcomes [gambetti2025].
- A loan-review team is tested on past applications with known repayment outcomes, with and without a risk score.

### 3.2 Purposes
Deciding whether decision support helps; comparing explanation designs [bansal2021].

### 3.3 Assumptions
The ground truth is right; study cases represent the real case mix.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
HCI and clinical researchers.

### 4.2 Consumers and decisions informed
Clinical leads, product owners, regulators.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Reporting the AI's accuracy as if it were the team's. Studies with unusually accurate AI overstate the benefit.

## 5. Related metrics

### 5.1 Operationally related metrics
Complementarity (team minus best single) is a variant on this page.

### 5.2 Conceptually related metrics
[Accuracy](accuracy.md) of the AI alone is the component counterpart. [Over-reliance Rate](over-reliance-rate.md) and [Under-reliance Rate](under-reliance-rate.md) explain where team errors come from.

<!-- generated:neighbours:start -->
- Broader construct: [Task Success Rate (user on task)](task-success-rate-user.md) (Task effectiveness)
- Sibling construct: [Precision (user on task)](precision-user-task.md) (Task effectiveness: situational relevance)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Teams with AI advice are often more accurate than people alone but not always more accurate than the AI alone [bansal2021] (check against the paper).

## 6. Links to business objectives
**Sustained use** and **improved usability:** positive, theoretical.

## 7. Sources
- [bansal2021]: complementary team performance.
- [gambetti2025]: clinical decision-support studies.
- [schemmer2023]: reliance and team performance.

## Open questions and review notes
- None yet.
