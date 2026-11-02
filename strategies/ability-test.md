---
id: ability-test
title: Ability tests
aliases: [knowledge test, skill test, literacy test, assessment test]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [embretson2000, lee2017, cokely2012, cui2024, ding2023]
---

# Ability tests

> A person answers questions that have right answers, to show what they know or can do.

## 1. What it is

### 1.1 Definition
Test items have correct answers fixed by the test's authors. The person's answers are scored against that key. The data describes the person's knowledge or skill, not their opinion. Literacy and numeracy tests are the main examples here [lee2017; cokely2012]. They are often given in the same way as questionnaires, on paper or online, but are scored differently.

### 1.2 Typical pairings
Answers are compared with the key; scores on many items are often modelled with item response theory, which estimates ability from which items were answered correctly [embretson2000].
<!-- generated:pairings:start -->
- [Comparison against reference data](reference-comparison.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Fixed-form tests:** every person answers the same items, such as VLAT [lee2017].
- **Short forms:** a subset of items chosen to keep most of the information.
- **Adaptive tests:** the next item depends on earlier answers, so fewer items are needed for the same precision [cui2024; embretson2000].
- **Packaged tests in study platforms:** platforms such as reVISit ship ready-to-use tests alongside questionnaires [ding2023].

## 2. When to use it
Use it for user characteristics measured by right answers: literacy, numeracy, domain knowledge. Use questionnaires for attitudes and perceptions, which have no right answer.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
A test covers the items its authors chose; a visualization literacy test built on common chart types says little about unusual ones. Scores depend on test-taking skill and effort, which online participants may not give.

### 3.2 Reliability
Short and adaptive forms trade items for time; check their reported reliability against the full form. Ceiling and floor effects appear when the test is too easy or too hard for the population.

### 3.3 Bias and gaming
Items leak and can be practised. Translations and new populations can change item difficulty, so norms from the original population may not apply.

## 4. Cost
Low per person once a validated test exists; building and validating a new test is costly.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Numeracy Score (ability test)](../metrics/numeracy-score.md)
- [Visualization Literacy Score (ability test)](../metrics/visualization-literacy-score.md)
<!-- generated:metrics:end -->

## 6. Sources
- [embretson2000]: item response theory.
- [lee2017]: VLAT.
- [cokely2012]: Berlin Numeracy Test.
- [cui2024]: adaptive visualization literacy tests.
- [ding2023]: reVISit.

## Open questions and review notes
- None yet.
