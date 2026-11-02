---
id: fairness
title: "Output quality: fairness"
aliases: [group fairness, bias]
page_type: construct
template_version: "0.1"
fields: [machine-learning, llm-evaluation]

broader: [output-quality]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [barocas2021, hardt2016, jacobs2021]
---

# Output quality: fairness

> Whether the system's outcomes or quality differ unjustly across groups of people.

## 1. Definition
The extent to which a system's decisions or output quality are similar across groups defined by sensitive attributes, under a chosen fairness criterion [hardt2016; barocas2021].

## 2. Boundaries
There are several fairness criteria, and they can conflict; each metric picks one. Fairness is itself a contested construct, which is a reason to state the criterion explicitly [jacobs2021].

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Group-difference metrics such as demographic parity difference compare one quantity across groups.
<!-- generated:metrics:start -->
- [Demographic Parity Difference (DPD)](../metrics/demographic-parity-difference.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: unfair systems lose trust and can cause legal and social harm.

## 6. How it is identified
Fair machine learning [hardt2016] and measurement theory [jacobs2021].

## 7. Sources
- [hardt2016]: equal opportunity.
- [barocas2021]: disaggregated evaluation.
- [jacobs2021]: fairness as a contested construct.

## Open questions and review notes
- Stereotyping in generated language (StereoSet, CrowS-Pairs) is a related but different construct; add it?
