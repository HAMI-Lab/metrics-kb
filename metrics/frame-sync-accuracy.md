---
id: frame-sync-accuracy
title: Frame-Sync Accuracy
aliases: [frame alignment accuracy, keyframe placement accuracy, annotation-video sync]
page_type: metric
template_version: "0.1"
fields: [computer-vision, data-annotation, software-testing]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "The share of annotation operations whose box is saved to, and later shown on, the same video frame the person saw when making it."
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task, system-specific]
  facet_status: provisional

operationalization:
  measure_type: direct
  collection_mode: [offline]
  data_source: [reference-answers, system-telemetry]
  unit: "proportion of operations on the exact frame"
  range: "0-1"
  better: higher

cost:
  level: low
  requires: ["a test suite of videos with known frame timestamps (constant, variable, offset start)", "scripted UI interactions (browser automation)"]
  automatable: true

related:
  - {metric: object-track-completeness, relation: causally-linked, note: "Boxes on the wrong frame drift off their objects and lower frame-level completeness."}
  - {metric: workaround-action-rate, relation: causally-linked, note: "Lagging boxes make labelers step back and forth to resync."}
  - {metric: response-latency, relation: complementary, note: "Latency is how fast the display updates; this is whether it shows the right frame."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Wrong-frame saves corrupt training data and undermine trust in the tool."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Boxes that snap back or land elsewhere force rework."}

sources: [bernardin2008]
---

# Frame-Sync Accuracy

> When a labeler draws a box on a frame, does it end up on that frame?

## 1. What is measured

### 1.1 Definition
Run a scripted set of labeling operations on test videos with known frame timestamps. For each operation, check that the saved keyframe's frame equals the frame displayed when it was made, and that on reload and on playback-pause the box is shown on that frame. The metric is the share of operations that pass.

### 1.2 Construct: property of subject in context
The property is **temporal correctness** of the video and annotation component. The subject is a **system component** (player, frame index, keyframe store). The context is a **test suite** of video types and interaction sequences, specific to this tool.

### 1.3 What it does not measure
Not whether boxes are on the right object (that is labeling quality). Not display smoothness. It tests only the interaction sequences scripted.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the scripted cases. Coverage of real use depends on how well the sequences and videos represent it.

### 2.2 Reliability
Deterministic for a given browser, video, and sequence, except where timing matters (playback then pause). Repeat timing-sensitive cases several times and report the worst.

### 2.3 Data collection and measurement error
Offline, in CI or before release.

Example, InfinityPool (requests #1 and #11, Brent's July 22 note):
- Test videos: constant 30 FPS; constant non-30 FPS (for example 24 and 60); variable frame rate (frames dropped at random each second); start offsets (first frame at 0.5 s and 0.9 s); the "malicious" test video from the requests document.
- Each video encodes its frame number in the pixels (a burned-in counter), so the test can read the displayed frame from a screenshot rather than trusting the player.
- Sequences: draw on frame N after step-forward; after play then pause; after seek; after mixing play/pause with step buttons; reload and reopen.
- The repo already has a frame index built from the container's frame table (`apps/web/src/hooks/readFrameTable.ts`, `useFrameIndex`), a presented-frame check (`verifyPresentedFrames.ts`), and drift unit tests; this metric lifts those to end-to-end checks with Cypress (already in CI).
- Also count, in the field, how often the "approximate frames" banner appears (`ApproximateFramesBanner.tsx`): the share of tasks where exact frames could not be indexed.

### 2.4 Computation
- Exact-frame rate = operations saved and shown on the intended frame ÷ operations.
- Report per video type and per sequence; also report mean frame offset for failures.
- Field companion: share of video tasks where the frame index is `unsupported` or approximate.

### 2.5 Unit and scale
Proportion (ratio). Target is 1.0 on the suite; any failure is a bug.

## 3. Why it is measured

### 3.1 Use cases
- InfinityPool: release gate for the frame-index work, so variable frame rate videos no longer need converting to 30 FPS with ffmpeg first.
- InfinityPool: checking request #11 (boxes lag during playback and do not resync on pause).
- A sports-analytics vendor verifies that event tags land on the exact broadcast frame across different encoders.
- A medical-video tool checks that surgical-phase markers survive re-encoding.

### 3.2 Purposes
Regression testing; release gating; deciding whether ingest still needs format normalization.

### 3.3 Assumptions
That the test videos cover the encodings seen in practice. That burned-in counters are read correctly.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Developers, in automated tests. Low cost after the suite exists.

### 4.2 Consumers and decisions informed
Developers and release managers; data engineers deciding whether to keep the ffmpeg conversion step.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Passing the suite does not prove field correctness; new encodings appear. Keep adding field failures to the suite.

## 5. Related metrics

### 5.1 Static relationships
Component-level cause of labeler-level problems. Complementary to [Response Latency](response-latency.md). Frame misalignment between labels and gold also adds error to [Object-Track Completeness](object-track-completeness.md) scoring, which matches boxes frame by frame [bernardin2008].

### 5.2 Dynamic relationships
Expected: failures here cause drift (lower completeness) and resync workarounds. Component accuracy does not guarantee better labeler outcomes; check those separately.

## 6. Links to business objectives
**Improved usability:** positive, theoretical. **Sustained use:** positive, theoretical. Both are indirect: this is a component test whose payoff comes through fewer workarounds and better labels.

## 7. Sources
- [bernardin2008]: frame-by-frame matching in tracking evaluation.

## Open questions and review notes
- **For team deliberation (InfinityPool interview, 2026-10-19):**
  - Proposed as the **primary** metric for goal G5 (frame-accurate on any video). Is this an evaluation metric for this wiki, or a test-suite pass rate that belongs in engineering docs only?
  - Which encodings do real InfinityPool sources produce? The suite should match them.
  - Should the ffmpeg conversion to constant 30 FPS stay as a safety step even when the suite passes?
