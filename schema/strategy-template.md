---
# ---- Identity ----
id: strategy-id                  # lowercase-hyphenated; must equal the file name without .md
title: Strategy Name
aliases: []
page_type: strategy
template_version: "0.2"

# A strategy page is one of two layers. A route says how gathered data becomes a number; a method says how
# the data is gathered. A method page's id must be a research_method value in schema/vocabulary.yaml.
layer: route                     # route | method
research_methods: []             # route pages only: research_method values this route typically works on; empty on method pages

# ---- Provenance ----
status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Strategy Name

> One-sentence summary of how this route turns observations into numbers.

## 1. What it is
<!-- Route: how does it produce a number, and from what kind of data? Method: how does it gather data, and what does the data record? -->

### 1.1 Definition
<!-- Plain-language description of the route or method. -->

### 1.2 Typical pairings
<!-- Route: which methods feed it. Method: which routes turn its data into numbers. The list is generated:
     from `research_methods` on route pages, and from the route pages that name this method on method pages. -->
<!-- generated:pairings:start -->
<!-- generated:pairings:end -->

### 1.3 Named practices
<!-- Well-known forms, each in a sentence or two (e.g. Cranfield test collections, LLM-as-a-judge,
     interleaving). A practice that combines a method and a route goes on both pages, briefly on one of them. -->

## 2. When to use it
<!-- What measurement needs does it fit, and when is another route or method better? -->

## 3. Shared caveats
<!-- Caveats that hold for every metric using this route or method, so metric pages need not repeat them.
     Method pages keep to what comes from gathering the data (who and what is sampled, what is recorded);
     caveats about scoring belong on route pages. -->

### 3.1 Validity: how the number can miss the construct
<!-- Route: typical gaps between the number and what people want to know. Method: what the data cannot show. -->

### 3.2 Reliability
<!-- Typical sources of inconsistency (judges, occasions, samples) and how they are checked. -->

### 3.3 Bias and gaming
<!-- Systematic biases of the route; how it can be gamed. -->

## 4. Cost
<!-- What it takes: people, equipment, reference data, compute; what is reusable once built. -->

## 5. Metrics using this strategy
<!-- Generated from metric pages' operationalization.route (route pages) or operationalization.research_method (method pages). -->
<!-- generated:metrics:start -->
<!-- generated:metrics:end -->

## 6. Sources
<!-- Rendered list of the keys in front matter `sources`, with what each one supports. -->

## Open questions and review notes
<!-- Unresolved issues, disagreements, things to verify. -->
