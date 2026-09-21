#!/usr/bin/env python3
"""Check metric pages against the template, vocabulary, and bibliography.

Usage: python scripts/validate.py          (exit code 1 if errors)
Requires: PyYAML (pip install pyyaml)
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
VOCAB = yaml.safe_load((ROOT / "schema/vocabulary.yaml").read_text())
BIB = yaml.safe_load((ROOT / "references/bibliography.yaml").read_text())
TEMPLATE = (ROOT / "schema/metric-template.md").read_text()

REQUIRED_HEADINGS = [h.strip() for h in re.findall(r"^#{2,3} .+$", TEMPLATE, re.M)]
FACETS = ["subject", "aspect", "perspective", "quantity_form", "context"]
RELATIONS = {"same-construct", "complementary", "trade-off", "component-of", "correlated", "causally-linked"}
DIRECTIONS = {"positive", "negative", "non-monotonic", "unknown"}
OBJECTIVES = {p.stem for p in (ROOT / "objectives").glob("*.md")}

errors, warnings = [], []


def split(path):
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        errors.append(f"{path.name}: missing front matter")
        return None, text
    return yaml.safe_load(m.group(1)), m.group(2)


def in_vocab(value, name):
    return isinstance(value, str) and (value in VOCAB[name] or value.startswith("other:"))


def check_metric(path, ids):
    fm, body = split(path)
    if fm is None:
        return
    n = path.name
    err = lambda msg: errors.append(f"{n}: {msg}")

    if fm.get("id") != path.stem:
        err(f"id '{fm.get('id')}' does not match file name")
    if fm.get("status") not in VOCAB["status"]:
        err(f"bad status '{fm.get('status')}'")

    c = fm.get("construct") or {}
    if not c.get("statement"):
        err("construct.statement is empty")
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
    for key in ["collection_mode", "data_source"]:
        for v in o.get(key) or []:
            if not in_vocab(v, key):
                err(f"operationalization.{key}: '{v}' not in vocabulary")

    if (fm.get("cost") or {}).get("level") not in VOCAB["cost_level"]:
        err("bad cost.level")

    for r in fm.get("related") or []:
        if r.get("metric") not in ids:
            err(f"related metric '{r.get('metric')}' has no page")
        if r.get("relation") not in RELATIONS:
            err(f"bad relation '{r.get('relation')}'")

    for obj, v in (fm.get("objectives") or {}).items():
        if obj not in OBJECTIVES:
            err(f"objective '{obj}' has no page")
        if v.get("direction") not in DIRECTIONS:
            err(f"objective {obj}: bad direction '{v.get('direction')}'")
        if v.get("evidence") not in VOCAB["evidence_strength"]:
            err(f"objective {obj}: bad evidence '{v.get('evidence')}'")

    for h in REQUIRED_HEADINGS:
        if not re.search("^" + re.escape(h) + r"\s*$", body, re.M):
            err(f"missing heading '{h}'")

    check_citations(n, fm, body)
    check_links(path, body)


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
            errors.append(f"{path.name}: broken link '{target}'")


def main():
    pages = sorted((ROOT / "metrics").glob("*.md"))
    ids = {p.stem for p in pages}
    for p in pages:
        check_metric(p, ids)
    for p in sorted((ROOT / "objectives").glob("*.md")):
        fm, body = split(p)
        if fm:
            check_citations(p.name, fm, body)
            check_links(p, body)
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:  ", e)
    print(f"{len(pages)} metric pages checked: {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
