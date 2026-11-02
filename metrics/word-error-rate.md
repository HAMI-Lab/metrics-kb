---
id: word-error-rate
title: "Word Error Rate (WER)"
aliases: [WER, CER, character error rate]
page_type: metric
template_version: "0.3"
fields: [speech-processing]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How many word errors a transcript contains, relative to the length of the correct transcript."
  measures: [transcription-correctness]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [benchmark]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "errors per reference word"
  range: "0 upward; can exceed 1"
  better: lower
  validity_concern: {level: low, note: "Direct for word-level agreement with the reference; treats all words alike."}
  instruments:
    - {name: "LibriSpeech", kind: content, sources: [panayotov2015], probes: "read English speech", scale: "WER", note: "Audiobook recordings with transcripts; separate clean and harder test sets."}

cost:
  level: low
  requires: ["audio with reference transcripts"]
  automatable: true

related:
  - {metric: accuracy, kind: conceptual, note: "Exact match counts a transcript right only if every word is right."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Recognition errors frustrate voice interaction."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Errors must be corrected by users."}

sources: [jurafsky2025, panayotov2015]
---

# Word Error Rate (WER)

> The number of substituted, deleted and inserted words in a transcript, divided by the number of words in the correct transcript.

## 1. What is measured

### 1.1 Definition
Word Error Rate (WER) aligns the system's transcript with the reference and counts substitutions (S), deletions (D) and insertions (I). WER = (S + D + I) ÷ N, where N is the number of words in the reference [jurafsky2025]. Character error rate (CER) does the same per character.

### 1.2 Construct: property of subject in context
The property is transcription correctness. The subject is a speech or text recognizer, a component. The context is a set of recordings with reference transcripts.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Transcription performance: correctness](../constructs/transcription-correctness.md) (under Component characteristics → Component performance → Transcription performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Whether errors change the meaning; whether the transcript is usable by people or downstream components.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for word-level agreement with the reference. All errors count the same, so a dropped negation weighs as much as a dropped filler word.

### 2.2 Reliability
Deterministic given the transcripts and normalization (case, punctuation, numbers); report the normalization.

### 2.3 Data collection and measurement error
Run the recognizer on the recordings; normalize both transcripts the same way.

### 2.4 Computation
- WER = (S + D + I) ÷ N, using the minimum-edit alignment.
- CER: the same per character, used for languages without word boundaries.

### 2.5 Unit and scale
Errors per reference word, from 0 upward; insertions can push it above 1. Lower is better.

### 2.6 Instruments
**Read speech**
- **LibriSpeech** [panayotov2015]: English audiobook recordings with transcripts, with a cleaner and a harder test set reported separately.

## 3. Why it is measured

### 3.1 Use cases
- A team choosing a speech model for a voice assistant compares WER on recordings of its own users.
- A model release reports WER on LibriSpeech's two test sets.

### 3.2 Purposes
Model selection and regression testing for speech recognition.

### 3.3 Assumptions
The reference transcripts are correct; the recordings match real use (accents, noise, vocabulary).

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Speech engineers.

### 4.2 Consumers and decisions informed
Teams building voice interfaces.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Low WER on clean read speech overstates accuracy on spontaneous, noisy or accented speech.

## 5. Related metrics

### 5.1 Operationally related metrics
CER is a variant on this page.

### 5.2 Conceptually related metrics
[Accuracy](accuracy.md) as exact match would count a transcript right only if every word matched.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** negative, theoretical: errors make users repeat or correct themselves.

## 7. Sources
- [jurafsky2025]: definition.
- [panayotov2015]: LibriSpeech.

## Open questions and review notes
- None yet.
