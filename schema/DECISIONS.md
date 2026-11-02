# Schema decisions

A record of decisions about the wiki's structure, why they were made, and what was considered instead. Newest first. Change a decision by adding a new entry that supersedes the old one; do not rewrite history.

---

## 2026-11-02 (who controls a variable; instruments revisited)

### D24. Roots differ in who controls the variable; latent abilities belong to the user root only
- **Decision.**
  - Component and system constructs are properties of what builders design and can change: swap the model, retune the retriever, change the prompt. Task constructs are outcomes of people using the system. User constructs are attributes of people that no one controls; a study can only select or sample people. In a study they serve as explanatory variables: covariates and moderators (does a design help low-numeracy users more than high-numeracy ones?).
  - Latent abilities (literacy, numeracy) are constructs at the user root. Machine capabilities such as math, reasoning or commonsense knowledge are not constructs in the DAG (D23). A builder who cares about them chooses test data and reads the scores, so a claim about them is a claim about the test data's validity.
  - User background (demographics, education) also sits at the user root. These attributes are recorded rather than tested, usually with a few questions on a questionnaire. They get constructs and short metric pages.
- **Why.** It extends the research-project reading of the wiki (README §1): the roots differ not only in what is needed to measure them (D12–D15) but in the role their variables play. Experimental design distinguishes variables that can be manipulated from attributes that can only be measured. The asymmetry between people and machines follows from that difference, so it is a principle, not an inconsistency.
- **Considered.** A page type for capabilities, covering both human abilities and machine capabilities, for symmetry. Rejected as heavy: it would curate a contested, open-ended taxonomy for what is, on the machine side, performance on chosen test data.
- **Boundary to watch.** Psychometric models fitted across many benchmarks estimate latent abilities of models, the way human abilities are estimated. If such a metric is added, it is a component metric with the [statistical modeling](../strategies/statistical-modeling.md) route and a generic construct; the abilities found are described in prose.
- **Vocabulary.** New `aspect` value `background` and new `quantity_form` value `category`, for recorded attributes such as age group or highest degree.

### D25. Instruments are named instantiations; instrument pages are grouped by construct and method (revises D19)
- **Decision.**
  - A standardized instrument (a questionnaire such as SUS, a test such as VLAT) is an instantiation of a metric, not a metric. Instruments that measure the same construct with the same method share one metric page, titled by the construct and the method: "Perceived Usability Score (questionnaire)" holds SUS, UMUX and UMUX-LITE.
  - Metric pages may list instruments in `operationalization.instruments` (name, sources, a one-line note) and describe them in a new section, 2.6 Instruments: what each asks, how it is scored, how they differ, when to choose which. Pages without named instruments say "None listed." Template version 0.3.
  - The 11 instrument pages were merged into 8: perceived usability (SUS, UMUX), mental workload (NASA-TLX, SMEQ), visualization literacy (VLAT, CALVI), numeracy (Berlin Numeracy Test), emotional response (SAM), user experience (UEQ), trust (Trust in Automation Scale), and visualization aesthetics (BeauVis). Instrument names stay searchable as aliases.
- **Refines D20.** For questionnaires and ability tests, "one computation" means scoring a standardized instrument for one construct. The scoring rules of individual instruments differ and are given per instrument in 2.4.
- **Why.** Pages named after instruments contradicted D19, which said instruments are named in prose. Merging them without a structured list lost the ability to compare instruments. The higher-level page states what the instruments share (construct, method, caveats) once, and the list keeps each instrument findable. For user-root constructs, the validated test is the operationalization, so the instruments matter more there than anywhere else.
- **Considered.** Keeping D19 unchanged and leaving instrument pages as they were (inconsistent). Instrument pages as their own page type (heavier, and D19's reasons against it still hold).


### D26. "Benchmark" is the canonical name and id of the test-collection method
- **Decision.** The method page for fixed inputs with reference outputs is titled "Benchmarks", and its id is renamed from `test-collection` to `benchmark` (vocabulary value, file name and every `research_method` list). The page explains that test collection, benchmark, labeled or annotated dataset, gold standard, ground truth, test set and test suite name the same concept in different fields; these are aliases. The D20 pages become "Precision (benchmark)" and "Recall (benchmark)", with ids `precision-benchmark` and `recall-benchmark`; the old titles stay as aliases.
- **Why.** "Test collection" is information-retrieval vocabulary that readers from machine learning and LLM evaluation did not recognize. "Benchmark" is the most widely understood name across the wiki's fields, and the agent-benchmark page already used it.
- **Considered.** Keeping "test collection" (precise in IR, unclear elsewhere); a combined title such as "Benchmark or test collection" (long, and the synonym list does the same job).

---

## 2026-11-02 (component types by input and output)

### D23. Component constructs are typed by input and output; latent demand is not a construct; route names removed from construct names
- **Decision.**
  - Under [component performance](../constructs/component-performance.md), constructs are sorted by the syntax and semantics of the component's computation: what it takes in, what it puts out, and what makes an output right for an input. The types so far are classification, closed answers, retrieval, generation, tool use and explanation.
  - New type **closed-answer performance** (`closed-answer-performance`), with **answer correctness** (`answer-correctness`): each item has one correct answer (an option given with the question, a number, a short span), and the set of possible answers changes from item to item. Accuracy (exact match), token-overlap F1 and pass@k (on problems with a key) now measure it.
  - What test data probes, such as knowledge, reasoning, math or language modeling, is the **latent demand** of the computation (its pragmatics, as opposed to its syntax and semantics). It is not a construct in the DAG. It belongs to the test data and is named in prose and cited, like instruments (D19).
  - Two constructs named after how they are scored are renamed: `reference-similarity` → **content adequacy** (`content-adequacy`), and `verifiable-correctness` → **functional correctness** (`functional-correctness`). Functional correctness now covers code only; final answers to math problems moved to answer correctness.
- **Why.**
  - Closed answers are not classification. A classifier chooses from one label set shared by all items; a multiple-choice question brings its own options. Question answering, classification and ranking have long been treated as different tasks in NLP and IR.
  - Any type of computation can be used to probe any demand. Classification in the broadest sense can test knowledge, reasoning and math, and language modeling is classification over the next token. A DAG sorted by demand would have no stable shape. One metric page (accuracy) serves every demand, so demand is not a property of the metric page either. When the wiki is adapted to a use case, the use case's goals are open-ended anyway. The registry of Every Eval Ever shows the alternative: about 110 flat tags that mix capabilities, qualities (safety), modalities, domains, languages and formats [batzner2026].
  - Route names in construct names break the separation of constructs and strategies (D1, D10). The old names also made ROUGE a "proxy" for a construct defined as what ROUGE computes; it is now a proxy for content adequacy.
- **Considered.** Broadening classification to "a correct answer from a constrained space" (rejected: hides the per-item answer space). A capability subtree for knowledge, reasoning and so on (rejected, see above). An optional `probes:` field on metric pages (not adopted: the same computation probes every demand).
- **Open.**
  - The definition of a construct says any concept of interest can be one, but latent demands are kept out of the DAG. The definition may need refining, for example by stating what kind of property each root admits.
  - The rule that separates component from system (one input-output mapping judged per call, vs a closed loop with an environment or the deployed configuration) is not decided.
  - Sketched but not adopted: retrieval broadened to ranking, generation split into open-ended text and code, and a judgment type (reward models, LLM-as-judge). Constructs that cut across types, such as confidence quality and instruction following, wait until a metric needs them.

---

## 2026-11-02 (no study records; docs map)

### D22. No pages or records for individual studies
- **Decision.** The wiki does not keep a list of studies or evidence records (one record per paper: which metric, construct, method and route it used, and what it found), and does not try to map relationships between constructs. Evidence stays where it is now: cited in section 5.3 and section 6 of metric pages, and in the objective tables.
- **Why.** Constructs are open-ended, so the space of construct-to-construct relationships is too. Curating study records would turn the wiki into a weaker copy of literature databases, and the effort of extracting each study would compete with keeping metric pages good.
- **Considered.** A structured file of evidence rows, starting from the objective tables. Not pursued.

### Also on 2026-11-02
- `docs/wiki-map.md` is generated by `scripts/build.py`: every page linked from one place, by root, layer and objective.
- The `migration/` notes were removed after the DAG population; they remain in git history.
- `vocabulary.yaml` no longer records where its facets came from; the facets are explained on their own.

---

## 2026-11-01 (comparison designs; agreement statistics)

### D21. Controlled comparison as a method, difference scoring as a route; agreement statistics stay on route pages
- **Decision.**
  - New method **controlled comparison of conditions** (`controlled-comparison`): the same measurement under conditions that differ in one deliberate way. Its named practices are baseline comparison, ablation, perturbation and stress testing, counterfactual testing, disaggregated (subgroup) evaluation, feature removal, and hypothesis testing.
  - New route **difference scoring: changes between conditions** (`difference-scoring`): the metric is the change between scores under the conditions, whether a difference, relative change, ratio, or average over steps.
  - New methods **task study**, **adversarial testing** and **ability tests**, each with a vocabulary value and a page. Ability tests settle the open question on the questionnaire page: tests with right answers are scored against a key, not self-rated.
  - Agreement statistics (Cohen's and Fleiss' kappa, Krippendorff's alpha, the intraclass correlation, judge-human correlation, position consistency) describe judges, not systems, tasks or users. They go in the reliability sections (3.2) of the route pages, not on metric pages or in the construct DAG.
- **Boundary with D10.** Study design stays out of scope when a comparison is used only to test an existing metric (an A/B test on task time). It is in scope when the difference is the metric itself (performance drop, subgroup gap). A significance test on a difference is analysis, not measurement.
- **Naming.** "Contrast" is the statistical term but is read differently in machine learning (contrastive learning, contrastive explanations, contrast sets). Plain "difference" and "relative scoring" were also considered. "Difference scoring" was chosen: it follows the measurement-theory term "difference scores" [cronbach1970] and reads as a route, distinct from comparative judgment and comparison against reference data.
- **Also.** D15's deferral of generation components is lifted: generation, tool use and explanation components were added with the DAG population (see commit history for 2026-11-01). Recommendation and interface components stay deferred.

---

## 2026-11-01 (same name, different root)

### D20. One metric page per computation per root; titles qualified by method
- **Decision.** If the same computation measures constructs under different roots of the construct DAG, it gets one page per root. All of a page's `construct.measures` must share a root; the validator checks this. Method variants within a root stay on one page: precision from explicit user judgments and precision inferred from clicks are the same task-level page. When a name exists under more than one root, the titles are qualified by how the number is obtained, e.g. "Precision (test collection)" and "Precision (user on task)"; aliases keep the plain name searchable. This refines D5 and limits D6 to constructs under one root.
- **Example.** Precision is split into [Precision (test collection)](../metrics/precision-benchmark.md) (component level: fixed queries, assessor judgments, topical relevance) and [Precision (user on task)](../metrics/precision-user-task.md) (task level: the user's own queries and judgments, the new construct [situational relevance](../constructs/situational-relevance.md)). Recall is renamed to Recall (test collection); its task-level page is not written yet.
- **Why.** Only the formula is shared. Who sets the inputs, who judges, the construct, and the method and route all differ, so the numbers mean different things. The gap between them is a principal-agent problem: builders optimize the cheap test-collection number, users experience the task-level one, and the two are linked only empirically and weakly [hersh2000; turpin2006]. Separate pages let that link be stated as an empirical relation (5.3) instead of hiding inside one page whose front matter mixed both methods.
- **Considered.** One page with several readings (D5 and D6 as they were): ambiguous front matter and no place for the gap. Splitting on every method change: too many pages, and the method is not what changes the meaning. Qualifying titles by root ("component level"): stable but less informative to readers; the user preferred qualifying by method. Avoided "offline/online": in IR "online evaluation" means live traffic and clicks, which belongs to the task-level page.

---

## 2026-11-01 (instruments not modeled)

### D19. Instruments are not modeled: no page type and no front matter list
*Revised by D25: instruments may be listed in front matter and described in section 2.6; they still get no pages of their own.*
- **Decision.** Specific instruments (a questionnaire's exact wording and layout, a test collection release, evaluation code such as trec_eval) get neither pages nor a structured `instruments` field. A metric page names an instrument in prose when it matters, and cites it. This closes the open item "measurement instruments as a page type" from D1 and the 2026-10-26 round.
- **Why.** A metric page should point to a way of operationalizing or computing the number that is specific enough to apply. It is not the place for the line-by-line implementation or the instrument itself; those live with their authors and are reached through citations.
- **Considered.** An optional `operationalization.instruments` list (name, version, role, source, note), with instrument pages once two or more metrics share one. Rejected as too detailed for the wiki's purpose.

---

## 2026-11-01 (research methods as a strategy layer)

### D18. Research methods get pages, as a second layer of strategy pages
- **Decision.** Strategy pages carry `layer: route | method` (strategy template 0.2). Route pages are the seven existing ones. A method page's id must be a `research_method` value in the vocabulary; the vocabulary stays the controlled list, and not every value needs a page. Section 1.2 is now "Typical pairings": route pages list their methods from `research_methods`, and method pages get the routes that name them, generated. Section 5 on a method page lists metrics whose `operationalization.research_method` includes it. Pilot pages: test collections, logs and telemetry, questionnaires and surveys.
- **Why.** In the analogy of a research project, constructs are the variables a study asks about (open-ended, can't be listed completely), strategies are its methodology (few, heavily reused, often renamed), and metrics are where the two meet. D10 gave only the route half of methodology a page. Methods carry caveats of their own that come from gathering the data (who and what is sampled, what is recorded) and that otherwise get repeated on metric pages or wrongly put on route pages.
- **Considered.** A fourth page type with its own template and folder: more structure than the pilot justifies. Keeping methods as tags only (D10): no place for method caveats, synonyms or lineage.
- **Test.** After the pilot, check whether method pages hold content not already on route or metric pages. If they stay thin, fold them back into the tag. Supersedes the part of D10 that kept methods as tags only.

---

## 2026-11-01 (InfinityPool proposals removed)

### D17. Metrics and constructs from the InfinityPool interview removed
- **Removed.** The five metric pages proposed from the InfinityPool metric-chat interview (2026-10-19): Active Labeling Time per Object, Object-Track Completeness, Pre-annotation Edit Rate, Work-Loss Incidence and Workaround Action Rate. Also removed: the six constructs added for them, namely annotation quality, annotation quality: completeness, machine pre-annotation quality, interaction friction, system reliability and work preservation. This supersedes D16's pending note.
- **Also removed.** Their rows in the objective tables, their links from other metric pages, and the seven unverified references added only for them (bernardin2008, ristani2016, luiten2021, vondrick2013, papadopoulos2017, parasuraman2010, alter2014).
- **Kept.** The schema 0.2 structure, the four construct roots and the "Use cases" subsection of the metric template. These are general, not InfinityPool-specific.
- **Why.** The team decided to drop the InfinityPool proposals rather than review them one by one. The pages remain in git history (last present at `fbb2bdd`) if any are wanted back.

---

## 2026-10-26 (frame sync removed)

### D16. Frame-Sync Accuracy removed for now
- **Removed.** The metric page Frame-Sync Accuracy (supersedes the relinking in D15). It is a component-level (interface) metric, so it should not sit under system reliability, and interface constructs are not yet defined. Temporal alignment stays removed.
- **Pending.** The team will revisit the interface and interaction metrics proposed for InfinityPool before adding interface constructs. The underlying issue (boxes out of step with video frames, InfinityPool requests #1 and #11) is still noted as an error source on [Object-Track Completeness](../metrics/object-track-completeness.md).

---

## 2026-10-26 (component clarifications)

### D15. Components: what counts, and what is deferred
- **Removed.** Interface performance and its child, temporal alignment (supersedes that part of D14). The interface was an example of a component; interface constructs will be added later. [Frame-Sync Accuracy](../metrics/frame-sync-accuracy.md) now links to system reliability, where temporal alignment sat before D14.
- **Deferred.** Generation and recommendation are components, because they can come from a backend without specifying how the front end renders them. Pages to be added later.
- **Component boundary.** A model that both retrieves and generates is still a component, or several components if those capabilities can be evaluated separately, because it leaves rendering to the interface, workflow, and UX design.

---

## 2026-10-26 (component split): Component characteristics as a fourth root

### D14. Separate what a component does from what the system does
- **Decision.** A new root, **Component characteristics** → **Component performance**, holds properties of single components or system functionalities judged on their own. Its children: **Retrieval performance** (moved from the system side, with retrieval effectiveness, relevance, and retrieval efficiency), **Classification performance** (new; classification correctness moved under it), **Interface performance** (new; temporal alignment moved under it), and **Machine pre-annotation quality** (moved; the team confirmed it is component level, not system level).
- **System side now.** System performance covers what the whole system delivers: end-to-end output quality, reliability, responsiveness. Output quality has no metric yet.
- **Why.** Classification, retrieval, and the interface are components or system functionalities. Gains in a component do not automatically become gains in the system or the task, and errors accumulate between components; keeping the levels apart makes that visible. It matches the `subject` facet (`system-component` vs `system`) and the component/system levels in the metric-chat skill.
- **Kept.** Trustworthiness keeps two parents: relevance (component side) and output quality (system side), as the same idea at two levels.
- **Open.** Name of "interface performance" (it may read as speed only); generation and recommendation components; where the component/system line falls for end-to-end models.

---

## 2026-10-26 (later still): User characteristics, system performance, annotation quality

### D13. Three roots, symmetric task and system sides
- **Decision.**
  - Added a third root, **User characteristics**: properties of the user alone, independent of a particular system or task. First child: **Literacy**, with information, visualization, and AI literacy, measurable by literacy tests.
  - Added **System performance** between System characteristics and its children (retrieval performance, output quality, system reliability, system responsiveness), mirroring Task characteristics → Task performance.
  - **Annotation quality** is a task characteristic (under task effectiveness): an annotation task involves both people and the system (interface, interaction design, machine pre-annotation). Label completeness now sits under it only.
  - Renamed `pre-annotation-quality` → `machine-pre-annotation-quality` ("Machine pre-annotation quality"), kept on the system side under output quality, because it is machine-generated.
  - Temporal alignment is now under system reliability only; its effect on annotation quality is an empirical link, as with responsiveness and task efficiency (D12).
- **Confirmed from D12.** Usability under task characteristics with task effectiveness and task efficiency under both task performance and usability; output quality, reliability, and responsiveness on the system side.
- **Open.** Whether reliability is part of system performance or a sibling; more user characteristics (expertise, propensity to trust automation, data literacy, numeracy).

---

## 2026-10-26 (later): Task characteristics vs system characteristics

### D12. Two top-level groups of constructs
- **Decision.** "Task" means the combined setting in which a user uses a system to achieve a certain goal. Constructs about that setting go under **Task characteristics**; constructs about the system alone (measurable without a user pursuing a goal) go under **System characteristics**. Either may sit several levels down.
- **Changes.**
  - Renamed `effectiveness` → `task-effectiveness` ("Task effectiveness") and `efficiency` → `task-efficiency` ("Task efficiency"). Both sit under the new **Task performance** (under Task characteristics) and also under Usability, which keeps the ISO 9241-11 decomposition.
  - Usability moved under Task characteristics.
  - New **Retrieval performance** (under System characteristics) with children Retrieval effectiveness and the new **Retrieval efficiency**. This settles D3's open point: retrieval effectiveness is a level in the DAG.
  - Output quality, System reliability, and System responsiveness moved under System characteristics. Responsiveness is no longer under task efficiency: its effect on task time is recorded as an empirical link on metric pages, not as a DAG edge.
- **Why.** Separating what can be measured on the system alone from what needs a user pursuing a goal mirrors the component/system vs interaction/outcome levels in the metric-chat skill, and makes explicit that system gains do not automatically become task gains.
- **To confirm.** Task effectiveness and task efficiency keep two parents (task performance and usability). Annotation quality stays under output quality (system side), while label completeness also sits under task effectiveness. Whether a third root for properties of the user alone (expertise, trust as an attitude) is needed. Whether an intermediate "system performance" construct is wanted.

---

## 2026-10-26: Constructs, strategies, and validity (metric template 0.2)

Decided in a design discussion between the project lead (after a team discussion) and an AI assistant. Each item gives the decision, the reason, and the alternatives considered.

### D1. Three first-class page types: constructs, metrics, strategies
- **Decision.** Constructs (what we want to know about) and metrics (procedures that yield a number) are both first-class. Strategies (quantification routes) are a third type.
- **Why.** A metric page alone cannot say that precision and recall are two measures of the same narrower concept, or how that concept sits under a broader one. Strategies recur across metrics and carry shared caveats, which would otherwise be repeated on every metric page.
- **Considered.** Metrics only, with flat tags (the previous design). Measurement instruments as a fourth page type (deferred; instruments stay as attributes of metric pages).

### D2. The layer is called "construct"; "concept" is a plain-language synonym
- **Why.** Measurement theory uses "construct" for a concept defined well enough to try to measure it [jacobs2021]; the wiki already used the word in every page's front matter.

### D3. Constructs form a DAG
- **Decision.** A construct may have several broader constructs (`broader: [...]`).
- **Why.** Constructs such as trustworthiness are useful in retrieval, recommendation, and other AI outputs, so a strict tree would force duplicates.
- **Assumed, to confirm.** "Retrieval effectiveness" is a level in the DAG (retrieval effectiveness → relevance → topical relevance), not just a namespace prefix on titles.

### D4. Metrics have no hierarchy of their own
- **Decision.** No "is-a" tree among metrics. Hierarchy lives in constructs; metrics attach to constructs.
- **Why.** What looks like a metric hierarchy is usually variants (precision@k), composition (F1 from precision and recall; SUS from its items), or derivation (MAP from AP). None of these is "is-a", and a second tree would drift from the construct DAG.

### D5. One page per operationalization, with one abstract construct statement
- **Decision.** A metric page is an operationalization. Variants that differ only in a parameter stay on the page. `construct.statement` is written at the level of the "spirit" of what the number measures. Uses in different fields (precision in search vs in classification) go in 3.1 Use cases.
- **Why.** If the computation is the same or very similar, the meaning should be too; splitting meaning per use would hair-split, and the ways of applying a computation are open-ended.
- **Considered.** Separate pages per field ("precision (retrieval)", "precision (classification)"); one page with a list of per-use construct statements. Both rejected.
- **When to split.** When computation differs, not just the name (e.g. "precision" as repeatability in measurement science), or when it is adapted to a different unit (Object-Track Completeness is its own page, linked to Recall as operationally related).

### D6. A metric can link to several constructs
- **Decision.** `construct.measures: [...]`, e.g. precision → topical relevance and classification correctness. How the metric reads under each construct is explained on the construct page.
- **Considered.** One link to a field-neutral construct (would mix "is-a" with "is measured by" in the DAG); one link to the primary construct only (would hide the metric from other parts of the DAG).

### D7. Related metrics: three untyped-but-grouped kinds
- **Decision.** Section 5 headings: 5.1 Operationally related metrics, 5.2 Conceptually related metrics, 5.3 Empirical co-movements. Front matter `related[].kind` is `operational | conceptual | empirical`. No finer relation types for now.
- **Why.** Fine-grained relation types were premature; three kinds group the prose and let scripts sort links. Empirical co-movement is kept apart because evidence often contradicts what concepts suggest.
- **Migration.** Old `relation` values were mapped: component-of → operational; same-construct and complementary → conceptual; trade-off, correlated, causally-linked → empirical. Exceptions made by hand: precision ↔ recall → conceptual (sibling property on the same judgments); Object-Track Completeness → Recall and Active Labeling Time → Task Completion Time → operational (variants); Pre-annotation Edit Rate → Precision → conceptual (a stand-in).

### D8. Every template heading carries a guiding note; a readable guide is generated
- **Decision.** Every `##` and `###` heading in each template has a comment saying what it answers. `scripts/build.py` turns these into `schema/page-guide.md`.
- **Why.** Comments are invisible on rendered pages; readers who do not open raw files still need the questions. One source (the template) avoids drift.

### D9. The construct DAG is kept in two synced places
- **Decision.** Each construct page's `broader` field is the structure; `constructs/dag.yaml` is a hand-editable view of the same structure. `scripts/sync_constructs.py` compares both with the last synced state and copies changes across; `constructs/index.md` (Mermaid diagram and nested list) is generated.
- **Rules.** Both sides changed the same construct differently → stop, resolve by hand. Removed from the YAML → stop; a person deletes or merges the page (the script never deletes pages). Renames use `renamed_from:` in the YAML. Cycles are refused. The validator fails if the two disagree.
- **Known limit.** Comments inside `dag.yaml` other than its header are not kept when the script rewrites it.

### D10. Measurement strategies: two layers; strategy pages are quantification routes
- **Decision.** Separate *how data is gathered* (research method, a vocabulary tag: test collection, logs, task study, questionnaire, interview, diary/ESM, observation/think-aloud, physiological sensing, expert inspection, analytical model, simulation) from *how data becomes a number* (route, a strategy page: direct reading, self-rating, external judgment, comparison against reference data, comparative judgment, coding qualitative data, statistical and latent-variable modeling). Named practices (Cranfield, LLM-as-a-judge, interleaving) are sections of route pages.
- **Why.** There is no single accepted taxonomy across HCI, IR, ML, and measurement theory, but several independent dimensions [webb1966; campbell1959; bollen1991; jacobs2021]. Mixing method and route made qualitative methods hard to place. Caveats that repeat across metrics attach mostly to the route.
- **Where qualitative methods sit.** As a source of numbers only through *coding qualitative data*. More often they serve roles around metrics: discovering constructs (construct pages, section 6), checking validity (metric pages, 2.1), explaining movements (5.3).
- **Out of scope for strategies.** Study design (A/B tests, within-subject experiments, longitudinal cohorts): it decides the strength of evidence about a metric (section 6), not how the number is produced.
- **Considered.** Pages for named method-route combinations; pages for both layers.

### D11. Validity: light on pages, deep in conversation
- **Decision.** Pages carry just enough validity content: a short prompt in 2.1, reliability in 2.2, the consequential side in 4.3, and a front matter flag `operationalization.validity_concern: {level: low | moderate | high, note}`. The full set of validity questions lives in the `metric-chat` interview skill, which raises them only when they matter.
- **Why.** Validity thinking is bimodal: unnecessary when a metric obviously is the thing, essential when no metric seems to capture it. A newcomer should not face a list of validity types on every page; an interactive assistant can ask the right questions when the flag, a proxy, an abstract construct, or a disagreement calls for it [jacobs2021].

### Open items from this round
- `aspect` (a facet tag) partly overlaps the construct DAG. Keep, derive from constructs, or drop?
- `data_source` overlaps with `research_method` and `route`. Proposal: retire `data_source` next round after mapping its values.
- Topical relevance: split into exactness and completeness as narrower constructs? Proposed, not decided.
- Placement questions noted on construct pages (mental workload under efficiency; system reliability as a root; output quality as a shared parent).
- Should LLM-as-a-judge, simulated users, and synthetic references get their own strategy pages as the practice matures?
- Measurement instruments (e.g. a specific questionnaire version) as a page type: deferred. (Closed by D19: not modeled.)

## Sources
Keys refer to `references/bibliography.yaml`: [jacobs2021], [webb1966], [campbell1959], [bollen1991].
