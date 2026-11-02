---
id: questionnaire-survey
title: Questionnaires and surveys
aliases: [survey, questionnaire, self-report instrument]
page_type: strategy
template_version: "0.2"

layer: method
research_methods: []

status: ai-draft
last_reviewed: null
reviewers: []

sources: [lazar2017, brooke1996, hart1988, lewis2018, bangor2008, embretson2000, campbell1959]
---

# Questionnaires and surveys

> People answer a fixed set of written questions, after a task, after a study, or on their own.

## 1. What it is

### 1.1 Definition
A questionnaire is a fixed set of written questions (items) given to people on paper or online. Items can be closed, such as rating scales and multiple choice, or open, asking for free text. A survey gives a questionnaire to a sample of a population, often independently of any task [lazar2017]. The data is what people say, not what they do.

### 1.2 Typical pairings
Closed rating items are scored by self-rating. Scales with many items are often scored with statistical or latent-variable models [embretson2000]. Open answers are coded. Preference questions ("which of the two did you prefer?") feed comparative judgment.
<!-- generated:pairings:start -->
- [Coding qualitative data](qualitative-coding.md)
- [Comparative judgment: preferences and interleaving](comparative-judgment.md)
- [Self-rating: questionnaires and rating scales](self-rating.md)
- [Statistical and latent-variable modeling](statistical-modeling.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Standardized questionnaires** with fixed items and scoring, such as SUS [brooke1996] and NASA-TLX [hart1988].
- **Post-task single items**, such as perceived difficulty after each task.
- **Population surveys** of users or non-users, for adoption and attitudes [lazar2017].

## 2. When to use it
Use it when the construct is perceived (satisfaction, perceived usability, attitudes), or to reach many people cheaply. Prefer observation or logs when the construct is behaviour, and interviews when the aim is to discover what matters rather than to measure it.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
Answers reflect what people remember and are willing to report, not what they did. Respondents may read an item differently from its designers. A custom item has no validation evidence until someone collects it; standardized instruments such as SUS have published evidence [lewis2018]. Measuring a construct only by questionnaire mixes the method's own variance into the result [campbell1959].

### 3.2 Reliability
Who answers matters: people who respond can differ from those who do not, and self-selected samples overrepresent strong opinions [lazar2017]. Timing changes answers (right after a task vs a week later). Changing wording, item order or translation breaks comparison with published norms, such as SUS benchmarks [bangor2008].

### 3.3 Bias and gaming
Leading wording and item order shift answers. Biases that come from rating (acquiescence, social desirability) are on the [self-rating](self-rating.md) page. Results can be inflated by surveying only engaged users or sending the survey right after a success.

## 4. Cost
Cheap per respondent once the items exist. Designing and validating new items is expensive, which is a reason to reuse standardized instruments. Recruiting enough of the right respondents is often the main cost.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Demographic Profile (questionnaire)](../metrics/demographic-profile.md)
- [Educational Attainment (questionnaire)](../metrics/educational-attainment.md)
- [Emotional Response Score (questionnaire)](../metrics/emotional-response-score.md)
- [Mental Workload Score (questionnaire)](../metrics/mental-workload-score.md)
- [Perceived Usability Score (questionnaire)](../metrics/perceived-usability-score.md)
- [Trust Score (questionnaire)](../metrics/trust-score.md)
- [User Experience Score (questionnaire)](../metrics/user-experience-score.md)
- [Visualization Aesthetics Score (questionnaire)](../metrics/visualization-aesthetics-score.md)
<!-- generated:metrics:end -->

## 6. Sources
- [lazar2017]: surveys and questionnaires in HCI, sampling and nonresponse.
- [brooke1996], [hart1988]: SUS and NASA-TLX as standardized instruments.
- [lewis2018]: validation evidence for SUS.
- [bangor2008]: SUS score benchmarks.
- [embretson2000]: latent-trait models for multi-item scales.
- [campbell1959]: method variance.

## Open questions and review notes
- Knowledge tests with right answers now have their own method page: [ability tests](ability-test.md).
