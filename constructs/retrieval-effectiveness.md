---
id: retrieval-effectiveness
title: Retrieval effectiveness
aliases: [search effectiveness]
page_type: construct
template_version: "0.1"
fields: [information-retrieval]

broader: [retrieval-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [manning2008, saracevic2007]
---

# Retrieval effectiveness

> How well a retrieval system returns information that serves the user's need.

## 1. Definition
The degree to which a search or retrieval system returns information that meets the information need behind a query [manning2008].

## 2. Boundaries
It concerns the system's results, measured without a particular user pursuing a goal. Its sibling [retrieval efficiency](retrieval-efficiency.md) covers what returning them costs. User-side outcomes, such as finding an answer faster, belong under [task performance](task-performance.md).

## 3. Narrower constructs
[Relevance](relevance.md) is the central narrower construct; other candidates (coverage, diversity, novelty) are not yet added.
<!-- generated:narrower:start -->
- [Retrieval effectiveness: relevance](relevance.md)
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical links to both objectives through users finding what they need.

## 6. How it is identified
IR literature [manning2008; saracevic2007].

## 7. Sources
- [manning2008]
- [saracevic2007]

## Open questions and review notes
- Placed under retrieval performance (decided 2026-10-26), so it is a level in the DAG, not just a prefix on titles.
