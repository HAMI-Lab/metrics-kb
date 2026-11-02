---
id: judge-rating
title: Judge Rating (model judge)
aliases: [LLM-as-a-judge score, LLM judge rating, MT-Bench score, GPT-4 score, single-answer grading, judge score]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How good a model judge rates a system's responses, on a scale defined by the judge's prompt or rubric."
  measures: [output-quality]
  subject: [system]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [rating-score]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [benchmark]
  route: [external-judgment]
  collection_mode: [offline]
  data_source: [model-judge]
  unit: "rating on the rubric's scale"
  range: "set by the instrument (for example 1-10)"
  better: higher
  validity_concern: {level: high, note: "A model judge stands in for people; its biases and errors become the metric's unless checked against human ratings."}
  instruments:
    - {name: "MT-Bench", kind: content, sources: [zheng2023], probes: "multi-turn conversation across writing, reasoning, math, coding and other categories", scale: "1-10 per answer, averaged", note: "Two-turn questions graded by a strong LLM judge."}
    - {name: "Single-answer grading with an LLM judge", kind: scorer, sources: [zheng2023, li2024], scale: "set by the rubric", note: "A judge model with a prompt or rubric rates each answer on its own."}

cost:
  level: low
  requires: ["a question set", "a judge model and prompt"]
  automatable: true

related:
  - {metric: answer-faithfulness, kind: conceptual, note: "Also uses a model judge, for one narrow property."}
  - {metric: instruction-following-accuracy, kind: conceptual, note: "Checkable instructions are scored by programs; others need a judge."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Better-rated responses are assumed to keep users coming back; depends on the judge matching users' taste."}
  improved-usability: {direction: unknown, evidence: none, note: "Judge preferences, such as for longer answers, may not match what helps users."}

sources: [zheng2023, li2024]
---

# Judge Rating (model judge)

> A score that a model judge, usually a strong LLM given a rubric, assigns to each of a system's responses, averaged over a question set.

## 1. What is measured

### 1.1 Definition
A judge model reads a question and a system's response, and rates the response on a scale defined by its prompt or rubric, such as 1 to 10. The ratings are averaged over the questions [zheng2023]. Pairwise comparison by a judge is a different computation and gives a win rate, not a rating.

### 1.2 Construct: property of subject in context
The property is the quality of the system's responses as the judge understands quality. The subject is the system, such as a chatbot answering end to end (D28). The context is the question set and the rubric.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Output quality](../constructs/output-quality.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
What users think of the responses, unless the judge has been shown to agree with them. Whether the responses are factually correct, unless the rubric and judge check that reliably.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy**: the judge's rating stands in for a human's. Model judges show known biases, such as favouring longer answers, answers in a certain position, or answers in their own style (check against [zheng2023]; [li2024]).

**Using a proxy with a known gap.** Judge ratings can screen many system versions cheaply and flag large changes. They cannot settle close comparisons, or claims about what users prefer, without checking the judge against human ratings on a sample. Before relying on them, measure judge-human agreement for your questions and keep the judge and prompt fixed.

### 2.2 Reliability
Depends on the judge model, prompt and sampling settings; changing any of them changes the scores. Agreement between strong judges and people has been reported to approach agreement between people on some sets (check against [zheng2023]). Agreement statistics for judges are on the [external judgment](../strategies/external-judgment.md) route page (D21).

### 2.3 Data collection and measurement error
Generate responses to the question set, then run the judge on each. Record the judge model, its version, the prompt and the decoding settings.

### 2.4 Computation
Mean rating over questions, and over turns where the instrument has several. Some instruments report per-category means.

### 2.5 Unit and scale
A rating on the rubric's scale, treated as interval data with caution. Ratings from different judges or rubrics are not comparable.

### 2.6 Instruments
**Content: multi-turn conversation**
- **MT-Bench** [zheng2023]: two-turn questions in categories such as writing, reasoning, math and coding, graded from 1 to 10 by a strong LLM judge.

**Scorers**
- **Single-answer grading with an LLM judge** [zheng2023; li2024]: the judge model, its prompt and its rubric together are the scorer. Report all three.

## 3. Why it is measured

### 3.1 Use cases
- A team iterating on a chatbot's system prompt reruns MT-Bench after each change to catch regressions.
- A model release reports an MT-Bench score next to benchmark accuracies.

### 3.2 Purposes
Cheap, fast comparison of open-ended responses where no answer key exists.

### 3.3 Assumptions
The judge's notion of quality matches the users'; the judge is not biased toward the systems compared (for example toward its own outputs).

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML engineers; cost is the judge's inference.

### 4.2 Consumers and decisions informed
Teams choosing models or prompts for open-ended assistants.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Optimizing for the judge's preferences, such as length or style, rather than for users. Using the same model family as system and judge.

## 5. Related metrics

### 5.1 Operationally related metrics
None on the wiki yet; win rate from pairwise judging is a candidate.

### 5.2 Conceptually related metrics
[Answer Faithfulness](answer-faithfulness.md) uses a judge for one property; [Instruction-Following Accuracy](instruction-following-accuracy.md) covers checkable instructions without a judge.

<!-- generated:neighbours:start -->
- Narrower construct: [Demographic Parity Difference (DPD)](demographic-parity-difference.md) (Output quality: fairness), [Attack Success Rate (ASR)](attack-success-rate.md) (Output quality: safety), [Toxicity Rate](toxicity-rate.md) (Output quality: safety)
- Sibling construct: [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (Autonomous task completion), [pass^k](pass-hat-k.md) (Consistency across runs), [Response Latency](response-latency.md) (System responsiveness), [Performance Drop Rate (PDR)](performance-drop-rate.md) (System robustness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use:** positive, theoretical. **Improved usability:** unknown: judge preferences may not match what helps users.

## 7. Sources
- [zheng2023]: MT-Bench and LLM-as-a-judge, including its biases.
- [li2024]: survey of LLM judges.

## Open questions and review notes
- The page sits at the system root because judged benchmarks usually evaluate a model used end to end (D28). A judged component output, such as a summary step, would measure a component construct; does output quality need a component-root parent?
