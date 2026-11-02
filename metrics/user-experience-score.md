---
id: user-experience-score
title: User Experience Score (questionnaire)
aliases: [User Experience Questionnaire, UEQ, UEQ-S, pragmatic quality, hedonic quality]
page_type: metric
template_version: "0.3"
fields: [hci]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How people rate their experience of a product on pragmatic (usability-like) and hedonic (pleasure, interest) qualities."
  measures: [user-experience]
  subject: [user]
  aspect: [satisfaction, ease-of-use, engagement]
  perspective: [perceived]
  quantity_form: [rating-score]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: direct
  research_method: [questionnaire-survey]
  route: [self-report]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "scale mean"
  range: "-3 to +3 per scale (UEQ, UEQ-S)"
  better: higher
  validity_concern: {level: low, note: "Direct for the experience as reported on the instrument's scales."}
  instruments:
    - {name: "User Experience Questionnaire (UEQ)", sources: [laugwitz2008], scale: "-3 to +3 per scale", note: "26 pairs of opposite adjectives, 7-point; six scales: attractiveness, perspicuity, efficiency, dependability, stimulation, novelty."}
    - {name: "UEQ-S", sources: [schrepp2017], scale: "-3 to +3 per scale", note: "8 items summarized as pragmatic and hedonic quality; under a minute."}

cost:
  level: low
  requires: ["people who have used the product", "a few minutes (UEQ) or under a minute (UEQ-S)"]
  automatable: false

related:
  - {metric: perceived-usability-score, kind: conceptual, note: "Usability only; UEQ adds hedonic qualities."}
  - {metric: emotional-response-score, kind: conceptual, note: "Momentary emotion rather than overall experience."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Attractive, stimulating products are expected to be used more."}
  improved-usability: {direction: positive, evidence: theoretical, note: "The pragmatic scales overlap with perceived usability."}

sources: [laugwitz2008, schrepp2017]
---

# User Experience Score (questionnaire)

> Ratings on pairs of opposite adjectives, summarized into scales such as attractiveness, efficiency and novelty.

## 1. What is measured

### 1.1 Definition
After using a product, people rate it on a standardized questionnaire that covers both pragmatic qualities (efficiency, clarity, dependability) and hedonic ones (stimulation, novelty). The User Experience Questionnaire (UEQ), the instrument on this page so far, asks for ratings on 26 pairs of opposite adjectives, such as annoying–enjoyable, on 7-point scales, grouped into six scales [laugwitz2008]. Its short version, UEQ-S, has 8 items [schrepp2017].

### 1.2 Construct: property of subject in context
The property is user experience: pragmatic (usability-like) and hedonic (pleasure, interest) qualities as the person perceives them. The subject is the person's judgment of a product. The context is having used it.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [User experience](../constructs/user-experience.md) (under Task characteristics)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure task performance. The pragmatic scales overlap with perceived usability; the hedonic ones are what usability questionnaires such as SUS lack.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for perceived experience on the instrument's scales.

### 2.2 Reliability
Multi-item scales allow internal consistency to be checked; short forms report fewer, broader scales. Figures for each instrument are in 2.6.

### 2.3 Data collection and measurement error
Questionnaire after use, often online. See [self-report](../strategies/self-report.md).

### 2.4 Computation
Each item is scored on the instrument's scale; a scale score is the mean of its items. Compare with the instrument's published benchmark data where it has one. Each instrument's rule is in 2.6.

### 2.5 Unit and scale
Scale means, treated as interval data, on the instrument's range (2.6). Higher is better. Report scales separately rather than one overall mean.

### 2.6 Instruments
- **User Experience Questionnaire (UEQ)** [laugwitz2008]: 26 pairs of opposite adjectives, such as annoying–enjoyable, on 7-point scales.
  - *Scales and scoring:* six scales: attractiveness, perspicuity, efficiency, dependability, stimulation and novelty. Each item is scored from −3 to +3; a scale score is the mean of its items. Compare with the published benchmark data set.
  - *Reliability:* scale reliabilities and benchmark data are published by the authors (check against the paper).
  - *Choose it* to see trade-offs between scales.
- **UEQ-S** [schrepp2017]: 8 items. Pragmatic and hedonic quality are the means of their four items each, from −3 to +3. Choose it for exit surveys and other short slots.

## 3. Why it is measured

### 3.1 Use cases
- A banking app team compares UEQ scores of the old and new app, looking at novelty and stimulation as well as efficiency.
- A web shop shows UEQ-S in an exit survey because it takes under a minute [schrepp2017].

### 3.2 Purposes
Comparing products or versions on experience beyond usability.

### 3.3 Assumptions
Respondents interpret adjective pairs similarly; translations keep meaning.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers.

### 4.2 Consumers and decisions informed
Product and design teams.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Reporting the overall mean hides trade-offs between scales.

## 5. Related metrics

### 5.1 Operationally related metrics
UEQ-S is a short form on this page.

### 5.2 Conceptually related metrics
[Perceived Usability Score (questionnaire)](perceived-usability-score.md) covers usability only. [Emotional Response Score (questionnaire)](emotional-response-score.md) captures momentary emotion.

<!-- generated:neighbours:start -->
- Narrower construct: [Emotional Response Score (questionnaire)](emotional-response-score.md) (User experience: emotional response), [Visualization Aesthetics Score (questionnaire)](visualization-aesthetics-score.md) (User experience: visualization aesthetics)
- Sibling construct: [Forward-Prediction Accuracy](forward-prediction-accuracy.md) (Explanation understanding), [Trust Score (questionnaire)](trust-score.md) (Trust in the system)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** positive, theoretical.

## 7. Sources
- [laugwitz2008]: UEQ.
- [schrepp2017]: UEQ-S.

## Open questions and review notes
- Renamed from the former UEQ page (D25).
