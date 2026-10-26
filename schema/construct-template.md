---
# ---- Identity ----
id: construct-id                 # lowercase-hyphenated; must equal the file name without .md
title: Construct Name            # may carry a field prefix, e.g. "Retrieval effectiveness: topical relevance"
aliases: []                      # "concept" is a plain-language synonym for construct
page_type: construct
template_version: "0.1"
fields: []

# ---- Place in the construct DAG ----
broader: []                      # parent construct ids; more than one allowed. Edit here or in constructs/dag.yaml, then run scripts/sync_constructs.py

# ---- Provenance ----
status: ai-draft
last_reviewed: null
reviewers: []

sources: []
---

# Construct Name

> One-sentence summary of what this construct is about.

## 1. Definition
<!-- What is this construct, in plain language? What would it mean for a system or a person to have
     more or less of it? -->

## 2. Boundaries
<!-- How does it differ from its broader construct(s) and from its siblings? What is it often
     confused with? -->

## 3. Narrower constructs
<!-- How do the narrower constructs relate to each other: do they add up to this one, trade off,
     or cover different situations? The list itself is generated from their `broader` fields. -->
<!-- generated:narrower:start -->
<!-- generated:narrower:end -->

## 4. Metrics
<!-- Which metrics measure this construct, and when would you choose one over another? What part of
     the construct does no current metric capture? The list is generated from metric pages'
     construct.measures. -->
<!-- generated:metrics:start -->
<!-- generated:metrics:end -->

## 5. Links to business objectives
<!-- Theoretical paths from this construct to sustained use and improved usability (e.g. perceived
     usefulness -> intention to use). Measured evidence belongs on metric pages. -->

## 6. How it is identified
<!-- Where does this construct come from: theory, prior literature, or qualitative work such as
     interviews, diary studies, and observation that showed it matters to users? -->

## 7. Sources
<!-- Rendered list of the keys in front matter `sources`, with what each one supports. -->

## Open questions and review notes
<!-- Placement in the DAG, naming, disagreements, things to verify. -->
