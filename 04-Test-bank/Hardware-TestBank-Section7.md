# Test Bank · Section 7: Sensors, Actuators and Microcontrollers

*Team DeepThink · Hardware part · Written by Merey · Draft for the team Test Bank*

This file holds **12 True/False, 12 multiple-choice and 3 open-ended questions** for Section 7 *Sensors, Actuators and Microcontrollers* of the Hardware Study Guide. Add them to the team Test Bank (minimum 20 True/False, 20 multiple-choice and 6 open-ended questions in total).

- Every question names its Study Guide section and, where it applies, the activity it connects to.
- All the information needed is inside the question, so no external platform is required.
- The answer key is at the end (Part B).
- **Status:** written, not yet attempted by another member (see the checking record at the end).

**Section and activity numbers.** The same content appears with different numbers in the team files. Question tags use the **Study Guide (Word)** numbers:

| Activity | Study Guide (Word) | `03-Study-guide/Hardware.md` | `03-Study-guide/Chapter 2: Hardware` |
|---|---|---|---|
| Round It Like a Converter | Activity 7 | Activity 6 | Activity 14 |
| Fast Enough? Sampling and Noise | Activity 8 | Activity 7 | Activity 15 |
| Sensor or Actuator? | Activity 9 | Activity 8 | Activity 16 |
| Drive the Motors | Activity 10 | Activity 9 | Activity 17 |
| From Echo to Distance | Activity 11 | Activity 10 | Activity 18 |
| Be the Microcontroller | Activity 12 | Activity 11 | Activity 19 |
| Design Challenge: A Parking Sensor | Activity 13 | Activity 12 | Activity 20 |
| Section | 7.1–7.5 | 7.1–7.5 | 8.1–8.5 |

**Contents:** [True/False](#truefalse-answer-true-or-false-for-each-statement) · [Multiple choice](#multiple-choice) · [Open-ended](#open-ended-answer-in-about-100-words-or-more-you-may-use-calculations-or-a-labelled-diagram) · [Answer key](#part-b-answer-key) · [Checking record](#checking-record)

## Part A: Questions

### True/False (answer True or False for each statement)

#### S7-TF1 · Guide section 7.1

A sensor turns a signal from the computer into a physical action such as movement or sound.

#### S7-TF2 · Guide section 7.1 · Activity 7

Quantization rounds each sampled value to the nearest whole number.

#### S7-TF3 · Guide section 7.1

Measuring a changing signal more times per second can show changes that fewer measurements would miss.

#### S7-TF4 · Guide section 7.3

A microcontroller is a tiny computer on a single chip that is built to run one dedicated program.

#### S7-TF5 · Guide section 7.5 · Activity 11

An ultrasonic sensor sends a sound pulse and the echo takes 1166 µs to return. The distance is therefore 343 m/s × 0.001166 s, with no further division.

#### S7-TF6 · Guide section 7.5 · Activity 12

The robot program contains the instruction "IF B is more than 20, JUMP to address 06" (address 06 is GO FORWARD, address 04 is STOP and TURN). When Register B holds exactly 20, the robot jumps to address 06 and drives forward.

#### S7-TF7 · Guide section 7.1

A bumper switch is an analog sensor, because it can report any value in a range.

#### S7-TF8 · Guide section 7.1

A 10-bit analog-to-digital converter can tell apart 1,024 different values.

#### S7-TF9 · Guide section 7.2 · Activity 10

With PWM at a 50 % duty cycle on a 6 V supply, the average voltage that reaches the motor is about 3 V.

#### S7-TF10 · Guide section 7.2

A microcontroller pin can safely power a wheel motor directly, so a motor driver is optional.

#### S7-TF11 · Guide section 7.3

In a microcontroller program, setup() repeats again and again, while loop() runs only once when the power comes on.

#### S7-TF12 · Guide section 7.1 · Activity 8

At 20 readings per second, averaging the last 100 readings always makes an obstacle-avoiding robot safer.

### Multiple choice

#### S7-MC1 · Guide section 7.2 — *one answer*

Which of the following is an actuator?

- **A.** Camera
- **B.** Gyroscope
- **C.** Wheel motor
- **D.** Microphone

#### S7-MC2 · Guide section 7.1 · Activity 7 — *one answer*

An imaginary converter has 3 bits and outputs only the whole numbers 0 to 7. A sensor measures 5.7 volts. Which 3-bit code does the converter write?

- **A.** 101
- **B.** 110
- **C.** 111
- **D.** 011

#### S7-MC3 · Guide section 7.3 — *select ALL correct answers*

Which statements about a microcontroller are correct?

- **A.** It contains a CPU, memory and connection pins on one chip.
- **B.** It is designed to run many different user programs at the same time.
- **C.** It is often used inside appliances and vehicles as part of an embedded system.
- **D.** A screen and a keyboard are normally its main way of communicating with the world.
- **E.** In some devices it must save battery power or react within strict time limits.

#### S7-MC4 · Guide section 7.5 · Activity 11 — *one answer*

An ultrasonic sensor reports an echo time of 2332 µs. The speed of sound is 343 m/s. What is the distance to the wall?

- **A.** 20 cm
- **B.** 40 cm
- **C.** 80 cm
- **D.** 160 cm

#### S7-MC5 · Guide section 7.5 · Activity 12 — *one answer*

The robot program drives forward when Register B (the distance in cm) is more than 20, and stops and turns otherwise. The sensor reports an echo time of 1749 µs. The program divides the echo time by 58 and ignores decimals. What does the robot do?

- **A.** It drives forward, because the distance is 30 cm.
- **B.** It stops and turns, because the distance is 30 cm.
- **C.** It drives forward, because the distance is 1749 cm.
- **D.** It stops and turns, because the distance is 20 cm.

#### S7-MC6 · Guide section 7.4 — *one answer*

Which order describes one pass of the loop that a simple robot repeats?

- **A.** act → sense → decide
- **B.** sense → decide → act
- **C.** decide → sense → act
- **D.** sense → act → decide

#### S7-MC7 · Guide section 7.1 · Activity 8 — *one answer*

A robot drives at 30 cm per second and reads its distance sensor 10 times per second. How far does it drive between two readings?

- **A.** 0.3 cm
- **B.** 3 cm
- **C.** 30 cm
- **D.** 300 cm

#### S7-MC8 · Guide section 7.2 · Activity 10 — *one answer*

A motor driver uses an H-bridge. IN1 = 1 and IN2 = 0 make the motor turn forward. What happens with IN1 = 0 and IN2 = 1?

- **A.** The motor turns forward faster.
- **B.** The motor turns backward.
- **C.** The motor stops.
- **D.** The microcontroller restarts.

#### S7-MC9 · Guide section 7.2 — *one answer*

A robot gripper must turn to exactly 90° and stay there. Which actuator fits best?

- **A.** DC motor
- **B.** Servo motor
- **C.** Speaker
- **D.** Ultrasonic sensor

#### S7-MC10 · Guide section 7.3 — *select ALL correct answers*

Which parts are found inside a typical microcontroller chip?

- **A.** CPU
- **B.** Flash memory that keeps the program without power
- **C.** Analog-to-digital converter
- **D.** A graphics card with gigabytes of memory
- **E.** Input/output pins

#### S7-MC11 · Guide section 7.2 · Activity 10 — *one answer*

Both wheels turn forward. The left wheel runs at 100 % and the right wheel at 50 %. What does the robot do?

- **A.** It drives straight ahead.
- **B.** It curves to the left.
- **C.** It curves to the right.
- **D.** It spins on the spot.

#### S7-MC12 · Guide section 7.5 · Activity 13 — *one answer*

A parking sensor uses distance (cm) = echo time (µs) ÷ 58. Which echo time matches a wall 100 cm away?

- **A.** 1740 µs
- **B.** 2900 µs
- **C.** 5800 µs
- **D.** 58,000 µs

### Open-ended (answer in about 100 words or more; you may use calculations or a labelled diagram)

#### S7-OE1 · Guide section 7.5 · Activity 11

A student programs an obstacle-avoiding robot. The robot should stop and turn when a wall is 20 cm away or closer. The student's program measures the echo time in seconds and calculates distance = 343 × echo time. The echo times it measures are correct, but the robot keeps hitting walls. (a) Explain what is wrong with the calculation. (b) Calculate how far from the wall the robot really is when it finally turns. (c) Explain how to fix the program and describe one extra change that would make the robot safer.

#### S7-OE2 · Guide sections 7.3 and 7.4 · Activities 9 and 12

A company wants to build an automatic night light. It should switch a lamp on when the room becomes dark and off when it becomes bright. (a) Name the sensor, the actuator and the computing part you would use, and say what each one does. (b) Describe how the sense–decide–act loop works for this device, including what the program compares and why the loop repeats. (c) Explain why a microcontroller is a better choice for this job than the processor of a laptop.

#### S7-OE3 · Guide sections 7.1–7.3 · Activities 8 and 10

A student builds an obstacle-avoiding robot that drives at 30 cm per second. (1) The program reads the distance sensor only twice per second. (2) The wheel motor is connected directly to a microcontroller pin. (3) To remove noise, the program averages the last 50 readings. The robot often crashes and sometimes restarts. Explain the problem caused by each design choice, use a calculation for at least one of them, and suggest a fix for each.

## Part B: Answer Key

### True/False

| **Question** | **Answer** | **Explanation (false statements are corrected)** |
| --- | --- | --- |
| S7-TF1 | False | A device that turns a computer signal into a physical action is an actuator. A sensor does the opposite: it measures the world and turns the measurement into a signal. |
| S7-TF2 | True | Quantization rounds each sample to the nearest whole number, for example 2.2 becomes 2 and 5.7 becomes 6. |
| S7-TF3 | True | Samples taken between measurements are never recorded, so a rapidly changing signal needs more samples per second than a smooth one. |
| S7-TF4 | True | A microcontroller combines a CPU, memory and connection pins on one chip and runs one dedicated program. |
| S7-TF5 | False | The sound travels to the wall and back, so the time must be divided by 2: 343 × 0.001166 ÷ 2 = 0.2 m = 20 cm. Without the division the result (0.4 m) is twice too large. |
| S7-TF6 | False | 20 is not more than 20, so the jump does not happen. The program continues to address 04 and the robot stops and turns. |
| S7-TF7 | False | A bumper switch is a digital sensor: it is either pressed (1) or not pressed (0). A light sensor is an example of an analog sensor. |
| S7-TF8 | True | 10 bits give 2¹⁰ = 1,024 values (0 to 1023), as in the Arduino Uno's converter. |
| S7-TF9 | True | Average voltage = duty cycle × supply = 0.5 × 6 V = 3 V. |
| S7-TF10 | False | A pin supplies only a tiny current (about 20 mA is recommended on an Arduino Uno), while a motor can need hundreds of milliamps. A motor driver must switch the battery current. |
| S7-TF11 | False | It is the other way round: setup() runs once when the power comes on, and loop() repeats forever. |
| S7-TF12 | False | 100 readings at 20 per second take 5 seconds. The average then describes the past, and the robot can drive 150 cm in that time. Averaging a few readings helps; averaging too many makes the robot react too late. |

### Multiple choice

| **Question** | **Correct choice** | **Reasoning** |
| --- | --- | --- |
| S7-MC1 | C | A wheel motor changes the world by moving the robot. A camera, a gyroscope and a microphone all measure the world, so they are sensors. |
| S7-MC2 | B (110) | 5.7 rounds to 6, and 6 = 4 + 2 is written 110 in 3 bits. A (101) is 5, which is what you get by rounding down instead of to the nearest value. C (111) is 7. D (011) is 3. |
| S7-MC3 | A, C and E | A is the definition. C and E describe typical embedded systems. B describes a general-purpose computer, and D is wrong because a microcontroller usually has no screen or keyboard and talks to the world through sensors and actuators. |
| S7-MC4 | B | 343 × 0.002332 = 0.8 m, and 0.8 ÷ 2 = 0.4 m = 40 cm. Choice C (80 cm) comes from forgetting to divide by 2. A and D do not match the calculation. |
| S7-MC5 | A | 1749 ÷ 58 = 30 (decimals ignored). 30 is more than 20, so the robot drives forward. B reverses the rule. C ignores the division. D confuses 30 with the threshold. |
| S7-MC6 | B | The robot first measures (sense), then compares and chooses (decide), then moves (act), and then repeats because the world has changed. |
| S7-MC7 | B | Time between readings = 1 ÷ 10 = 0.1 s, and 30 cm/s × 0.1 s = 3 cm. C (30 cm) is the distance for one whole second. |
| S7-MC8 | B | Swapping IN1 and IN2 reverses the current through the motor, so it turns backward. With both at 0 it would stop. |
| S7-MC9 | B | A servo motor turns to a chosen angle and holds it. A DC motor spins continuously; a speaker and a sensor are not suitable. |
| S7-MC10 | A, B, C and E | A microcontroller has a CPU, flash, RAM, an ADC, timers and pins on one chip. D describes a laptop or PC, not a microcontroller. |
| S7-MC11 | C | The left wheel travels faster, so the robot turns toward the slower right side. Equal speeds would drive straight (A). |
| S7-MC12 | C | 100 cm × 58 = 5800 µs. A (1740 µs) matches 30 cm, B (2900 µs) matches 50 cm, and D is ten times too large. |

### Open-ended: sample answers and key points

#### S7-OE1: key points

(a) The program forgets to divide by 2. The echo time covers the path to the wall and back, so 343 × echo time gives twice the real distance.

(b) The program believes the wall is twice as far away as it is. It turns only when the calculated distance is 20 cm or less, which means the real distance is about 10 cm.

(c) Fix: distance = 343 × echo time ÷ 2. A further safety change: raise the threshold (for example to 30 cm), so the robot has room to turn, or check the sensor more often.

**Sample answer:**

The student forgot that the sound pulse travels to the wall and then back to the sensor. The measured echo time therefore covers the distance twice. Multiplying the speed of sound by the echo time gives the length of the whole round trip, not the distance to the wall. Because the program does not divide by 2, it always believes that the wall is twice as far away as it really is. The robot turns only when its calculated distance falls to 20 cm, and that happens when the wall is really only about 10 cm away. At that point the robot may not have enough room to stop and turn, so it hits the wall. To fix the program, the calculation must be distance = 343 m/s × echo time ÷ 2. For example, an echo time of 1166 µs gives 343 × 0.001166 ÷ 2 = 0.2 m, which is 20 cm. To make the robot safer, the student could also raise the threshold to 30 cm, so that the robot reacts earlier and has more space to turn. Other valid improvements, such as measuring more often, should also be accepted if they are explained.

#### S7-OE2: key points

(a) Sensor: a light sensor measures how bright the room is. Computing part: a microcontroller runs the program. Actuator: the lamp (or a switch for the lamp) turns light on and off.

(b) Sense: measure the brightness and convert it into a number. Decide: compare the number with a threshold. Act: switch the lamp on or off. Repeat: the light level changes during the day and when the lamp itself is on, so the loop must keep checking.

(c) The job is one dedicated task that needs little computing power. A microcontroller is small, cheap, uses little power, has pins to connect a sensor and a lamp directly, and needs no screen, keyboard or large operating system.

**Sample answer:**

I would use a light sensor as the sensor, a microcontroller as the computing part, and the lamp, switched through a small driver circuit, as the actuator. The light sensor measures how bright the room is and turns the brightness into an electrical signal. The microcontroller converts that signal into a number by sampling and rounding it, and then runs a program that compares the number with a threshold. If the number is below the threshold, the room is dark, so the program tells the lamp to switch on. If the number is above the threshold, the program switches the lamp off. This is the sense–decide–act loop. The loop must repeat all the time because the brightness changes during the day, and the lamp itself changes how bright the room is. A microcontroller suits this job better than a laptop processor because the task is simple and never changes. A microcontroller is small, cheap and uses very little power, so the light can stay on all year. It has connection pins for the sensor and the lamp, and it does not need a screen, a keyboard or a large operating system. A laptop processor is designed for many different programs and would be a waste of money and energy here.

#### S7-OE3: key points

(1) Two readings per second means 0.5 s between readings, so the robot drives 30 cm/s × 0.5 s = 15 cm "blind", most of its 20 cm safety distance. Fix: read the sensor much more often, for example 20 times per second (1.5 cm between readings).

(2) A microcontroller pin cannot supply the current a motor needs. The motor barely turns and the overload can disturb the microcontroller's supply, so it restarts. Fix: use a motor driver (H-bridge) that switches the battery current.

(3) Averaging 50 readings at 2 per second covers 25 seconds, so the distance is badly out of date. Fix: average only a few readings (for example 3), or use two thresholds (hysteresis).

**Sample answer:**

The first problem is the sampling rate. If the sensor is read only twice per second, there are 0.5 seconds between readings. At 30 cm per second the robot drives 30 × 0.5 = 15 cm without any new information, which is most of its 20 cm safety distance. A wall that was 30 cm away at one reading can be only 15 cm away at the next, or the robot can hit it before it reacts. The fix is to read the sensor far more often; at 20 readings per second the robot moves only 1.5 cm between readings. The second problem is the motor connection. A microcontroller pin can only supply a very small current, about 20 milliamps on an Arduino Uno, but a wheel motor needs much more. The motor gets too little power and the overloaded pin can pull down the microcontroller's supply, which explains why it restarts. The motor must be connected through a motor driver with an H-bridge, which switches the battery current and also allows forward and backward driving. The third problem is the averaging. At two readings per second, 50 readings cover 25 seconds, so the average describes where the wall was long ago. The robot reacts to the past instead of the present. A better solution is to average only the last three readings, or to use two thresholds so that small noise near the limit does not make the robot switch back and forth.

## Checking record

Another member must attempt every question without looking at the answer key and compare the results. Fill in this table after checking.

| **Reviewer** | **Date** | **Questions attempted** | **Problems found** | **Changes made** |
| --- | --- | --- | --- | --- |
| (to be filled in) |  | S7-TF1–12, S7-MC1–12, S7-OE1–3 |  |  |

*Sources for the content: Brookshear, Computer Science: An Overview, 11th ed., pp. 114, 462–463, 497–499; Forouzan, Foundations of Computer Science, 4th ed., pp. 62–63, 105, 176. Arduino Uno Rev3 documentation (docs.arduino.cc) for the 10-bit converter and pin current. The speed of sound (343 m/s at about 20 °C), the 58 µs per cm shortcut, PWM and H-bridge behaviour are standard physics and electronics and should be confirmed by a teammate.*