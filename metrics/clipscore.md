---
id: clipscore
title: CLIPScore
aliases: [CLIP score, CLIP-S, CLIP R-Precision]
page_type: metric
template_version: "0.3"
fields: [computer-vision, generative-ai]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How well an image and a text correspond, as judged by the similarity of their embeddings in a model trained on image-text pairs."
  measures: [text-image-alignment]
  subject: [system-component]
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
  unit: "rescaled cosine similarity"
  range: "0 upward; typically below 1 after rescaling"
  better: higher
  validity_concern: {level: moderate, note: "The scoring model's notion of correspondence stands in for people's; it misses details such as counting and spatial relations."}
  instruments:
    - {name: "CLIP", kind: scorer, sources: [radford2021], scale: "cosine similarity of embeddings", note: "A model trained on image-text pairs to embed both in one space."}
    - {name: "MS-COCO captions", kind: content, sources: [lin2014], probes: "everyday scenes described in one sentence", scale: "—", note: "Images with human captions; captions also serve as prompts for image generation."}

cost:
  level: low
  requires: ["the scoring model", "images and texts"]
  automatable: true

related:
  - {metric: learned-reference-score, kind: conceptual, note: "Also a learned scorer, for text against reference text."}

objectives:
  sustained-use: {direction: unknown, evidence: none, note: "Too far from what users experience to say."}
  improved-usability: {direction: unknown, evidence: none, note: "Not measured with users."}

sources: [hessel2021, radford2021, lin2014]
---

# CLIPScore

> A rescaled cosine similarity between CLIP embeddings of an image and a text.

## 1. What is measured

### 1.1 Definition
CLIPScore embeds an image and a text with CLIP, a model trained on image-text pairs [radford2021], and reports their rescaled cosine similarity [hessel2021]. It needs no reference text, so it can score captions for an image or generated images for a prompt.

### 1.2 Construct: property of subject in context
The property is text-image alignment. The subject is an image generator or a captioner, a component. The context is a set of prompts or images.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Image generation performance: text-image alignment](../constructs/text-image-alignment.md) (under Component characteristics → Component performance → Image generation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Image quality or realism; fine details such as counts, attributes bound to the right objects, or positions.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy**: CLIP's similarity stands in for people's judgment of correspondence. Hypothesis: it is weak on counting, spatial relations and attribute binding. Why it could be true: the model is trained to match whole images to whole captions, which rarely depend on such details (further reference needed).

**Using a proxy with a known gap.** CLIPScore can screen generators for gross mismatches with prompts. It cannot certify that images match detailed prompts; check a sample with people.

### 2.2 Reliability
Deterministic for a fixed CLIP model; different CLIP models give different scores.

### 2.3 Data collection and measurement error
Generate images for prompts, or captions for images; embed both; compute the score.

### 2.4 Computation
CLIPScore = w · max(cos(image embedding, text embedding), 0), with a rescaling weight w [hessel2021] (check against the paper).

### 2.5 Unit and scale
Rescaled similarity; comparable only with the same CLIP model and rescaling.

### 2.6 Instruments
**Scorers**
- **CLIP** [radford2021]: the embedding model; its version is part of the instrument.

**Content: everyday scenes**
- **MS-COCO captions** [lin2014]: images with human captions; the captions are also used as prompts for image generation.

## 3. Why it is measured

### 3.1 Use cases
- A team tuning a text-to-image model tracks CLIPScore on a fixed prompt set between checkpoints.

### 3.2 Purposes
Cheap screening of text-image correspondence.

### 3.3 Assumptions
The scoring model's judgments match people's for the prompts used.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Generative-model engineers.

### 4.2 Consumers and decisions informed
Teams choosing image or caption models.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Generators trained against CLIP can exploit its blind spots.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[Learned Reference-Based Score](learned-reference-score.md) is the text counterpart with references.

<!-- generated:neighbours:start -->
_None found from the construct DAG yet._
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** unknown.

## 7. Sources
- [hessel2021]: CLIPScore.
- [radford2021]: CLIP.
- [lin2014]: MS-COCO.

## Open questions and review notes
- CLIP R-Precision, which ranks the right caption among distractors, is listed as an alias; it may deserve its own section once a source is added.
