---
id: action-efficiency-vs-humans
title: Action Efficiency Relative to Humans
aliases: [RHAE, Relative Human Action Efficiency, human-normalized action efficiency]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation, agents]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "How few actions an autonomous agent needs to complete a task, compared with people doing the same task for the first time."
  measures: [autonomous-task-efficiency]
  subject: [system]
  aspect: [efficiency]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [benchmark]
  route: [difference-scoring, direct-reading]
  collection_mode: [offline]
  data_source: [interaction-logs]
  unit: "score relative to the human baseline"
  range: "0-1 per task, capped (see 2.6)"
  better: higher
  validity_concern: {level: moderate, note: "Direct for action counts against the chosen human baseline; depends on how the baseline is chosen and what counts as an action."}
  instruments:
    - {name: "ARC-AGI-3", kind: content, sources: [arcprize2026], probes: "learning and acting in unfamiliar interactive games", scale: "RHAE: per-level score from the action ratio, squared and capped", note: "Interactive game environments; human baseline from people playing each game for the first time."}

cost:
  level: medium
  requires: ["an agent benchmark with recorded human baselines"]
  automatable: true

related:
  - {metric: task-success-rate-benchmark, kind: conceptual, note: "Whether the agent completes the task, not how efficiently."}
  - {metric: cost-per-task, kind: conceptual, note: "Efficiency in money rather than actions."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Efficient agents finish sooner and cost less."}
  improved-usability: {direction: unknown, evidence: none, note: "Users rarely see action counts directly."}

sources: [arcprize2026]
---

# Action Efficiency Relative to Humans

> An agent's action count on a task compared with how many actions people needed, scored so that matching people is the top of the scale.

## 1. What is measured

### 1.1 Definition
For each task or level the agent completes, its number of actions is compared with a human baseline, the number of actions people needed. The ratio of human to agent actions gives the score; uncompleted tasks score zero [arcprize2026].

### 1.2 Construct: property of subject in context
The property is the efficiency of an autonomous system acting without a user (D28). The subject is the agent as a whole. The context is a set of interactive tasks with a human baseline.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Autonomous task efficiency](../constructs/autonomous-task-efficiency.md) (under System characteristics → System performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Whether the agent completes tasks at all (see [agent task success](task-success-rate-benchmark.md)), or cost in money or time.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for actions relative to the baseline; **proxy** for efficient problem solving in general, hence `mixed`. The baseline matters: a different human group or a different choice of human (best, median, second-best) shifts every score.

**Using a proxy with a known gap.** The score can compare agents on the same environments and baseline. It cannot show that an agent is efficient on tasks unlike the benchmark's, or in time or money. Check what counts as an action and how the baseline was chosen before comparing across sources.

### 2.2 Reliability
Agents that sample actions vary between runs; report the number of runs.

### 2.3 Data collection and measurement error
Log every action the agent submits; record which tasks it completed.

### 2.4 Computation
Per task: a function of (human baseline actions ÷ agent actions), capped; zero if not completed. Averaged over tasks. Each instrument's exact rule is in 2.6.

### 2.5 Unit and scale
A proportion, with matching people at or near the top. The cap and any transformation are instrument-specific.

### 2.6 Instruments
**Learning and acting in unfamiliar games**
- **ARC-AGI-3** [arcprize2026]: interactive games the agent has not seen. Its score, Relative Human Action Efficiency (RHAE), squares the ratio of human to agent actions per level, so inefficiency is penalized sharply, and caps each level. The human baseline comes from people playing each game for the first time (check the exact formula, cap and baseline against the paper and the current methodology page).

## 3. Why it is measured

### 3.1 Use cases
- An agent team compares two planning strategies on ARC-AGI-3 and finds one completes as many levels with far fewer actions.
- A benchmark report contrasts agents that solve tasks by brute-force exploration with agents that solve them as efficiently as people.

### 3.2 Purposes
Telling apart agents that complete tasks by trying everything from those that act efficiently.

### 3.3 Assumptions
Actions are comparable between people and agents; the human baseline is representative.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
Agent researchers; the human baseline is costly once, cheap to reuse.

### 4.2 Consumers and decisions informed
Teams choosing agent designs; benchmark organizers.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Agents tuned to the benchmark's action accounting, for example by batching moves into one action if allowed.

## 5. Related metrics

### 5.1 Operationally related metrics
None.

### 5.2 Conceptually related metrics
[Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) asks whether tasks are completed; [Cost per Task](cost-per-task.md) measures efficiency in money.

<!-- generated:neighbours:start -->
- Sibling construct: [Task Success Rate (agent benchmark)](task-success-rate-benchmark.md) (Autonomous task completion), [pass^k](pass-hat-k.md) (Consistency across runs), [Elo Rating (pairwise comparison)](elo-rating.md) (Output quality), [Judge Rating (model judge)](judge-rating.md) (Output quality), [Win Rate (pairwise comparison)](win-rate.md) (Output quality), [Response Latency](response-latency.md) (System responsiveness), [Performance Drop Rate (PDR)](performance-drop-rate.md) (System robustness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use:** positive, theoretical. **Improved usability:** unknown.

## 7. Sources
- [arcprize2026]: ARC-AGI-3 and RHAE.

## Open questions and review notes
- The formula is reported differently across ARC Prize sources (squared or not, the cap); verify before citing numbers.
