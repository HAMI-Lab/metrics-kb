---
id: mental-workload-score
title: Mental Workload Score (questionnaire)
aliases: [NASA-TLX, NASA Task Load Index, TLX, Raw TLX, RTLX, SMEQ, Subjective Mental Effort Questionnaire, Rating Scale Mental Effort, RSME, perceived workload]
page_type: metric
template_version: "0.3"
fields: [hci, human-factors, human-ai-interaction, visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much demand and effort a person reports a task placed on them, rated right after the task."
  measures: [mental-workload]
  subject: [user]
  aspect: [workload]
  perspective: [perceived]
  quantity_form: [rating-score, composite-index]
  context: [task, user-specific]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [questionnaire-survey]
  route: [self-rating]
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "workload or effort score (dimensionless)"
  range: "0-100 (NASA-TLX); 0-150 (SMEQ)"
  better: context-dependent
  validity_concern: {level: moderate, note: "Self-reported workload; may differ from physiological or performance-based workload measures."}
  instruments:
    - {name: "NASA Task Load Index (NASA-TLX)", sources: [hart1988, hart2006], note: "Six subscales rated 0-100, combined by pairwise weights (weighted TLX) or a plain mean (Raw TLX)."}
    - {name: "Subjective Mental Effort Questionnaire (SMEQ)", sources: [zijlstra1985], note: "One vertical scale, 0 to about 150, with verbal labels; mental effort only."}

cost:
  level: medium
  requires: [participants, "seconds per task (SMEQ) to 1-2 minutes per task (Raw TLX), longer with TLX weighting"]
  automatable: false

related:
  - {metric: perceived-usability-score, kind: conceptual, note: "Demand on the person vs. perceived qualities of the system."}
  - {metric: task-completion-time, kind: empirical, note: "Time pressure is one TLX subscale, and harder tasks usually take longer; the two often but not always move together."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "High workload is assumed to discourage continued use; not established with retention data here."}
  improved-usability: {direction: negative, evidence: correlational, note: "Lower workload for the same outcome is generally read as better usability, but too little demand can signal disengagement."}

sources: [hart1988, hart2006, zijlstra1985, sauro2009onequestion, iso9241-11, kim2024, rong2022, gambetti2025]
---

# Mental Workload Score (questionnaire)

> A short questionnaire, given after a task, on which a person rates how demanding or effortful the task was, such as NASA-TLX (six subscales) or SMEQ (one scale).

## 1. What is measured

### 1.1 Definition
Right after a task, a person rates the workload it placed on them on a standardized questionnaire. NASA-TLX asks about six subscales: mental demand, physical demand, temporal demand, performance, effort, and frustration, and combines them into an overall score [hart1988]. SMEQ asks only about mental effort, on one scale [zijlstra1985]. Section 2.6 compares them.

### 1.2 Construct: property of subject in context
The property is **perceived workload**. The subject is the **user**. The context is a specific **task** done with a specific system by a specific person. The same system can produce very different scores for novices and experts.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Mental workload](../constructs/mental-workload.md) (under Task characteristics → Task performance → Task efficiency; Task characteristics → Usability → Task efficiency)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure the system's quality directly: a hard task can have high workload even with an excellent tool. It does not measure workload *during* the task moment by moment; it is a single retrospective judgment. And it does not tell you which interface element caused the load. SMEQ covers mental effort only, not physical demand, time pressure or frustration.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
The questionnaires are a **direct** measure of *perceived* workload and a **proxy** for the cognitive resources actually spent. Physiological measures (pupil dilation, heart-rate variability, EEG) and secondary-task performance get closer to resource use and can track it continuously, but they cost far more in equipment and expertise. This is a typical cheap-proxy vs. costly-direct trade-off. (TODO: add pages and sources for those measures.)

**Using a proxy with a known gap.** The score can compare designs or assistance conditions within one study on how demanding people found them. It cannot show how much cognitive capacity was used, or whether people had spare capacity to catch errors. Before relying on it for safety-critical decisions, pair it with a performance measure under load.

### 2.2 Reliability
NASA-TLX has been used and validated in many domains since the 1980s [hart2006]. (TODO: add specific test-retest or internal-consistency figures from a verified source.) SMEQ is a single item, but sensitive to differences between tasks in comparisons with other one-question measures [sauro2009onequestion] (check against the paper).

### 2.3 Data collection and measurement error
Given right after each task, on paper or on screen. Errors come from memory decay (long tasks), anchoring on the first task rated, confusion about the TLX *performance* subscale (whose scale runs from "perfect" to "failure", opposite to the others), and differences in how individuals use the scale.

### 2.4 Computation
- **NASA-TLX:** each subscale is rated from 0 to 100 (the original paper form has 21 marks in steps of 5).
  - **Weighted TLX** (original): the person also makes 15 pairwise comparisons of the subscales; each subscale's weight is how many times it was chosen, and the overall score is the weighted mean [hart1988].
  - **Raw TLX (RTLX):** the unweighted mean of the six ratings. Widely used because it is quicker; Hart's 20-year review discusses its use [hart2006].
  - Many studies also report the six subscales separately, which is often more informative than the overall score.
- **SMEQ:** the position marked, 0-150. Average per task across participants.

### 2.5 Unit and scale
Dimensionless: 0-100 for NASA-TLX, 0-150 for SMEQ. There is no universal "acceptable" threshold; scores are best compared across conditions within one study, with the same instrument.

### 2.6 Instruments
- **NASA Task Load Index (NASA-TLX)** [hart1988; hart2006]: multi-dimensional. Choose it when you need to know *which kind* of demand changed (time pressure vs. frustration, for example), or when comparing with the large body of TLX studies.
- **Subjective Mental Effort Questionnaire (SMEQ)** [zijlstra1985]: one scale with verbal labels from "not at all hard to do" to "tremendously hard to do". Choose it for a quick rating after every task in a usability test [sauro2009onequestion]. It corresponds to the mental-demand side of TLX.

## 3. Why it is measured

### 3.1 Use cases
- An automotive HMI team compares perceived workload across two in-car voice-assistant designs, to decide which is safe to ship to drivers.
- A hospital runs a simulated-scenario study to check whether a new clinical-decision-support alert adds to nurses' workload during a shift.
- A research team studying an AI pair-programming assistant gives TLX after coding sessions to see whether suggestions add or reduce cognitive load.
- A usability test of a tax-filing app asks for SMEQ after each task to find the most effortful step.

### 3.2 Purposes
Comparing designs or AI-assistance conditions for how demanding they are; checking that added features (such as explanations) do not overload people [rong2022; gambetti2025]; finding the most effortful steps in a usability test [sauro2009onequestion]; safety-critical work where overload leads to errors.

### 3.3 Assumptions
That people can introspect on and report their workload right after the task. That the questions cover the relevant kinds of demand (for AI assistance, demands such as checking the AI's output may not map neatly). That lower is better, which does not always hold (see 4.3).

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Human factors and UX researchers. Cheap per task, but it needs participants and repeats after every task, which adds up in long studies.

### 4.2 Consumers and decisions informed
Designers choosing between alternatives; safety and operations teams deciding whether a workflow is sustainable; researchers testing whether assistance reduces load.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Treating lower as always better: very low demand can mean people have handed judgment to the system and stopped checking it, which matters for human-AI reliance. Comparing absolute scores across studies with different tasks. Averaging away informative subscale differences.

## 5. Related metrics

### 5.1 Operationally related metrics
The six TLX subscale ratings are parts of the overall score. Raw TLX is a common variant (see 2.4).

### 5.2 Conceptually related metrics
Same construct, different operationalization: physiological workload measures and secondary-task performance (no pages yet). Complementary: [Perceived Usability Score (questionnaire)](perceived-usability-score.md) (system qualities), [Task Completion Time](task-completion-time.md) and task success (outcomes).

<!-- generated:neighbours:start -->
- Broader construct: [Task Completion Time](task-completion-time.md) (Task efficiency)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Workload often rises with task time and time pressure, and falls as users gain expertise. Speed and accuracy can be bought with extra effort, so an improvement in performance with a rise in workload may not be a net gain. (TODO: add correlation evidence.)

## 6. Links to business objectives
**Improved usability:** lower workload for the same outcome is generally read as better usability; the ISO definition includes resources spent, of which effort is one [iso9241-11]. Evidence strength: correlational, and non-monotonic at the low end.

**Sustained use:** high workload is assumed to discourage continued use. Evidence: theoretical only; reviews note that human-centered XAI studies rarely follow up on actual continued use [rong2022].

## 7. Sources
- [hart1988]: NASA-TLX; [hart2006]: 20-year review including Raw TLX.
- [zijlstra1985]: SMEQ.
- [sauro2009onequestion]: comparison of one-question post-task measures.
- [iso9241-11]: usability definition.
- [kim2024], [rong2022], [gambetti2025]: use of TLX in XAI and clinical decision-support evaluation.

## Open questions and review notes
- Merged from the former NASA-TLX and SMEQ pages (D25).
- Add verified reliability figures and a source on physiological workload measures.
- The usability link is marked `negative` in front matter; should it be `non-monotonic` given the low-end caveat?
- ReVISit lists the SMEQ year as 1985; some sources date the scale to 1993. Check the original report.
