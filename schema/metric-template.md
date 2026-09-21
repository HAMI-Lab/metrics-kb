---
# ---- Identity ----
id: metric-id                    # lowercase-hyphenated; must equal the file name without .md
title: Metric Name
aliases: []
page_type: metric
template_version: "0.1"
fields: []                       # e.g. hci, information-retrieval, recommender-systems, visualization, human-ai-interaction, llm-evaluation

# ---- Provenance ----
status: ai-draft                 # see schema/vocabulary.yaml#status
last_reviewed: null              # YYYY-MM-DD
reviewers: []

# ---- 1. What (construct) ----
construct:
  statement: ""                  # one sentence in plain language; this is the authoritative definition
  subject: []                    # vocabulary: subject
  aspect: []                     # vocabulary: aspect
  perspective: []                # vocabulary: perspective
  quantity_form: []              # vocabulary: quantity_form
  context: []                    # vocabulary: context
  facet_status: provisional

# ---- 2. How (operationalization) ----
operationalization:
  measure_type: direct           # direct | proxy | mixed, relative to construct.statement
  collection_mode: []            # vocabulary: collection_mode
  data_source: []                # vocabulary: data_source
  unit: ""
  range: ""
  better: higher                 # higher | lower | target-range | context-dependent

# ---- 4. Who (cost) ----
cost:
  level: low                     # vocabulary: cost_level
  requires: []                   # free text, e.g. "participants", "relevance judgments", "eye tracker"
  automatable: true

# ---- 5. Related metrics ----
related:                         # each item: {metric: <id>, relation: <see below>, note: "..."}
  []
  # relation values: same-construct | complementary | trade-off | component-of | correlated | causally-linked

# ---- 6. Business objectives ----
objectives:
  sustained-use:   {direction: unknown, evidence: none, note: ""}   # direction: positive | negative | non-monotonic | unknown
  improved-usability: {direction: unknown, evidence: none, note: ""}

# ---- 7. Sources ----
sources: []                      # keys in references/bibliography.yaml, e.g. [S13, brooke1996]
---

# Metric Name

> One-sentence summary a newcomer can read in five seconds.

## 1. What is measured

### 1.1 Definition
<!-- Plain-language definition. Formula goes in 2.4. -->

### 1.2 Construct: property of subject in context
<!-- Expand construct.statement: what property, of what subject, in what context.
     Name the abstract construct of interest if there is one (e.g. "perceived usability"). -->

### 1.3 What it does not measure
<!-- Common misreadings; neighbouring constructs this metric is often confused with. -->

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
<!-- Is it a direct or proxy measure of the construct in 1.2? How well does the measurement align
     with the construct? What epistemic uncertainty remains? -->

### 2.2 Reliability
<!-- Is the construct measured consistently across subjects and contexts? Known reliability figures. -->

### 2.3 Data collection and measurement error
<!-- Online / offline / in-lab / field. Instruments. Sources of measurement error and statistical uncertainty. -->

### 2.4 Computation
<!-- Data selection, transformation, aggregation. The formula. Common variants. -->

### 2.5 Unit and scale
<!-- Unit, range, scale type (ratio / interval / ordinal), what "good" looks like, benchmarks. -->

## 3. Why it is measured

### 3.1 Purposes
<!-- Evaluation, documentation, comparison, improvement, monitoring... and for which kinds of systems. -->

### 3.2 Assumptions
<!-- Hidden beliefs. What reference anchors the unit? For system metrics: the assumed user model.
     For user metrics: the assumed user population. -->

## 4. Who is involved

### 4.1 Measurers and cost of measuring
<!-- Who collects it, what it takes (participants, equipment, expertise, time). -->

### 4.2 Consumers and decisions informed
<!-- Who reads it; which decisions it informs. -->

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
<!-- Is it prone to misuse or misreading? Can it be gamed, and who has the incentive? -->

## 5. Related metrics

### 5.1 Static relationships
<!-- Metrics with similar construct / operationalization / purpose / stakeholders.
     Complementary (together characterize the subject) or supplementary (substitutes)?
     Include the cost vs directness trade-off where relevant. -->

### 5.2 Dynamic relationships
<!-- If this metric moves, how do others move? Known correlations (with sign and strength)
     and causal links, with evidence. -->

## 6. Links to business objectives
<!-- Sustained use over time; improved usability. State direction, evidence strength, and the
     causal path assumed. Be explicit when the link is only theoretical. -->

## 7. Sources
<!-- Rendered list of the keys in front matter `sources`, with what each one supports. -->

## Open questions and review notes
<!-- Unresolved issues, disagreements, things to verify. -->
