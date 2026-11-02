---
id: task-efficiency
title: Task efficiency
aliases: [resource efficiency]
page_type: construct
template_version: "0.1"
fields: [hci]

broader: [task-performance, usability]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [iso9241-11, hornbaek2006]
---

# Task efficiency

> Resources spent (time, effort, waiting) relative to the outcome achieved.

## 1. Definition
The resources used in relation to the results achieved [iso9241-11]. Resources include the user's time, mental and physical effort, and time spent waiting for the system.

## 2. Boundaries
Efficiency is only meaningful at a given level of [task effectiveness](task-effectiveness.md): a quick but failed task is not efficient. Time is the most common resource measured, but not the only one [hornbaek2006].

## 3. Narrower constructs
The person's effort is split out as [mental workload](mental-workload.md). The system's speed ([system responsiveness](responsiveness.md)) is a system characteristic, not a narrower construct here; how much waiting adds to task time is an empirical link, recorded on metric pages.
<!-- generated:narrower:start -->
- [Mental workload](mental-workload.md)
<!-- generated:narrower:end -->

## 4. Metrics
Time-based metrics are cheap but ignore effort; pair them with a workload measure when effort matters.
<!-- generated:metrics:start -->
- [Task Completion Time](../metrics/task-completion-time.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Lower resources at equal outcome is positive for [Improved Usability](../objectives/improved-usability.md). For [Sustained Use](../objectives/sustained-use.md), the link is unclear: faster is not always more engaging.

## 6. How it is identified
Standard definition [iso9241-11].

## 7. Sources
- [iso9241-11]
- [hornbaek2006]

## Open questions and review notes
- None yet.
