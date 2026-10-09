---
id: system-usability-scale
title: System Usability Scale (SUS)
aliases: [SUS]
page_type: metric
template_version: "0.1"
fields: [hci, human-ai-interaction, visualization, information-retrieval]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How usable people who have just used a system perceive it to be, summarized as one score."
  subject: [system, user]
  aspect: [ease-of-use, satisfaction]
  perspective: [perceived]
  quantity_form: [rating-score]
  context: [task, system-specific, user-specific]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "SUS score (dimensionless)"
  range: "0-100"
  better: higher

cost:
  level: medium
  requires: [participants who have used the system, "about 1-2 minutes per participant"]
  automatable: false

related:
  - {metric: nasa-tlx, relation: complementary, note: "SUS asks about the system; NASA-TLX asks about the demand the task placed on the person."}
  - {metric: task-completion-time, relation: complementary, note: "Objective efficiency vs. perceived usability; correlations are modest."}
  - {metric: response-latency, relation: causally-linked, note: "Slow responses plausibly lower perceived usability; not quantified for SUS specifically."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Via perceived ease of use -> intention to use (TAM), and satisfaction -> continuance (expectation-confirmation model). Links to logged retention for SUS itself are not established here."}
  improved-usability: {direction: positive, evidence: correlational, note: "SUS is a perceived-usability measure by construction; its correlation with objective usability measures is moderate."}

sources: [brooke1996, bangor2008, bangor2009, lewis2009, sauro2011positive, lewis2018, sauro2009, hornbaek2007, davis1989, bhattacherjee2001, iso9241-11, sauro2016, strathern1997, S13, S15]
---

# System Usability Scale (SUS)

> A 10-item questionnaire that gives one 0-100 score for how usable people perceive a system to be, cheap enough to run after almost any usability study.

## 1. What is measured

### 1.1 Definition
SUS is a standardized questionnaire of ten statements about a system, answered on a five-point agreement scale right after the respondent has used the system [brooke1996]. The responses are combined into one score from 0 to 100.

### 1.2 Construct: property of subject in context
The property is **perceived usability**, which blends ease of use and satisfaction. The subject is the **system**, as judged by a **user**. The context is the use the respondent just had: the tasks they did and who they are. A SUS score therefore describes the system *for these people doing these tasks*, not the system in general.

Factor analyses suggest SUS has two related parts, often called "usable" (eight items) and "learnable" (two items) [lewis2009], though later work questions how stable that split is [lewis2018]. Most practice treats it as one overall score.

### 1.3 What it does not measure
It does not measure objective performance. People can rate a system highly and still fail tasks, or the reverse [sauro2009; hornbaek2007]. It also does not diagnose *what* is wrong: a low score says there is a problem, not where it is. And it is not a percentage or a percentile, even though its range is 0-100.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
SUS is a **direct** measure of *perceived* usability, in the sense that the construct is defined by what people report. It is a **proxy** for usability in the ISO 9241-11 sense (effectiveness, efficiency, and satisfaction), because only the satisfaction part is observed directly [iso9241-11]. Hence `measure_type: mixed`.

### 2.2 Reliability
Internal consistency is high; Bangor et al. reported a coefficient alpha of about 0.91 over a large set of studies [bangor2008]. Reliability of a *mean* score depends on sample size; small samples give wide confidence intervals [sauro2016].

### 2.3 Data collection and measurement error
Given on paper or online right after a session or a set of tasks. Error sources include recency (the last task dominates), social desirability toward the moderator, respondents misreading the negatively worded items, and ceiling effects for simple systems. A variant with all items worded positively gives similar scores and avoids some misreading [sauro2011positive].

### 2.4 Computation
For each respondent: odd-numbered (positive) items contribute (response − 1); even-numbered (negative) items contribute (5 − response). Sum the ten contributions (0-40) and multiply by 2.5 to get 0-100 [brooke1996]. Report the mean with a confidence interval across respondents.

### 2.5 Unit and scale
A dimensionless score, 0-100. Usually treated as interval data. A commonly cited average across many studies is about 68 [sauro2016]. Adjective labels ("OK", "good", "excellent") have been mapped to score ranges [bangor2009]. Scores are most meaningful when compared with the same system over time or with competitors measured the same way.

## 3. Why it is measured

### 3.1 Purposes
Quick benchmark of perceived usability; before-and-after comparisons across design iterations; comparison of alternative designs; a standard number to report to stakeholders. Common in HCI and increasingly in human-AI and explainable AI user studies [S13; S15].

### 3.2 Assumptions
That respondents have used the system enough to judge it. That ten generic items capture what matters for this system (for AI systems, trust and output quality may matter more and are not asked about). That the respondent population resembles the eventual users. That the score's meaning carries across cultures and translations.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
UX researchers and study teams. Cost is low per participant (a minute or two), but it needs participants who have actually used the system, so it cannot be computed automatically from logs.

### 4.2 Consumers and decisions informed
Product and design teams (did the redesign help?), managers (is the product at an acceptable level?), and researchers (is condition A perceived as more usable than B?).

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Reading 70 as "70%" is a common mistake. Comparing scores across very different tasks or populations is misleading. Scores can be inflated by moderator presence, by selecting friendly participants, or by giving the questionnaire only after easy tasks. As a target, it invites polishing the surface experience without improving task outcomes [strathern1997].

## 5. Related metrics

### 5.1 Static relationships
Other perceived-usability questionnaires (for example UMUX, UMUX-LITE, PSSUQ) are close substitutes. [NASA-TLX](nasa-tlx.md) is complementary: it asks about demand on the person rather than qualities of the system. [Task Completion Time](task-completion-time.md) and task success are complementary objective measures; SUS is cheaper to add to a study than careful timing, but it says nothing about actual performance.

### 5.2 Dynamic relationships
Across studies, perceived-satisfaction measures correlate only modestly with efficiency and effectiveness measures [hornbaek2007], with somewhat stronger correlations when measured at the task level [sauro2009]. So improving task time will not reliably raise SUS, and vice versa. Slower response times plausibly lower SUS; see [Response Latency](response-latency.md).

## 6. Links to business objectives
**Improved usability:** positive, correlational. SUS measures perceived usability by definition, and it tracks objective usability only moderately.

**Sustained use:** positive, theoretical. The Technology Acceptance Model links perceived ease of use to intention to use [davis1989], and the expectation-confirmation model links satisfaction to continued use [bhattacherjee2001]. Reviews of human-centered XAI note that most studies stop at intention rather than logged continued use [S13]. Whether SUS predicts retention in a given product should be checked against logs.

## 7. Sources
- [brooke1996] original instrument and scoring.
- [bangor2008], [bangor2009], [lewis2009], [lewis2018], [sauro2011positive]: psychometrics, norms, variants.
- [sauro2009], [hornbaek2007]: correlations with other usability measures.
- [davis1989], [bhattacherjee2001]: theoretical path to sustained use.
- [S13], [S15]: use in human-centered XAI evaluation.

## Open questions and review notes
- AI-suggested references are marked `verified: false` in the bibliography; check them.
- Should AI-assistant studies use SUS as is, or add trust or output-quality items? Decide whether that belongs here or on a separate page.

*Notes:*
1. *All checked -> `verified: true`*
2. *Use SUS unchanged when reporting a SUS score. Trust and output quality are separate constructs and could be covered on a separate metric page; they can be noted here as complementary measures.*
3. *"causally-linked" may be stronger than the SUS-specific evidence currently supports. Consider a weaker relation label (e.g., "correlated"), or clarify that the causal evidence is indirect and not SUS-specific.*
4. *Consider adding [Hertzum (2026)](https://doi.org/10.1080/10447318.2026.2625260), a meta-analysis of 105 studies comparing SUS with workload, task time, and error rate. It provides newer SUS-specific evidence for the relationships with NASA-TLX and task-completion measures.*
