---
id: work-loss-incidence
title: Work-Loss Incidence
aliases: [lost-work rate, data-loss incidents, save failure rate]
page_type: metric
template_version: "0.2"
fields: [hci, data-annotation, software-reliability]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "The share of labeling sessions in which work the person did is not present when they or the system next read it."
  measures: [work-preservation]
  subject: [system]
  aspect: [effectiveness, trust]
  perspective: [objective]
  quantity_form: [proportion]
  context: [session]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [logs-telemetry]
  route: [direct-reading]
  collection_mode: [online, field]
  data_source: [system-telemetry, interaction-logs]
  unit: "proportion of sessions (also: minutes of work lost per incident)"
  range: "0-1"
  better: lower
  validity_concern: {level: low, note: "Direct when detected by comparing client and server state; otherwise limited to losses users notice."}

cost:
  level: low
  requires: ["checksums or edit counters on drafts and submitted labels", "client error reporting for failed saves and media crashes"]
  automatable: true

related:
  - {metric: active-labeling-time-per-object, kind: empirical, note: "Lost work is redone, inflating time."}
  - {metric: workaround-action-rate, kind: conceptual, note: "Users who fear loss submit early or avoid long sessions, a workaround logs may miss."}
  - {metric: system-usability-scale, kind: empirical, note: "Expected to lower perceived usability and trust; not measured."}

objectives:
  sustained-use: {direction: negative, evidence: theoretical, note: "Losing work is a strong reason to stop trusting a tool; not tested here."}
  improved-usability: {direction: negative, evidence: theoretical, note: "Lost work is an effectiveness failure and forces redo."}

sources: [nielsen1993]
---

# Work-Loss Incidence

> How often does a labeler lose work they already did?

## 1. What is measured

### 1.1 Definition
The share of labeling sessions with at least one loss event: edits made in the session that are missing from the saved draft or submitted label when it is next read. Also report the size of the loss (edits or minutes lost).

### 1.2 Construct: property of subject in context
The property is **reliability of keeping the user's work**. The subject is the **system** (client, network, server). The context is a **session**. Usability heuristics treat preventing loss and allowing recovery as basic requirements [nielsen1993].

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Work preservation](../constructs/work-preservation.md) (under System characteristics → System performance → System reliability)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Not wrong labels saved correctly (those are quality issues). Not loss the user caused on purpose (deleting). Not the user's fear of loss, which changes behavior even if loss is rare.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** when detected by comparing what the client sent with what the server stores. **Proxy** when inferred from user reports or from symptoms (a reopen showing fewer keyframes than the last autosave). Hence `mixed`.

### 2.2 Reliability
Rare events: needs many sessions to estimate. Report counts, not only rates, and confidence intervals.

### 2.3 Data collection and measurement error
Example, InfinityPool: drafts autosave after 3 s idle and at most every 15 s (`apps/web/src/hooks/useLabelDraft.tsx`), with a `keepalive` path for small drafts and a fallback for drafts over 64 KB that page teardown can cancel. Long video tracks are exactly the large ones. Instrument:
- Client keeps an edit counter (or hash) of the current state; send it with every draft save and the submit.
- Server stores it with the draft and the label; on restore, the client compares the stored counter with its local last-known value (kept in session storage) and reports a mismatch.
- Log draft status transitions the hook already has (`saving`, `saved`, `error`, `unreadable`) and media load failures and retries.
- Charlie's report (labels disappearing after long sessions, then submit and reopen) is the scenario to test first: a scripted long session in a test environment, compare submitted labels to the client's final state.

Error sources: incidents users never notice; reports of loss that were user error.

### 2.4 Computation
- Incidence = sessions with ≥ 1 loss event ÷ sessions.
- Severity = edits (or minutes, from activity logs) lost per incident.
- Split by session length and draft size; loss is suspected to grow with both.

### 2.5 Unit and scale
Proportion of sessions (ratio). Target close to zero.

## 3. Why it is measured

### 3.1 Use cases
- InfinityPool: confirming that autosave fixed request #2 and the Aug 3 report of disappearing labels, especially for long videos with large drafts.
- InfinityPool: checking whether video load failures (request #4) still force labelers to submit incomplete tasks.
- A web form builder tracks how often respondents lose answers on a timeout.
- A collaborative editor monitors sync conflicts that drop edits.

### 3.2 Purposes
Release gating (block a release that raises it); monitoring; reassuring users with evidence.

### 3.3 Assumptions
That loss can be detected by comparing states. That sessions are a meaningful unit (labelers may resume across days).

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Developers, from telemetry. Low cost once built.

### 4.2 Consumers and decisions informed
Developers and release managers; project managers deciding whether labelers can trust long sessions.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Low incidence can hide one catastrophic loss; always report severity. If users avoid long sessions because they fear loss, incidence looks good while workload rises.

## 5. Related metrics

### 5.1 Operationally related metrics
No operationally related metric pages yet. Severity (edits or minutes lost per incident, 2.4) is computed from the same events.

### 5.2 Conceptually related metrics
Reliability counterpart to effectiveness measures. Complementary to [Workaround Action Rate](workaround-action-rate.md) and to [Active Labeling Time per Object](active-labeling-time-per-object.md) (redo time).

<!-- generated:neighbours:start -->
- Broader construct: [Frame-Sync Accuracy](frame-sync-accuracy.md) (System reliability)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
Each incident adds redo time; links to satisfaction and continued use are expected but not measured here.

## 6. Links to business objectives
**Sustained use:** negative, theoretical. **Improved usability:** negative, theoretical. No study links measured loss rates to these objectives in the sources listed.

## 7. Sources
- [nielsen1993]: error prevention and recovery as usability requirements.

## Open questions and review notes
- **For team deliberation (InfinityPool interview, 2026-10-19):**
  - Proposed as the **primary** metric for goal G4 (work is never lost). Is it a usability metric, or should it live with reliability engineering (an SLO, a service-level objective) rather than this wiki?
  - What counts as one session when labelers resume a task later?
  - Alternative: a post-session question "Did you lose any work?" is cheap and catches losses telemetry misses, but relies on users noticing.
