[🏠 Start here](03-Study-guide/00-Start-Here.md) · [README](README.md)

# Resource map – where each topic is taught and tested

*Team DeepThink · updated for the Stage 3 final Markdown content (v3.0, 25 November 2026)*

The Markdown chapters in `03-Study-guide/` are the shared foundation. The table shows, for every major topic, where it is used in the Study Guide, the Test Bank, the PPT slides and the video tutorials. **—** means that the topic was deliberately not selected for that medium (it is covered in the guide and test bank instead).

**Resources referred to**

- **Guide:** the chapter files in `03-Study-guide/` (section, activity and figure numbers are the same as in Study Guide V1.0).
- **TB:** [04-Test-bank/Test-Bank.md](04-Test-bank/Test-Bank.md), questions Q1–Q97.
- **PPT:** `DeepThink_Stage2_PPT_V1.pptx` (35 slides with presenter notes): opening question (slide 2), Hardware dive, Networks dive (slides 14–22), Behaviorist AI dive, finale (slide 32) and wrap-up (slides 33–35). Submitted under the PPT Slides assignment; not stored in this repository.
- **Video:** four MP4 tutorials submitted under the Video Tutorials assignment, not stored in this repository: **V01** *Inside the Machine: How a Computer Runs a Program* (3:36), **V02** *How Devices Talk: Addresses, Packets and Protocols* (3:44), **V03** *Behaviorist AI* (3:47), **V04** *One Robot, Three Ideas: Sense, Decide, Act* (4:18).

Slide and video positions below are those of the Stage 2 versions as recorded in the peer reviews of 17 November 2026; positions marked *(slide no. to confirm)* must be checked against the final deck.

## Chapter 1 – Hardware

| Topic (Markdown section) | Guide: activities and figures | Test Bank | PPT slides | Video |
|---|---|---|---|---|
| Computer subsystems (1.1) | Activity 1; Fig. 1.1–1.3 | Q22 | Hardware dive, opening *(slide no. to confirm)* | V01 |
| CPU: ALU, registers, control unit (1.2) | Activity 2; Fig. 1.4–1.13 | Q1–Q3, Q23 | Slides 5–6 (CPU components and analogy) | V01 |
| Main memory, RAM/ROM, cache (1.3) | Activity 3; Fig. 1.14–1.19 | Q4–Q6, Q26, Q28, Q45 | Hardware dive *(slide no. to confirm)* | V01 |
| Input/output and storage (1.4) | Activity 4; Fig. 1.20–1.25 | Q7, Q8, Q28, Q45 | Hardware dive *(slide no. to confirm)* | — |
| Buses and I/O controllers (1.5) | Activity 5; Fig. 1.26–1.27 | Q9, Q27, Q44 | — | — |
| Stored program and fetch–decode–execute (1.6) | Activity 6; Optional CPU simulator lab (new); Fig. 1.28–1.31 | Q11, Q24, Q25, Q44 | Hardware dive *(slide no. to confirm)* | V01 (address tables and program trace, 1:40–3:10) |
| Sensors, sampling and noise (1.7.1) | Activities 7–8; Fig. 1.32–1.33 | Q12–Q14, Q18, Q21, Q29, Q30, Q33, Q38, Q49 | "How does a machine sense?" *(slide no. to confirm)* | — |
| Actuators, PWM, H-bridge (1.7.2) | Activities 9–10; Fig. 1.34–1.35 | Q10, Q19, Q32, Q39, Q40, Q42, Q46, Q49 | PWM with three duty cycles *(slide no. to confirm)* | — |
| Microcontrollers, setup()/loop() (1.7.3) | Fig. 1.36–1.37 | Q15, Q20, Q31, Q34, Q41, Q48 | Laptop vs. microcontroller *(slide no. to confirm)* | V04 |
| Sense–decide–act loop (1.7.4) | Fig. 1.38 | Q37, Q48 | Behaviorist AI dive (sense–act loop) | V04 (title and structure) |
| Echo time → distance; robot program (1.7.5) | Activities 11–13; Fig. 1.39 | Q16, Q17, Q35, Q36, Q43, Q47 | Slides 12–13 (formula; 2915 µs ≈ 50 cm) | V04 (1166 µs and the forgotten ÷ 2, 1:10–2:30; program trace, 2:40–3:20) |

## Chapter 2 – Networks

| Topic (Markdown section) | Guide: activities and figures | Test Bank | PPT slides | Video |
|---|---|---|---|---|
| Network types (2.1.1) | Quick check 1; Fig. 2.1 | Q50, Q51, Q61 | Networks dive (slides 14–22) | V02 |
| Media and devices (2.1.2–2.1.3) | Quick checks 2–3; Fig. 2.2–2.3 | Q52, Q62, Q71 | Networks dive (slides 14–22) | V02 |
| Architecture, OSI and TCP/IP layers (2.2) | Quick check 4; Fig. 2.4–2.5 | Q53, Q63 | Networks dive (slides 14–22) | V02 |
| Internet, protocols, TCP/UDP, packets (2.3.1–2.3.2) | Quick checks 5 and "Internet vs Web"; Fig. 2.6 | Q54, Q55, Q64, Q65, Q72 | Networks dive (slides 14–22) | V02 (packets; 3:00–3:20 "STOP one second late = 30 cm") |
| IP addresses, DHCP, domains, DNS (2.3.3–2.3.4) | Quick checks 6–7; Fig. 2.7–2.8 | Q56, Q57, Q66–Q68, Q73 | Networks dive (slides 14–22) | V02 (addresses) |
| Routing and servers (2.3.5–2.3.6) | Quick checks 8–9; Fig. 2.9 | Q58, Q60, Q69 | Networks dive (slides 14–22) | V02 |
| **Network Lab** (new in Stage 3, end of 2.3) | Lab with terminal commands and expected results | Q73 (DNS, IP addresses and routing, in writing) | — (new in Stage 3) | — (new in Stage 3) |
| Security: firewall, privacy, authentication, integrity, non-repudiation (2.4) | Quick check 10; Fig. 2.10 | Q59, Q70, Q74 | Networks dive (slides 14–22) | — |
| Rover's message through the layers (2.5) | Mission question; Fig. 2.11 | Q73 | Finale (slide 32) | V02, V04 |

## Chapter 3 – Behaviorist AI

| Topic (Markdown section) | Guide: activities and figures | Test Bank | PPT slides | Video |
|---|---|---|---|---|
| Behaviorism: Pavlov and Skinner (3.1) | Activity 1.1; Fig. 3.1–3.4 | Q75–Q77, Q85, Q95 | Behaviorist AI dive *(slide no. to confirm)* | V03 |
| Reactive agents, sense–act loop, ultrasonic sensor (3.2) | Activity 2.1 (paper + Python); Fig. 3.5–3.8 | Q78, Q79, Q86, Q87 | Behaviorist AI dive *(slide no. to confirm)* | V03, V04 |
| Behavior rules, priorities, hysteresis (3.3) | Activity 3.1; Python program in 3.3.5; Fig. 3.9–3.10 | Q80, Q81, Q88–Q90, Q96 | Behaviorist AI dive *(slide no. to confirm)* | V03 |
| Brooks's subsumption architecture (3.4) | Activity 4.1; Fig. 3.11–3.13 | Q82, Q91 | Behaviorist AI dive *(slide no. to confirm)* | V03 |
| Case study: hardware + network + behavior, local safety (3.5) | Activities 5.1–5.2; Python trace in 3.5.8; Fig. 3.14–3.15 | Q83, Q92, Q93, Q97 | Slide 2 (opening question) and slide 32 (finale: 1.5 cm / 6 cm / 30 cm) | V04 |
| Reinforcement learning, limits, ethics (3.6) | Activities 6.1 (Corner Trap) and 6.2; Fig. 3.16–3.17 | Q84, Q94, Q97 | Slide 33 (limits, corner trap, RL, hybrid AI, ethics) | — |
| Review and final design challenge (3.7) | Final Challenge; Fig. 3.18 | Q97 | Wrap-up slides 34–35 *(slide no. to confirm)* | — |

## Shared examples that must stay identical

| Example | Value used everywhere | Where it appears |
|---|---|---|
| Echo time → distance | 1166 µs → 20 cm (343 m/s × 0.001166 s ÷ 2); shortcut ÷ 58 | Guide 1.7.5 and Activity 12, Section 3.2 Check yourself, Chapter 3 Quiz MC 3; TB Q16, Q87; V04 |
| Second echo example | 2332 µs → 40 cm; 2915 µs ≈ 50 cm | Guide Activity 11; TB Q35; slides 12–13 |
| Rover's speed and reaction distance | 0.3 m/s; 50 ms on the robot → 1.5 cm; 0.2 s Wi-Fi → 6 cm; 1 s → 30 cm | Guide 1.7.1, 1.7.4, 3.5.7; TB Q92, Q97; slide 32; V02 |
| CPU program | LOAD 5, LOAD 3, ADD, STORE at 20, HALT → 8 | Guide 1.6.3, Activity 6, CPU lab; TB Q44; V01 |
| Priority convention | Rank 1 = highest priority (Avoid) | Guide 3.3; TB Q80, Q88; Behaviorist AI dive |
| PWM | average voltage = duty cycle × supply; speed is *not exactly* proportional | Guide 1.7.2, Activity 10; TB Q10, Q46 |

## Corrections in Stage 3 that the other resources must follow

1. **Test Bank numbers.** All questions now form one sequence Q1–Q97. The appendix of the Test Bank converts the old Stage 2 numbers (for example, old "Chapter 3, Q13" = Q87). Any "Practise next" pointer in the videos or slides should use the new numbers.
2. **Figure numbers in Chapter 1.** Figures 7.1–7.8 of Study Guide V1.0 are now Figures 1.32–1.39, so every figure number starts with its chapter number.
3. **PWM wording.** "50 % duty cycle = about half speed" was changed to "about half the power; the speed is lower but not exactly half". The PWM slide should use the same wording.
4. **Sense–decide–act vs. sense–act.** Chapter 3 now says that both names describe the same loop (Chapter 1 and V04 use *sense–decide–act*).
5. **Answers.** Activity answers moved to the answer key at the end of each chapter. The three slide prompts without answer slides (slides 13, 18 and 26 in the Stage 2 deck) can take their answers from the chapter answer keys.
