#!/usr/bin/env python3
"""Keep constructs/dag.yaml and the construct pages in sync, then rebuild generated content.

The DAG structure (id, title, broader) can be edited in either place:
  - in constructs/dag.yaml, convenient for reshaping the tree;
  - in a construct page's front matter (`title:`, `broader:`).

Both sides are compared with the state at the last sync (constructs/.sync-snapshot.yaml):
  - only the YAML changed a node    -> the page is updated (or a stub page is created);
  - only the page changed a node    -> the YAML is updated (a deleted page is dropped from the YAML);
  - both changed it differently     -> conflict: nothing is written, resolve by hand;
  - node removed from the YAML      -> nothing is written: delete or merge the page by hand
                                       (the script never deletes a page, to protect its content).

To rename a construct, change its id in the YAML and add `renamed_from: <old id>`. The page file is
moved, and links in metric pages (`construct.measures`) and other constructs (`broader`) are updated.

Usage: python scripts/sync_constructs.py
"""
import re
import sys

import yaml

from common import ROOT, flow_list, load, set_fm_line, split, yaml_scalar
import build

DAG = ROOT / "constructs" / "dag.yaml"
SNAP = ROOT / "constructs" / ".sync-snapshot.yaml"
TEMPLATE = ROOT / "schema" / "construct-template.md"

HEADER = """\
# The construct DAG: one entry per construct page in constructs/.
# Edit freely, then run `python scripts/sync_constructs.py` to update the pages.
#   title:        the page title (a field prefix such as "Retrieval effectiveness: ..." is fine)
#   broader:      parent construct ids; several parents are allowed (it is a DAG, not a tree)
#   renamed_from: (optional, one-off) the old id when renaming; removed after the sync
# Adding an entry creates a stub page. Removing an entry stops the sync until the page is deleted or
# merged by hand. Comments in this file are not kept when the script rewrites it; only this header is.
# Entries are listed parents first.
"""


def norm(entry):
    if entry is None:
        return None
    return {"title": str(entry.get("title") or ""), "broader": sorted(entry.get("broader") or [])}


def read_yaml(path):
    if not path.exists():
        return None
    return yaml.safe_load(path.read_text()) or {}


def page_state():
    return {cid: {"title": str((c["fm"] or {}).get("title") or ""),
                  "broader": list((c["fm"] or {}).get("broader") or [])}
            for cid, c in load("construct").items()}


def ordered(state):
    """Ids with parents first (depth-first from roots, alphabetical by title)."""
    kids = {}
    roots = []
    for cid, e in state.items():
        ps = [p for p in e["broader"] if p in state]
        if not ps:
            roots.append(cid)
        for p in ps:
            kids.setdefault(p, []).append(cid)
    key = lambda x: state[x]["title"].lower()
    out, seen = [], set()

    def walk(cid):
        if cid in seen:
            return
        if any(p in state and p not in seen for p in state[cid]["broader"]):
            return  # visited again once its last parent is placed
        seen.add(cid)
        out.append(cid)
        for k in sorted(kids.get(cid, []), key=key):
            walk(k)

    for r in sorted(roots, key=key):
        walk(r)
    out += sorted([c for c in state if c not in seen], key=key)  # cycles or dangling parents
    return out


def dump(state, header=""):
    lines = [header] if header else []
    for cid in ordered(state):
        e = state[cid]
        lines.append(f"{cid}:\n  title: {yaml_scalar(e['title'])}\n  broader: {flow_list(e['broader'])}\n")
    return "\n".join(lines)


def cycles(state):
    """Problems for every cycle among `broader` links."""
    found, mark = [], {}

    def visit(cid, stack):
        if mark.get(cid) == "done":
            return
        if mark.get(cid) == "active":
            found.append("cycle in broader links: " + " -> ".join(stack + [cid]))
            return
        mark[cid] = "active"
        for p in state[cid]["broader"]:
            if p in state:
                visit(p, stack + [cid])
        mark[cid] = "done"

    for cid in sorted(state):
        visit(cid, [])
    return found


def stub(cid, entry):
    text = TEMPLATE.read_text()
    # Template guidance comments belong in the template, not in every new page's front matter.
    fm, body = text[4:].split("\n---\n", 1)
    fm = "\n".join(re.sub(r"\s+#.*$", "", line) for line in fm.splitlines() if not line.lstrip().startswith("#"))
    text = "---\n" + fm + "\n---\n" + body
    text = set_fm_line(text, "id", cid)
    text = set_fm_line(text, "title", yaml_scalar(entry["title"]))
    text = set_fm_line(text, "broader", flow_list(entry["broader"]))
    return text.replace("\n# Construct Name\n", f"\n# {entry['title']}\n", 1)


def apply_renames(dag, snap):
    """Move pages and rewrite references for entries with renamed_from. Returns messages."""
    msgs = []
    constructs, metrics = load("construct"), load("metric")
    for new, entry in list(dag.items()):
        old = (entry or {}).pop("renamed_from", None)
        if not old:
            continue
        src, dst = ROOT / "constructs" / f"{old}.md", ROOT / "constructs" / f"{new}.md"
        if dst.exists():
            sys.exit(f"cannot rename {old} -> {new}: constructs/{new}.md already exists")
        if src.exists():
            dst.write_text(set_fm_line(src.read_text(), "id", new))
            src.unlink()
            msgs.append(f"renamed page {old}.md -> {new}.md")
        for cid, c in constructs.items():
            b = (c["fm"] or {}).get("broader") or []
            if old in b and cid != old:
                c["path"].write_text(set_fm_line(c["path"].read_text(), "broader",
                                                 flow_list([new if x == old else x for x in b])))
        for mid, m in metrics.items():
            meas = ((m["fm"] or {}).get("construct") or {}).get("measures") or []
            if old in meas:
                text = m["path"].read_text()
                fm_new = text.replace("measures: " + flow_list(meas),
                                      "measures: " + flow_list([new if x == old else x for x in meas]), 1)
                m["path"].write_text(fm_new)
                msgs.append(f"updated construct.measures in metrics/{mid}.md")
        for e in dag.values():
            if e and old in (e.get("broader") or []):
                e["broader"] = [new if x == old else x for x in e["broader"]]
        for e in snap.values():
            if e and old in (e.get("broader") or []):
                e["broader"] = [new if x == old else x for x in e["broader"]]
        if old in snap:
            snap[new] = snap.pop(old)
            if snap[new]:
                snap[new]["broader"] = [new if x == old else x for x in snap[new].get("broader") or []]
    return msgs


def main():
    dag = read_yaml(DAG)
    snap = read_yaml(SNAP) or {}
    msgs = apply_renames(dag, snap) if dag else []
    pages = page_state()
    if dag is None:
        dag = {}
        snap = {}
    ids = sorted(set(dag) | set(pages) | set(snap))
    problems, page_updates, stubs, result = [], {}, {}, {}

    for cid in ids:
        y, p, s = norm(dag.get(cid)), norm(pages.get(cid)), norm(snap.get(cid))
        y_changed, p_changed = y != s, p != s
        if not y_changed and not p_changed:
            if p is not None:
                result[cid] = pages[cid]
            continue
        if y_changed and p_changed and y != p:
            if y is None and s is None:
                result[cid] = pages[cid]  # page added, not yet in the YAML
                continue
            if y is None:
                problems.append(f"{cid}: removed from dag.yaml but its page also changed; resolve by hand")
            elif p is None and s is None:
                stubs[cid] = dag[cid]  # new in YAML, no page yet
                result[cid] = {"title": y["title"], "broader": list(dag[cid].get("broader") or [])}
            else:
                problems.append(f"{cid}: changed in both dag.yaml {y} and its page {p}; make them agree by hand")
            continue
        if y_changed and not p_changed:
            if y is None:
                problems.append(f"{cid}: removed from dag.yaml; delete or merge constructs/{cid}.md by hand "
                                f"(and fix links to it), then sync again")
            elif p is None:
                stubs[cid] = dag[cid]
                result[cid] = {"title": y["title"], "broader": list(dag[cid].get("broader") or [])}
            else:
                page_updates[cid] = dag[cid]
                result[cid] = {"title": y["title"], "broader": list(dag[cid].get("broader") or [])}
        else:  # only the page changed, or both changed to the same thing
            if p is not None:
                result[cid] = pages[cid]

    for cid, e in result.items():
        for b in e["broader"]:
            if b not in result:
                problems.append(f"{cid}: broader construct '{b}' does not exist")

    problems += cycles(result)
    if problems:
        print("Sync stopped; nothing was written:")
        for m in problems:
            print("  -", m)
        sys.exit(1)

    for cid, entry in stubs.items():
        (ROOT / "constructs" / f"{cid}.md").write_text(stub(cid, norm(entry) | {"broader": list(entry.get("broader") or [])}))
        msgs.append(f"created stub constructs/{cid}.md")
    for cid, entry in page_updates.items():
        path = ROOT / "constructs" / f"{cid}.md"
        text = path.read_text()
        text = set_fm_line(text, "title", yaml_scalar(str(entry.get("title") or "")))
        text = set_fm_line(text, "broader", flow_list(list(entry.get("broader") or [])))
        path.write_text(text)
        msgs.append(f"updated constructs/{cid}.md from dag.yaml")

    new_yaml = dump(result, HEADER)
    if not DAG.exists() or DAG.read_text() != new_yaml:
        DAG.write_text(new_yaml)
        msgs.append("wrote constructs/dag.yaml")
    SNAP.write_text(dump(result, "# Last synced state. Written by scripts/sync_constructs.py; do not edit.\n"))

    for m in msgs:
        print(m)
    for p, t in build.render_all().items():
        if not p.exists() or p.read_text() != t:
            p.write_text(t)
            print("wrote", p.relative_to(ROOT))
    print("sync complete")


if __name__ == "__main__":
    main()
