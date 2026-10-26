---
id: retrieval-efficiency
title: Retrieval efficiency
aliases: [search efficiency, retrieval cost]
page_type: construct
template_version: "0.1"
fields: [information-retrieval]

broader: [retrieval-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [manning2008]
---

# Retrieval efficiency

> The resources a retrieval system uses to answer queries.

## 1. Definition
How much time, compute, memory, and storage a retrieval system spends to answer queries, for example query latency, throughput, and index size [manning2008].

## 2. Boundaries
These are the system's resources, not the user's ([task efficiency](task-efficiency.md)). [System responsiveness](responsiveness.md) is the user-facing speed of any system; query latency is where the two meet.

## 3. Narrower constructs

<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Gap: no metric page yet. Candidates: query latency, queries per second, index size, cost per query.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Indirect: through responsiveness and operating cost.

## 6. How it is identified
Added on 2026-10-26 as the sibling of retrieval effectiveness.

## 7. Sources
- [manning2008]

## Open questions and review notes
- Should [Response Latency](../metrics/response-latency.md) also link to this construct, or should a separate query-latency metric be added?
