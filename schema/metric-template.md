---
# ---- Identity ----
id: metric-id                    # lowercase-hyphenated; must equal the file name without .md
title: Metric Name
aliases: []
page_type: metric
template_version: "0.2"
fields: []                       # e.g. hci, information-retrieval, recommender-systems, visualization, human-ai-interaction, llm-evaluation

# ---- Provenance ----
status: ai-draft                 # see schema/vocabulary.yaml#status
last_reviewed: null              # YYYY-MM-DD
reviewers: []

# ---- 1. What (construct) ----
# One page = one operationalization. Variants that differ only in a parameter (precision@k) stay on this page.
# One page per computation per root (D20): if the same formula measures constructs under different roots,
# make one page per root and qualify the title, e.g. "Precision (test collection)", "Precision (user on task)".
# Method variants within a root (judgments vs clicks) stay on one page.
construct:
  statement: ""                  # one sentence in plain language: the "spirit" of what this number measures, across all its uses. Authoritative.
  measures: []                   # construct ids from constructs/ (one or more); the place(s) this metric sits in the construct DAG
  subject: []                    # vocabulary: subject
  aspect: []                     # vocabulary: aspect
  perspective: []                # vocabulary: perspective
  quantity_form: []              # vocabulary: quantity_form
  context: []                    # vocabulary: context
  facet_status: provisional

# ---- 2. How (operationalization) ----
operationalization:
  measure_type: direct           # direct | proxy | mixed, relative to construct.statement
  research_method: []            # vocabulary: research_method (how the data is gathered)
  route: []                      # strategy ids from strategies/ (how the data becomes a number)
  collection_mode: []            # vocabulary: collection_mode
  data_source: []                # vocabulary: data_source
  unit: ""
  range: ""
  better: higher                 # higher | lower | target-range | context-dependent
  validity_concern:              # how much thought the gap between number and construct deserves
    level: low                   # vocabulary: validity_concern
    note: ""                     # one line: why

# ---- 4. Who (cost) ----
cost:
  level: low                     # vocabulary: cost_level
  requires: []                   # free text, e.g. "participants", "relevance judgments", "eye tracker"
  automatable: true

# ---- 5. Related metrics ----
related:                         # each item: {metric: <id>, kind: operational | conceptual | empirical, note: "..."}
  []

# ---- 6. Business objectives ----
objectives:
  sustained-use:   {direction: unknown, evidence: none, note: ""}   # direction: positive | negative | non-monotonic | unknown
  improved-usability: {direction: unknown, evidence: none, note: ""}

# ---- 7. Sources ----
sources: []                      # keys in references/bibliography.yaml
---

# Metric Name

> One-sentence summary a newcomer can read in five seconds.

## 1. What is measured
<!-- What property, of what subject, in what context, does this number capture? -->

### 1.1 Definition
<!-- Plain-language definition. Formula goes in 2.4. -->

### 1.2 Construct: property of subject in context
<!-- Expand construct.statement: what property, of what subject, in what context. Write it at the level
     of the "spirit" of the measurement, so it holds for every use in 3.1. The links to the construct
     DAG (front matter construct.measures) are listed automatically below; do not edit between the markers. -->
<!-- generated:constructs:start -->
<!-- generated:constructs:end -->

### 1.3 What it does not measure
<!-- Common misreadings; neighbouring constructs this metric is often confused with. -->

## 2. How it is measured
<!-- How are observations gathered and turned into this number, and how far can the number be trusted? -->

### 2.1 Direct or proxy; construct validity
<!-- Is it a direct or proxy measure of the construct in 1.2? If it is a proxy, what gap between the
     number and the construct could mislead a user of this metric, and what evidence says the gap is
     small? Keep this short when the metric obviously is the thing (validity_concern: low); say more
     when it is contested (moderate or high). The research method and route in the front matter link
     to strategy pages that hold the caveats shared by all metrics using that route. -->

### 2.2 Reliability
<!-- Would the metric give the same answer twice: across judges, occasions, samples? Known figures. -->

### 2.3 Data collection and measurement error
<!-- Online / offline / in-lab / field. Instruments. Sources of measurement error and statistical uncertainty. -->

### 2.4 Computation
<!-- Data selection, transformation, aggregation. The formula. Common variants (e.g. @k, macro vs micro). -->

### 2.5 Unit and scale
<!-- Unit, range, scale type (ratio / interval / ordinal), what "good" looks like, benchmarks. -->

## 3. Why it is measured
<!-- In which situations, and for which purposes, do people pull up this number? -->

### 3.1 Use cases
<!-- 2-4 concrete scenarios where this metric would actually be pulled up, real or realistic.
     Name a specific system, team, or decision, not a generic task category (e.g. not just
     "information retrieval") -- these are seeds for a reviewer to swap in their own.
     Different fields' uses of the same computation (e.g. precision in search vs in classification) go here. -->

### 3.2 Purposes
<!-- Evaluation, documentation, comparison, improvement, monitoring... and for which kinds of systems. -->

### 3.3 Assumptions
<!-- Hidden beliefs. What reference anchors the unit? For system metrics: the assumed user model.
     For user metrics: the assumed user population. -->

## 4. Who is involved
<!-- Who collects the number, who acts on it, and what can go wrong once people act on it? -->

### 4.1 Measurers and cost of measuring
<!-- Who collects it, what it takes (participants, equipment, expertise, time). -->

### 4.2 Consumers and decisions informed
<!-- Who reads it; which decisions it informs. -->

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
<!-- Is it prone to misuse or misreading? Can it be gamed, and who has the incentive? This is the
     consequential side of validity: what happens to the link between number and construct once
     people start optimizing the number or are judged by it. -->

## 5. Related metrics
<!-- Which other metrics share its computation, its construct, or its movements? -->

### 5.1 Operationally related metrics
<!-- Metrics that share computation with this one: variants, parts, metrics built from it or derived
     from it (e.g. F1 and average precision from precision; NASA-TLX subscales). Front matter kind: operational. -->

### 5.2 Conceptually related metrics
<!-- Metrics that measure the same or a related construct, including siblings in the construct DAG
     (precision and recall). Say whether each is a substitute or a complement, and the trade-off
     between cost and directness. Front matter kind: conceptual. Metrics that share a construct or
     a neighbouring construct are listed automatically below. -->
<!-- generated:neighbours:start -->
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
<!-- If this metric moves, how do others move? Known correlations (with sign and strength), trade-offs
     and causal links, with evidence. Front matter kind: empirical. -->

## 6. Links to business objectives
<!-- Sustained use over time; improved usability. State direction, evidence strength, and the
     causal path assumed. Be explicit when the link is only theoretical. -->

## 7. Sources
<!-- Rendered list of the keys in front matter `sources`, with what each one supports. -->

## Open questions and review notes
<!-- Unresolved issues, disagreements, things to verify. -->
