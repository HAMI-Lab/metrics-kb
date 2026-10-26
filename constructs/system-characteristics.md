---
id: system-characteristics
title: System characteristics
aliases: [system properties]
page_type: construct
template_version: "0.1"
fields: [information-retrieval, machine-learning, software-engineering]

broader: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [hersh2000, turpin2006]
---

# System characteristics

> Properties of the system that can be stated without a particular user doing a particular task.

## 1. Definition
Properties of a system or its components, such as the quality of its outputs, its speed, and its reliability, measured with test data, benchmarks, or telemetry.

## 2. Boundaries
Unlike [task characteristics](task-characteristics.md), they do not need a user pursuing a goal. Whether a better system characteristic yields better task characteristics is an empirical question: in IR, large gains in batch effectiveness did not always improve users' task performance [hersh2000; turpin2006].

## 3. Narrower constructs
Groups of system properties. Several are indirect causes of task characteristics, recorded as empirical links on metric pages rather than as DAG edges.
<!-- generated:narrower:start -->
- [Output quality](output-quality.md)
- [Retrieval performance](retrieval-performance.md)
- [System reliability](system-reliability.md)
- [System responsiveness](responsiveness.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect: through task characteristics.

## 6. How it is identified
Top-level split decided by the team on 2026-10-26 (see `schema/DECISIONS.md`).

## 7. Sources
- [hersh2000]
- [turpin2006]

## Open questions and review notes
- Should there be an intermediate "system performance" construct grouping retrieval performance, output quality, responsiveness, and reliability?
