---
id: improved-usability
title: "Objective 2: Improved Usability"
page_type: objective
template_version: "0.1"
status: ai-draft
sources: [iso9241-11, hornbaek2007, sauro2009, S13, S15]
---

# Objective 2: Improved Usability

> The system lets its intended users reach their goals more effectively, more efficiently, and with more satisfaction.

## What it means
ISO 9241-11 defines usability as the extent to which specified users can use a system to achieve specified goals with effectiveness, efficiency, and satisfaction in a specified context of use [iso9241-11]. "Improved" means these move in the right direction between versions, without trading one away for another.

## How it can be observed
No single measure captures it. The usual practice is to measure all three parts:
- Effectiveness: task success, error rate, output quality ([Precision](../metrics/precision.md) for the system side).
- Efficiency: [Task Completion Time](../metrics/task-completion-time.md), effort ([NASA-TLX](../metrics/nasa-tlx.md)), waiting time ([Response Latency](../metrics/response-latency.md)).
- Satisfaction: [SUS](../metrics/system-usability-scale.md) and similar questionnaires.

These parts correlate only modestly with one another [hornbaek2007; sauro2009], so improving one does not guarantee improvement in the others.

## Metrics linked to this objective

| Metric | Direction | Evidence | Note |
|---|---|---|---|
| [Response Latency](../metrics/response-latency.md) | negative | causal (visual analytics) | |
| [SUS](../metrics/system-usability-scale.md) | positive | correlational | Measures perceived usability |
| [Task Completion Time](../metrics/task-completion-time.md) | negative | correlational | For the same outcome |
| [NASA-TLX](../metrics/nasa-tlx.md) | negative | correlational | Not at very low workload |
| [Precision](../metrics/precision.md) | positive | correlational | Weaker than assumed |

## Open questions
- For AI systems, should trust and appropriate reliance count as part of usability, or be treated as a third objective? Several spreadsheet sources treat them as central [S13; S15].
