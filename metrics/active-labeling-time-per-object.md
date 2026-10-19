---
id: active-labeling-time-per-object
title: Active Labeling Time per Object
aliases: [annotation time per track, labeling cost per object, time per bounding-box track]
page_type: metric
template_version: "0.1"
fields: [data-annotation, hci, computer-vision]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How much active working time a labeler spends, using the tool, to produce one finished object track in a video."
  subject: [user-system-team]
  aspect: [efficiency]
  perspective: [objective]
  quantity_form: [duration]
  context: [task, user-specific]
  facet_status: provisional

operationalization:
  measure_type: mixed
  collection_mode: [field, in-lab]
  data_source: [interaction-logs, timing]
  unit: "seconds per gold object (or per submitted track)"
  range: "> 0"
  better: lower

cost:
  level: low
  requires: ["client-side event logging with an idle cutoff (not present yet)", "object count per video, ideally from a gold set"]
  automatable: true

related:
  - {metric: task-completion-time, relation: same-construct, note: "Task time normalized by object count, with idle time removed."}
  - {metric: object-track-completeness, relation: trade-off, note: "Only compare times at equal completeness."}
  - {metric: pre-annotation-edit-rate, relation: correlated, note: "More corrections are expected to cost more time."}
  - {metric: workaround-action-rate, relation: correlated, note: "Workarounds add time without adding labels."}
  - {metric: nasa-tlx, relation: complementary, note: "Time does not capture how demanding the work felt."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Labeling is paid, repetitive work; lower cost per object makes the tool worth keeping. Not tested."}
  improved-usability: {direction: negative, evidence: correlational, note: "Efficiency is part of the ISO usability definition; lower time at equal completeness is better."}

sources: [iso9241-11, papadopoulos2017, vondrick2013, sauro2010, hornbaek2006, hornbaek2007]
---

# Active Labeling Time per Object

> Working time per finished object track, with idle time removed.

## 1. What is measured

### 1.1 Definition
Total active time a labeler spends on a video task (summed across sessions, minus idle gaps), divided by the number of objects in that video.

### 1.2 Construct: property of subject in context
The property is **labeling efficiency**. The subject is the **labeler and tool together**. The context is a **task** (one video) and depends on the labeler's experience and on video properties (length, object count, motion).

### 1.3 What it does not measure
Not label quality; it must be read together with [Object-Track Completeness](object-track-completeness.md). Not how demanding the work felt ([NASA-TLX](nasa-tlx.md)). Not time lost to crashes that led to redoing work, unless redone work is logged too.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for "active time spent." **Proxy** for labeling cost, which also includes rework after review and setup time. Normalizing by object count assumes cost scales with objects; it also scales with video length and motion, so record those as covariates. Hence `mixed`.

### 2.2 Reliability
Task times are right-skewed and vary widely between people [sauro2010]. The idle cutoff choice changes totals. Compare the same labelers across conditions where possible.

### 2.3 Data collection and measurement error
Field: needs instrumentation, which InfinityPool does not have today (labels and drafts only store created and updated timestamps).

Example, InfinityPool instrumentation plan:
- Client: in the labeling page (`apps/web/src/routes/TasksetLabel/LabelTasksetByTask.tsx` and `LabelTaskset.tsx`), emit `task_open`, `task_close`, `submit`, and a heartbeat every 15 s while there is input (mouse, key, play/seek) in the last 60 s. Batch-send to a new API endpoint.
- Server: a new `labeling_events` table (user, task, session id, event type, timestamp, small JSON payload). Autosave already writes `label_drafts` every 3 to 15 s of activity, so draft `updated_at` gives a rough fallback before new logging exists.
- Mode tag: record whether the task had imported pre-annotations, so time can be split by mode.
- Lab alternative: time a fixed set of videos in a controlled study (from scratch vs pre-annotated vs new tool version), which avoids uncertainty about object counts.

Error sources: multitasking in field logs; idle cutoff; tasks split across days; crashes that force redoing work.

### 2.4 Computation
- Active time = sum of intervals between consecutive events, capping each gap at the idle cutoff (for example 60 s).
- Per object = active time ÷ gold object count (or ÷ submitted tracks if no gold).
- Report geometric mean or median per condition, with intervals [sauro2010]; state whether abandoned tasks are included [hornbaek2006].

### 2.5 Unit and scale
Seconds per object (ratio). Comparable only for similar video types.

## 3. Why it is measured

### 3.1 Use cases
- InfinityPool: testing the main claim behind pre-annotation, that it reduces labeling time per object compared with labeling from scratch, at equal completeness.
- InfinityPool: before/after a release containing the interpolation fixes (span modes, trailing keyframe), checking time per object on comparable videos.
- An image-annotation team compares click-based box drawing methods by human seconds per box [papadopoulos2017].
- A robotics lab budgets labeling hours for a new camera dataset from measured time per object.

### 3.2 Purposes
Comparing tool versions and labeling modes; budgeting; finding video types that are slow.

### 3.3 Assumptions
That lower time at equal quality is better (true for routine labeling). That object count is the right normalizer. That labelers in logs are working, not idle with input events.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Developers implement logging once; data teams compute. A lab study needs participants and a facilitator.

### 4.2 Consumers and decisions informed
Project managers (staffing and budget); developers (which fixes paid off); ML teams (whether pre-annotation is worth running).

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Used as a per-labeler productivity score, it pushes people to skip checking and lowers completeness. Event logging of individual labelers is also a workplace monitoring concern; agree on access and aggregation rules first.

## 5. Related metrics

### 5.1 Static relationships
Refinement of [Task Completion Time](task-completion-time.md). Complementary: [Object-Track Completeness](object-track-completeness.md), [NASA-TLX](nasa-tlx.md). Its components include [Response Latency](response-latency.md) (waiting for video loads and seeks) and [Workaround Action Rate](workaround-action-rate.md).

### 5.2 Dynamic relationships
Video annotation research shows labeling cost can be traded against quality through keyframe spacing and interpolation [vondrick2013]; expect speed-completeness trade-offs. Efficiency, effectiveness, and satisfaction correlate only modestly in general [hornbaek2007].

## 6. Links to business objectives
**Improved usability:** negative (lower is better), correlational in general [iso9241-11]; not measured for InfinityPool.

**Sustained use:** negative, theoretical. Cheaper labeling makes the tool worth keeping; untested.

## 7. Sources
- [iso9241-11]: efficiency.
- [papadopoulos2017]: time per box as an annotation cost measure.
- [vondrick2013]: cost-quality trade-off in video annotation.
- [sauro2010], [hornbaek2006]: summarizing and reporting times.
- [hornbaek2007]: correlations among usability measures.

## Open questions and review notes
- **For team deliberation (InfinityPool interview, 2026-10-19):**
  - Proposed as the **primary** metric for goal G2 (pre-annotation saves effort). Is time the right primary, or should it be labor cost including review and rework?
  - Is client event logging acceptable in the deployment environment? Asked in the interview, not yet answered. If not, the lab study is the only route.
  - Normalize per object, per object-frame, or per video minute? Per object is proposed because "all objects should be tracked" is the stated success criterion.
  - Idle cutoff of 60 s is a placeholder.
