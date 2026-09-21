---
id: response-latency
title: Response Latency
aliases: [response time, latency, time to first token, TTFT, end-to-end latency]
page_type: metric
template_version: "0.1"
fields: [hci, information-retrieval, visualization, llm-evaluation, systems]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How long the system takes to respond after the user acts."
  subject: [system]
  aspect: [responsiveness, efficiency]
  perspective: [objective]
  quantity_form: [duration]
  context: [task, time-location]
  facet_status: provisional

operationalization:
  measure_type: direct
  collection_mode: [offline, online]
  data_source: [system-telemetry, timing]
  unit: "milliseconds"
  range: "> 0"
  better: lower

cost:
  level: low
  requires: [instrumentation of request and response events]
  automatable: true

related:
  - {metric: task-completion-time, relation: component-of, note: "Latency is part of the time users spend on a task."}
  - {metric: system-usability-scale, relation: causally-linked, note: "Delays plausibly lower perceived usability."}

objectives:
  sustained-use: {direction: negative, evidence: causal, note: "Controlled online experiments in web search show added latency reduces engagement; transfer to AI assistants, where users expect slower answers, is untested here."}
  improved-usability: {direction: negative, evidence: causal, note: "Added interactive latency changed how people explored data in a controlled visualization study."}

sources: [miller1968, card1983, nielsen1993, dean2013, arapakis2014, liu2014, kohavi2020, S4, S5, S10, S31]
---

# Response Latency

> The time between a user's action and the system's response, usually reported as a median and a high percentile.

## 1. What is measured

### 1.1 Definition
The elapsed time from a user action (a click, a query, a prompt) to the system's response. For streaming AI systems, two readings are common: **time to first token** (when output starts appearing) and **end-to-end latency** (when the response is complete).

### 1.2 Construct: property of subject in context
The property is **responsiveness**. The subject is the **system**, including its network path. The context is the kind of request (a simple lookup vs. a long generation) and the time and place (load, network conditions, the user's device).

### 1.3 What it does not measure
It does not measure how fast the response *feels*: progress indicators and streaming change perception without changing latency. It does not measure the quality of the response; a fast wrong answer scores well. It does not include the user's own time to read or act; see [Task Completion Time](task-completion-time.md).

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** measure of system responsiveness. Validity issues come from choosing the start and end events: server-side timings miss network and rendering time, which users do experience.

### 2.2 Reliability
Individual measurements are noisy and have long tails. Distribution summaries over many requests are stable when load and conditions are controlled; they drift with load, hardware, and deployment.

### 2.3 Data collection and measurement error
Offline: benchmark runs on fixed inputs [S4; S5]. Online: telemetry from the deployed system. Client-side measurement is closer to experience but harder to collect; server-side is easy but partial. Clock differences between machines and sampling of logs introduce error.

### 2.4 Computation
Collect per-request durations and report percentiles, typically the median (p50) and a tail value (p95 or p99), not only the mean. Tail latency matters because users of large systems regularly hit the slow cases [dean2013]. For AI agents, also report latency per completed task, which includes all intermediate steps and tool calls [S10; S31].

### 2.5 Unit and scale
Milliseconds or seconds (ratio scale). Classic rules of thumb for interactive systems: about 0.1 s feels instantaneous, about 1 s keeps the flow of thought, and about 10 s is the limit for holding attention [miller1968; card1983; nielsen1993]. These predate AI assistants and should be treated as guidance, not thresholds.

## 3. Why it is measured

### 3.1 Purposes
Service-level monitoring and alerting; choosing models or hardware under a quality-cost-latency trade-off [S4; S31]; checking that a new feature does not slow the product; A/B testing the effect of speed on user behavior [kohavi2020].

### 3.2 Assumptions
That faster is always better, which may not hold where users read a delay as care or effort, or where speed costs quality. That the user is waiting on this response (background tasks tolerate more delay). That the thresholds from command-line and web interaction carry over to conversational AI.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Engineering and infrastructure teams. Very cheap once instrumented.

### 4.2 Consumers and decisions informed
Engineers (capacity, optimization), product managers (is the product fast enough?), researchers (latency-quality trade-offs).

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Reporting the mean hides tail problems. Measuring server time only hides client and network delays. Optimizing time to first token can make the start fast while the full answer stays slow. Cutting latency by switching to a weaker model trades away quality without showing it on this metric.

## 5. Related metrics

### 5.1 Static relationships
Component of [Task Completion Time](task-completion-time.md). Trade-off with output quality metrics such as [Precision](precision.md) and task success, and with compute cost [S31]. Complementary: perceived speed ratings, [SUS](system-usability-scale.md).

### 5.2 Dynamic relationships
In web search, controlled experiments that added delay found reduced user engagement [arapakis2014; kohavi2020]. In exploratory visual analysis, added latency of 500 ms changed how people interacted with the data and reduced the amount of exploration [liu2014] (check the exact figures against the paper).

## 6. Links to business objectives
**Sustained use:** negative, with causal evidence from online experiments in web search [kohavi2020; arapakis2014]. How far this carries to AI assistants, where users may expect answers to take seconds, is not known.

**Improved usability:** negative, with causal evidence from a controlled visual analytics study [liu2014]. The long-standing response-time guidelines [nielsen1993] are consistent with this.

This is one of the few metrics in the pilot where the path to the business objectives is supported by experiments, not only theory.

## 7. Sources
- [miller1968], [card1983], [nielsen1993]: response-time guidelines.
- [dean2013]: tail latency.
- [arapakis2014], [kohavi2020]: effects of latency on user behavior in web search.
- [liu2014]: effects of latency in visual analytics.
- [S4], [S5], [S10], [S31]: efficiency and cost reporting in LLM and agent evaluation.

## Open questions and review notes
- Verify the specific figures attributed to [liu2014] and add figures from [arapakis2014].
- Should time to first token be a separate page?
