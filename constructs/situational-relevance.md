---
id: situational-relevance
title: "Task effectiveness: situational relevance"
aliases: [user relevance, task relevance, usefulness of results]
page_type: construct
template_version: "0.1"
fields: [information-retrieval, hci]

broader: [task-effectiveness]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [saracevic2007, barry1998, hersh2000, turpin2006]
---

# Task effectiveness: situational relevance

> Whether what the system returned helps this user with the task they are actually doing.

## 1. Definition
The relation between a retrieved item and the situation of the person who asked for it: their task, what they already know, and what they need now [saracevic2007]. An item has more situational relevance when the user can use it to move their task forward. Users judge it by criteria beyond topic, such as how new, current, reliable or understandable an item is [barry1998].

## 2. Boundaries
It differs from [topical relevance](topical-relevance.md), which asks whether an item is about the query topic as an assessor reads it. Topical relevance is a property of a component's output on fixed queries. Situational relevance needs a user doing their own task, so it sits under [task effectiveness](task-effectiveness.md). The two are linked only empirically: components that score higher on topical relevance do not reliably give users better results for their tasks [hersh2000; turpin2006].

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
The test-collection forms of precision and recall measure topical relevance. Their task-level counterparts, computed on the user's own queries and judgments, measure this construct.
<!-- generated:metrics:start -->
- [Precision (user on task)](../metrics/precision-user-task.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: results that help users with their own tasks make the system worth returning to ([Sustained Use](../objectives/sustained-use.md)) and are part of effectiveness in [Improved Usability](../objectives/improved-usability.md).

## 6. How it is identified
Information science frameworks of relevance [saracevic2007] and studies of the criteria users apply when judging relevance [barry1998].

## 7. Sources
- [saracevic2007]: manifestations of relevance, including situational relevance.
- [barry1998]: criteria users apply beyond topic.
- [hersh2000], [turpin2006]: the gap between batch and user outcomes.

## Open questions and review notes
- [Relevance](relevance.md) lists situational relevance as one of its manifestations, but on the component side. Here it is placed under task effectiveness because it needs a user on a task. Keep both readings, or narrow the relevance page to the component-side manifestations?
