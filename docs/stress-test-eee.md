# Stress test: Every Eval Ever metrics mapped onto the wiki

> Run on 2026-11-02 against wiki commit `0cbe6cc` (39 metrics, 59 constructs, decisions D1-D27). Hand-classified by an AI assistant; treat each row as a judgment to check.

## Why

[Every Eval Ever](https://github.com/evaleval/every_eval_ever) (EEE) is a shared schema and repository for AI evaluation results [batzner2026]. Its companion [eval-card-registry](https://github.com/evaleval/eval-card-registry) gives canonical ids to 457 metrics. The test asked: if those metrics came into this wiki, would the schema hold?

The two projects sit at different levels. EEE records **runs**: one score, from one model on one benchmark, under one configuration. The wiki describes **classes** (metric pages) and representative **objects** (instruments) (D27). A run in EEE is keyed by benchmark and metric, which is the wiki's (instrument, metric) pair.

## Method

- **Sample.** 50 of the 457 registry metrics, drawn at random (seed 20261102) and stratified by the registry's own labels: unlabeled drafts 19, `bespoke-paper` family 7, `rate` family 7, reviewed core metrics 7, dataset-specific 3, catch-all 1, other families (pose error, codecs, speech quality and so on) 6.
- **Scope.** **in**: text and LLM, IR, recommender systems, HCI, agents. **border**: other modalities whose output people consume (speech, images, video, documents). **out**: no human-facing use (pose, 3D detection, codecs, driving, RL games). **?**: the registry gives no definition.
- **Fit.** **existing**: an existing page, possibly as a parameter variant or a new instrument. **new page**: fits the schema as it is. **new type/construct**: fits the D23 rule, but the DAG needs a new output type or construct. **object**: an instrument, not a metric. **unresolvable**: no definition to map.

## Mapping

| # | Registry id | Scope | Fit | Wiki target / note |
|---|---|---|---|---|
| 1 | acc-at-0-25 | out | — | 3D visual grounding (IoU ≥ 0.25). |
| 2 | auc-5 | out | — | Pose accuracy curve. |
| 3 | clip-r-precision | border | new type | Text-to-image alignment judged by CLIP. Needs an image-generation output type; the scorer (CLIP) is the instrument. |
| 4 | comet | in | new page | Content adequacy (MT) scored by a learned model. The scorer is the instrument. |
| 5 | counting-precision | ? | unresolvable | "CntP"; no definition in the registry. |
| 6 | hits-at-50 | in | existing | Recall (benchmark), k = 50 with one relevant item. |
| 7 | human-normalized-score | out | — | Atari RL; normalization to a human baseline. |
| 8 | inception-score | border | new type | Image generation quality via a classifier. |
| 9 | llm-score | in | unresolvable | Generic LLM-judge score; would belong on a missing "judge rating" page. |
| 10 | maniqa | out | — | No-reference image quality. |
| 11 | map-at-10 | in | new page | Mean Average Precision: a coverage gap, fits trivially. |
| 12 | maph | out | — | 3D detection. |
| 13 | mse | border | new type | Regression; in scope via rating prediction in recommenders. Needs a numeric-prediction output type. |
| 14 | ndcg-at-5 | in | existing | nDCG, k = 5. |
| 15 | radgraph-f1 | in | existing | F1 over clinical entities in generated reports; adds content adequacy to F1's constructs. |
| 16 | rouge-lsum | in | existing | ROUGE variant. |
| 17 | soda | out | — | Dense video captioning. |
| 18 | tar-at-far | border | existing | Face verification; Recall at an operating point fixed by the false-accept rate. |
| 19 | wer | border | new page | Speech recognition; answer correctness with partial credit (one correct transcript per item). |
| 20 | collision-rate-2s | out | — | Driving. |
| 21 | drivelm-p1-3-gpt-score | out | — | Driving VQA, GPT judge. |
| 22 | lps | out | — | Image restoration. |
| 23 | mmau-pro-open-ended-judge-score | border | new page | Audio QA, LLM judge; same missing "judge rating" class as #9. |
| 24 | restoration-score-rs | out | — | Image restoration, VLM judge. |
| 25 | rhae | in | new construct | Agent action efficiency relative to humans (ARC-AGI-3): a system-level efficiency construct is missing. |
| 26 | sim | border | new type | Saliency-map similarity (used in visualization research). Needs a map-prediction output type. |
| 27 | auroc | in | existing | ROC-AUC. |
| 28 | avg-accuracy | in | existing | Accuracy averaged over several benchmarks: an aggregate across instruments. |
| 29 | cds | ? | unresolvable | No definition in the registry. |
| 30 | r-at-1-iou-0-3 | border | existing | Video moment retrieval; Recall@k with an IoU match rule. |
| 31 | r-at-100-iou-0-3 | border | existing | Same. |
| 32 | r-at-5-iou-0-1 | border | existing | Same. |
| 33 | segmentation-f1-max | out | — | Anomaly segmentation; F1 at the best threshold. |
| 34 | accuracy | in | existing | Accuracy. |
| 35 | ast-accuracy | in | existing | Tool Call Accuracy; BFCL as an instrument. |
| 36 | bertscore-recall | in | new page | Content adequacy by embedding similarity. The scorer is the instrument. |
| 37 | pass-at-1 | in | existing | pass@k, k = 1. |
| 38 | prompt-level-loose-accuracy | in | new construct | IFEval: instruction following, the construct deferred in D23, is now needed. |
| 39 | scicode.main | in | existing | pass@k; SciCode as an instrument. |
| 40 | summac | in | new page | Groundedness of summaries by an NLI scorer (sibling of Answer Faithfulness). |
| 41 | mdpbench-latin | border | object | A benchmark subset score, not a metric. |
| 42 | ocrbench-v2-chinese-score | border | object | Same. |
| 43 | truthfulqa-mc2 | in | new page | Probability mass on true answers: a different computation on an existing instrument (TruthfulQA). |
| 44 | mean-score | in | unresolvable | Registry catch-all. |
| 45 | b-nmje | out | — | Pose error. |
| 46 | bd-rate-ms-ssim-rgb | out | — | Video codec. |
| 47 | bpsp | out | — | Compression. |
| 48 | pesq-wb | border | new page | Predicted perceived speech quality; the scorer is the instrument. |
| 49 | plcmos | border | new page | Predicted mean opinion score; same. |
| 50 | stoi | border | new page | Predicted speech intelligibility; same. |

### Counts

| Scope | n | existing | new page | new type/construct | object | unresolvable |
|---|---|---|---|---|---|---|
| in | 19 | 10 | 5 | 2 | 0 | 2 |
| border | 15 | 4 | 5 | 4 | 2 | 0 |
| out | 14 | — | — | — | — | — |
| ? | 2 | — | — | — | — | 2 |

## Findings

**What held**
- About half of the in-scope metrics (10 of 19) map to existing pages, mostly as parameter variants (nDCG@5, Hits@50, Pass@1) or new instruments (BFCL for Tool Call Accuracy, SciCode for pass@k). Keeping parameter variants on one page (D5) absorbs the registry's fragmentation.
- The input/output rule for component constructs (D23) extends without strain: the new output types the sample needed (numeric prediction, map prediction, image generation, spatial grounding) are each defined by their output space.
- The class/object split (D27) handles the registry's dataset-specific "metrics", which are benchmark subset scores, that is, instruments.
- The two constructs the sample needed, instruction following and agent efficiency, fit the DAG rules.
- Name ambiguity was milder than expected. EEE holds only benchmark results, so every registry id maps to the benchmark-method page; the D20 split never caused a collision.

**What strained**
- **Scorers.** About a dozen metrics are defined by a scoring model rather than by test data: COMET, BERTScore, SummaC, CLIP, Inception Score, PESQ, PLCMOS and several LLM judges. D27 said an object fixes the content; these fix the judgment.
- **Aggregates.** Averages over several benchmarks are neither a class nor a single object.
- **Coverage gaps.** Mean Average Precision, judge ratings, learned reference-based scores, Word Error Rate, and win rate or Elo from pairwise comparison had no page.
- **Component or system.** Judged LLM outputs had no clear root.
- **Scope.** 29 of 50 metrics were out of scope or in other modalities; the wiki had no stated boundary.

## Outcome

- **D28**: component or system is decided by the role a model plays.
- **D29**: in scope when people consume the output or interact with the system, in any modality.
- **D30**: instruments are content, scorer or suite; suites carry a prominent caveat.

### Pages added

| Page | Covers from the sample | Notes |
|---|---|---|
| [Instruction-Following Accuracy](../metrics/instruction-following-accuracy.md) | #38 IFEval prompt-level loose accuracy | With the new construct [instruction following](../constructs/instruction-following.md). |
| [Mean Average Precision (MAP)](../metrics/mean-average-precision.md) | #11 mAP@10 | Notes that mAP in object detection is a different computation. |
| [Judge Rating (model judge)](../metrics/judge-rating.md) | #9 LLM-Score, #23 MMAU-Pro judge score | System root (D28); MT-Bench as content, the LLM judge as scorer. |
| [Learned Reference-Based Score](../metrics/learned-reference-score.md) | #4 COMET, #36 BERTScore | BERTScore, COMET and BLEURT as scorer instruments (D30). |

Existing pages gained scorer or suite instruments: Toxicity Rate (Perspective API), Answer Faithfulness (RAGAS), FActScore (its estimator) and Accuracy (HELM as a suite).

Still open: the agent-efficiency construct (RHAE), Word Error Rate, win rate and Elo, the new output types for other modalities, and an `external_ids` field that records the registry ids each page covers.
