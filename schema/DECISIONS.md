# Schema decisions

A record of decisions about the wiki's structure, why they were made, and what was considered instead. Newest first. Change a decision by adding a new entry that supersedes the old one; do not rewrite history.

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
- Measurement instruments (e.g. a specific questionnaire version) as a page type: deferred.

## Sources
Keys refer to `references/bibliography.yaml`: [jacobs2021], [webb1966], [campbell1959], [bollen1991].
