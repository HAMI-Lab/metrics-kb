---
id: machine-pre-annotation-quality
title: Machine pre-annotation quality
aliases: [model-suggestion quality]
page_type: construct
template_version: "0.1"
fields: [data-annotation, human-ai-interaction]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [parasuraman2010]
---

# Machine pre-annotation quality

> How close a model's proposed labels are to what a careful person would accept.

## 1. Definition
The quality of model-generated labels offered to a person as a starting point.

## 2. Boundaries
It is about the model's proposals, not the final labels, so it is a characteristic of a component (the pre-annotation model); the final labels are [annotation quality](annotation-quality.md), a task characteristic. When people accept proposals without checking, final labels inherit their errors [parasuraman2010].

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Human edits are a cheap but biased signal; comparison to a gold set is more valid.
<!-- generated:metrics:start -->
- [Pre-annotation Edit Rate](../metrics/pre-annotation-edit-rate.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Non-monotonic link to continued use of pre-annotation (see the metric page).

## 6. How it is identified
Added from the InfinityPool metric-chat interview (2026-10-19).

## 7. Sources
- [parasuraman2010]

## Open questions and review notes
- Component level only, not system level: confirmed by the team (2026-10-26).
