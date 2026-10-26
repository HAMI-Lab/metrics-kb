---
id: interface-performance
title: Interface performance
aliases: [UI correctness, front-end performance]
page_type: construct
template_version: "0.1"
fields: [hci, software-engineering]

broader: [component-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Interface performance

> How well the user interface component does its own job: showing the right thing, at the right time, and capturing input correctly.

## 1. Definition
The correctness and speed of the interface as a component: rendering data faithfully, keeping displayed state in sync with stored state, and recording user input as intended.

## 2. Boundaries
This is the interface measured on its own (often with scripted tests). Whether people can use it well is [usability](usability.md), a task characteristic. End-to-end speed as users experience it is [system responsiveness](responsiveness.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Annotation tool: temporal alignment](temporal-alignment.md)
<!-- generated:narrower:end -->

## 4. Metrics
Metrics attach to narrower constructs.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect: interface faults show up as workarounds and lost trust.

## 6. How it is identified
Added on 2026-10-26: the interface is a component, like retrieval and classification.

## 7. Sources
- None yet.

## Open questions and review notes
- "Performance" may suggest speed only; is "interface correctness" a better name?
- Add rendering speed (frame rate, time to interactive) as a narrower construct?
