#!/usr/bin/env python3
"""Regenerate derived content from the pages' front matter.

Writes:
  - generated blocks in construct pages (narrower constructs, metrics),
    strategy pages (pairings between routes and methods, metrics using each), and metric pages (construct links, neighbours);
  - constructs/index.md: the construct DAG as a Mermaid diagram and a nested list;
  - docs/wiki-map.md: every page linked from one place, by root, layer and objective;
  - schema/page-guide.md: every template heading with the question it answers.

Usage: python scripts/build.py           (rewrite files that are out of date)
       python scripts/build.py --check   (exit 1 and list them, change nothing)
"""
import re
import sys

from common import ROOT, load, replace_block, has_block


def title_of(pages, pid):
    fm = pages[pid]["fm"] or {}
    return str(fm.get("title") or pid)


def construct_graph(constructs):
    parents = {cid: [b for b in ((c["fm"] or {}).get("broader") or []) if b in constructs]
               for cid, c in constructs.items()}
    children = {cid: [] for cid in constructs}
    for cid, ps in parents.items():
        for p in ps:
            children[p].append(cid)
    for cid in children:
        children[cid].sort(key=lambda x: title_of(constructs, x).lower())
    roots = sorted([cid for cid, ps in parents.items() if not ps], key=lambda x: title_of(constructs, x).lower())
    return parents, children, roots


def paths_to_root(cid, parents, seen=()):
    """All chains from a root down to cid (cycle-safe)."""
    if cid in seen:
        return [[cid]]
    ps = parents.get(cid) or []
    if not ps:
        return [[cid]]
    out = []
    for p in ps:
        for chain in paths_to_root(p, parents, seen + (cid,)):
            out.append(chain + [cid])
    return out


def measured_by(metrics):
    by = {}
    for mid, m in metrics.items():
        for cid in ((m["fm"] or {}).get("construct") or {}).get("measures") or []:
            by.setdefault(cid, []).append(mid)
    return by


def bullets(lines, empty):
    return "\n".join(f"- {line}" for line in lines) if lines else empty


def render_construct_page(cid, c, constructs, metrics, children, by):
    text = c["text"]
    narrower = [f"[{title_of(constructs, k)}]({k}.md)" for k in children[cid]]
    text = replace_block(text, "narrower", bullets(narrower, "_None yet._"))
    ms = sorted(by.get(cid, []), key=lambda x: title_of(metrics, x).lower())
    text = replace_block(text, "metrics", bullets(
        [f"[{title_of(metrics, m)}](../metrics/{m}.md)" for m in ms], "_No metric page yet._"))
    return text


def layer_of(s):
    return (s["fm"] or {}).get("layer") or "route"


def render_strategy_page(sid, s, metrics, strategies):
    if layer_of(s) == "method":
        field = "research_method"
        pairs = sorted([rid for rid, r in strategies.items()
                        if layer_of(r) == "route" and sid in ((r["fm"] or {}).get("research_methods") or [])],
                       key=lambda x: title_of(strategies, x).lower())
        lines = [f"[{title_of(strategies, r)}]({r}.md)" for r in pairs]
        empty = "_No route page names this method yet._"
    else:
        field = "route"
        lines = []
        for v in (s["fm"] or {}).get("research_methods") or []:
            if v in strategies and layer_of(strategies[v]) == "method":
                lines.append(f"[{title_of(strategies, v)}]({v}.md)")
            else:
                lines.append(f"`{v}` (no method page yet)")
        empty = "_No method listed yet._"
    text = replace_block(s["text"], "pairings", bullets(lines, empty))
    users = sorted([mid for mid, m in metrics.items()
                    if sid in (((m["fm"] or {}).get("operationalization") or {}).get(field) or [])],
                   key=lambda x: title_of(metrics, x).lower())
    return replace_block(text, "metrics", bullets(
        [f"[{title_of(metrics, m)}](../metrics/{m}.md)" for m in users], "_No metric page uses it yet._"))


def render_metric_page(mid, m, constructs, metrics, parents, children, by):
    text = m["text"]
    measures = [c for c in (((m["fm"] or {}).get("construct") or {}).get("measures") or []) if c in constructs]
    lines = []
    for cid in measures:
        chains = paths_to_root(cid, parents)
        where = "; ".join(" → ".join(title_of(constructs, x) for x in ch[:-1]) for ch in chains if len(ch) > 1)
        link = f"[{title_of(constructs, cid)}](../constructs/{cid}.md)"
        lines.append(link + (f" (under {where})" if where else " (a root construct)"))
    text = replace_block(text, "constructs", "Measures, in the [construct DAG](../constructs/index.md):\n\n"
                         + bullets(lines, "_No construct linked yet._") if lines else "_No construct linked yet._")

    groups = []
    seen = {mid}

    def add(label, cids):
        found = []
        for cid in cids:
            for other in sorted(by.get(cid, []), key=lambda x: title_of(metrics, x).lower()):
                if other not in seen:
                    seen.add(other)
                    found.append((other, cid))
        if found:
            items = ", ".join(f"[{title_of(metrics, o)}]({o}.md) ({title_of(constructs, c)})" for o, c in found)
            groups.append(f"{label}: {items}")

    add("Same construct", measures)
    add("Narrower construct", [k for c in measures for k in children.get(c, [])])
    add("Broader construct", [p for c in measures for p in parents.get(c, [])])
    add("Sibling construct", [s for c in measures for p in parents.get(c, []) for s in children.get(p, []) if s not in measures])
    text = replace_block(text, "neighbours", bullets(groups, "_None found from the construct DAG yet._"))
    return text


def mermaid_id(prefix, pid):
    return prefix + re.sub(r"[^A-Za-z0-9]", "_", pid)


def render_index(constructs, metrics, parents, children, roots, by):
    out = ["# Construct DAG", "",
           "> Generated by `scripts/build.py` from the `broader` field of each construct page and the "
           "`construct.measures` field of each metric page. Do not edit by hand. To change the structure, "
           "edit construct pages or `constructs/dag.yaml`, then run `python scripts/sync_constructs.py`.", "",
           "Rounded boxes are constructs; square boxes are metrics. Solid arrows point from a broader "
           "construct to a narrower one; dotted arrows point from a construct to a metric that measures it.", "",
           "```mermaid", "graph TD"]
    for cid in sorted(constructs):
        out.append(f'  {mermaid_id("c_", cid)}(["{title_of(constructs, cid)}"])')
    for mid in sorted(metrics):
        if any(mid in v for v in by.values()):
            out.append(f'  {mermaid_id("m_", mid)}["{title_of(metrics, mid)}"]:::metric')
    for cid in sorted(constructs):
        for k in children[cid]:
            out.append(f'  {mermaid_id("c_", cid)} --> {mermaid_id("c_", k)}')
    for cid in sorted(by):
        if cid in constructs:
            for mid in sorted(by[cid]):
                out.append(f'  {mermaid_id("c_", cid)} -.-> {mermaid_id("m_", mid)}')
    out += ["  classDef metric stroke-dasharray: 4 2", "```", "", "## As a nested list", "",
            "A construct with several broader constructs appears under each of them.", ""]

    def walk(cid, depth, stack):
        ms = sorted(by.get(cid, []), key=lambda x: title_of(metrics, x).lower())
        mtxt = (" · metrics: " + ", ".join(f"[{title_of(metrics, m)}](../metrics/{m}.md)" for m in ms)) if ms else ""
        out.append("  " * depth + f"- [{title_of(constructs, cid)}]({cid}.md){mtxt}")
        if cid in stack:
            return
        for k in children[cid]:
            walk(k, depth + 1, stack + (cid,))

    for r in roots:
        walk(r, 0, ())
    empty = sorted([c for c in constructs if not by.get(c)], key=lambda x: title_of(constructs, x).lower())
    out += ["", "## Constructs with no metric yet", "",
            bullets([f"[{title_of(constructs, c)}]({c}.md)" for c in empty], "_None._"), ""]
    return "\n".join(out)


def render_map(constructs, metrics, strategies, parents, children, roots, by):
    """docs/wiki-map.md: every page, reachable from one place, grouped the way the schema thinks."""
    C = lambda c: f"[{title_of(constructs, c)}](../constructs/{c}.md)"
    Mt = lambda m: f"[{title_of(metrics, m)}](../metrics/{m}.md)"
    S = lambda x: f"[{title_of(strategies, x)}](../strategies/{x}.md)" if x in strategies else f"`{x}`"
    layer = lambda x: (strategies[x]["fm"] or {}).get("layer") or "route"
    op = lambda m: ((metrics[m]["fm"] or {}).get("operationalization") or {})
    out = ["# Wiki map", "",
           "> Generated by `scripts/build.py` from the front matter of every page. Do not edit by hand.", "",
           "Every page in the wiki, linked from one place. The [README](../README.md) explains the design; "
           "[`schema/DECISIONS.md`](../schema/DECISIONS.md) gives the reasons for each decision.", "",
           "## How the page types connect", "",
           "```mermaid", "graph LR",
           '  O["Objectives<br/>(why it matters)"]',
           '  C(["Constructs<br/>(what we want to know)"])',
           '  M["Metrics<br/>(the number)"]',
           '  R["Routes<br/>(how data becomes a number)"]',
           '  D["Methods<br/>(how data is gathered)"]',
           '  I["Instruments<br/>(objects of a metric)"]',
           "  C -- broader / narrower --> C",
           "  M -- measures --> C",
           "  M -- uses --> R",
           "  M -- uses --> D",
           "  I -- instantiates --> M",
           "  R -- typically fed by --> D",
           "  M -. evidence .-> O",
           "```", "",
           f"Counts: {len(constructs)} constructs, {len(metrics)} metrics, "
           f"{sum(1 for x in strategies if layer(x) == 'route')} routes, "
           f"{sum(1 for x in strategies if layer(x) == 'method')} methods, "
           f"{sum(len(op(m).get('instruments') or []) for m in metrics)} instrument entries.", "",
           "## 1. Constructs and their metrics, by root", "",
           "The construct DAG with the metrics attached to each construct. A construct with several broader "
           "constructs appears under each of them. The diagram version is in [constructs/index.md](../constructs/index.md).", ""]

    def walk(cid, depth, stack):
        ms = sorted(by.get(cid, []), key=lambda x: title_of(metrics, x).lower())
        tail = (" — " + ", ".join(Mt(m) for m in ms)) if ms else ""
        out.append("  " * depth + f"- {C(cid)}{tail}")
        if cid in stack:
            return
        for k in children[cid]:
            walk(k, depth + 1, stack + (cid,))

    for r in roots:
        out.append(f"### {title_of(constructs, r)}")
        out.append("")
        walk(r, 0, ())
        out.append("")

    out += ["## 2. Metrics, by root", "",
            "Each metric measures constructs under exactly one root (D20).", ""]
    def root_of(m):
        rs = set()
        for c in ((metrics[m]["fm"] or {}).get("construct") or {}).get("measures") or []:
            for ch in paths_to_root(c, parents):
                rs.add(ch[0])
        return sorted(rs)
    for r in roots:
        ms = sorted([m for m in metrics if r in root_of(m)], key=lambda x: title_of(metrics, x).lower())
        if not ms:
            continue
        out += [f"### {title_of(constructs, r)}", "", "| Metric | Constructs | Methods | Routes |", "|---|---|---|---|"]
        for m in ms:
            cs = ", ".join(C(c) for c in ((metrics[m]["fm"] or {}).get("construct") or {}).get("measures") or [] if c in constructs)
            out.append(f"| {Mt(m)} | {cs} | {', '.join(S(x) for x in op(m).get('research_method') or [])} | "
                       f"{', '.join(S(x) for x in op(m).get('route') or [])} |")
        out.append("")

    out += ["## 3. Strategies", "",
            "Two layers: methods gather the data; routes turn it into a number.", "",
            "### Routes", "", "| Route | Typical methods | Metrics |", "|---|---|---|"]
    for x in sorted([x for x in strategies if layer(x) == "route"], key=lambda x: title_of(strategies, x).lower()):
        meths = ", ".join(S(v) for v in (strategies[x]["fm"] or {}).get("research_methods") or [])
        ms = sorted([m for m in metrics if x in (op(m).get("route") or [])], key=lambda y: title_of(metrics, y).lower())
        out.append(f"| {S(x)} | {meths} | {', '.join(Mt(m) for m in ms) or '—'} |")
    out += ["", "### Methods", "", "| Method | Routes that use it | Metrics |", "|---|---|---|"]
    for x in sorted([x for x in strategies if layer(x) == "method"], key=lambda x: title_of(strategies, x).lower()):
        rs = sorted([r for r in strategies if layer(r) == "route" and x in ((strategies[r]["fm"] or {}).get("research_methods") or [])],
                    key=lambda y: title_of(strategies, y).lower())
        ms = sorted([m for m in metrics if x in (op(m).get("research_method") or [])], key=lambda y: title_of(metrics, y).lower())
        out.append(f"| {S(x)} | {', '.join(S(r) for r in rs) or '—'} | {', '.join(Mt(m) for m in ms) or '—'} |")
    out += ["", "Research methods without a page yet are listed in `research_method` in "
            "[`schema/vocabulary.yaml`](../schema/vocabulary.yaml).", ""]

    out += ["## 4. Instruments", "",
            "A metric page is a class; its instruments are objects (D25, D27): standardized questionnaires, tests and "
            "benchmarks. Lists are representative, not complete. Details are in section 2.6 of each metric page.", "",
            "Kinds (D30): **content** fixes what is measured on, **scorer** fixes how outputs are judged, "
            "**suite** is an aggregate over benchmarks and measures no single construct.", "",
            "| Instrument | Kind | Metric | Probes | Scale |", "|---|---|---|---|---|"]
    rows = []
    for m in metrics:
        for ins in op(m).get("instruments") or []:
            if isinstance(ins, dict) and ins.get("name"):
                rows.append((ins["name"], ins.get("kind") or "content", m, ins.get("probes") or "", ins.get("scale") or ""))
    for name, kind, m, probes, scale in sorted(rows, key=lambda r: (r[0].lower(), title_of(metrics, r[2]).lower())):
        out.append(f"| {name} | {kind} | {Mt(m)} | {probes or '—'} | {scale or '—'} |")
    out.append("")

    objs = sorted((ROOT / "objectives").glob("*.md"))
    out += ["## 5. Objectives", ""] + [f"- [{p.stem.replace('-', ' ').capitalize()}](../objectives/{p.name})" for p in objs] + [""]
    out += ["## 6. Schema", "",
            "- [Page guide](../schema/page-guide.md): every section of every page type and the question it answers.",
            "- Templates: [metric](../schema/metric-template.md), [construct](../schema/construct-template.md), [strategy](../schema/strategy-template.md).",
            "- [Vocabulary](../schema/vocabulary.yaml): allowed tag values.",
            "- [Decisions](../schema/DECISIONS.md): what was decided, why, and what was considered instead.",
            "- [Bibliography](../references/bibliography.yaml): every source pages may cite.", ""]
    return "\n".join(out)


def template_guide(path, label):
    text = path.read_text()
    fm_text, body = text.split("\n---\n", 1)
    out = [f"## {label}", "", f"Source: [`schema/{path.name}`]({path.name})", "", "### Front matter fields", ""]
    for line in fm_text.splitlines():
        m = re.match(r"^(\s*)([a-z_\-]+):[^#]*#\s*(.+)$", line)
        parent = re.match(r"^(\s*)([a-z_\-]+):\s*$", line)
        if m:
            indent = len(m.group(1)) // 2
            out.append("  " * indent + f"- `{m.group(2)}`: {m.group(3).strip()}")
        elif parent:
            # A block key such as `construct:` heads the indented fields that follow it.
            out.append("  " * (len(parent.group(1)) // 2) + f"- `{parent.group(2)}`")
    out += ["", "### Sections", ""]
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        h = re.match(r"^(#{2,3}) (.+)$", lines[i])
        if h:
            note, j = "", i + 1
            if j < len(lines) and lines[j].strip().startswith("<!--") and "generated:" not in lines[j]:
                chunk = []
                while j < len(lines):
                    chunk.append(lines[j])
                    if "-->" in lines[j]:
                        break
                    j += 1
                note = " ".join(x.strip() for x in chunk)
                note = re.sub(r"^<!--\s*|\s*-->$", "", note).strip()
            bullet = "- " if h.group(1) == "##" else "  - "
            out.append(f"{bullet}**{h.group(2)}**" + (f": {note}" if note else ""))
        i += 1
    return "\n".join(out)


def render_guide():
    parts = ["# Page guide", "",
             "> Generated by `scripts/build.py` from the comments in the templates in `schema/`. "
             "Do not edit by hand; edit the template comments instead.", "",
             "Each page type answers a fixed set of questions. This page lists them, so readers who do "
             "not open the raw template files can see what each section is for.", ""]
    for name, label in [("metric-template.md", "Metric pages"), ("construct-template.md", "Construct pages"),
                        ("strategy-template.md", "Strategy pages")]:
        p = ROOT / "schema" / name
        if p.exists():
            parts += [template_guide(p, label), ""]
    return "\n".join(parts)


def render_all():
    """Return {path: expected text} for every generated file or page with generated blocks."""
    constructs, metrics, strategies = load("construct"), load("metric"), load("strategy")
    parents, children, roots = construct_graph(constructs)
    by = measured_by(metrics)
    files = {}
    for cid, c in constructs.items():
        files[c["path"]] = render_construct_page(cid, c, constructs, metrics, children, by)
    for sid, s in strategies.items():
        files[s["path"]] = render_strategy_page(sid, s, metrics, strategies)
    for mid, m in metrics.items():
        if has_block(m["text"], "constructs") or has_block(m["text"], "neighbours"):
            files[m["path"]] = render_metric_page(mid, m, constructs, metrics, parents, children, by)
    if constructs:
        files[ROOT / "constructs" / "index.md"] = render_index(constructs, metrics, parents, children, roots, by)
    files[ROOT / "schema" / "page-guide.md"] = render_guide()
    files[ROOT / "docs" / "wiki-map.md"] = render_map(constructs, metrics, strategies, parents, children, roots, by)
    return files


def stale():
    return [p for p, t in render_all().items() if not p.exists() or p.read_text() != t]


def main():
    check = "--check" in sys.argv
    files = render_all()
    changed = [p for p, t in files.items() if not p.exists() or p.read_text() != t]
    if check:
        for p in changed:
            print("out of date:", p.relative_to(ROOT))
        sys.exit(1 if changed else 0)
    for p in changed:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(files[p])
        print("wrote", p.relative_to(ROOT))
    if not changed:
        print("everything up to date")


if __name__ == "__main__":
    main()
