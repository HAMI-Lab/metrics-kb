---
id: instruction-following-accuracy
title: Instruction-Following Accuracy
aliases: [IFEval accuracy, prompt-level accuracy, instruction-level accuracy, prompt_level_strict_acc, prompt_level_loose_acc]
page_type: metric
template_version: "0.3"
fields: [llm-evaluation]

status: ai-draft
last_reviewed: null
reviewers: []

construct:
  statement: "Of the instructions or prompts given to a model, the share whose checkable instructions the output satisfies."
  measures: [instruction-following]
  subject: [system-component]
  aspect: [effectiveness]
  perspective: [objective]
  quantity_form: [proportion]
  context: [task]
  facet_status: provisional

operationalization:
  measure_type: mixed
  research_method: [benchmark]
  route: [reference-comparison]
  collection_mode: [offline]
  data_source: [reference-answers]
  unit: "proportion"
  range: "0-1"
  better: higher
  validity_concern: {level: moderate, note: "Direct for checkable instructions such as format and length; a narrow proxy for following instructions in general (see 2.1)."}
  instruments:
    - {name: "Instruction-Following Evaluation (IFEval)", kind: content, sources: [zhou2023], probes: "checkable instructions on format, length, keywords and structure", scale: "proportion, 0-1", note: "Prompts with one or more verifiable instructions, each checked by a program."}

cost:
  level: low
  requires: ["prompts with verifiable instructions and their checking programs"]
  automatable: true

related:
  - {metric: accuracy, kind: operational, note: "Same share-correct computation, but correctness is checked against the instructions, not against an answer key."}
  - {metric: judge-rating, kind: conceptual, note: "Instructions that need judgment are usually scored by a model judge."}

objectives:
  sustained-use: {direction: positive, evidence: theoretical, note: "Outputs that follow instructions need less rework."}
  improved-usability: {direction: positive, evidence: theoretical, note: "Fewer retries and corrections; not measured with users."}

sources: [zhou2023]
---

# Instruction-Following Accuracy

> The share of prompts, or of individual instructions, whose checkable instructions a model's output satisfies.

## 1. What is measured

### 1.1 Definition
Each prompt carries one or more instructions that a program can check, such as "answer in fewer than 100 words", "use no commas" or "include the keyword X at least twice". A program checks each instruction on the output. Instruction-Following Accuracy is the share of prompts whose instructions are all satisfied, or the share of individual instructions satisfied [zhou2023].

### 1.2 Construct: property of subject in context
The property is following the instructions stated in the input. The subject is a model, here a component judged per call (D28). The context is a set of prompts with checkable instructions.

<!-- generated:constructs:start -->
Measures, in the [construct DAG](../constructs/index.md):

- [Generation performance: instruction following](../constructs/instruction-following.md) (under Component characteristics → Component performance → Generation performance)
<!-- generated:constructs:end -->

### 1.3 What it does not measure
Whether the content is correct or useful: a model can follow every format instruction while answering wrongly. Instructions that need judgment, such as tone or focus.

## 2. How it is measured

### 2.1 Direct or proxy; construct validity
**Direct** for the checkable instructions in the test; **proxy** for following instructions in general, hence `mixed`. Checkable instructions are mostly about form, so the number says little about instructions on substance.

**Using a proxy with a known gap.** The number can compare models or prompts on keeping to stated formats and constraints. It cannot show that a model follows instructions about content, priorities or tone. Before relying on it for those, add a judged evaluation of such instructions, for example with a [judge rating](judge-rating.md).

### 2.2 Reliability
Deterministic given the outputs and checking programs. Variation comes from sampling the model; report the decoding settings.

### 2.3 Data collection and measurement error
Run the model on the prompts and apply the checking programs. Checkers can misfire, for example when a model wraps its answer in extra text; loose checking (2.4) reduces this.

### 2.4 Computation
- **Prompt-level:** share of prompts whose instructions are all satisfied.
- **Instruction-level:** share of individual instructions satisfied, over all prompts.
- **Strict vs loose:** loose checking first applies transformations to the output, such as removing markdown or a first or last line, and counts an instruction as followed if any version passes [zhou2023] (check against the paper).

### 2.5 Unit and scale
A proportion from 0 to 1. Prompt-level is lower than instruction-level for the same outputs.

### 2.6 Instruments
**Checkable instructions on form**
- **IFEval** [zhou2023]: prompts with verifiable instructions in categories such as length, keywords, format, case and punctuation; reported at prompt and instruction level, strict and loose.

## 3. Why it is measured

### 3.1 Use cases
- A team building an email-drafting feature checks that a new model keeps to required lengths and formats before switching.
- A model release reports IFEval prompt-level strict accuracy next to knowledge and math benchmarks.

### 3.2 Purposes
Model selection and regression testing for format and constraint compliance.

### 3.3 Assumptions
Checkable instructions stand for the instructions users give; the checking programs are correct.

## 4. Who is involved

### 4.1 Measurers and cost of measuring
ML engineers; cheap once the prompts and checkers exist.

### 4.2 Consumers and decisions informed
Teams choosing models for features with strict output formats.

### 4.3 Risks: misuse, misinterpretation, gaming, Goodhart's law
Tuning on the instruction categories in the test raises the score without improving instructions on substance.

## 5. Related metrics

### 5.1 Operationally related metrics
[Accuracy](accuracy.md) uses the same share-correct computation against an answer key.

### 5.2 Conceptually related metrics
[Judge Rating (model judge)](judge-rating.md) can score instructions that need judgment.

<!-- generated:neighbours:start -->
- Sibling construct: [Learned Reference-Based Score](learned-reference-score.md) (Generation performance: content adequacy), [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](rouge.md) (Generation performance: content adequacy), [Factual Precision in Atomicity Score (FActScore)](factscore.md) (Generation performance: factuality), [pass@k](pass-at-k.md) (Generation performance: functional correctness), [Answer Faithfulness](answer-faithfulness.md) (Generation performance: groundedness)
<!-- generated:neighbours:end -->

### 5.3 Empirical co-movements
None recorded.

## 6. Links to business objectives
**Sustained use** and **improved usability:** positive, theoretical: outputs that follow instructions need fewer retries. Not measured with users.

## 7. Sources
- [zhou2023]: IFEval.

## Open questions and review notes
- A separate page from Accuracy because correctness is checked against instructions by programs, not against an answer key (D5). Is that the right split?
