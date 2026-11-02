---
id: answer-faithfulness
title: Answer Faithfulness
aliases: [faithfulness, RAGAS faithfulness, groundedness score, context faithfulness]
page_type: metric
template_version: "0.3"
fields: [nlp, llm-evaluation, information-retrieval]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the claims in a generated answer, the share that the context given to the model supports."
  measures: [groundedness]
  subject: [system-component]
  aspect: [effectiveness, trust]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [benchmark]
  route: [external-judgment]
  collection_mode: [offline]
  data_source: [model-judge]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: high, note: "Usually judged by an LLM; checks support by the context, not truth, and the judge goes unchecked unless sampled."}

cost:
  level: low
  requires: ["question-context-answer triples", "a model judge"]
  automatable: true

related:
  - {metric: factscore, kind: conceptual, note: "Checks truth against a knowledge source instead of support by the given context."}
  - {metric: precision-benchmark, kind: operational, note: "Precision applied to the claims of one answer."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Grounded answers are expected to keep trust."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Answers users can trace to sources support checking."}

sources: [es2023, ragas2026, li2024]
---

# Answer Faithfulness

> Split a RAG answer into claims and count the share that the retrieved context supports.

## 1. What is measured

### 1.1 Definition
In retrieval-augmented generation (RAG), the answer is split into claims, and each claim is checked against the passages that were retrieved for the question. The score is the share of claims the passages support [es2023]. RAGAS is the best-known implementation; similar checks exist in other tools [ragas2026].

### 1.2 Construct: property of subject in context
The property is groundedness: whether the answer stays within what its sources say. The subject is the generator in a RAG pipeline. The context is a set of questions with retrieved passages.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Generation performance: groundedness](../constructs/groundedness.md) (under Component characteristics → Component performance → Generation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not check whether the passages are true or relevant, or whether the answer is complete or useful.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for support by the given context, as the judge reads it; **proxy** for trustworthy answers. An LLM judge does the splitting and checking, so the number inherits the judge's errors; sample and compare with people before relying on it [li2024].

**Using a proxy with a known gap.** A high score means the answer did not go beyond its sources, not that it is true or useful: a faithful answer can repeat a wrong passage or miss the point of the question. Use it to catch answers that invent content, alongside metrics for retrieval quality and correctness, not as a quality score on its own.

### 2.2 Reliability
Depends on the judge model and prompt; changing either changes scores. The original RAGAS paper compared automatic scores with human judgments on a small set (check against [es2023]).

### 2.3 Data collection and measurement error
Log or generate question-context-answer triples; run the judge over them.

### 2.4 Computation
- Faithfulness = claims supported by the context ÷ all claims in the answer [es2023].
- Averaged over answers; report the judge model and prompt version.

### 2.5 Unit and scale
0 to 1.

### 2.6 Instruments
None listed.

## 3. Why it is measured

### 3.1 Use cases
- A company's internal policy assistant is checked nightly: do its answers stick to the retrieved policy documents?
- A legal research tool compares two prompts by how often answers make claims the cited passages do not support.

### 3.2 Purposes
Detecting hallucination relative to sources in RAG systems; comparing prompts and models [es2023].

### 3.3 Assumptions
The judge can tell support from non-support; claims can be checked independently.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
LLM application engineers.

### 4.2 Consumers and decisions informed
Teams shipping RAG products.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Answers that hedge or say little score well. The judge can be gamed by phrasing that mirrors the context.

## 5. Related metrics

### 5.1 Operationally related metrics
The same computation as [precision](precision-benchmark.md), applied to an answer's claims.

### 5.2 Conceptually related metrics
[FActScore](factscore.md) checks truth instead of support by context.

<!-- generated:neighbours:start -->
- Sibling construct: [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](rouge.md) (Generation performance: content adequacy), [Factual Precision in Atomicity Score (FActScore)](factscore.md) (Generation performance: factuality), [pass@k](pass-at-k.md) (Generation performance: functional correctness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Improved usability** and **sustained use:** positive, theoretical.

## 7. Sources
- [es2023]: RAGAS.
- [ragas2026]: metric documentation.
- [li2024]: reliability of LLM judges.

## Open questions and review notes
- The title avoids the tool name (D19); is "Answer Faithfulness" clear enough, or should the alias RAGAS be in the title?
