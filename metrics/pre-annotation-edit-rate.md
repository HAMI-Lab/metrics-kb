---
id: pre-annotation-edit-rate
title: Pre-annotation Edit Rate
aliases: [correction rate, model-suggestion edit rate, acceptance rate (its complement), human edit distance on pre-labels]
page_type: metric
template_version: "0.2"
fields: [data-annotation, human-ai-interaction, computer-vision]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the annotations a model proposed before a person started labeling, the share the person changed or deleted before submitting."
  measures: [pre-annotation-quality]
  subject: [system-component, user-system-team]
  aspect: [effectiveness, trust]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task, system-specific]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [logs-telemetry]
  route: [external-judgment]
  collection_mode: [offline, field]
  data_source: [interaction-logs]
  unit: "proportion of model keyframes (or tracks)"
  range: "0-1"
  better: context-dependent
  validity_concern: {level: high, note: "Untouched model labels may be unchecked rather than correct (automation bias); validate against a gold sample."}

cost:
  level: low
  requires: ["per-annotation provenance (model vs human) kept through the edit and submit path"]
  automatable: true

related:
  - {metric: precision, kind: conceptual, note: "A model with low precision forces many deletions; edit rate is a human-observed stand-in for model precision."}
  - {metric: object-track-completeness, kind: conceptual, note: "Edit rate sees what was changed; it cannot see objects the model missed and the person also missed."}
  - {metric: active-labeling-time-per-object, kind: empirical, note: "More edits are expected to take more time; the size of the link is unknown."}

objectives:
  sustained-use: {direction: non-monotonic, evidence: theoretical, note: "Very high edit rates make pre-annotation pointless; near-zero rates can mean blind acceptance rather than good models."}
  improved-usability: {direction: unknown, evidence: none, note: "Measures model fit to labeler judgment more than tool usability."}

sources: [manning2008, vondrick2013, parasuraman2010]
---

# Pre-annotation Edit Rate

> How much of the model's proposed labeling did the person have to change?

## 1. What is measured

### 1.1 Definition
Among annotations that came from a model (imported pre-annotations), the share that the labeler moved, resized, re-identified, or deleted before submitting. Reported at two units: keyframes and tracks.

### 1.2 Construct: property of subject in context
The property is **how far the model's proposal was from what the person accepted as correct**. The subject is the **pre-annotation model as seen through the labeler**, and partly the labeler's own checking behavior. The context is a **task** (one video) in a **system-specific** setting: the number depends on how the tool records edits.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Annotation quality: pre-annotation quality](../constructs/pre-annotation-quality.md) (under Output quality → Annotation quality)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
It does not measure model quality directly: an unchanged model box may be wrong and simply unchecked. It does not count objects the model missed and the person added (count those separately as "added tracks"). It does not measure effort: one deletion and one careful resize count the same.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy.** It stands in for model error as judged by the labeler. It is valid only if labelers check pre-annotations carefully; under automation bias (accepting suggestions without checking) [parasuraman2010], low edit rates overstate model quality. Validate against [Object-Track Completeness](object-track-completeness.md) on a gold sample.

### 2.2 Reliability
Depends on labeler checking habits and on tool behavior: a tool that silently rewrites model boxes (for example when interpolation or merge reshapes a track) inflates the rate. Compare within the same tool version.

### 2.3 Data collection and measurement error
Computed offline from submitted labels if each annotation carries its provenance.

Example, InfinityPool: each keyframe already carries `source: 'human' | 'model' | 'generated'` and an optional model `score` (`packages/shared/src/validators/label_validator.ts`). `keyframeProvenance.ts` flips a box to `human` when a labeler moves or creates it, and treats merges and splits separately. So the edit rate can be computed from the import JSON and the submitted label, with no new logging. Two gaps: (1) deletions are only visible by diffing against the imported taskset, so keep the import file; (2) a box the labeler confirmed without changing looks the same as one never looked at. Adding an explicit "reviewed" mark, or logging which frames were visited, would close the second gap.

### 2.4 Computation
- Keyframe edit rate = model keyframes changed or deleted ÷ model keyframes imported.
- Track edit rate = model tracks with any change (including ID merge/split or deletion) ÷ model tracks imported.
- Report separately: added tracks per video (model misses fixed by the person).
- Optional: bin by model `score` to see whether low-confidence boxes are the ones edited; if so, a confidence threshold at import could skip them.

### 2.5 Unit and scale
Proportion 0 to 1 (ratio). There is no universal "good" value; it is mainly a trend and comparison measure across model versions.

## 3. Why it is measured

### 3.1 Use cases
- InfinityPool: comparing two pre-annotation tracker versions by how much labelers corrected each, before choosing one for the next taskset.
- InfinityPool: deciding a confidence cutoff for importing pre-annotations, by checking edit rate per score bin.
- A medical-imaging team tracks how often radiologists change AI-drafted lesion outlines, as an early warning of model drift.
- A document-OCR vendor tracks how much of the machine transcription reviewers correct per page type.

### 3.2 Purposes
Cheap monitoring of pre-annotation model usefulness; choosing model versions and import thresholds; spotting blind acceptance (when compared with a gold check).

### 3.3 Assumptions
That every change a labeler makes is a correction, not a style preference. That untouched means accepted after checking. That provenance is recorded faithfully by the tool.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Developers or ML engineers, from stored data. Near zero cost once provenance is kept.

### 4.2 Consumers and decisions informed
ML engineers (which model to ship for pre-annotation); project managers (whether pre-annotation is worth it for a taskset type); developers (whether the tool's own reshaping inflates edits).

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
If labelers are rewarded for low edit rates, or if it is read as "model is good", it rewards not checking. If ML teams are judged on it, they may tune models toward what labelers do not bother to fix. Do not use it as a labeler performance score.

## 5. Related metrics

### 5.1 Operationally related metrics
Added tracks per video and the edit rate per model-score bin (2.4) are computed from the same diff.

### 5.2 Conceptually related metrics
A human-observed stand-in for model [Precision](precision.md) (deletions) and localization error (resizes) [manning2008]. Complementary: [Object-Track Completeness](object-track-completeness.md), which sees misses. Cheaper than a gold-standard model evaluation, but only valid when checking is careful.

<!-- generated:neighbours:start -->
- Sibling construct: [Object-Track Completeness](object-track-completeness.md) (Annotation quality: completeness), [Frame-Sync Accuracy](frame-sync-accuracy.md) (Annotation tool: temporal alignment)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Video annotation work has long traded labeler effort against automated interpolation and tracking [vondrick2013]; better pre-annotation should lower edit rate and labeling time together. Whether it does here is untested.

## 6. Links to business objectives
**Sustained use:** non-monotonic, theoretical. Labelers abandon pre-annotation that needs too many fixes; very low rates may hide blind acceptance.

**Improved usability:** unknown, no evidence. It reflects the model more than the interface.

## 7. Sources
- [manning2008]: precision as the counterpart.
- [vondrick2013]: cost and quality trade-offs in video annotation with interpolation and tracking.
- [parasuraman2010]: automation bias.

## Open questions and review notes
- **For team deliberation (InfinityPool interview, 2026-10-19):**
  - Is this a primary or secondary metric? Proposed as secondary for goal G2 (pre-annotation saves effort), since it reflects the model more than the tool.
  - Should an explicit "reviewed this track" action be added so that untouched-and-checked differs from untouched-and-unseen? It costs labeler clicks.
  - Alternative: compare model output directly to the gold set (model completeness and precision) and skip the human-observed proxy. More valid, but needs gold labels for every model version.
  - What share of InfinityPool work is pre-annotated vs from scratch? Not yet known; it decides how much this metric matters.
