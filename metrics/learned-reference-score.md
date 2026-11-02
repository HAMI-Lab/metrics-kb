---
id: learned-reference-score
title: Learned Reference-Based Score
aliases: [BERTScore, COMET, BLEURT, model-based reference metric, learned metric, embedding-based similarity]
page_type: metric
template_version: "0.3"
fields: [nlp, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well generated text conveys the content of a reference, as judged by a model trained to compare texts or to predict human ratings."
  measures: [content-adequacy]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [rating-score]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [benchmark]
  route: [reference-comparison, external-judgment]
  collection_mode: [offline]
  data_source: [reference-answers, model-judge]
  unit: "score on the scorer's scale"
  range: "set by the scorer (see 2.6)"
  better: higher
  validity_concern: {level: moderate, note: "Closer to human judgments of adequacy than n-gram overlap, but inherits the scoring model's training data and blind spots."}
  instruments:
    - {name: "BERTScore", kind: scorer, sources: [zhang2020], scale: "precision, recall and F1 of embedding matches; often rescaled", note: "Matches tokens of output and reference by contextual embeddings."}
    - {name: "COMET", kind: scorer, sources: [rei2020], scale: "model-predicted quality score", note: "Trained on human judgments of translation; uses source, output and reference."}
    - {name: "BLEURT", kind: scorer, sources: [sellam2020], scale: "model-predicted rating", note: "A pretrained model fine-tuned on human ratings of generated text."}

cost:
  level: low
  requires: ["reference texts", "the scoring model"]
  automatable: true

related:
  - {metric: rouge, kind: conceptual, note: "Same construct by n-gram overlap; cheaper and more transparent, further from human judgments."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}
  improved-usability: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}

sources: [zhang2020, rei2020, sellam2020, chang2024]
---

# Learned Reference-Based Score

> A score for generated text from a model that compares it with a reference, such as BERTScore, COMET or BLEURT.

## 1. What is measured

### 1.1 Definition
A scoring model compares a generated text with one or more reference texts, and sometimes the source, and outputs a score. Some scorers match words by meaning rather than spelling (BERTScore [zhang2020]); others are trained to predict human quality ratings (COMET [rei2020], BLEURT [sellam2020]).

### 1.2 Construct: property of subject in context
The property is content adequacy: whether the text conveys what the reference conveys. The subject is a generating component. The context is a benchmark with references.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Generation performance: content adequacy](../constructs/content-adequacy.md) (under Component characteristics → Component performance → Generation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Factual correctness beyond the reference, faithfulness to a source, or whether users find the text useful.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy** for content adequacy. Learned scorers are built to agree with human judgments better than n-gram overlap, which is their reason for existing (check against [zhang2020; rei2020; sellam2020]). They inherit the scorer's training data: Hypothesis: they are less reliable on domains, languages or text types far from that data. Why it could be true: a model's judgments generalize poorly outside its training distribution (further reference needed).

**Using a proxy with a known gap.** These scores can compare generators on the same references with the same scorer version. They cannot certify that outputs are correct or helpful. Check a sample with people, and do not mix scorer versions.

### 2.2 Reliability
Deterministic for a fixed scorer version, references and preprocessing. Scores change with the scorer model and version.

### 2.3 Data collection and measurement error
Generate outputs on the benchmark; run the scorer against the references. Record the scorer, version and any rescaling.

### 2.4 Computation
Per-output score from the scorer, averaged over the benchmark. Each scorer's rule is in 2.6.

### 2.5 Unit and scale
Set by the scorer; not comparable across scorers.

### 2.6 Instruments
**Scorers**
- **BERTScore** [zhang2020]: matches each token of the output to the most similar token of the reference by contextual embeddings and reports precision, recall and F1; often rescaled against a baseline to spread scores out.
- **COMET** [rei2020]: a neural model trained on human judgments of translation quality; reads the source, output and reference.
- **BLEURT** [sellam2020]: a pretrained model fine-tuned on human ratings of generated text.

Content: any benchmark with reference texts, such as the summarization sets under [ROUGE](rouge.md).

## 3. Why it is measured

### 3.1 Use cases
- A translation team reports COMET next to BLEU when comparing two models.
- A summarization study reports BERTScore next to ROUGE to show gains are not only in wording.

### 3.2 Purposes
Comparing generators on adequacy where references exist, closer to human judgments than overlap counts [chang2024].

### 3.3 Assumptions
The references are good; the scorer's training matches the texts being scored.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
NLP researchers and ML engineers.

### 4.2 Consumers and decisions informed
Teams choosing generation models.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing a generator directly against the scorer can exploit its blind spots.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[ROUGE](rouge.md) measures the same construct by n-gram overlap.

<!-- generated:neighbours:start -->
- Same construct: [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](rouge.md) (Generation performance: content adequacy)
- Sibling construct: [Factual Precision in Atomicity Score (FActScore)](factscore.md) (Generation performance: factuality), [pass@k](pass-at-k.md) (Generation performance: functional correctness), [Answer Faithfulness](answer-faithfulness.md) (Generation performance: groundedness), [Instruction-Following Accuracy](instruction-following-accuracy.md) (Generation performance: instruction following)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded beyond the authors' correlations with human judgments.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [zhang2020]: BERTScore.
- [rei2020]: COMET.
- [sellam2020]: BLEURT.
- [chang2024]: evaluation of generated text.

## Open questions and review notes
- One page for all learned reference-based scorers, since they share construct, method and route and differ in the scorer (D30). Split if one of them needs its own caveats.
