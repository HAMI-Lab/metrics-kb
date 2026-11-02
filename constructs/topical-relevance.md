---
id: topical-relevance
title: "Retrieval effectiveness: topical relevance"
aliases: [topicality, aboutness]
page_type: construct
template_version: "0.1"
fields: [information-retrieval]

broader: [relevance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [saracevic2007, manning2008]
---

# Retrieval effectiveness: topical relevance

> Whether a retrieved item is about the topic of the query.

## 1. Definition
The match between what an item is about and the topic of the query [saracevic2007]. It is what most test-collection relevance judgments record [manning2008].

## 2. Boundaries
It ignores whether the item is new to the user, current, credible, or usable for the task. Those are sibling aspects of [relevance](relevance.md).

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Precision and recall are its classic metrics. They capture two different properties, exactness (no false hits) and completeness (no misses), which could become narrower constructs.
<!-- generated:metrics:start -->
- [F1 Score](../metrics/f1-score.md)
- [Mean Average Precision (MAP)](../metrics/mean-average-precision.md)
- [Mean Reciprocal Rank (MRR)](../metrics/reciprocal-rank.md)
- [Precision (benchmark)](../metrics/precision-benchmark.md)
- [Recall (benchmark)](../metrics/recall-benchmark.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
See the metric pages: links to user outcomes are weaker than often assumed.

## 6. How it is identified
IR test-collection practice [manning2008].

## 7. Sources
- [saracevic2007]
- [manning2008]

## Open questions and review notes
- Split into exactness and completeness as narrower constructs? Proposed, not decided.
