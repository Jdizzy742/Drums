# UNT Jazz Drum Set: Self-Study BM

A self-study version of the University of North Texas BM in Jazz Studies (drum set). The weekly lessons come from UNT's actual 2022-23 jazz drum set syllabus. The classroom courses follow UNT's 2025-26 semester plan. Built for 3-5 hours of practice a week.

## How it works

- UNT jazz drummers must pass these drum set barrier levels in order to graduate: Deficient, 1, 2.1, 2.2, 3.1, 3.2, 4.1, 4.2. Each semester here is one level.
- Each level has 12-13 weekly lessons, a jury transcription, and a jury (barrier exam).
- **Move on when you pass the jury, not when the calendar says so.** UNT majors practice 3-4 hours a day. At 3-5 hours a week, expect each lesson week to take you 1-3 real weeks.
- Record every jury. Your video archive is your proof of progress.
- If you find a teacher, hand them the semester page and ask them to grade the jury.

## Levels

| # | Semester | Level | Focus |
|---|---|---|---|
| 0 | [Prep 1: Foundations](curriculum/00-prep-1.md) | Pre-UNT (beginner) | Hands, time, reading |
| 1 | [Prep 2: Deficient](curriculum/01-prep-2.md) | UNT Deficient | Soph Musical Time, Reed, Morgan reading |
| 2 | [Year 1 Fall](curriculum/02-y1-fall.md) | UNT Level 1 | Big band reading, Dawson vocabulary, samba and songo |
| 3 | [Year 1 Spring](curriculum/03-y1-spring.md) | UNT Level 2.1 | Second line, brushes, big band Latin, 6/8 |
| 4 | [Year 2 Fall](curriculum/04-y2-fall.md) | UNT Level 2.2 | Garibaldi funk, triplets between the limbs, Elvin |
| 5 | [Year 2 Spring](curriculum/05-y2-spring.md) | UNT Level 3.1 | Brazilian styles |
| 6 | [Year 3 Fall](curriculum/06-y3-fall.md) | UNT Level 3.2 | Odd forms, hits, Guiliana, up-tempo to 320 |
| 7 | [Year 3 Spring](curriculum/07-y3-spring.md) | UNT Level 4.1 | Odd and mixed meter, funk, soul, Motown |
| 8 | [Year 4 Fall](curriculum/08-y4-fall.md) | UNT Level 4.2 | Afro-Cuban styles |
| 9 | [Year 4 Spring](curriculum/09-y4-spring.md) | Senior Recital | 45-minute recital |

Prep 1 is my addition for a true beginner. Not every UNT student starts at Deficient; some start at Level 1.

## Jury transcription (every UNT level)

| Week | Milestone |
|---|---|
| 3 | Choose the transcription |
| 5 | First draft written out |
| 8 | Revised draft |
| 10 | Playable at a slow tempo |
| 12 | Memorized and playable with the recording |
| 13 | Record it (UNT: upload) |

## Tune routine

UNT's routine for every assigned tune:

1. Sing the melody accurately (lyrics not required)
2. Melody on snare with time in the feet
3. Melody around the kit with time in the feet
4. Comp through the melody as if playing with a group
5. Comp over the form as if backing a soloist
6. Solo over the form: (A) bebop vocabulary, (B) melodic motifs, (C) ideas from your transcription
7. Arrange it

## Weekly routine (about 4 hours)

5 sessions of 45 minutes:

- 10 min: hands on pad
- 15 min: this week's lesson items
- 10 min: reading (Morgan, Helbing, Reed)
- 10 min: tune routine, play-along, or musicianship

## Snare and rudimental track

UNT jazz drummers also pass snare and rudimental barriers. These run alongside the drum set levels in your 10-minute hands slot:

| Paired with | Level | Source |
|---|---|---|
| Prep 2 | Snare Deficient | UNT snare syllabus (Fall 2018) |
| Prep 2 | Mock UNT audition | UNT's reported audition requirements |
| Year 1 Spring | Snare Level 1 | UNT snare syllabus (exact etude numbers not found) |
| Year 2 Spring | Snare Level 2 | UNT snare syllabus |
| Year 3 Fall | Rudimental Development Level 1 | Self-study version (UNT syllabus not found) |

## Not covered

- Mallets (Deficient, Level 1, Level 2): UNT requires these for jazz majors. Skipped by choice since they need a marimba or xylophone.
- Timpani: not required for jazz studies majors.
- University core courses (math, science, English, government, history). Only the music-related ones are included.

## Course catalog

See [courses.md](courses.md) for every course by year, what it covers, and whether it is built out yet.

## Books

See [materials.md](materials.md).

## Tracking progress

- **Web tracker:** interactive checklist with a practice log.
- **In GitHub:** tick the checkboxes on each semester page.

## Editing the curriculum

All content lives in `data/curriculum.json`. After editing, run:

```
python3 scripts/build.py
```

This regenerates `curriculum/*.md` and `tracker/index.html`.

## Sources

- UNT Percussion, Applied Lesson Syllabus, Drum Set - Jazz (Rev. 8/1/22)
- UNT Jazz Studies (Instrumental) B.M. semester plan, 2025-2026 (Updated May 2025). UNT notes it is not an official degree plan.
- [UNT Percussion Applied Lesson Syllabus, Snare (Fall 2018)](https://music.unt.edu/percussion/files/snare_syllabi_template_fall_2018_updated_0928.pdf)
- [UNT Percussion Area Policy Handbook (Fall 2023)](https://music.unt.edu/files/default/files/percussion_handbook-posted_8-9-23_0.pdf)

Weekly lessons for UNT levels follow the syllabus. Prep 1, the musicianship tasks, listening lists, and electives are self-study additions.
