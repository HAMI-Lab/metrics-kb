---
id: output-quality
title: Output quality
aliases: [result quality]
page_type: construct
template_version: "0.1"
fields: [machine-learning, llm-evaluation, data-annotation]

broader: [system-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Output quality

> How good the system's end-to-end outputs are: final answers, reports, labels, recommendations as delivered.

## 1. Definition
The quality of what the system as a whole delivers, judged against what it should have been. Outputs of single components (a retriever's ranking, a classifier's labels) are component characteristics.

## 2. Boundaries
It judges outputs, not the user's outcome ([task effectiveness](task-effectiveness.md)) or the experience ([usability](usability.md)).

## 3. Narrower constructs
Narrower constructs are qualities of end-to-end output. Trustworthiness, safety and fairness so far; correctness, completeness and faithfulness of end-to-end outputs are candidates.
<!-- generated:narrower:start -->
- [Output quality: fairness](fairness.md)
- [Output quality: safety](safety.md)
- [Trustworthiness](trustworthiness.md)
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
- [Judge Rating (model judge)](../metrics/judge-rating.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical links to both objectives.

## 6. How it is identified
Added as a shared parent so that constructs like trustworthiness can be reused across fields.

## 7. Sources
- None yet.

## Open questions and review notes
- No metric measures end-to-end output quality yet; which metric should be added first?
