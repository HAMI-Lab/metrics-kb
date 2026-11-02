#!/usr/bin/env python3
"""Check metric, construct, and strategy pages against templates, vocabulary, bibliography, and each other.

Usage: python scripts/validate.py          (exit code 1 if errors)
Requires: PyYAML (pip install pyyaml)
"""
import re
import sys

import yaml

import build
from common import ROOT, load, split

VOCAB = yaml.safe_load((ROOT / "schema/vocabulary.yaml").read_text())
BIB = yaml.safe_load((ROOT / "references/bibliography.yaml").read_text())


def headings(template):
    return [h.strip() for h in re.findall(r"^#{2,3} .+$", (ROOT / "schema" / template).read_text(), re.M)]


METRIC_HEADINGS = headings("metric-template.md")
CONSTRUCT_HEADINGS = headings("construct-template.md")
STRATEGY_HEADINGS = headings("strategy-template.md")
FACETS = ["subject", "aspect", "perspective", "quantity_form", "context"]
DIRECTIONS = {"positive", "negative", "non-monotonic", "unknown"}
OBJECTIVES = {p.stem for p in (ROOT / "objectives").glob("*.md")}

errors, warnings = [], []


def in_vocab(value, name):
    return isinstance(value, str) and (value in VOCAB[name] or value.startswith("other:"))


def common_checks(where, pid, fm, body, page_type, required_headings):
    err = lambda msg: errors.append(f"{where}: {msg}")
    if fm is None:
        err("missing front matter")
        return False
    if fm.get("id") != pid:
        err(f"id '{fm.get('id')}' does not match file name")
    if fm.get("page_type") != page_type:
        err(f"page_type should be '{page_type}'")
    if fm.get("status") not in VOCAB["status"]:
        err(f"bad status '{fm.get('status')}'")
    for h in required_headings:
        if not re.search("^" + re.escape(h) + r"\s*$", body, re.M):
            err(f"missing heading '{h}'")
    return True


def check_metric(mid, page, metrics, constructs, strategies):
    fm, body = page["fm"], page["body"]
    n = f"metrics/{mid}.md"
    if not common_checks(n, mid, fm, body, "metric", METRIC_HEADINGS):
        return
    err = lambda msg: errors.append(f"{n}: {msg}")

    c = fm.get("construct") or {}
    if not c.get("statement"):
        err("construct.statement is empty")
    measures = c.get("measures") or []
    if not measures:
        err("construct.measures is empty: link at least one construct")
    for cid in measures:
        if cid not in constructs:
            err(f"construct.measures: '{cid}' has no page in constructs/")
    for f in FACETS:
        vals = c.get(f) or []
        if not vals:
            warnings.append(f"{n}: construct.{f} is empty")
        for v in vals:
            if not in_vocab(v, f):
                err(f"construct.{f}: '{v}' not in vocabulary")

    o = fm.get("operationalization") or {}
    if o.get("measure_type") not in VOCAB["measure_type"]:
        err(f"bad measure_type '{o.get('measure_type')}'")
    for key, vocab in [("collection_mode", "collection_mode"), ("data_source", "data_source"),
                       ("research_method", "research_method")]:
        for v in o.get(key) or []:
            if not in_vocab(v, vocab):
                err(f"operationalization.{key}: '{v}' not in vocabulary")
    if not o.get("research_method"):
        err("operationalization.research_method is empty")
    route = o.get("route") or []
    if not route:
        err("operationalization.route is empty")
    for r in route:
        if r not in strategies:
            err(f"operationalization.route: '{r}' has no page in strategies/")
        elif (strategies[r]["fm"] or {}).get("layer") == "method":
            err(f"operationalization.route: '{r}' is a method page; list it under research_method instead")
    vc = o.get("validity_concern") or {}
    if vc.get("level") not in VOCAB["validity_concern"]:
        err(f"bad validity_concern.level '{vc.get('level')}'")
    if not vc.get("note"):
        warnings.append(f"{n}: validity_concern.note is empty")

    if (fm.get("cost") or {}).get("level") not in VOCAB["cost_level"]:
        err("bad cost.level")

    for r in fm.get("related") or []:
        if r.get("metric") not in metrics:
            err(f"related metric '{r.get('metric')}' has no page")
        if r.get("kind") not in VOCAB["related_kind"]:
            err(f"related '{r.get('metric')}': bad kind '{r.get('kind')}'")

    for obj, v in (fm.get("objectives") or {}).items():
        if obj not in OBJECTIVES:
            err(f"objective '{obj}' has no page")
        if v.get("direction") not in DIRECTIONS:
            err(f"objective {obj}: bad direction '{v.get('direction')}'")
        if v.get("evidence") not in VOCAB["evidence_strength"]:
            err(f"objective {obj}: bad evidence '{v.get('evidence')}'")

    check_citations(n, fm, body)
    check_links(page["path"], body)


def check_construct(cid, page, constructs):
    fm, body = page["fm"], page["body"]
    n = f"constructs/{cid}.md"
    if not common_checks(n, cid, fm, body, "construct", CONSTRUCT_HEADINGS):
        return
    for b in fm.get("broader") or []:
        if b not in constructs:
            errors.append(f"{n}: broader construct '{b}' has no page")
        if b == cid:
            errors.append(f"{n}: lists itself as broader")
    check_citations(n, fm, body)
    check_links(page["path"], body)


def check_strategy(sid, page):
    fm, body = page["fm"], page["body"]
    n = f"strategies/{sid}.md"
    if not common_checks(n, sid, fm, body, "strategy", STRATEGY_HEADINGS):
        return
    layer = fm.get("layer")
    if layer not in ("route", "method"):
        errors.append(f"{n}: layer should be 'route' or 'method', not '{layer}'")
    if layer == "method":
        if sid not in VOCAB["research_method"]:
            errors.append(f"{n}: a method page's id must be a research_method value in the vocabulary")
        if fm.get("research_methods"):
            errors.append(f"{n}: research_methods should be empty on a method page")
    elif sid in VOCAB["research_method"]:
        errors.append(f"{n}: id is a research_method value, so layer should be 'method'")
    for v in fm.get("research_methods") or []:
        if not in_vocab(v, "research_method"):
            errors.append(f"{n}: research_methods: '{v}' not in vocabulary")
    check_citations(n, fm, body)
    check_links(page["path"], body)


def check_cycles(constructs):
    parents = {cid: [b for b in ((c["fm"] or {}).get("broader") or []) if b in constructs]
               for cid, c in constructs.items()}
    state = {}

    def visit(cid, stack):
        if state.get(cid) == "done":
            return
        if state.get(cid) == "active":
            errors.append("construct DAG has a cycle: " + " -> ".join(stack + [cid]))
            return
        state[cid] = "active"
        for p in parents[cid]:
            visit(p, stack + [cid])
        state[cid] = "done"

    for cid in sorted(parents):
        visit(cid, [])


def check_dag_yaml(constructs):
    path = ROOT / "constructs" / "dag.yaml"
    if not path.exists():
        if constructs:
            errors.append("constructs/dag.yaml is missing; run scripts/sync_constructs.py")
        return
    dag = yaml.safe_load(path.read_text()) or {}
    for cid in sorted(set(dag) | set(constructs)):
        if cid not in constructs:
            errors.append(f"constructs/dag.yaml lists '{cid}' but there is no page; run scripts/sync_constructs.py")
            continue
        if cid not in dag:
            errors.append(f"constructs/{cid}.md is not in dag.yaml; run scripts/sync_constructs.py")
            continue
        fm = constructs[cid]["fm"] or {}
        e = dag[cid] or {}
        if "renamed_from" in e:
            errors.append(f"dag.yaml '{cid}' has renamed_from; run scripts/sync_constructs.py")
        if str(e.get("title")) != str(fm.get("title")) or sorted(e.get("broader") or []) != sorted(fm.get("broader") or []):
            errors.append(f"dag.yaml and constructs/{cid}.md disagree; run scripts/sync_constructs.py")


def check_citations(n, fm, body):
    listed = set(fm.get("sources") or [])
    for k in listed - set(BIB):
        errors.append(f"{n}: source '{k}' not in bibliography")
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    cited = set()
    for group in re.findall(r"\[([A-Za-z0-9\-;, ]+)\](?!\()", body):
        for k in re.split(r"[;,]\s*", group):
            k = k.strip()
            if k in BIB or re.fullmatch(r"S\d+|[a-z][a-z\-]*\d{4}[a-z]*", k):
                cited.add(k)
    for k in cited - set(BIB):
        errors.append(f"{n}: cites [{k}] which is not in bibliography")
    for k in cited - listed:
        warnings.append(f"{n}: cites [{k}] in text but not in front matter sources")


def check_links(path, body):
    for target in re.findall(r"\]\(([^)#:]+\.md)\)", body):
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link '{target}'")


def main():
    metrics, constructs, strategies = load("metric"), load("construct"), load("strategy")
    for mid, p in metrics.items():
        check_metric(mid, p, metrics, constructs, strategies)
    for cid, p in constructs.items():
        check_construct(cid, p, constructs)
    for sid, p in strategies.items():
        check_strategy(sid, p)
    check_cycles(constructs)
    check_dag_yaml(constructs)
    for p in sorted((ROOT / "objectives").glob("*.md")):
        fm, body = split(p.read_text())
        if fm:
            check_citations(p.name, fm, body)
            check_links(p, body)
    for p in build.stale():
        errors.append(f"{p.relative_to(ROOT)} is out of date; run scripts/build.py")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:  ", e)
    print(f"{len(metrics)} metric, {len(constructs)} construct, {len(strategies)} strategy pages checked: "
          f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
