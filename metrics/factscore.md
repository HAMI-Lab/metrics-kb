---
id: factscore
title: FActScore
aliases: [atomic factual precision, factual precision]
page_type: metric
template_version: "0.2"
fields: [nlp, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the facts a generated text states, the share that a trusted knowledge source supports."
  measures: [factuality]
  subject: [system-component]
  aspect: [effectiveness, trust]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [test-collection]
  route: [external-judgment, reference-comparison]
  collection_mode: [offline]
  data_source: [model-judge, reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: high, note: "Depends on how text is split into facts, on the knowledge source's coverage, and on an automatic judge."}

cost:
  level: medium
  requires: ["a knowledge source", "a model judge or human annotators"]
  automatable: true

related:
  - {metric: answer-faithfulness, kind: conceptual, note: "Checks support by the given sources, not by trusted knowledge."}
  - {metric: rouge, kind: conceptual, note: "Overlap with a reference; does not check truth."}
  - {metric: precision-test-collection, kind: operational, note: "The same precision computation applied to atomic facts."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "False content erodes trust."}
  improved-usability: {direction: positive, evidence: theoretical, note: "False content harms users' tasks."}

sources: [min2023, chang2024]
---

# FActScore

> Split a generated text into atomic facts and count the share supported by a knowledge source.

## 1. What is measured

### 1.1 Definition
A long generated text, such as a biography, is broken into short atomic facts. Each fact is checked against a knowledge source, such as Wikipedia. The score is the share of facts that are supported [min2023].

### 1.2 Construct: property of subject in context
The property is factuality: whether stated facts are true. The subject is a text generator. The context is a set of prompts and a knowledge source.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Generation performance: factuality](../constructs/factuality.md) (under Component characteristics → Component performance → Generation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not reward completeness (a short text with few facts can score high). It does not check whether facts are relevant to the question.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for support by the chosen source; **proxy** for truth, because the source can be incomplete or wrong. Results depend on how facts are split and on the judge that checks them [min2023].

### 2.2 Reliability
Automatic judges are reported to agree reasonably with human annotation in the original study (check against [min2023]); re-check when changing the judge model or the source.

### 2.3 Data collection and measurement error
Generate texts for a prompt set, split them into facts (by people or a model), and check each fact against the source.

### 2.4 Computation
- FActScore = supported atomic facts ÷ all atomic facts, averaged over texts [min2023].
- Some versions penalize very short responses; report which.

### 2.5 Unit and scale
0 to 1.

## 3. Why it is measured

### 3.1 Use cases
- An LLM team compares two models on factual precision of biographies before choosing one for a people-search feature [min2023].
- A health chatbot team checks factual precision of answers against a curated medical knowledge base.

### 3.2 Purposes
Comparing generators on hallucination; tracking factuality across model versions [chang2024].

### 3.3 Assumptions
The knowledge source is correct and covers the facts; facts can be checked one at a time.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
LLM evaluation teams.

### 4.2 Consumers and decisions informed
Teams choosing models for factual tasks.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Models can score well by saying less. Swapping the judge changes the scores.

## 5. Related metrics

### 5.1 Operationally related metrics
The same computation as [precision](precision-test-collection.md), applied to atomic facts.

### 5.2 Conceptually related metrics
[Answer Faithfulness](answer-faithfulness.md) is the counterpart for support by given context. [ROUGE](rouge.md) does not check truth.

<!-- generated:neighbours:start -->
- Sibling construct: [Answer Faithfulness](answer-faithfulness.md) (Generation performance: groundedness), [F1 Score](f1-score.md) (Generation performance: similarity to reference), [ROUGE](rouge.md) (Generation performance: similarity to reference)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical.

## 7. Sources
- [min2023]: FActScore.
- [chang2024]: factuality and hallucination evaluation.

## Open questions and review notes
- None yet.
