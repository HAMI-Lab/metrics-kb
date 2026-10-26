---
id: component-characteristics
title: Component characteristics
aliases: [module properties, system functionality]
page_type: construct
template_version: "0.1"
fields: [information-retrieval, machine-learning, hci, software-engineering]

broader: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [hersh2000, turpin2006]
---

# Component characteristics

> Properties of one component or functionality of a system, judged on its own.

## 1. Definition
Properties of a single component or functionality that a system is built from, such as a retriever, a classifier, a pre-annotation model, or the user interface, measured in isolation with test data or scripted tests.

## 2. Boundaries
A component does one part of the job; the [system](system-characteristics.md) is what the components do together, as delivered. Gains in a component do not automatically become gains in the system or in the task: in IR, large gains in batch retrieval effectiveness did not always improve users' task performance [hersh2000; turpin2006]. Errors also accumulate between components, which only system-level measurement shows.

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Component performance](component-performance.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs. Component metrics are usually the cheapest to compute and the furthest from what users experience.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect: through system and task characteristics.

## 6. How it is identified
Fourth top-level group, decided by the team on 2026-10-26. Matches the component level of evaluation in the metric-chat interview guide.

## 7. Sources
- [hersh2000]
- [turpin2006]

## Open questions and review notes
- Settled (2026-10-26): a model that both retrieves and generates is still a component, or several components if those capabilities can be evaluated separately, because it leaves rendering to the interface, workflow, and UX design.
