---
id: demographic-parity-difference
title: "Demographic Parity Difference (DPD)"
aliases: [DPD, statistical parity difference, disparate impact ratio, demographic parity ratio]
page_type: metric
template_version: "0.3"
fields: [machine-learning, fairness]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much the rate of favourable decisions differs between groups of people."
  measures: [fairness]
  subject: [system]
  aspect: [fairness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [controlled-comparison, benchmark, logs-telemetry]
  route: [difference-scoring]
  collection_mode: [offline, online]
  data_source: [reference-answers, interaction-logs]
  unit: "difference in proportions"
  range: "0-1 (absolute)"
  better: lower
  validity_concern: {level: high, note: "Fairness has competing definitions; equal rates can be unfair when groups differ in relevant ways."}

cost:
  level: low
  requires: ["decisions or predictions", "group membership for each case"]
  automatable: true

related:
  - {metric: accuracy, kind: conceptual, note: "Equalized odds compares error rates instead of decision rates."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: ""}
  improved-usability: {direction: unknown, evidence: none, note: ""}

sources: [fairlearn2024, hardt2016, barocas2021, chang2024, jacobs2021]
---

# Demographic Parity Difference (DPD)

> The largest gap between groups in the share of cases that get the favourable decision.

## 1. What is measured

### 1.1 Definition
Demographic Parity Difference (DPD) compares groups defined by a sensitive attribute, such as gender or age, on one quantity: the share of cases that receive the favourable outcome (selected, approved, recommended). DPD is the largest difference between any two groups [fairlearn2024; chang2024].

### 1.2 Construct: property of subject in context
The property is fairness under the demographic-parity criterion: equal selection rates. The subject is the system making decisions. The context is a population with known group membership.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Output quality: fairness](../constructs/fairness.md) (under System characteristics → System performance → Output quality)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not check whether the decisions are correct within each group; equal rates can hide very different error rates. Other criteria, such as equal true-positive rates (equal opportunity), can conflict with it [hardt2016].

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the parity criterion; **proxy** for fairness, which is a contested construct with several incompatible definitions [jacobs2021; hardt2016].

**Using a proxy with a known gap.** DPD can show that selection rates differ, which may call for a closer look. It cannot show that a system is fair or unfair on its own: when groups differ in qualifications that legitimately matter, equal rates may be the wrong target. State the criterion and why it fits the decision; report error-rate criteria such as equalized odds next to it; and do not read a ratio below a legal rule of thumb as a legal finding [fairlearn2024].

### 2.2 Reliability
Small groups give unstable rates and gaps; report group sizes and intervals [barocas2021]. With many groups, the largest gap grows by chance.

### 2.3 Data collection and measurement error
Needs the decision and the group for each case, from a test set or from logged decisions. Group labels may be missing or self-reported, which adds error.

### 2.4 Computation
- Selection rate per group = favourable decisions ÷ cases in the group.
- DPD = max over groups − min over groups of the selection rate [fairlearn2024].
- Ratio variant (disparate impact ratio) = min ÷ max.

### 2.5 Unit and scale
Difference in proportions, 0 to 1 (0 = equal rates). The ratio variant runs from 0 to 1, with 1 = equal.

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A bank audits a loan-approval model by comparing approval rates across age groups before deployment.
- A job platform checks whether its candidate recommender shows candidates of different genders to recruiters at similar rates.
- A content moderation team compares how often posts in different dialects are removed.

### 3.2 Purposes
Fairness audits; documentation for regulators; comparing mitigation methods [barocas2021].

### 3.3 Assumptions
Equal selection rates are the right target for this decision; group labels are correct.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML fairness and compliance teams.

### 4.2 Consumers and decisions informed
Product owners, legal and compliance, regulators.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing parity alone can lower accuracy for everyone or move unfairness to another criterion. A good number can be presented as proof of fairness.

## 5. Related metrics

### 5.1 Operationally related metrics
The ratio variant is on this page. Equalized odds difference applies the same subgroup comparison to error rates [hardt2016]; not yet a page.

### 5.2 Conceptually related metrics
[Accuracy](accuracy.md) per group, compared across groups, gives a performance-disparity view.

<!-- generated:neighbours:start -->
- Sibling construct: [Attack Success Rate (ASR)](attack-success-rate.md) (Output quality: safety), [Toxicity Rate](toxicity-rate.md) (Output quality: safety)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: reducing DPD through post-processing tends to lower overall accuracy when base rates differ between groups. Why it could be true: equalizing selection rates then requires accepting more cases the model scores low in one group or rejecting high-scoring cases in another (further reference needed).

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown. The links run mainly through trust, reputation and regulation, not usability.

## 7. Sources
- [fairlearn2024]: definitions and the ratio variant.
- [hardt2016]: equal opportunity and conflicting criteria.
- [barocas2021]: disaggregated evaluation.
- [chang2024]: DPD in LLM evaluation.
- [jacobs2021]: fairness as a contested construct.

## Open questions and review notes
- Should equalized odds difference get its own page?
