#!/usr/bin/env python3
"""Consistency checks for the Memory Prism repository.

Run from anywhere:  python3 tools/check_repo.py

Checks
  1. skill/memory-prism/references/checklist.md is byte-identical to the canonical checklist.
  2. SKILL.md has valid frontmatter (name matches folder, description <= 1024 chars) and is < 500 lines.
  3. All seven essays and the Framework text exist, with no empty Markdown headings.
  4. The Framework text matches the PDF (word-level similarity; needs `pdftotext`, skipped if absent).
  5. Relative Markdown links resolve (historical test records, the wiki seed and code blocks are skipped).
  6. tests/records/DEVELOPMENT_LOG.md and the record files list each other exactly.
  7. Records dated 2026-11-24 or later carry a well-formed SCORES line.

Exit status is non-zero if any check fails.
"""
import difflib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skill" / "memory-prism"
CORPUS = SKILL / "references" / "source-corpus"
RECORDS = ROOT / "tests" / "records"
failures = []


def fail(msg):
    failures.append(msg)
    print(f"  FAIL  {msg}")


def ok(msg):
    print(f"  ok    {msg}")


# 1 ---------------------------------------------------------------
print("1. Checklist sync")
canon = [p for p in (ROOT / "starter-kit").glob("Memory-Prism-Starter-Kit-Checklist-v*.md") if "superseded" not in p.read_text().splitlines()[0]]
if len(canon) != 1:
    fail(f"expected exactly one canonical checklist in starter-kit/, found {len(canon)}")
else:
    copy = SKILL / "references" / "checklist.md"
    if copy.read_bytes() == canon[0].read_bytes():
        ok(f"{copy.relative_to(ROOT)} == {canon[0].relative_to(ROOT)}")
    else:
        fail("skill checklist copy differs from canonical; copy the canonical file over it")

# 2 ---------------------------------------------------------------
print("2. SKILL.md")
text = (SKILL / "SKILL.md").read_text()
m = re.match(r"---\n(.*?)\n---\n", text, re.S)
if not m:
    fail("SKILL.md has no YAML frontmatter")
else:
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name or name.group(1) != SKILL.name:
        fail("frontmatter name missing or does not match the folder name")
    elif not desc or len(desc.group(1)) > 1024:
        fail("frontmatter description missing or over 1024 characters")
    else:
        ok(f"name={name.group(1)}, description {len(desc.group(1))} chars")
lines = len(text.splitlines())
(ok if lines < 500 else fail)(f"SKILL.md is {lines} lines (limit 500)")

# 3 ---------------------------------------------------------------
print("3. Source corpus")
expected = [
    "Memory-Prism-Framework.md",
    "foundations/Boards.md",
    "foundations/Audits.md",
    "foundations/Identity.md",
    "foundations/Flow-under-Constraint.md",
    "supplementary/Working-Lines.md",
    "supplementary/No-Sacred-States.md",
    "supplementary/Accumulation-Patterns.md",
]
for rel in expected:
    p = CORPUS / rel
    if not p.exists():
        fail(f"missing {rel}")
        continue
    empties = len(re.findall(r"^#{1,6}\s*$", p.read_text(), re.M))
    (ok if empties == 0 else fail)(f"{rel}: {empties} empty headings")

# 4 ---------------------------------------------------------------
print("4. Framework text vs PDF")
pdf = ROOT / "MemoryPrism-Framework.pdf"
if shutil.which("pdftotext") and pdf.exists():
    raw = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout

    def words(t):
        t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
        t = re.sub(r"https://www\.memoryprism\.com/framework\s+\d+/11", "", t)
        t = re.sub(r"\d\d/\d\d/\d{4}, \d\d:\d\d\s+Memory Prism - Framework", "", t)
        t = re.sub(r"https?://\S+", " ", t)  # links render differently in the two formats
        t = re.sub(r"[#*_>`\\\f]", " ", t).replace("’", "'").replace("“", '"').replace("”", '"')
        return re.findall(r"[\w'\-]+", t.lower())

    a = words(raw)
    b = words((CORPUS / "Memory-Prism-Framework.md").read_text())
    ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    (ok if ratio >= 0.97 else fail)(f"word-level similarity {ratio:.3f} (threshold 0.97)")
else:
    print("  skip  pdftotext or PDF not available")

# 5 ---------------------------------------------------------------
print("5. Relative links")
bad = 0
for md in ROOT.rglob("*.md"):
    if RECORDS in md.parents and md.name != "DEVELOPMENT_LOG.md":
        continue
    if (ROOT / "wiki-seed") in md.parents:  # wiki links use page names, not paths
        continue
    body = re.sub(r"```.*?```", "", md.read_text(), flags=re.S)  # ignore code/templates
    for target in re.findall(r"\]\(([^)\s]+)\)", body):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        path = target.split("#")[0]
        if path and not (md.parent / path).exists():
            fail(f"{md.relative_to(ROOT)} -> {target}")
            bad += 1
if bad == 0:
    ok("all relative links resolve")

# 6 ---------------------------------------------------------------
print("6. Test index")
log = (RECORDS / "DEVELOPMENT_LOG.md").read_text()
listed = set(re.findall(r"\]\(([^)]+\.md)\)", log))
present = {p.name for p in RECORDS.glob("*.md")} - {"DEVELOPMENT_LOG.md"}
for n in sorted(present - listed):
    fail(f"record not in index: {n}")
for n in sorted(listed - present):
    fail(f"index entry without file: {n}")
if present == listed:
    ok(f"{len(present)} records, index matches")
if "## Collection rule" not in log:
    fail("DEVELOPMENT_LOG.md lost its '## Collection rule' anchor")

# 7 ---------------------------------------------------------------
print("7. SCORES lines (records dated 2026-11-24 or later)")
pat = re.compile(r"^SCORES: IQ(?:_\w+)?=\S+/12(?:; IQ_\w+=\S+/12)*(?:; MPF=\S+/\d+)?; scorer=\w[\w ]*; blind=(yes|no)\s*$", re.M)
new = [p for p in present if (d := re.search(r"(\d{4}-\d{2}-\d{2})\.md$", p)) and d.group(1) >= "2026-11-24"]
if not new:
    ok("no such records yet")
for n in sorted(new):
    (ok if pat.search((RECORDS / n).read_text()) else fail)(f"{n}: SCORES line")

print()
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed")
