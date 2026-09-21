---
id: nasa-tlx
title: NASA Task Load Index (NASA-TLX)
aliases: [NASA-TLX, TLX, Raw TLX, RTLX]
page_type: metric
template_version: "0.1"
fields: [hci, human-factors, human-ai-interaction, visualization]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much mental, physical, and time demand a person felt while doing a task, and how much effort, frustration, and (in)success they felt, combined into one workload score."
  subject: [user]
  aspect: [workload]
  perspective: [perceived]
  quantity_form: [rating-score, composite-index]
  context: [task, user-specific]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [in-lab, field]
  data_source: [questionnaire]
  unit: "workload score (dimensionless)"
  range: "0-100"
  better: context-dependent

cost:
  level: medium
  requires: [participants, "about 1-2 minutes per task for Raw TLX, longer with weighting"]
  automatable: false

related:
  - {metric: system-usability-scale, relation: complementary, note: "Demand on the person vs. perceived qualities of the system."}
  - {metric: task-completion-time, relation: correlated, note: "Time pressure is one TLX subscale; the two often but not always move together."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "High workload is assumed to discourage continued use; not established with retention data here."}
  improved-usability: {direction: negative, evidence: correlational, note: "Lower workload for the same outcome is generally read as better usability, but too little demand can signal disengagement."}

sources: [hart1988, hart2006, iso9241-11, S13, S15, S18]
---

# NASA Task Load Index (NASA-TLX)

> A short questionnaire, given after a task, that rates perceived workload on six subscales and combines them into one 0-100 score.

## 1. What is measured

### 1.1 Definition
NASA-TLX asks a person to rate a task they just did on six subscales: mental demand, physical demand, temporal demand, performance, effort, and frustration [hart1988]. The ratings are combined into an overall workload score.

### 1.2 Construct: property of subject in context
The property is **perceived workload**. The subject is the **user**. The context is a specific **task** done with a specific system by a specific person. The same system can produce very different TLX scores for novices and experts.

### 1.3 What it does not measure
It does not measure the system's quality directly: a hard task can have high workload even with an excellent tool. It does not measure workload *during* the task moment by moment; it is a single retrospective judgment. And it does not tell you which interface element caused the load.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
TLX is a **direct** measure of *perceived* workload and a **proxy** for the cognitive resources actually spent. Physiological measures (pupil dilation, heart-rate variability, EEG) and secondary-task performance get closer to resource use and can track it continuously, but they cost far more in equipment and expertise. This is a typical cheap-proxy vs. costly-direct trade-off. (TODO: add pages and sources for those measures.)

### 2.2 Reliability
TLX has been used and validated in many domains since the 1980s [hart2006]. (TODO: add specific test-retest or internal-consistency figures from a verified source.)

### 2.3 Data collection and measurement error
Given right after each task, on paper or on screen. Errors come from memory decay (long tasks), anchoring on the first task rated, confusion about the *performance* subscale (whose scale runs from "perfect" to "failure", opposite to the others), and differences in how individuals use the scale.

### 2.4 Computation
Each subscale is rated from 0 to 100 (the original paper form has 21 marks in steps of 5).
- **Weighted TLX** (original): the person also makes 15 pairwise comparisons of the subscales; each subscale's weight is how many times it was chosen, and the overall score is the weighted mean [hart1988].
- **Raw TLX (RTLX)**: the unweighted mean of the six ratings. Widely used because it is quicker; Hart's 20-year review discusses its use [hart2006].

Many studies also report the six subscales separately, which is often more informative than the overall score.

### 2.5 Unit and scale
Dimensionless, 0-100. There is no universal "acceptable" threshold; scores are best compared across conditions within one study.

## 3. Why it is measured

### 3.1 Purposes
Comparing designs or AI-assistance conditions for how demanding they are; checking that added features (such as explanations) do not overload people [S15; S18]; safety-critical work where overload leads to errors.

### 3.2 Assumptions
That people can introspect on and report their workload. That the six subscales cover the relevant kinds of demand (for AI assistance, demands such as checking the AI's output may not map neatly). That lower is better, which does not always hold (see 4.3).

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Human factors and UX researchers. Cheap per task, but it needs participants and repeats after every task, which adds up in long studies.

### 4.2 Consumers and decisions informed
Designers choosing between alternatives; safety and operations teams deciding whether a workflow is sustainable; researchers testing whether assistance reduces load.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Treating lower as always better: very low demand can mean people have handed judgment to the system and stopped checking it, which matters for human-AI reliance. Comparing absolute scores across studies with different tasks. Averaging away informative subscale differences.

## 5. Related metrics

### 5.1 Static relationships
Same construct, different operationalization: single-item workload scales, physiological workload measures, secondary-task performance. Complementary: [SUS](system-usability-scale.md) (system qualities), [Task Completion Time](task-completion-time.md) and task success (outcomes).

### 5.2 Dynamic relationships
Workload often rises with task time and time pressure, and falls as users gain expertise. Speed and accuracy can be bought with extra effort, so an improvement in performance with a rise in TLX may not be a net gain. (TODO: add correlation evidence.)

## 6. Links to business objectives
**Improved usability:** lower workload for the same outcome is generally read as better usability; the ISO definition includes resources spent, of which effort is one [iso9241-11]. Evidence strength: correlational, and non-monotonic at the low end.

**Sustained use:** high workload is assumed to discourage continued use. Evidence: theoretical only; reviews note that human-centered XAI studies rarely follow up on actual continued use [S15].

## 7. Sources
- [hart1988] original instrument; [hart2006] 20-year review including Raw TLX.
- [iso9241-11] usability definition.
- [S13], [S15], [S18]: use of TLX in XAI and clinical decision-support evaluation.

## Open questions and review notes
- Add verified reliability figures and a source on physiological workload measures.
- The usability link is marked `negative` in front matter; should it be `non-monotonic` given the low-end caveat?
