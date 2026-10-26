---
id: temporal-alignment
title: "Annotation tool: temporal alignment"
aliases: [frame sync]
page_type: construct
template_version: "0.1"
fields: [data-annotation, computer-vision]

broader: [system-reliability, annotation-quality]

status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Annotation tool: temporal alignment

> Whether annotations on time-based media land on, and are shown at, the moment the person intended.

## 1. Definition
Correct placement of annotations in time: a box drawn on a video frame is stored for that frame and displayed on it.

## 2. Boundaries
It is a reliability property of the tool that directly affects label quality, hence two parents.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
<!-- generated:metrics:start -->
- [Frame-Sync Accuracy](../metrics/frame-sync-accuracy.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical.

## 6. How it is identified
InfinityPool requests about frame-rate handling and boxes lagging during playback.

## 7. Sources
- None yet.

## Open questions and review notes
- None yet.
