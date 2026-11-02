---
id: perceived-usability-score
title: Perceived Usability Score (questionnaire)
aliases: [SUS, System Usability Scale, UMUX, Usability Metric for User Experience, UMUX-LITE, PSSUQ, perceived usability questionnaire]
page_type: metric
template_version: "0.3"
fields: [hci, human-ai-interaction, visualization, information-retrieval]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How usable people who have just used a system perceive it to be, summarized as one score."
  measures: [perceived-usability]
  subject: [system, user]
  aspect: [ease-of-use, satisfaction]
  perspective: [perceived]
  quantity_form: [rating-score]
  context: [task, system-specific, user-specific]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [questionnaire-survey]
  route: [self-rating]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "score (dimensionless)"
  range: "0-100 for SUS, UMUX and UMUX-LITE"
  better: higher
  validity_concern: {level: low, note: "Direct for perceived usability as reported; a proxy for usability in the ISO sense (see 2.1)."}
  instruments:
    - {name: "System Usability Scale (SUS)", sources: [brooke1996], scale: "0-100", note: "10 statements, 5-point agreement, alternately positive and negative. The most widely used, with published norms."}
    - {name: "Usability Metric for User Experience (UMUX)", sources: [finstad2010], scale: "0-100", note: "4 items, 7-point; designed to correspond to SUS."}
    - {name: "UMUX-LITE", sources: [lewis2013], scale: "0-100", note: "The 2 positively worded UMUX items; a proposed adjustment aligns it with SUS."}

cost:
  level: medium
  requires: [participants who have used the system, "under a minute (UMUX-LITE) to about 1-2 minutes (SUS) per participant"]
  automatable: false

related:
  - {metric: mental-workload-score, kind: conceptual, note: "These questionnaires ask about the system; workload questionnaires ask about the demand the task placed on the person."}
  - {metric: user-experience-score, kind: conceptual, note: "Adds hedonic qualities to usability."}
  - {metric: task-completion-time, kind: conceptual, note: "Objective efficiency vs. perceived usability; correlations are modest."}
  - {metric: response-latency, kind: empirical, note: "Slow responses plausibly lower perceived usability; not quantified for SUS specifically."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Via perceived ease of use -> intention to use (TAM), and satisfaction -> continuance (expectation-confirmation model). Links to logged retention are not established here."}
  improved-usability: {direction: positive, evidence: correlational, note: "Perceived usability by construction; its correlation with objective usability measures is moderate."}

sources: [brooke1996, bangor2008, bangor2009, lewis2009, sauro2011positive, lewis2018, sauro2009, hornbaek2007, davis1989, bhattacherjee2001, iso9241-11, sauro2016, strathern1997, kim2024, rong2022, finstad2010, lewis2013]
---

# Perceived Usability Score (questionnaire)

> A short standardized questionnaire, such as SUS or UMUX, that gives one 0-100 score for how usable people perceive a system to be, cheap enough to run after almost any usability study.

## 1. What is measured

### 1.1 Definition
People answer a short standardized questionnaire about a system right after using it, and their answers are combined into one score. The best known is the System Usability Scale (SUS): ten statements answered on a five-point agreement scale, scored from 0 to 100 [brooke1996]. Shorter instruments such as UMUX and UMUX-LITE measure the same construct with fewer items [finstad2010; lewis2013]. Section 2.6 compares them.

### 1.2 Construct: property of subject in context
The property is **perceived usability**, which blends ease of use and satisfaction. The subject is the **system**, as judged by a **user**. The context is the use the respondent just had: the tasks they did and who they are. A score therefore describes the system *for these people doing these tasks*, not the system in general.

Factor analyses suggest SUS has two related parts, often called "usable" (eight items) and "learnable" (two items) [lewis2009], though later work questions how stable that split is [lewis2018]. Most practice treats it as one overall score.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Usability: perceived usability](../constructs/perceived-usability.md) (under Task characteristics → Usability)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure objective performance. People can rate a system highly and still fail tasks, or the reverse [sauro2009; hornbaek2007]. It also does not diagnose *what* is wrong: a low score says there is a problem, not where it is. The short instruments are too short to diagnose anything. And the score is not a percentage or a percentile, even though its range is 0-100.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
These questionnaires are a **direct** measure of *perceived* usability, in the sense that the construct is defined by what people report. They are a **proxy** for usability in the ISO 9241-11 sense (effectiveness, efficiency, and satisfaction), because only the satisfaction part is observed directly [iso9241-11]. Hence `measure_type: mixed`.

### 2.2 Reliability
Multi-item perceived-usability questionnaires are internally consistent; shorter instruments trade some reliability for brevity. Reliability of a *mean* score depends on sample size; small samples give wide confidence intervals [sauro2016]. Figures for each instrument are in 2.6.

### 2.3 Data collection and measurement error
Given on paper or online right after a session or a set of tasks. Error sources include recency (the last task dominates), social desirability toward the moderator, respondents misreading negatively worded items, and ceiling effects for simple systems.

### 2.4 Computation
For each respondent, each item response is turned into an item score, with negatively worded items reversed; the item scores are summed and rescaled to 0-100. Report the mean with a confidence interval across respondents. Each instrument's exact rule is in 2.6.

### 2.5 Unit and scale
A dimensionless score from 0 to 100 for all the instruments listed, usually treated as interval data. It is not a percentage. Scores are most meaningful when compared with the same system over time or with competitors measured with the same instrument; norms are instrument-specific (2.6).

### 2.6 Instruments
- **System Usability Scale (SUS)** [brooke1996]. Ten statements, alternately positive and negative, on a five-point agreement scale.
  - *Scoring:* odd-numbered (positive) items contribute (response − 1); even-numbered (negative) items contribute (5 − response). Sum the ten contributions (0-40) and multiply by 2.5 to get 0-100 [brooke1996].
  - *Reliability and norms:* Bangor et al. reported a coefficient alpha of about 0.91 over a large set of studies [bangor2008]. A commonly cited average across many studies is about 68 [sauro2016], and adjective labels ("OK", "good", "excellent") have been mapped to score ranges [bangor2009]. A variant with all items worded positively gives similar scores and avoids some misreading [sauro2011positive].
  - *Choose it* by default: it has the most published norms and benchmarks.
- **Usability Metric for User Experience (UMUX)** [finstad2010]. Four items about how well the system meets the person's needs, how frustrating and how easy it is, and how much time it takes to correct things.
  - *Scoring:* 7-point items, odd items scored as response − 1 and even items as 7 − response, summed and rescaled to 0-100 (check against [finstad2010]).
  - *Reliability:* acceptable internal consistency for a short scale (check against [finstad2010]). Designed so its scores correspond to SUS scores (check against the paper).
- **UMUX-LITE** [lewis2013]. The two positively worded UMUX items.
  - *Scoring:* rescaled to 0-100; a regression adjustment to align with SUS has been proposed (check against [lewis2013]).
  - *Choose it* for in-app or exit surveys where SUS is too long [lewis2018].
- Other perceived-usability questionnaires, such as PSSUQ, are close substitutes; they have no entry here yet.

Do not compare scores across instruments without the published conversions, and keep the instrument fixed within a study.

## 3. Why it is measured

### 3.1 Use cases
- A UX team runs SUS after a usability test comparing two onboarding flows for a budgeting app, to decide which design to ship.
- An enterprise software vendor gives SUS to pilot customers' employees after rolling out a new CRM feature, as one input into the renewal conversation.
- A research team studying an AI writing assistant administers SUS after each session, reporting it alongside task performance in a paper.
- A SaaS team adds UMUX-LITE to an in-app survey because SUS is too long for a pop-up [lewis2013].

### 3.2 Purposes
Quick benchmark of perceived usability; before-and-after comparisons across design iterations; comparison of alternative designs; a standard number to report to stakeholders. Common in HCI and increasingly in human-AI and explainable AI user studies [kim2024; rong2022].

### 3.3 Assumptions
That respondents have used the system enough to judge it. That a few generic items capture what matters for this system (for AI systems, trust and output quality may matter more and are not asked about). That the respondent population resembles the eventual users. That the score's meaning carries across cultures and translations.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers, product teams and study teams. Cost is low per participant (a minute or two), but it needs participants who have actually used the system, so it cannot be computed automatically from logs.

### 4.2 Consumers and decisions informed
Product and design teams (did the redesign help?), managers (is the product at an acceptable level?), and researchers (is condition A perceived as more usable than B?).

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Reading 70 as "70%" is a common mistake. Comparing scores across very different tasks or populations is misleading. Scores can be inflated by moderator presence, by selecting friendly participants, or by giving the questionnaire only after easy tasks. As a target, it invites polishing the surface experience without improving task outcomes [strathern1997].

## 5. Related metrics

### 5.1 Operationally related metrics
The SUS "usable" and "learnable" subscores (1.2) are computed from subsets of the same ten items [lewis2009]. UMUX-LITE is a subset of UMUX.

### 5.2 Conceptually related metrics
[Mental Workload Score (questionnaire)](mental-workload-score.md) is complementary: it asks about demand on the person rather than qualities of the system. [User Experience Score (questionnaire)](user-experience-score.md) adds hedonic qualities. [Task Completion Time](task-completion-time.md) and task success are complementary objective measures; a questionnaire is cheaper to add to a study than careful timing, but it says nothing about actual performance.

<!-- generated:neighbours:start -->
- Sibling construct: [Task Success Rate (user on task)](task-success-rate-user.md) (Task effectiveness), [Task Completion Time](task-completion-time.md) (Task efficiency)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Across studies, perceived-satisfaction measures correlate only modestly with efficiency and effectiveness measures [hornbaek2007], with somewhat stronger correlations when measured at the task level [sauro2009]. So improving task time will not reliably raise SUS, and vice versa. Slower response times plausibly lower SUS; see [Response Latency](response-latency.md).

## 6. Links to business objectives
**Improved usability:** positive, correlational. The score measures perceived usability by definition, and it tracks objective usability only moderately.

**Sustained use:** positive, theoretical. The Technology Acceptance Model links perceived ease of use to intention to use [davis1989], and the expectation-confirmation model links satisfaction to continued use [bhattacherjee2001]. Reviews of human-centered XAI note that most studies stop at intention rather than logged continued use [kim2024]. Whether the score predicts retention in a given product should be checked against logs.

## 7. Sources
- [brooke1996]: SUS and its scoring.
- [finstad2010]: UMUX. [lewis2013]: UMUX-LITE.
- [bangor2008], [bangor2009], [lewis2009], [lewis2018], [sauro2011positive]: psychometrics, norms, variants.
- [sauro2009], [hornbaek2007]: correlations with other usability measures.
- [davis1989], [bhattacherjee2001]: theoretical path to sustained use.
- [kim2024], [rong2022]: use in human-centered XAI evaluation.

## Open questions and review notes
Merged from the former SUS and UMUX pages (D25). Issues filed against the SUS page are tracked in GitHub Issues: [#5](https://github.com/HAMI-Lab/metrics-kb/issues/5) (flip bibliography `verified` flags after reviewer check), [#6](https://github.com/HAMI-Lab/metrics-kb/issues/6) (closed — trust/output-quality items, decision recorded), [#7](https://github.com/HAMI-Lab/metrics-kb/issues/7) (reconsider "causally-linked" relation to Response Latency), [#8](https://github.com/HAMI-Lab/metrics-kb/issues/8) (consider adding Hertzum 2026 as a source).
