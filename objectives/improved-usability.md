---
id: improved-usability
title: "Objective 2: Improved Usability"
page_type: objective
template_version: "0.1"
status: ai-draft
sources: [iso9241-11, hornbaek2007, sauro2009, kim2024, rong2022]
---

# Objective 2: Improved Usability

> The system lets its intended users reach their goals more effectively, more efficiently, and with more satisfaction.

## What it means
ISO 9241-11 defines usability as the extent to which specified users can use a system to achieve specified goals with effectiveness, efficiency, and satisfaction in a specified context of use [iso9241-11]. "Improved" means these move in the right direction between versions, without trading one away for another.

## How it can be observed
No single measure captures it. The usual practice is to measure all three parts:
- Effectiveness: task success, error rate, output quality ([Precision (benchmark)](../metrics/precision-benchmark.md) for the system side).
- Efficiency: [Task Completion Time](../metrics/task-completion-time.md), effort ([NASA-TLX](../metrics/mental-workload-score.md)), waiting time ([Response Latency](../metrics/response-latency.md)).
- Satisfaction: [SUS](../metrics/perceived-usability-score.md) and similar questionnaires.

These parts correlate only modestly with one another [hornbaek2007; sauro2009], so improving one does not guarantee improvement in the others.

## Metrics linked to this objective

| Metric | Direction | Evidence | Note |
|---|---|---|---|
| [Response Latency](../metrics/response-latency.md) | negative | causal (visual analytics) | |
| [Perceived Usability Score (questionnaire)](../metrics/perceived-usability-score.md) | positive | correlational | Measures perceived usability |
| [Task Completion Time](../metrics/task-completion-time.md) | negative | correlational | For the same outcome |
| [Mental Workload Score (questionnaire)](../metrics/mental-workload-score.md) | negative | correlational | Not at very low workload |
| [Precision (benchmark)](../metrics/precision-benchmark.md) | positive | correlational | Weaker than assumed |
| [Recall (benchmark)](../metrics/recall-benchmark.md) | positive | correlational | Batch gains do not always translate to users |
| [Precision (user on task)](../metrics/precision-user-task.md) | positive | theoretical | Part of effectiveness for the user's own task |
| [Accuracy](../metrics/accuracy.md) | positive | theoretical | Correct components are a precondition for effective tasks; the link to user outcomes is not measured. |
| [F1 Score](../metrics/f1-score.md) | positive | theoretical | Through output quality; not measured. |
| [Area Under the ROC Curve (ROC-AUC)](../metrics/roc-auc.md) | positive | theoretical | Through output quality; not measured. |
| [Expected Calibration Error (ECE)](../metrics/expected-calibration-error.md) | positive | theoretical | Calibrated confidence lets users decide when to rely on outputs. |
| [Normalized Discounted Cumulative Gain (nDCG)](../metrics/ndcg.md) | positive | theoretical | Better rankings are assumed to help users; offline-online links are weak. |
| [Mean Reciprocal Rank (MRR)](../metrics/reciprocal-rank.md) | positive | theoretical | When one answer suffices, finding it sooner saves effort. |
| [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](../metrics/rouge.md) | unknown | none | Too far from what users experience to say. |
| [Factual Precision in Atomicity Score (FActScore)](../metrics/factscore.md) | positive | theoretical | False content harms users' tasks. |
| [Answer Faithfulness](../metrics/answer-faithfulness.md) | positive | theoretical | Answers users can trace to sources support checking. |
| [Tool Call Accuracy](../metrics/tool-call-accuracy.md) | positive | theoretical | Through autonomous task completion; not measured. |
| [Area Over the Perturbation Curve (AOPC)](../metrics/aopc.md) | positive | theoretical | Faithful explanations are a precondition for users to understand the model. |
| [Attack Success Rate (ASR)](../metrics/attack-success-rate.md) | unknown | none | Safety measures can also make the system refuse harmless requests. |
| [Toxicity Rate](../metrics/toxicity-rate.md) | negative | theoretical | Toxic outputs make the system unpleasant to use. |
| [Demographic Parity Difference (DPD)](../metrics/demographic-parity-difference.md) | unknown | none |  |
| [Performance Drop Rate (PDR)](../metrics/performance-drop-rate.md) | negative | theoretical | Users rarely phrase inputs the way benchmarks do. |
| [pass^k](../metrics/pass-hat-k.md) | positive | theoretical | Consistent behaviour is easier to learn. |
| [Task Success Rate (agent benchmark)](../metrics/task-success-rate-benchmark.md) | positive | theoretical | Untested with users here. |
| [Cost per Task](../metrics/cost-per-task.md) | unknown | none | Cost is not something users experience directly. |
| [pass@k](../metrics/pass-at-k.md) | unknown | none | Users see one output at a time and often cannot check it, so large-k scores say little about their experience. |
| [Task Success Rate (user on task)](../metrics/task-success-rate-user.md) | positive | correlational | Effectiveness is part of usability by definition; correlations with other usability measures are modest. |
| [Decision Accuracy with AI Assistance](../metrics/decision-accuracy-with-ai.md) | positive | theoretical | Effectiveness of the person and system together. |
| [Over-reliance Rate](../metrics/over-reliance-rate.md) | negative | theoretical | Inappropriate reliance lowers decision quality. |
| [Under-reliance Rate](../metrics/under-reliance-rate.md) | negative | theoretical | Inappropriate reliance lowers decision quality. |
| [Forward-Prediction Accuracy](../metrics/forward-prediction-accuracy.md) | positive | theoretical | Understanding supports appropriate use of the system. |
| [User Experience Score (questionnaire)](../metrics/user-experience-score.md) | positive | theoretical | The pragmatic scales overlap with perceived usability. |
| [Emotional Response Score (questionnaire)](../metrics/emotional-response-score.md) | unknown | none |  |
| [Visualization Aesthetics Score (questionnaire)](../metrics/visualization-aesthetics-score.md) | unknown | none | Aesthetic pleasure is distinct from readability. |
| [Trust Score (questionnaire)](../metrics/trust-score.md) | unknown | none | More trust is good only when it matches trustworthiness. |
| [Visualization Literacy Score (ability test)](../metrics/visualization-literacy-score.md) | unknown | none | Describes users; used to explain or control for differences in outcomes, not as a target. |
| [Numeracy Score (ability test)](../metrics/numeracy-score.md) | unknown | none | Describes users; used to explain or control for differences in outcomes, not as a target. |
| [Demographic Profile (questionnaire)](../metrics/demographic-profile.md) | unknown | none | Describes users; used to explain or control for differences in outcomes, not as a target. |
| [Educational Attainment (questionnaire)](../metrics/educational-attainment.md) | unknown | none | Describes users; used to explain or control for differences in outcomes, not as a target. |
| [Instruction-Following Accuracy](../metrics/instruction-following-accuracy.md) | positive | theoretical | Fewer retries and corrections; not measured with users. |
| [Mean Average Precision (MAP)](../metrics/mean-average-precision.md) | positive | correlational | Batch effectiveness gains do not always reach users' tasks. |
| [Judge Rating (model judge)](../metrics/judge-rating.md) | unknown | none | Judge preferences, such as for longer answers, may not match what helps users. |
| [Learned Reference-Based Score](../metrics/learned-reference-score.md) | unknown | none | Too far from what users experience to say. |
| [Action Efficiency Relative to Humans](../metrics/action-efficiency-vs-humans.md) | unknown | none | Users rarely see action counts directly. |
| [Word Error Rate (WER)](../metrics/word-error-rate.md) | negative | theoretical | Errors must be corrected by users. |
| [Win Rate (pairwise comparison)](../metrics/win-rate.md) | unknown | none | Judge preferences may not match what helps users. |
| [Elo Rating (pairwise comparison)](../metrics/elo-rating.md) | unknown | none | Preference in a side-by-side vote is not the same as task success. |
| [Root Mean Squared Error (RMSE)](../metrics/root-mean-squared-error.md) | unknown | none | Too far from what users experience to say. |
| [Saliency Map Similarity (SIM)](../metrics/saliency-map-similarity.md) | unknown | none | Predicting attention can help designers, but the link to usability is not measured. |
| [CLIPScore](../metrics/clipscore.md) | unknown | none | Not measured with users. |
| [Grounding Accuracy](../metrics/grounding-accuracy.md) | unknown | none | Too far from what users experience to say. |

## Open questions
- For AI systems, should trust and appropriate reliance count as part of usability, or be treated as a third objective? Several spreadsheet sources treat them as central [kim2024; rong2022].
