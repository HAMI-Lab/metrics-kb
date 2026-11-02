---
id: self-report
title: "Self-report: ratings and answers about oneself"
aliases: [self-rating, subjective rating, self-reported data, background questions]
page_type: strategy
template_version: "0.2"

layer: route
research_methods: [questionnaire-survey, diary-esm, task-study]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [brooke1996, hart1988, bolger2003, campbell1959, webb1966]
---

# Self-report: ratings and answers about oneself

> People answer questions about themselves: they rate their own experience on a scale, or state facts about themselves, and the answers become the data.

## 1. What it is

### 1.1 Definition
A person answers questions about themselves. It takes two forms:
- **Ratings of experience**: the person rates their experience or judgment on a scale, such as how easy a system was to use, and the ratings are scored into a number by a fixed rule.
- **Factual answers**: the person states facts about themselves, such as age or highest degree, and the answers are recorded as given.

### 1.2 Typical pairings
Post-task and post-study questionnaires, surveys, diary entries, and experience-sampling prompts during the day [bolger2003].
<!-- generated:pairings:start -->
- [Questionnaires and surveys](questionnaire-survey.md)
- `diary-esm` (no method page yet)
- [Task studies with people](task-study.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Standardized questionnaires** with fixed scoring, such as SUS [brooke1996] and NASA-TLX [hart1988].
- **Single-item post-task ratings** (for example, perceived difficulty).
- **Experience sampling** ratings collected in the moment over days or weeks [bolger2003].
- **Background questions** on demographics and education, usually at the start or end of a study.

## 2. When to use it
Use ratings when the construct is perceived (satisfaction, perceived usability, workload as experienced); they are a weak substitute for observing behaviour or outcomes. Use factual answers for background that no test or log can supply, such as age or education.

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
Ratings are direct for perceived constructs and proxies for objective ones. Factual answers are direct for what people report, but answer options that do not fit someone, or a question they would rather not answer, distort the record. The same construct measured by questionnaire and by behaviour often disagrees, partly because the method itself contributes variance [campbell1959].

### 3.2 Reliability
For ratings, check internal consistency for multi-item scales and test-retest stability; means from small samples have wide intervals. Factual answers are stable for most attributes.

### 3.3 Bias and gaming
Shared by both forms: being asked changes what people report [webb1966], and social desirability toward the researcher biases answers. Ratings also suffer from recency (the last task dominates) and acquiescence (agreeing with items). Factual answers suffer from recall errors and from questions people prefer not to answer; make sensitive questions optional. Scores can be inflated by choosing friendly respondents or easy tasks.

## 4. Cost
Low per respondent (minutes), but needs people who actually used the system; cannot be computed from logs.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Demographic Profile (questionnaire)](../metrics/demographic-profile.md)
- [Educational Attainment (questionnaire)](../metrics/educational-attainment.md)
- [Emotional Response Score (questionnaire)](../metrics/emotional-response-score.md)
- [Mental Workload Score (questionnaire)](../metrics/mental-workload-score.md)
- [Perceived Usability Score (questionnaire)](../metrics/perceived-usability-score.md)
- [Precision (user on task)](../metrics/precision-user-task.md)
- [Trust Score (questionnaire)](../metrics/trust-score.md)
- [User Experience Score (questionnaire)](../metrics/user-experience-score.md)
- [Visualization Aesthetics Score (questionnaire)](../metrics/visualization-aesthetics-score.md)
<!-- generated:metrics:end -->

## 6. Sources
- [brooke1996]
- [hart1988]
- [bolger2003]
- [campbell1959]
- [webb1966]

## Open questions and review notes
- None yet.
