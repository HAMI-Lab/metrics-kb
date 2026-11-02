---
id: transcription-accuracy
title: "Transcription performance: accuracy"
aliases: [recognition accuracy]
page_type: construct
template_version: "0.1"
fields: [speech-processing]

broader: [transcription-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [jurafsky2025]
---

# Transcription performance: accuracy

> How closely a transcript matches the correct one.

## 1. Definition
The match between the output text and the reference transcript, counted in word or character errors [jurafsky2025].

## 2. Boundaries
Errors are counted alike regardless of meaning: a dropped "not" costs as much as a dropped "um".

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Word error rate is the standard metric.
<!-- generated:metrics:start -->
- [Word Error Rate (WER)](../metrics/word-error-rate.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: fewer errors mean less correction by users.

## 6. How it is identified
Speech recognition evaluation [jurafsky2025].

## 7. Sources
- [jurafsky2025]: word error rate.

## Open questions and review notes
- None yet.
