---
id: trustworthiness
title: Trustworthiness
aliases: [credibility, reliability of information]
page_type: construct
template_version: "0.1"
fields: [information-retrieval, human-ai-interaction]

broader: [relevance, output-quality]

status: ai-draft
last_reviewed: null
reviewers: []

sources: [lee2004, barry1998]
---

# Trustworthiness

> Whether a retrieved item or system output deserves to be relied on; a construct with several facets.

## 1. Definition
The degree to which information or an output can be relied on: true, supported by its sources, from a credible source, and honest about its limits. It has several facets, each measured in its own way: [factuality](factuality.md) (are the claims true?) and [groundedness](groundedness.md) (are they supported by the given sources?) are measured on outputs, and calibrated confidence shows whether the system is honest about its limits.

## 2. Boundaries
Trustworthiness is a property of the information or system. [Trust in the system](trust-in-system.md) is the user's attitude toward it, measured with questionnaires such as the [Trust Score](../metrics/trust-score.md); it shows how trustworthy people *perceive* the system to be, not how trustworthy it is. The two are kept in separate places in the DAG because the gap between them is what good design closes: trust that matches trustworthiness (appropriate reliance) [lee2004]. Source quality is one of the criteria users apply when judging relevance [barry1998].

## 3. Narrower constructs
<!-- generated:narrower:start -->
- [Generation performance: factuality](factuality.md)
- [Generation performance: groundedness](groundedness.md)
<!-- generated:narrower:end -->

## 4. Metrics
Measured through its facets: metrics attach to factuality and groundedness. Candidates for other facets include source credibility ratings and calibration of confidence.
<!-- generated:metrics:start -->
_No metric page yet._
<!-- generated:metrics:end -->

## 5. Links to business objectives
Theoretical: untrustworthy outputs erode reliance and continued use.

## 6. How it is identified
Retrieval, recommendation, and AI-output literature; the two parents show it is shared across fields.

## 7. Sources
- [lee2004]
- [barry1998]

## Open questions and review notes
- Should user trust (the attitude) be a separate construct with its own metrics?
