# UNT Jazz Drum Set: Self-Study BM

A four-year, eight-semester drum curriculum modeled on the University of North Texas BM in Jazz Studies (drum set), with a Semester 0 to get a beginner to Level 1. Built for 3-5 hours of practice a week.

## How it works

- Each semester maps to a real UNT drum set proficiency level (Deficient, 1, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2) and the UNT courses taken that term.
- A semester is 16 weeks: 12 weeks of units, then a 4-week jury window.
- **Move on when you pass the jury, not when the calendar says so.** UNT majors practice 3-4 hours a day. At 3-5 hours a week, plan on some semesters taking longer. That is expected.
- Record every jury. Your video archive is your proof of progress.
- If you find a teacher, hand them the semester page and ask them to grade the jury.

## Semesters

| # | Semester | UNT level | Focus |
|---|---|---|---|
| 0 | [Pre-College Prep](curriculum/00-prep.md) | Deficient | Hands, time, reading |
| 1 | [Year 1 Fall](curriculum/01-y1-fall.md) | Level 1 | Ride cymbal, comping, brushes |
| 2 | [Year 1 Spring](curriculum/02-y1-spring.md) | Level 2.1 | Big band, shuffles, 6/8 |
| 3 | [Year 2 Fall](curriculum/03-y2-fall.md) | Level 2.2 | Independence, soloing, funk |
| 4 | [Year 2 Spring](curriculum/04-y2-spring.md) | Level 3.1 | Odd meters, jazz history |
| 5 | [Year 3 Fall](curriculum/05-y3-fall.md) | Level 3.2 | Polyrhythm, recording, gospel chops |
| 6 | [Year 3 Spring](curriculum/06-y3-spring.md) | Level 4.1 | Modern jazz, prog, illusions |
| 7 | [Year 4 Fall](curriculum/07-y4-fall.md) | Level 4.2 | Your sound, demo |
| 8 | [Year 4 Spring](curriculum/08-y4-spring.md) | Senior Recital | 45-minute recital |

## Weekly routine (about 4 hours)

5 sessions of 45 minutes:

- 10 min: hands on pad (rudiments, Stick Control)
- 15 min: current unit focus
- 10 min: reading or comping
- 10 min: play-along tune or musicianship (theory, ear, keyboard, transcription)

## Books to get

See [materials.md](materials.md).

## Tracking progress

- **Web tracker:** interactive checklist with a practice log (link in the session that created this repo).
- **In GitHub:** tick the checkboxes on each semester page.

## Editing the curriculum

All content lives in `data/curriculum.json`. After editing, run:

```
python3 scripts/build.py
```

This regenerates `curriculum/*.md` and `tracker/index.html`.

## Sources

- [UNT Jazz Drum Set Applied Lesson Syllabus (2022-23)](https://music.unt.edu/percussion/files/jazz-drum-set-curriculum-2022-23.pdf)
- [UNT Percussion Area Policy Handbook (Fall 2023)](https://music.unt.edu/files/default/files/percussion_handbook-posted_8-9-23_0.pdf)
- [UNT BM Jazz Instrumental semester plan](https://music.unt.edu/resources/students/advising/2024-25_degree_plans/semester_plan_bm_jazz_instrumental.pdf)
- [UNT undergraduate audition requirements](https://music.unt.edu/admissions/undergraduate-repertoire.html)

The level structure and course sequence come from UNT. The specific exercises, tempos, and album picks inside each level are a synthesis for self-study, not UNT's official assignments.
