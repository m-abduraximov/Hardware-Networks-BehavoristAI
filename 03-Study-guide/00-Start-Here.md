[Chapter 1: Hardware →](01-Hardware.md)

# Hardware, Networks and Behaviorist AI – Start Here

![DeepThink logo and mascot](../assets/branding/deepthink-cover.jpg)

*A beginner's guide with Rover, the obstacle-avoiding robot · Team DeepThink · Final Markdown content, Stage 3 (version 3.0, 25 November 2026)*

## Module overview

This module explains how a simple smart machine works. We follow one robot, **Rover**, through three topics:

| Chapter | Main question | What you will be able to do |
|---|---|---|
| [1. Hardware](01-Hardware.md) | What is a computer made of, and how does it follow instructions? | Name the main parts of a computer and a robot, trace a tiny program through the CPU, and calculate a distance from a sensor's echo time. |
| [2. Networks](02-Networks.md) | How do devices talk to each other? | Follow a message through the layers of a network, from Rover to a phone, and explain basic network security. |
| [3. Behaviorist AI](03-Behaviorist-AI.md) | How can a robot act sensibly without a plan? | Design behavior rules and priorities, explain Brooks's layers, and decide which decisions must stay on the robot. |

Rover is a small robot that drives around a room and avoids obstacles. Chapter 1 shows what Rover is built from, Chapter 2 shows how Rover sends a report to a phone, and Chapter 3 shows how Rover decides what to do. The case study in Section 3.5 puts all three together.

## Intended learners

First-year university students and recent high-school graduates. The guide is written for independent study, but the activities also work in pairs or in class.

## Prerequisites

- No previous knowledge of hardware, networks, artificial intelligence or programming is needed. Every new word is explained before it is used, and each chapter ends with a glossary.
- Basic arithmetic (multiplication, division, percentages) and the idea of a decimal number.
- For the optional computer activities only: a computer with a web browser (Section 1.6 lab), a terminal (Network Lab in Chapter 2) or Python 3 / an online Python editor (Chapter 3). Every computer activity has a paper version.

## Learning outcomes

By the end of the module you will be able to:

1. Identify the main hardware parts of a computer (CPU, memory, storage, input/output, buses) and explain what each one does.
2. Trace how the CPU follows a small program with the fetch–decode–execute cycle.
3. Explain how a robot senses and acts (sensors, actuators, PWM, H-bridge, microcontroller) and calculate a distance from an ultrasonic echo time.
4. Describe network types, media and devices, and match protocols to the layers of the OSI and TCP/IP models.
5. Explain how a message crosses the Internet using IP addresses, DNS, TCP or UDP and routing, and name five basic ideas of network security.
6. Explain the basic ideas of behaviorism and why "Behaviorist AI" is an analogy.
7. Write behavior rules, solve conflicts with priorities, and describe Brooks's subsumption architecture.
8. Use network delay to decide which decisions must run on the robot itself, and describe the limits of reactive robots, reinforcement learning and the ethical questions they raise.

## Recommended reading order

1. **This page**, then the chapters in order: [Hardware](01-Hardware.md) → [Networks](02-Networks.md) → [Behaviorist AI](03-Behaviorist-AI.md). Each chapter builds on the previous one.
2. Inside each chapter: make the prediction, read the section, look at the figures, do the activity or Quick check, and only then compare with the **Answer Key** at the end of the chapter.
3. Finish each chapter with its **Quiz**, then practise with the [Test Bank](../04-Test-bank/Test-Bank.md) (Q1–Q49 Hardware, Q50–Q74 Networks, Q75–Q97 Behaviorist AI).
4. The slides and the four video tutorials cover the same examples; [RESOURCE-MAP.md](../RESOURCE-MAP.md) shows which video and which questions belong to each section.

**Estimated time:** about 3–4 hours for Chapter 1, 2 hours for Chapter 2 and 3–4 hours for Chapter 3, spread over several short sessions.

## How each chapter works

1. Use the **Contents** list at the top of each chapter to jump to a section.
2. For each section, make a prediction first, then read the explanation and look at the figures.
3. Do the **activity** or **Quick check** before you look at the answer. Answers are collected in the **Answer Key** at the end of each chapter, so they do not spoil the task; every answer links back to its task.
4. Compare your answer with the answer key or feedback, and go back if something is unclear.
5. Finish the chapter with the **Quiz**. The separate Test Bank gives more practice.

## Labels used in this guide

| Label | What it means |
|---|---|
| Think first / Mission question / Predict first | A question to answer before reading, to activate what you already know. |
| Activity / Lab | A hands-on task with Goal, Preparation, Task, Observation and Reflection. Labs use a computer and always have a paper fallback. |
| Quick check / Check yourself | A few short questions to test what you just read. |
| ✅ Check your answers | A link to the matching answer in the chapter's Answer Key. |
| Key idea / Common misconception | The most important point, or a common mistake to avoid. |
| Quiz | Review questions at the end of each chapter, with answers in the Answer Key. |

## Activities that use a computer

| Where | Activity | What you need | Paper fallback |
|---|---|---|---|
| Chapter 1, Section 1.6 | [Optional Interactive Lab: See a CPU Execute Instructions](01-Hardware.md#optional-interactive-lab-see-a-cpu-execute-instructions) | Web browser (Little Man Computer simulator) | Trace the same program by hand |
| Chapter 2, Section 2.3 | [Network Lab: Look at a Real Network from Your Own Computer](02-Networks.md#network-lab-look-at-a-real-network-from-your-own-computer) | Terminal / Command Prompt | Expected results in the answer key |
| Chapter 3, Sections 3.2, 3.3, 3.5 | "Run it" Python programs | Python 3 or an online Python editor | Paper trace and printed expected output |

## Team and credits

Written by Team DeepThink: Batyr (CEO), Mukhammadamin (CIO), Zere and Ardak (visual design), Merey (video), Asilbek (quality), Altair (content). Sources are listed in the **References** section of each chapter. Diagrams were drawn by the team for this guide.

[Chapter 1: Hardware →](01-Hardware.md)
