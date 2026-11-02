"""Shared helpers for the wiki scripts: reading pages, front matter edits, generated blocks."""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = {"metric": "metrics", "construct": "constructs", "strategy": "strategies"}
# Files in content folders that are not pages.
NON_PAGES = {"index.md", "README.md"}

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


def split(text):
    """Return (front matter dict or None, body) for a page's text."""
    m = FM_RE.match(text)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def load(page_type):
    """All pages of one type, keyed by file stem: {id: {"path", "text", "fm", "body"}}."""
    pages = {}
    folder = ROOT / FOLDERS[page_type]
    if not folder.exists():
        return pages
    for p in sorted(folder.glob("*.md")):
        if p.name in NON_PAGES:
            continue
        text = p.read_text()
        fm, body = split(text)
        pages[p.stem] = {"path": p, "text": text, "fm": fm, "body": body}
    return pages


def flow_list(items):
    return "[" + ", ".join(items) + "]"


def yaml_scalar(s):
    """Quote a string for a one-line YAML value when needed."""
    if re.search(r"[:#\[\]{},&*!|>'\"%@`]", s) or s != s.strip():
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def set_fm_line(text, key, value):
    """Replace the top-level front matter line `key: ...` with `key: value` (value already formatted).

    Keeps any trailing `# comment` on the line. Raises if the key is not present at top level.
    """
    m = FM_RE.match(text)
    fm = m.group(1)
    pat = re.compile(r"^(" + re.escape(key) + r":)[^\n#]*?(\s+#[^\n]*)?$", re.M)
    if not pat.search(fm):
        raise KeyError(f"front matter has no top-level '{key}:' line")
    fm = pat.sub(lambda mm: f"{mm.group(1)} {value}" + (mm.group(2) or ""), fm, count=1)
    return "---\n" + fm + "\n---\n" + m.group(2)


def block_markers(name):
    return f"<!-- generated:{name}:start -->", f"<!-- generated:{name}:end -->"


def replace_block(text, name, content):
    """Put `content` between the generated markers called `name`. Text without the markers is returned unchanged."""
    start, end = block_markers(name)
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        return text
    inner = start + "\n" + (content.rstrip() + "\n" if content.strip() else "") + end
    return pat.sub(lambda _: inner, text, count=1)


def has_block(text, name):
    start, end = block_markers(name)
    return start in text and end in text
