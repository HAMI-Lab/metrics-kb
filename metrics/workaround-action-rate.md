---
id: workaround-action-rate
title: Workaround Action Rate
aliases: [corrective action rate, fighting-the-tool rate, compensatory edits, undo rate]
page_type: metric
template_version: "0.2"
fields: [hci, data-annotation, human-ai-interaction]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How often a person performs actions that exist only to undo or compensate for the tool's own behavior, rather than to state their labeling judgment."
  measures: [interaction-friction]
  subject: [user-system-team]
  aspect: [ease-of-use, efficiency]
  perspective: [objective]
  quantity_form: [rate]
  context: [task, system-specific]
  facet_status: provisional

operationalization:
  measure_type: proxy
  research_method: [logs-telemetry, observation-think-aloud]
  route: [direct-reading, qualitative-coding]
  collection_mode: [field, in-lab]
  data_source: [interaction-logs, observation]
  unit: "workaround actions per object (or per 100 edit actions)"
  range: ">= 0"
  better: lower
  validity_concern: {level: high, note: "Inferred from a hand-built catalog of log patterns; validate the catalog against observation."}

cost:
  level: medium
  requires: ["a team-agreed catalog of workaround patterns", "client event logging of edit actions (not present yet)", "a short observation or think-aloud pilot to validate the catalog"]
  automatable: true

related:
  - {metric: active-labeling-time-per-object, kind: operational, note: "Workarounds add time without adding labels."}
  - {metric: nasa-tlx, kind: empirical, note: "Fighting the tool is expected to raise frustration and effort ratings."}
  - {metric: system-usability-scale, kind: conceptual, note: "Behavioral vs perceived view of the same problem."}
  - {metric: work-loss-incidence, kind: conceptual, note: "Lost work forces redo, a large workaround the event catalog may not see."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Users who must keep working around a tool look for another one; not tested here."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Workarounds signal that the system blocks the user's goal [alter2014]."}

sources: [alter2014, nielsen1993, card1983]
---

# Workaround Action Rate

> How often does the labeler have to fight the tool instead of labeling?

## 1. What is measured

### 1.1 Definition
The number of actions, per object labeled, that match a predefined catalog of workaround patterns: action sequences whose only purpose is to correct or prevent something the tool did on its own.

### 1.2 Construct: property of subject in context
The property is **friction**: the extra work the tool's behavior imposes. The subject is the **labeler and tool together**. The context is a **task**, and the catalog is **system-specific**: it is written for one tool's known problems. A workaround is a goal-directed adaptation that gets around an obstacle the system puts in the way [alter2014].

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Interaction friction](../constructs/interaction-friction.md) (under Task characteristics → Usability)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Not ordinary edits (correcting a wrong pre-annotation is the job, not a workaround). Not friction the catalog does not anticipate. Not how frustrating it felt.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Proxy.** Patterns are inferred from logs; the same sequence can be a workaround or a legitimate edit. Validate the catalog against observation: watch or think-aloud with a few labelers, code which sequences were workarounds, and check how well the log rules match.

### 2.2 Reliability
Depends on the rules. Expect differences between labelers who learned the tricks (for example "add a keyframe one frame before a jump") and new labelers. Report by experience level.

### 2.3 Data collection and measurement error
Needs edit-level event logging (see the plan on [Active Labeling Time per Object](active-labeling-time-per-object.md)), with each canvas or sidebar edit logged as an event: keyframe add, move, resize, delete, mode change (move / hold / away), merge, split, undo, frame step, play, pause.

Example, InfinityPool catalog drawn from the pre-annotation requests document (each is a candidate; the team should confirm):
- **Drift-guard keyframe:** a keyframe added on the frame just before a jump with the same box as the previous keyframe (request #6). Span modes now offer `hold`; count how often the old trick is still used.
- **Pull-back fix:** moving a box back toward the object shortly after a keyframe because interpolation dragged it (requests #5, #10).
- **Pause-resync:** step back one frame then forward one frame right after pausing, with no edit in between (request #11).
- **Long delete:** more than 3 actions to remove an object that is visible only briefly (request #12).
- **Delete-and-redraw:** deleting a track and creating a new one that overlaps it within a short time (requests #8, #9, where bulk edit or merge was missing).
- **Undo burst:** three or more undos in a row.
- **URL navigation:** reaching a task by editing the URL instead of the UI (request #3); visible in server access logs.

Error sources: rules that are too broad or too narrow; changes in the UI that change the patterns.

### 2.4 Computation
- Count catalog matches per task; divide by objects in the video (or by 100 edit actions).
- Report per pattern, not only the total: each pattern points to a specific fix.
- Compare tool versions on similar videos.

### 2.5 Unit and scale
Count per object (ratio). Lower is better; zero for a pattern after the related fix is a direct check that the fix works.

## 3. Why it is measured

### 3.1 Use cases
- InfinityPool: checking, after the span-mode release, whether labelers stopped adding drift-guard keyframes.
- InfinityPool: ranking the remaining open requests (bulk edit, task list, delete key) by how often their workaround appears.
- A spreadsheet product team counts how often users paste values into a helper column to get around a missing feature.
- An electronic health record team counts free-text notes used where a structured field fails.

### 3.2 Purposes
Prioritizing fixes; confirming a fix changed behavior; tracking friction over releases.

### 3.3 Assumptions
That workarounds can be recognized from action sequences. That fewer workarounds mean less friction rather than labelers giving up on quality.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Developers build the logging and rules; a UX researcher validates them with a small observation study. Ongoing cost is low.

### 4.2 Consumers and decisions informed
Developers and product managers choosing what to fix next; labelers' leads deciding what to teach.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Read per labeler, it can penalize careful people. A drop can mean labelers stopped bothering to fix problems, so read it with [Object-Track Completeness](object-track-completeness.md). The catalog ages as the tool changes.

## 5. Related metrics

### 5.1 Operationally related metrics
Part of [Active Labeling Time per Object](active-labeling-time-per-object.md).

### 5.2 Conceptually related metrics
Behavioral counterpart to perceived usability ([SUS](system-usability-scale.md)) and to usability-test error and problem counts [nielsen1993]. Keystroke-level models [card1983] can estimate how many steps a workaround costs, which is cheaper than logging for single patterns like the 7-step delete.

<!-- generated:neighbours:start -->
- Sibling construct: [Active Labeling Time per Object](active-labeling-time-per-object.md) (Task efficiency), [Task Completion Time](task-completion-time.md) (Task efficiency), [System Usability Scale (SUS)](system-usability-scale.md) (Usability: perceived usability)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Expected to move with time per object and with workload ratings ([NASA-TLX](nasa-tlx.md)); no measured link here.

## 6. Links to business objectives
**Improved usability:** negative, theoretical [alter2014].

**Sustained use:** negative, theoretical: tools that must be worked around get replaced. The requests document frames InfinityPool's problem as labelers having to "actively work around or fight" the tool.

## 7. Sources
- [alter2014]: what workarounds are and why they arise.
- [nielsen1993]: usability problem and error counts.
- [card1983]: estimating action costs with keystroke-level models.

## Open questions and review notes
- **For team deliberation (InfinityPool interview, 2026-10-19):**
  - Proposed as the **primary** metric for goal G3 (labelers do not have to fight the tool). Is a hand-built catalog acceptable, or too subjective?
  - Which catalog patterns are real workarounds for experienced labelers? The list comes from the requests document, not from observation.
  - Alternative: a short post-task question ("Did the tool get in your way on this video? Where?") is cheaper and catches unanticipated problems, but is self-report.
  - Alternative: count raw undo actions only. Easy, but undo is also used for normal mistakes.
