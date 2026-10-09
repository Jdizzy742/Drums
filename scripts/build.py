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


def add_transcription_items():
    """Expand each semester's transcription flag into checklist items."""
    for s in DATA["semesters"]:
        s["transcriptionItems"] = [
            {"id": f"{s['id']}-t-{n}", "text": f"Week {t['week']}: {t['text']}"}
            for n, t in enumerate(DATA["transcriptionSteps"], 1)
        ] if s["transcription"] else []


def semester_md(s, prev, nxt):
    src = "UNT 2022-23 drum set syllabus" if s["source"] == "unt" else "Self-study prep (not a UNT level)"
    parts = [
        f"# {s['term']}",
        f"**Level:** {s['untLevel']}  \n**Focus:** {s['theme']}  \n**Source:** {src}",
        "## Courses this mirrors\n" + bullets(s["untCourses"]),
        "## Barrier materials\n" + bullets(s["barriers"]),
    ]
    if s.get("tempos"):
        parts.append(f"**Tempos:** {s['tempos']}")
    parts += ["## Goals\n" + bullets(s["goals"]), "## Weekly lessons"]
    for w in s["weeks"]:
        label = f"Week {w['n']}" + (f": {w['topic']}" if w.get("topic") else "")
        parts.append(f"### {label}\n" + checks(w["items"]))
    if s["transcriptionItems"]:
        parts.append(f"## {s['transcription']}\n" + checks(s["transcriptionItems"]))
    parts.append("## Musicianship (classroom courses)\n" + checks(s["musicianship"]))
    if s["electives"]:
        parts.append("## Electives (your interests, not UNT)\n" + checks(s["electives"]))
    parts += [
        "## Listening\n" + bullets(s["listening"]),
        "## Tunes\n" + bullets(s["tunes"]) + "\n\nWork every tune through the [tune routine](../README.md#tune-routine).",
        "## Jury\nRecord yourself. Pass every item before moving on.\n\n" + checks(s["jury"]),
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
    for old in OUT.glob("*.md"):
        old.unlink()
    add_transcription_items()
    sems = DATA["semesters"]
    for n, s in enumerate(sems):
        s["file"] = f"{n:02d}-{s['code'].lower().replace(' ', '-')}.md"
    for n, s in enumerate(sems):
        prev = sems[n - 1] if n else None
        nxt = sems[n + 1] if n + 1 < len(sems) else None
        (OUT / s["file"]).write_text(semester_md(s, prev, nxt))
    tpl = (ROOT / "tracker" / "template.html").read_text()
    (ROOT / "tracker" / "index.html").write_text(
        tpl.replace("/*CURRICULUM*/null", json.dumps(DATA, separators=(",", ":")))
    )
    print(f"Wrote {len(sems)} semester pages and tracker/index.html")


if __name__ == "__main__":
    main()
