---
id: object-track-completeness
title: Object-Track Completeness
aliases: [track recall, object recall in video, "frame-coverage recall", mostly-tracked ratio]
page_type: metric
template_version: "0.1"
fields: [computer-vision, data-annotation, human-ai-interaction]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of all the objects of interest that appear in a video, the share that the finished labels track, counted per object and per frame of visibility."
  subject: [user-system-team]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher

cost:
  level: medium
  requires: ["gold-standard tracks for a sample of videos (two careful labelers plus adjudication)", "a matching rule (IoU threshold) between labeled and gold boxes"]
  automatable: true

related:
  - {metric: recall, relation: same-construct, note: "A recall variant for video tracks: the unit is an object (or object-frame) instead of a document."}
  - {metric: precision, relation: trade-off, note: "Labeling every blob raises completeness and adds false tracks; report false-track rate alongside."}
  - {metric: active-labeling-time-per-object, relation: trade-off, note: "Faster labeling is only a gain if completeness holds."}
  - {metric: pre-annotation-edit-rate, relation: correlated, note: "Low edit rate with low completeness suggests labelers accepted model misses."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Teams keep using a labeling tool whose output they do not have to re-check; not tested."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Effectiveness is one of the three ISO usability parts; here it is the joint output of labeler and tool."}

sources: [manning2008, bernardin2008, ristani2016, luiten2021, iso9241-11, parasuraman2010]
---

# Object-Track Completeness

> Did the finished labels track every object of interest, for every frame it is visible?

## 1. What is measured

### 1.1 Definition
The share of gold-standard objects in a video that the submitted labels cover. Two readings, both reported:
- **Object-level**: an object counts as tracked if a labeled track matches it on at least a set share of its visible frames (for example 80%, the "mostly tracked" idea from tracking benchmarks).
- **Frame-level**: of all (object, frame) pairs where an object of interest is visible, the share covered by a matching labeled box.

### 1.2 Construct: property of subject in context
The property is **completeness of labeled output**. The subject is the **labeler and tool together**: misses come from the person overlooking an object, from the tool (interpolation drift moving a box off its object, lost work), or from a pre-annotation model that missed the object and the labeler did not add it. The context is a **task**: one video with a taskset's object classes.

### 1.3 What it does not measure
Not box tightness (localization error), not false tracks (that is a precision-type count), and not identity consistency (one object split across several track IDs still counts as covered). These are separate numbers; see 2.4. It also says nothing about effort or time.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for "the labels cover the gold objects." **Proxy** for "the labels are good enough to train a model", which also depends on box quality and ID consistency. Validity rests on the gold standard: if the gold set itself misses objects, completeness is overstated. Hence `measure_type: mixed`.

### 2.2 Reliability
Depends on agreement about what counts as an "object of interest" (partly occluded, tiny, at the frame edge). Measure agreement between the two gold labelers before trusting differences of a few points. Object-level completeness on a few videos is noisy because a video has few objects; frame-level is more stable but dominated by long-visible objects.

### 2.3 Data collection and measurement error
Offline. Build a gold sample: videos labeled independently by two experienced labelers, disagreements adjudicated. Compare ordinary submitted labels to the gold set, using the expanded (per-frame) export so that interpolated frames are scored, not just keyframes.

Example, InfinityPool: the server already expands keyframes into per-frame boxes (`apps/api/app/libraries/expandLabels.ts`), so the comparison script can read the same expansion the training pipeline uses. Stratify the gold sample by mode (from scratch vs pre-annotated) and by video type (constant vs variable frame rate, short vs long). A first pilot of roughly 20 to 30 videos per mode gives a usable estimate; size the full study from the pilot's spread.

Error sources: IoU threshold choice; frame misalignment between labels and gold (which is itself a known InfinityPool issue, see [Frame-Sync Accuracy](frame-sync-accuracy.md)); disagreement on borderline objects.

### 2.4 Computation
- Match labeled boxes to gold boxes per frame with an IoU threshold (commonly 0.5), as in CLEAR MOT [bernardin2008].
- Frame-level completeness = matched gold (object, frame) pairs ÷ all gold (object, frame) pairs.
- Object-level completeness = gold objects matched on ≥ T% of visible frames ÷ all gold objects.
- Report alongside: false tracks per video, ID switches [bernardin2008], and optionally IDF1 [ristani2016] or HOTA [luiten2021], which combine detection, association, and localization.
- Aggregate per video, then across videos (macro), and per mode.

### 2.5 Unit and scale
Proportion 0 to 1 (ratio). Target thresholds are a team decision; the requirement stated in the interview is "all objects should be tracked", which implies object-level completeness close to 1.

## 3. Why it is measured

### 3.1 Use cases
- InfinityPool: checking whether labelers using pre-annotations miss objects the model missed, compared with labelers working from scratch.
- InfinityPool: checking whether the interpolation fixes (span modes, trailing keyframe) reduce frames where a box has drifted off its object.
- A traffic-camera dataset team audits a vendor's labeled clips before paying, sampling 5% of clips against an in-house gold set.
- A wildlife-video project compares two labeling tools on the same clips before choosing one for a season of footage.

### 3.2 Purposes
Quality acceptance of labeled data; comparing labeling modes or tool versions; finding which object types or video conditions get missed.

### 3.3 Assumptions
That a gold standard can define "all objects of interest" unambiguously. That IoU matching captures "the object is tracked." That misses matter equally across object classes (often false: a missed rare class may matter more for training).

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Data-quality leads or developers run the comparison script; expert labelers build the gold set. The gold set is the cost; once built, rescoring is free.

### 4.2 Consumers and decisions informed
Project managers accepting data; ML engineers deciding whether data is fit for training; developers prioritizing tool fixes; labelers getting feedback.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Labelers can raise completeness by adding boxes for everything, including non-objects; pair with false-track rate. A gold set labeled with the same tool inherits that tool's systematic errors. With pre-annotations, labelers may accept model output without checking (automation bias [parasuraman2010]); completeness is the metric that reveals this, so do not drop it in favor of speed metrics.

## 5. Related metrics

### 5.1 Static relationships
Same construct as [Recall](recall.md) with objects as the unit [manning2008]. Complementary: false-track rate (precision side), ID switches, localization error. Cheaper proxy: reviewer pass/fail on a task, which is quick but does not count misses. Costlier alternative: full HOTA scoring [luiten2021], which separates detection from association errors.

### 5.2 Dynamic relationships
Expected trade-off with [Active Labeling Time per Object](active-labeling-time-per-object.md): rushing lowers completeness. With pre-annotations, completeness is bounded below by model recall only if labelers add what the model missed; a low [Pre-annotation Edit Rate](pre-annotation-edit-rate.md) together with lower completeness than the from-scratch mode suggests anchoring on the model. These are hypotheses for this system, not measured.

## 6. Links to business objectives
**Improved usability:** positive, theoretical. Effectiveness is part of usability [iso9241-11]; a tool that makes complete labeling hard is less usable.

**Sustained use:** positive, theoretical. Downstream teams keep using a tool whose labels they trust; no evidence recorded.

## 7. Sources
- [manning2008]: recall definition.
- [bernardin2008]: IoU matching, ID switches, CLEAR MOT.
- [ristani2016], [luiten2021]: identity-aware and combined tracking scores.
- [iso9241-11]: effectiveness in usability.
- [parasuraman2010]: automation bias with model suggestions.

## Open questions and review notes
- **For team deliberation (from the InfinityPool interview, 2026-10-19):**
  - Is object-level or frame-level completeness the primary number? The interview said "all objects should be tracked", which reads as object-level; downstream training may care more about frame-level.
  - Which objects count: every instance of the taskset classes, or also unclassified moving objects? Not yet answered.
  - Thresholds: IoU 0.5 and "mostly tracked" at 80% are placeholders taken from tracking benchmarks, not team decisions.
  - Should identity errors (ID switches) be part of this metric or a separate page? Track merging (request #9) targets them directly.
  - Alternative to a gold set: reviewer-found misses per task in an existing review queue. Cheaper, but only counts misses someone noticed.
