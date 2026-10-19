---
id: recall
title: Recall
aliases: [sensitivity, true positive rate, hit rate, "recall@k", R@k]
page_type: metric
template_version: "0.1"
fields: [information-retrieval, recommender-systems, machine-learning, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of all the items that are actually relevant or correct, the share that the system returns or labels as positive."
  subject: [system-component, system]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [offline]
  data_source: [relevance-judgments, reference-answers, model-judge]
  unit: "proportion"
  range: "0-1"
  better: higher

cost:
  level: medium
  requires: ["relevance judgments that cover all relevant items, not only the returned ones (costlier than for precision)"]
  automatable: true

related:
  - {metric: precision, relation: trade-off, note: "Returning more items usually raises recall and lowers precision."}
  - {metric: task-completion-time, relation: correlated, note: "In recall-oriented tasks, finding more of the relevant items usually takes users longer; not quantified here."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Matters mainly where users need to find everything (e.g. systematic reviews); users rarely notice what is missing."}
  improved-usability: {direction: positive, evidence: correlational, note: "Batch recall gains do not always translate into better user task performance."}

sources: [vanrijsbergen1979, manning2008, voorhees2000, hersh2000, kelly2009, schoolofai2025, es2023]
---

# Recall

> The fraction of all relevant or correct items that the system actually found.

## 1. What is measured

### 1.1 Definition
Recall = relevant items returned ÷ all relevant items. In classification it is true positives ÷ (true positives + false negatives). In ranked retrieval it is often computed on the top *k* results (recall@k) [manning2008].

### 1.2 Construct: property of subject in context
The property is **output completeness** (the absence of misses, or false negatives). The subject is usually a **system component** such as a retriever, ranker, or classifier, or the whole system when outputs are judged end to end. The context is a **task** defined by a test collection: a set of queries or inputs with judgments of what counts as relevant.

### 1.3 What it does not measure
It ignores how many irrelevant items were returned along with the relevant ones (that is [Precision](precision.md)). A system that returns everything has perfect recall. It says nothing about ranking order within the returned set, how results are presented, how long the user took, or whether the user was satisfied.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for "what share of the known relevant items were returned." **Proxy** for what users care about: whether they found the information they needed. Many everyday searches need only one good answer, so recall matters little there; it matters most in recall-oriented tasks such as legal discovery, systematic literature reviews, and medical screening. User studies found that batch measures did not always predict user performance [hersh2000] (check against the paper for recall specifically). Hence `measure_type: mixed`.

### 2.2 Reliability
Depends on the judgments. Different assessors disagree about relevance, although system rankings tend to be stable across assessors [voorhees2000]. Recall is less stable than precision when relevant items are few: with three relevant items per query, missing one moves recall by a third.

### 2.3 Data collection and measurement error
Recall needs to know **all** relevant items, which is rarely possible in a large collection. Test collections usually judge only a pool of items returned by several systems, so recall is measured against the pool, not the true total [manning2008]. Relevant items that no pooled system found are invisible, so recall tends to be overestimated. LLM-as-judge labeling is cheaper but adds the judge's own errors [es2023]. Recall is rarely measured online, because live logs show what users clicked, not what they never saw.

### 2.4 Computation
- Set-based: |relevant ∩ retrieved| ÷ |relevant|.
- Recall@k: the same over the top *k* results.
- Averaged over queries: macro (mean of per-query recall) or micro (pooled counts); report which.
- Combined with precision in F1 or F-beta [vanrijsbergen1979], or plotted against precision in a precision-recall curve.
- Undefined when a query has no relevant items (0 ÷ 0); state how such queries are handled.

### 2.5 Unit and scale
A proportion from 0 to 1 (ratio scale). Only comparable across systems on the same collection, judgment rules, and *k*. Recall@k is capped by *k*: if a query has 50 relevant items, recall@10 cannot exceed 0.2.

## 3. Why it is measured

### 3.1 Use cases
- A law firm's e-discovery review checks the recall of its predictive-coding tool against a random sample of documents the tool did *not* flag, since a missed responsive document can have legal consequences.
- A hospital's radiology team reports the recall (sensitivity) of a cancer-screening model to an internal review board before letting it flag cases for a second read.
- A team doing a systematic literature review checks how many of a hand-curated set of known-relevant papers their ML-assisted screening tool actually surfaced.
- A RAG-based product FAQ assistant is evaluated for context recall: whether the retriever pulled in the passages actually needed to answer each test question, before the team ships it.

### 3.2 Purposes
Comparing retrieval or classification components during development, especially where misses are costly; checking that a retriever surfaces enough material for a later step (for example, the context given to an LLM in retrieval-augmented generation [es2023]); reporting benchmark results [schoolofai2025].

### 3.3 Assumptions
Implicit user model: the user wants all relevant items and will look through everything returned, so a missed item is a loss and an extra irrelevant item is not. Relevance is treated as binary and independent of other results (duplicates count as extra hits). The set of relevant items is assumed to be known, which pooling only approximates. The query set represents real use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Engineers and IR/ML researchers. Judgments are the costly step, and more so than for precision: the judges must look beyond the returned items to find what was missed. Once judgments exist, recall is free to recompute.

### 4.2 Consumers and decisions informed
Engineers choosing models, thresholds, and how many results to retrieve; researchers comparing methods; teams in recall-critical domains (legal, medical, research reviews) deciding whether a system is safe to rely on.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Recall alone is easy to game by returning more results (recall rises, precision falls); always report it with [Precision](precision.md). Pooled recall can look high simply because the pool missed the same items the system missed. Treating a recall gain as a user-experience gain without checking with users [hersh2000].

## 5. Related metrics

### 5.1 Static relationships
Trade-off: [Precision](precision.md). Summaries of both: F1, average precision, precision-recall curves. Complementary user-side measures: [Task Completion Time](task-completion-time.md), task success. Recall is cheap once judgments exist; user measures are costlier but closer to the construct that matters.

### 5.2 Dynamic relationships
Returning more results usually raises recall and lowers precision. Raising recall in a recall-oriented task usually gives users more to read, which can lengthen task time. Links from recall to user outcomes are weaker than often assumed [hersh2000].

## 6. Links to business objectives
**Improved usability:** positive, correlational, and limited to tasks where completeness matters.

**Sustained use:** positive, theoretical: in recall-oriented work, users who cannot trust the system to find everything are assumed to stop relying on it. No direct evidence recorded here.

## 7. Sources
- [vanrijsbergen1979], [manning2008]: definitions, variants, and pooling.
- [voorhees2000]: assessor disagreement and stability.
- [hersh2000], [kelly2009]: relation to user performance.
- [schoolofai2025], [es2023]: use in classical ML and RAG evaluation.

## Open questions and review notes
Tracked in GitHub Issues: [#2](https://github.com/HAMI-Lab/metrics-kb/issues/2) (sources for pooling bias and recall-oriented domains), [#3](https://github.com/HAMI-Lab/metrics-kb/issues/3) (confirm hersh2000 reports recall specifically), [#4](https://github.com/HAMI-Lab/metrics-kb/issues/4) (RAG "context recall" as its own page?).
