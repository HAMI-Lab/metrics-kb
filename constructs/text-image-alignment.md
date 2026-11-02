---
id: text-image-alignment
title: "Image generation performance: text-image alignment"
aliases: [prompt alignment, image-text consistency]
page_type: construct
template_version: "0.1"
fields: [computer-vision, generative-ai]

broader: [image-generation-performance]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [hessel2021]
---

# Image generation performance: text-image alignment

> Whether an image shows what its text says, or the text describes what the image shows.

## 1. Definition
The correspondence between an image and a text, such as a generated image and its prompt, or an image and its caption [hessel2021].

## 2. Boundaries
Not image quality: a blurry image can match its prompt, and a beautiful one can miss it.

## 3. Narrower constructs
<!-- generated:narrower:start -->
_None yet._
<!-- generated:narrower:end -->

## 4. Metrics
Usually scored by a model that embeds images and text together.
<!-- generated:metrics:start -->
- [CLIPScore](../metrics/clipscore.md)
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: images that match the request need fewer retries.

## 6. How it is identified
Captioning and text-to-image evaluation [hessel2021].

## 7. Sources
- [hessel2021]: CLIPScore.

## Open questions and review notes
- None yet.
