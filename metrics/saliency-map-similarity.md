---
id: saliency-map-similarity
title: "Saliency Map Similarity (SIM)"
aliases: [SIM, histogram intersection, saliency similarity, CC, NSS]
page_type: metric
template_version: "0.3"
fields: [visualization, computer-vision]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much a predicted saliency map overlaps with the map of where people actually looked."
  measures: [saliency-prediction-accuracy]
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
  unit: "overlap of two distributions"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Direct for overlap with recorded fixations; saliency metrics rank models differently, so one metric is not enough."}
  instruments:
    - {name: "MASSVIS eye-tracking data", kind: content, sources: [borkin2016], probes: "where people look on visualizations", scale: "fixation maps", note: "Visualizations with eye-tracking data recorded during encoding and recall."}

cost:
  level: low
  requires: ["fixation maps from an eye-tracking study"]
  automatable: true

related:
  []

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}
  improved-usability: {direction: unknown, evidence: none, note: "Predicting attention can help designers, but the link to usability is not measured."}

sources: [bylinskii2019, borkin2016]
---

# Saliency Map Similarity (SIM)

> The overlap between a predicted saliency map and the observed fixation map, both treated as distributions.

## 1. What is measured

### 1.1 Definition
Both the predicted map and the map of recorded fixations are normalized to sum to 1. SIM is the sum, over all locations, of the smaller of the two values: 1 when the maps are identical, 0 when they do not overlap [bylinskii2019].

### 1.2 Construct: property of subject in context
The property is how well a component predicts where people look. The subject is a saliency model. The context is images or visualizations with recorded fixations.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Visual attention prediction performance: accuracy](../constructs/saliency-prediction-accuracy.md) (under Component characteristics → Component performance → Visual attention prediction performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Whether people understand or remember what they looked at.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for overlap with the recorded fixations. Saliency metrics, such as SIM, correlation (CC) and normalized scanpath saliency (NSS), reward different things and can rank models differently [bylinskii2019]; report several.

### 2.2 Reliability
Depends on how many viewers' fixations make the reference map and on how it is blurred.

### 2.3 Data collection and measurement error
Predict a map per image; build reference maps from fixations with a stated blur.

### 2.4 Computation
SIM = Σ min(P(x), Q(x)) over locations x, with P and Q normalized to sum to 1. CC and NSS are other common choices [bylinskii2019].

### 2.5 Unit and scale
0 to 1; higher is better. Comparable only with the same reference maps and preprocessing.

### 2.6 Instruments
**Where people look on visualizations**
- **MASSVIS eye-tracking data** [borkin2016]: visualizations with fixations recorded while people viewed and later recalled them.

## 3. Why it is measured

### 3.1 Use cases
- A visualization researcher compares saliency models for predicting which chart elements draw attention.

### 3.2 Purposes
Choosing saliency models for design feedback.

### 3.3 Assumptions
Recorded fixations represent the attention of the intended viewers.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Vision and visualization researchers.

### 4.2 Consumers and decisions informed
Designers using predicted attention as feedback.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Blurring predictions can raise some saliency metrics without better prediction [bylinskii2019] (check against the paper).

## 5. Related metrics

### 5.1 Operationally related metrics
CC and NSS are other saliency metrics on the same maps; not separate pages yet.

### 5.2 Conceptually related metrics
None yet.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [bylinskii2019]: saliency metrics.
- [borkin2016]: MASSVIS eye tracking.

## Open questions and review notes
- CC, NSS and the AUC variants could join this page as a family of saliency metrics, or get their own.
