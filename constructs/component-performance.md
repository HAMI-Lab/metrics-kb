---
id: component-performance
title: Component performance
aliases: [module performance]
page_type: construct
template_version: "0.1"
fields: [information-retrieval, machine-learning, hci]

broader: [component-characteristics]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Component performance

> How well a single component does its own job.

## 1. Definition
The quality, speed, and correctness of one component's work, judged against what that component is supposed to do.

## 2. Boundaries
It mirrors [system performance](system-performance.md) and [task performance](task-performance.md) one level down.

## 3. Narrower constructs
One narrower construct per kind of component, typed by what the component takes in and puts out: classification (a label from a fixed set), closed answers (one correct answer per item), retrieval (items ranked from a collection), generation (open-ended content), tool use (a structured call) and explanation (an attribution over the input). What the test data probes, such as knowledge or reasoning, is not a type (D23).
<!-- generated:narrower:start -->
- [Classification performance](classification-performance.md)
- [Closed-answer performance](closed-answer-performance.md)
- [Explanation performance](explanation-performance.md)
- [Generation performance](generation-performance.md)
- [Grounding performance](grounding-performance.md)
- [Image generation performance](image-generation-performance.md)
- [Numeric prediction performance](numeric-prediction-performance.md)
- [Retrieval performance](retrieval-performance.md)
- [Tool-use performance](tool-use-performance.md)
- [Transcription performance](transcription-performance.md)
- [Visual attention prediction performance](visual-attention-prediction-performance.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect.

## 6. How it is identified
Added on 2026-10-26 to mirror the system and task sides.

## 7. Sources
- None yet.

## Open questions and review notes
- Generation was added on 2026-11-01. Recommendation is also a component (it can come from a backend without specifying how the front end renders it); its page is to be added later.
- The interface is also a component; interface constructs are to be added later.
