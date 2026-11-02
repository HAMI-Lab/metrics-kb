---
id: rouge
title: "Recall-Oriented Understudy for Gisting Evaluation (ROUGE)"
aliases: [ROUGE, ROUGE-1, ROUGE-2, ROUGE-L]
page_type: metric
template_version: "0.3"
fields: [nlp, llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much of a reference text's wording a generated text reproduces."
  measures: [content-adequacy]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [benchmark]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: high, note: "Word overlap is a weak proxy for quality; correct paraphrases score low and fluent errors can score high."}
  instruments:
    - {name: "CNN/DailyMail", sources: [hermann2015], probes: "summarizing news articles in several sentences", scale: "ROUGE-1/2/L, 0-1", note: "News articles with bullet-point highlights used as reference summaries."}
    - {name: "XSum", sources: [narayan2018], probes: "summarizing news articles in one sentence", scale: "ROUGE-1/2/L, 0-1", note: "BBC articles with one-sentence summaries."}

cost:
  level: low
  requires: ["reference texts written by people"]
  automatable: true

related:
  - {metric: f1-score, kind: conceptual, note: "Token-overlap F1 also counts shared words with a reference."}
  - {metric: factscore, kind: conceptual, note: "Checks whether claims are true instead of whether words match."}
  - {metric: answer-faithfulness, kind: conceptual, note: "Checks support by sources instead of overlap with a reference."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}
  improved-usability: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}

sources: [lin2004, papineni2002, liang2022, chang2024, hermann2015, narayan2018]
---

# Recall-Oriented Understudy for Gisting Evaluation (ROUGE)

> Overlap of words and word sequences between a generated text and reference texts.

## 1. What is measured

### 1.1 Definition
Recall-Oriented Understudy for Gisting Evaluation (ROUGE) counts how many words (ROUGE-1), word pairs (ROUGE-2), or longest shared word sequences (ROUGE-L) of a reference text also appear in the generated text [lin2004]. It was made for summaries and is reported as recall, precision or F1 of the overlap.

### 1.2 Construct: property of subject in context
The property is content adequacy: whether the text carries the content it should. ROUGE estimates it by similarity to human-written references. The subject is a text generator, such as a summarizer. The context is a test set with references [liang2022].

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Generation performance: content adequacy](../constructs/content-adequacy.md) (under Component characteristics → Component performance → Generation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure whether the text is correct, faithful to its source, or fluent [chang2024].

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy**. Different correct summaries share few words, so ROUGE punishes valid paraphrase. A summary can copy the reference's words and still state something false.

**Using a proxy with a known gap.** ROUGE can support a narrow decision, such as catching a regression between two versions of the same generator on the same references. It cannot support claims that outputs are good, correct or useful. Before using it for those, check a sample of outputs with people, and report ROUGE next to a metric closer to the construct, such as [FActScore](factscore.md) for truth.

### 2.2 Reliability
Deterministic given the references and tokenization; results depend strongly on the number of references and the preprocessing.

### 2.3 Data collection and measurement error
A test set with one or more references per input.

### 2.4 Computation
- ROUGE-N recall = shared n-grams ÷ n-grams in the reference [lin2004].
- ROUGE-L: based on the longest common subsequence.
- Report stemming, stopword handling, and whether F1 or recall is used.

### 2.5 Unit and scale
0 to 1 (often ×100).

### 2.6 Instruments
**News summarization**
- **CNN/DailyMail** [hermann2015]: news articles whose bullet-point highlights serve as reference summaries; built for reading comprehension and later adapted for summarization (check against the paper). Highlights copy much of the article's wording, which favours extractive systems on ROUGE.
- **XSum** [narayan2018]: BBC articles with a one-sentence summary that rewords the article, so overlap with the reference is lower for all systems.

Scores are comparable only within one data set, with the same reference set and preprocessing.

## 3. Why it is measured

### 3.1 Use cases
- A news summarization model is compared with ROUGE on CNN/DailyMail-style articles [liang2022].
- A team uses ROUGE-L as a cheap regression check on meeting summaries, while sampling outputs for human review.

### 3.2 Purposes
Fast, cheap regression testing of generators; benchmark reporting.

### 3.3 Assumptions
A good output resembles the reference in wording.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
NLP engineers and researchers.

### 4.2 Consumers and decisions informed
Teams tracking generator changes; benchmark readers.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing ROUGE rewards copying and length tuning, not quality.

## 5. Related metrics

### 5.1 Operationally related metrics
ROUGE-1, -2 and -L are variants on this page. BLEU (Bilingual Evaluation Understudy) [papineni2002] is a related overlap metric built on precision instead of recall, for translation.

### 5.2 Conceptually related metrics
[FActScore](factscore.md) checks truth and [Answer Faithfulness](answer-faithfulness.md) checks support by sources, both closer to what users care about.

<!-- generated:neighbours:start -->
- Same construct: [Learned Reference-Based Score](learned-reference-score.md) (Generation performance: content adequacy)
- Sibling construct: [Factual Precision in Atomicity Score (FActScore)](factscore.md) (Generation performance: factuality), [pass@k](pass-at-k.md) (Generation performance: functional correctness), [Answer Faithfulness](answer-faithfulness.md) (Generation performance: groundedness), [Instruction-Following Accuracy](instruction-following-accuracy.md) (Generation performance: instruction following)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Hypothesis: ROUGE agrees only weakly with human judgments of quality for open-ended generation. Why it could be true: when many different outputs are acceptable, a single reference covers few of them, so overlap with it says little about quality. Surveys raise this limit [chang2024] (further reference needed for measured agreement).

## 6. Links to business objectives
**Improved usability** and **sustained use:** unknown, no evidence: the number is too far from what users experience.

## 7. Sources
- [lin2004]: ROUGE.
- [papineni2002]: BLEU.
- [liang2022]: ROUGE in summarization benchmarks.
- [chang2024]: limits of overlap metrics.

## Open questions and review notes
- Should BLEU get its own page, or stay a mention here?
