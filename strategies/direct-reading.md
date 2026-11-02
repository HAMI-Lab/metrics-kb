---
id: direct-reading
title: "Direct reading: timing and counting"
aliases: [instrumented measurement, event counting]
page_type: strategy
template_version: "0.2"

layer: route
research_methods: [logs-telemetry, task-study, test-collection]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [webb1966, hornbaek2006, kohavi2020]
---

# Direct reading: timing and counting

> The number is read off an instrument: a timer, a counter, a log, or a test harness.

## 1. What it is

### 1.1 Definition
Durations, counts, and rates are recorded directly from events: when a task started and ended, how many times an action happened, how long the server took, whether a test passed. No one is asked to judge anything.

### 1.2 Typical pairings
Logs and telemetry, timed tasks in lab or field studies, and automated test suites.
<!-- generated:pairings:start -->
- [Interaction logs and telemetry](logs-telemetry.md)
- [Task studies with people](task-study.md)
- [Test collections and benchmarks](test-collection.md)
<!-- generated:pairings:end -->

### 1.3 Named practices
- **Time on task** in usability tests.
- **Event counts and rates** from interaction logs (undos, retries, sessions per week).
- **Latency telemetry** from servers and clients; online controlled experiments that vary it [kohavi2020].
- **Test-suite pass rates** for component behaviour.

## 2. When to use it
Use it when the construct is itself an observable event or duration, or when a cheap, non-reactive signal is needed at scale. Prefer another route when the construct is a judgment (quality, relevance) or an experience (satisfaction).

## 3. Shared caveats

### 3.1 Validity: how the number can miss the construct
The reading is exact about the event but the event is often not the construct: elapsed time is not efficiency unless the outcome is fixed, and a count of clicks is not engagement. Start and end points of tasks are often ambiguous in field logs [hornbaek2006].

### 3.2 Reliability
High for the reading itself; threats come from instrumentation bugs, clock differences between client and server, idle time, and multitasking.

### 3.3 Bias and gaming
Logs are non-reactive: people do not change behaviour because they are being asked [webb1966]. But counts are easy to game by changing what counts as an event, and by people who know they are monitored.

## 4. Cost
Low per measurement once instrumented; the cost is engineering time to add and maintain logging, and agreeing on privacy and access rules.

## 5. Metrics using this strategy
<!-- generated:metrics:start -->
- [Cost per Task](../metrics/cost-per-task.md)
- [Response Latency](../metrics/response-latency.md)
- [Task Completion Time](../metrics/task-completion-time.md)
<!-- generated:metrics:end -->

## 6. Sources
- [webb1966]
- [hornbaek2006]
- [kohavi2020]

## Open questions and review notes
- None yet.
