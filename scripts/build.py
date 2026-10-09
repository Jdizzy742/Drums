"""Generate semester Markdown pages and the tracker from data/curriculum.json.

Run from the repo root: python3 scripts/build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "curriculum.json").read_text())
OUT = ROOT / "curriculum"


def checks(items):
    return "\n".join(f"- [ ] {i['text']}" for i in items)


def bullets(items):
    return "\n".join(f"- {i}" for i in items)


def semester_md(n, s, prev, nxt):
    parts = [
        f"# {s['term']}",
        f"**UNT equivalent:** {s['untLevel']}  \n**Focus:** {s['theme']}",
        "## UNT courses this mirrors\n" + bullets(s["untCourses"]),
        "## Goals\n" + bullets(s["goals"]),
        "## Drum set (applied lessons)",
    ]
    for u in s["units"]:
        parts.append(f"### {u['name']} (weeks {u['weeks']})\n" + checks(u["items"]))
    parts += [
        "## Musicianship (theory, ear, keyboard)\n" + checks(s["musicianship"]),
        "## Listening\n" + bullets(s["listening"]),
        "## Tunes to learn\n" + bullets(s["tunes"]),
        "## Jury (weeks 13-16)\nRecord yourself. Pass every item before moving on.\n\n" + checks(s["jury"]),
    ]
    nav = []
    if prev:
        nav.append(f"Previous: [{prev['term']}]({prev['file']})")
    nav.append("[Back to overview](../README.md)")
    if nxt:
        nav.append(f"Next: [{nxt['term']}]({nxt['file']})")
    parts.append("---\n" + " | ".join(nav))
    return "\n\n".join(parts) + "\n"


def main():
    OUT.mkdir(exist_ok=True)
    sems = DATA["semesters"]
    for n, s in enumerate(sems):
        s["file"] = f"{n:02d}-{s['code'].lower().replace(' ', '-')}.md"
    for n, s in enumerate(sems):
        prev = sems[n - 1] if n else None
        nxt = sems[n + 1] if n + 1 < len(sems) else None
        (OUT / s["file"]).write_text(semester_md(n, s, prev, nxt))
    tpl = (ROOT / "tracker" / "template.html").read_text()
    (ROOT / "tracker" / "index.html").write_text(
        tpl.replace("/*CURRICULUM*/null", json.dumps(DATA, separators=(",", ":")))
    )
    print(f"Wrote {len(sems)} semester pages and tracker/index.html")


if __name__ == "__main__":
    main()
