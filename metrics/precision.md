---
id: precision
title: Precision
aliases: [positive predictive value, "precision@k", P@k]
page_type: metric
template_version: "0.1"
fields: [information-retrieval, recommender-systems, machine-learning, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the items a system returns or labels as positive, the share that are actually relevant or correct."
  subject: [system-component, system]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [offline, online]
  data_source: [relevance-judgments, reference-answers, model-judge]
  unit: "proportion"
  range: "0-1"
  better: higher

cost:
  level: medium
  requires: ["relevance judgments or gold labels (costly to create once, cheap to reuse)"]
  automatable: true

related:
  - {metric: task-completion-time, relation: correlated, note: "Better ranking is expected to shorten search tasks; user studies show the link is weaker than assumed."}
  - {metric: system-usability-scale, relation: correlated, note: "Output quality is one input to perceived usability; not measured directly."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Relevant results are assumed to make the system worth returning to; long causal chain."}
  improved-usability: {direction: positive, evidence: correlational, note: "Batch precision gains do not always translate into better user task performance."}

sources: [vanrijsbergen1979, manning2008, voorhees2000, hersh2000, turpin2006, kelly2009, S24, S34]
---

# Precision

> The fraction of what the system returned (or flagged as positive) that was actually relevant or correct.

## 1. What is measured

### 1.1 Definition
Precision = relevant items returned ÷ all items returned. In classification it is true positives ÷ (true positives + false positives). In ranked retrieval it is usually computed on the top *k* results (precision@k) [manning2008].

### 1.2 Construct: property of subject in context
The property is **output correctness** (the absence of false positives). The subject is usually a **system component** such as a retriever, ranker, or classifier, or the whole system when outputs are judged end to end. The context is a **task** defined by a test collection: a set of queries or inputs with judgments of what counts as relevant.

### 1.3 What it does not measure
It ignores what was missed (that is recall, which has no page yet). It says nothing about how results are presented, how long the user took, or whether the user was satisfied. For LLM outputs, "precision" is sometimes used loosely for the share of correct claims; make sure the counting unit is stated.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for "how many returned items meet the relevance criterion." **Proxy** for what users actually care about: whether the results help them finish their task. User studies found that systems with higher batch precision did not always lead to better user performance [hersh2000; turpin2006]. Hence `measure_type: mixed`.

### 2.2 Reliability
Depends on the judgments. Different assessors disagree about relevance substantially, although system *rankings* by precision tend to be stable across assessors [voorhees2000]. Precision@k with small *k* and few queries has high variance.

### 2.3 Data collection and measurement error
Offline: run the system on a test collection with existing judgments. Online: infer relevance from clicks or ratings (biased by position and presentation). LLM-as-judge labeling is cheaper but adds the judge's own errors [S34]. Unjudged items in pooled collections are usually counted as not relevant, which can penalize new systems.

### 2.4 Computation
- Set-based: |relevant ∩ retrieved| ÷ |retrieved|.
- Precision@k: the same over the top *k* results.
- Averaged over queries: macro (mean of per-query precision) or micro (pooled counts); report which.
- Combined with recall in F1 or F-beta [vanrijsbergen1979], or across ranks in average precision.

### 2.5 Unit and scale
A proportion from 0 to 1 (ratio scale). Only comparable across systems on the same collection and judgment rules.

## 3. Why it is measured

### 3.1 Purposes
Comparing retrieval or classification components during development; regression testing; reporting benchmark results; evaluating RAG retrievers and LLM classifiers [S24; S34].

### 3.2 Assumptions
Implicit user model: the user looks at the top *k* results, all positions equally, and every irrelevant item costs the same. Relevance is treated as binary and independent of other results (no credit for novelty or penalty for duplicates). The query set represents real use.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Engineers and IR/ML researchers. Building judgments is the costly step; after that, it is essentially free to recompute, which is why it is so popular.

### 4.2 Consumers and decisions informed
Engineers choosing models and settings; researchers comparing methods; product teams tracking quality over releases.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Precision alone is easy to game by returning fewer, safer results (precision rises, recall falls). Overfitting to a fixed test collection. Treating a precision gain as a user-experience gain without checking with users [turpin2006].

## 5. Related metrics

### 5.1 Static relationships
Trade-off: recall. Summaries of both: F1, average precision, nDCG. Complementary user-side measures: [Task Completion Time](task-completion-time.md), task success, [SUS](system-usability-scale.md). Precision is cheap once judgments exist; user measures are costlier but closer to the construct that matters.

### 5.2 Dynamic relationships
Raising precision by being more selective usually lowers recall. Links from precision to user outcomes are weaker than often assumed: in controlled studies, large precision differences produced small or no differences in user task success [hersh2000; turpin2006].

## 6. Links to business objectives
**Improved usability:** positive, correlational, and weaker than commonly assumed (see 5.2).

**Sustained use:** positive, theoretical: relevant results are assumed to make the system worth returning to. No direct evidence recorded here.

## 7. Sources
- [vanrijsbergen1979], [manning2008]: definitions and variants.
- [voorhees2000]: assessor disagreement and stability.
- [hersh2000], [turpin2006], [kelly2009]: relation to user performance.
- [S24], [S34]: use in LLM and RAG evaluation.

## Open questions and review notes
- Create the Recall page and link it from 1.3 and 5.1.
- Should precision for LLM claim-level correctness be its own page?
