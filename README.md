<h1 align="center">Hardware, Networks and Behaviorist AI</h1>
<h3 align="center">Team DeepThink · Foundations of CS &amp; AI · 2026</h3>

<p align="center"><img src="assets/branding/deepthink-cover.jpg" alt="DeepThink logo and mascot" width="360"></p>

> **Final version: v3.0 – Stage 3 Final Markdown Content (28 November 2026).**
> Start reading at **[03-Study-guide/00-Start-Here.md](03-Study-guide/00-Start-Here.md)**.

## 1. Team

- **Team name:** DeepThink
- **Selected module:** Hardware, Networks & Behaviorist AI

| Name | Role | GitHub username |
|------|------|-----------------|
| Batyr 巴图 | CEO | [batyrkhassanbayev](https://github.com/batyrkhassanbayev) |
| Mukhammadamin 安明信 | CIO | [m-abduraximov](https://github.com/m-abduraximov) |
| Zere 梦璃 | Visual design lead | [zererere03](https://github.com/zererere03) |
| Merey 袁媄芮 | Video lead (video editing) | [mere1kan](https://github.com/mere1kan) |
| Ardak 诺安 | Visual design lead | [ardyxxie](https://github.com/ardyxxie) |
| Asilbek 苏昀 | Quality lead | [Asilbek-08](https://github.com/Asilbek-08) |
| Altair 阿勒泰尔 | Content lead | [altron-bit](https://github.com/altron-bit) |

## 2. Purpose, learners and learning goals

Our module explains how a simple smart machine works. One running example, **Rover, the obstacle-avoiding robot**, connects the three topics:

| Topic | In simple words | Everyday example |
|-------|-----------------|------------------|
| **Hardware** | The physical parts of a computer or robot: processor, memory, storage, sensors and motors. | The parts inside your phone or a robot vacuum cleaner. |
| **Networks** | Connections that let devices send information to each other using agreed rules. | Sending a message from your phone to a friend. |
| **Behaviorist AI** | AI that reacts to the environment with simple rules instead of building a complex plan first. | A robot that turns when its sensor detects a wall. |

**Intended learners:** first-year university students and recent high-school graduates. No previous knowledge of hardware, networks, AI or programming is needed.

**Learning goals:** after the module, learners can (1) name the parts of a computer and trace a program through the CPU, (2) explain how a sensor reading becomes a robot action, (3) follow a message across a network and the Internet, (4) design behavior rules and priorities for a reactive robot, and (5) explain which decisions must stay on the robot when the network is slow. The full list of eight outcomes is in [00-Start-Here.md](03-Study-guide/00-Start-Here.md#learning-outcomes).

## 3. Where to start and recommended reading order

1. [00-Start-Here.md](03-Study-guide/00-Start-Here.md) – module overview, prerequisites, learning outcomes and how to use the guide.
2. [01-Hardware.md](03-Study-guide/01-Hardware.md) – Chapter 1 (13 activities, an optional CPU simulator lab, quiz).
3. [02-Networks.md](03-Study-guide/02-Networks.md) – Chapter 2 (10 Quick checks, a Network Lab, quiz).
4. [03-Behaviorist-AI.md](03-Study-guide/03-Behaviorist-AI.md) – Chapter 3 (activities, Python "Run it" programs, final design challenge, quiz).
5. [Test-Bank.md](04-Test-bank/Test-Bank.md) – 97 questions (42 true/false, 43 multiple choice, 12 open-ended), numbered Q1–Q97, with answer key and marking guide.
6. [RESOURCE-MAP.md](RESOURCE-MAP.md) – where each topic appears in the study guide, test bank, slides and videos.

Every chapter starts with a linked contents list and ends with a glossary, references, a quiz and an **Answer Key**. Answers are kept out of the learning path; each task links to its answer and back.

## 4. Folder structure

```
.
├── README.md                  ← this file
├── RESOURCE-MAP.md            ← topic → guide / test bank / slides / videos
├── 01-Planning/               ← rough plan and to-do list
├── 02-Material-for-research/  ← textbooks and chapters used as sources
├── 03-Study-guide/            ← FINAL MARKDOWN CONTENT (start here)
│   ├── 00-Start-Here.md
│   ├── 01-Hardware.md
│   ├── 02-Networks.md
│   └── 03-Behaviorist-AI.md
├── 04-Test-bank/
│   └── Test-Bank.md           ← one test bank for all three chapters
├── 05-Slides/README.md        ← where the PPT deck is and what it covers
├── 06-Videos/README.md        ← where the four video tutorials are and what they cover
└── assets/                    ← all images used by the Markdown files
    ├── branding/
    ├── ch1-hardware/          ← fig-1-01 … fig-1-39
    ├── ch2-networks/          ← fig-2-01 … fig-2-11
    └── ch3-behaviorist-ai/    ← fig-3-01 … fig-3-18
```

| Folder | Contents |
|--------|----------|
| [`03-Study-guide/`](03-Study-guide/) | The complete module content in Markdown: explanations, worked examples, figures, activities, quizzes, glossaries, references and answer keys. |
| [`04-Test-bank/`](04-Test-bank/) | The Test Bank. Tags such as `[1.6.2]` link each question to the section that teaches it. |
| [`assets/`](assets/) | 68 figures, named `fig-<chapter>-<number>-<topic>`. The number matches the figure number in the text (for example `fig-2-06-…` is Figure 2.6). All Markdown files use relative paths such as `../assets/ch2-networks/…`. |
| [`05-Slides/`](05-Slides/), [`06-Videos/`](06-Videos/) | Descriptions of the PPT deck and the video tutorials. The files themselves are submitted as separate assignments (see below). |
| [`01-Planning/`](01-Planning/), [`02-Material-for-research/`](02-Material-for-research/) | Planning documents and the list of textbook chapters we used. |

## 5. Opening and using the materials

- **On GitHub:** open any `.md` file; images, tables and links render directly. Use the links at the top and bottom of each chapter to move between chapters.
- **Offline:** download the repository (Code → Download ZIP), unzip it and open the `.md` files in any Markdown viewer (for example VS Code with *Markdown Preview*, or Typora). Keep the folder structure unchanged so the relative image paths keep working.
- **Optional CPU simulator lab (Chapter 1, Section 1.6):** needs a web browser and https://peterhigginson.co.uk/lmc/. The full program, steps and expected results are in the chapter; a paper version needs no Internet.
- **Network Lab (Chapter 2):** uses the built-in commands `ipconfig`/`ip addr`, `nslookup`, `ping` and `tracert`/`traceroute` in a terminal. The commands only read information. Expected results are in the chapter's answer key.
- **Python programs (Chapter 3):** copy a program into a file such as `robot.py` and run `python3 robot.py`, or paste it into any online Python editor. Each program is followed by its expected output, so the activity also works on paper.
- **Slides and videos:** the PPT deck and the four MP4 tutorials are submitted through the course's Learning Center under their own assignments and are not stored in this repository because of their size. See [05-Slides/README.md](05-Slides/README.md) and [06-Videos/README.md](06-Videos/README.md).

## 6. Version information

| Version | Date | What changed |
|---|---|---|
| v1.0 (Stage 1–2) | Oct–Nov 2026 | Rough plan, first chapter drafts in Markdown, Study Guide V1.0 and Test Bank V1.0 (Word/PDF). |
| v2.0 (Stage 2) | 7 Nov 2026 | Chapters rewritten and expanded; Networks chapter and Networks questions added. |
| **v3.0 (Stage 3, final)** | **28 Nov 2026** | Markdown brought in line with Study Guide V1.0 and all reviewed corrections; 68 figures added to `assets/`; answers moved to answer keys; linked contents; Hardware chapter reformatted as real Markdown; one Test Bank (Q1–Q97) with marking guides; new Network Lab and a tested CPU simulator lab; draft notes, placeholders and duplicate files removed. Details: the Final Revision Summary in the Stage 3 submission report and the commit history of branch `stage3-final`. |

The submitted Stage 3 snapshot is identified by the commit ID given in the submission report. Later commits do not change the submitted version.

## 7. Known limitations

- The PPT slides and the MP4 videos are not stored in this repository (size); they are described in `05-Slides/` and `06-Videos/` and submitted separately.
- Results of the Network Lab depend on the learner's network; some school networks block `ping` or `tracert`. The answer key explains what to expect in that case.
- Chapter 3 keeps the activity names used in Study Guide V1.0 and the slides (for example *Activity 2.1* in Section 3.2). They are always shown with their section number to avoid confusion with Chapter 2.
- Six figures in Chapter 1 marked *(illustration)* are photorealistic illustrations from Study Guide V1.0; they show typical hardware, not a specific product.
