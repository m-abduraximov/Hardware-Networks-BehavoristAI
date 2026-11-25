[🏠 Start here](../03-Study-guide/00-Start-Here.md) · [Chapter 1](../03-Study-guide/01-Hardware.md) · [Chapter 2](../03-Study-guide/02-Networks.md) · [Chapter 3](../03-Study-guide/03-Behaviorist-AI.md)

# Test Bank – Hardware, Networks and Behaviorist AI

*Team DeepThink · Final Markdown version (Stage 3) · one numbered sequence for the whole module*

## How to use this Test Bank

- Every question has one number (Q1–Q97), so a reference such as "Test Bank Q57" points to exactly one question.
- The tag in brackets, for example `[1.6.2]`, names the Study Guide section that teaches the idea. Activity numbers are those of the chapter files in `03-Study-guide/`.
- Every question is self-contained: all numbers and rules needed to answer it are in the question.
- The answer key is at the end of the file, not after the questions. True/false answers correct every false statement; open-ended answers give key points and a 10-point marking guide.

| Chapter | True / False | Multiple choice | Open-ended |
|---|---|---|---|
| Chapter 1 – Hardware | 21 (Q1–Q21) | 22 (Q22–Q43) | 6 (Q44–Q49) |
| Chapter 2 – Networks | 11 (Q50–Q60) | 11 (Q61–Q71) | 3 (Q72–Q74) |
| Chapter 3 – Behaviorist AI | 10 (Q75–Q84) | 10 (Q85–Q94) | 3 (Q95–Q97) |
| **Total (97 questions)** | **42** | **43** | **12** |

**Contents:** [Chapter 1 – Hardware](#chapter-1--hardware) · [Chapter 2 – Networks](#chapter-2--networks) · [Chapter 3 – Behaviorist AI](#chapter-3--behaviorist-ai) · [Answer key](#answer-key)

---

## Chapter 1 – Hardware

*Study Guide: [Chapter 1 – Hardware](../03-Study-guide/01-Hardware.md)*

### Chapter 1 · Part A – True / False

*Write True or False. If a statement is false, correct it.*

<a id="q1"></a>**1.** `[1.2.2]` The ALU performs arithmetic, logic and shift operations on data.

<a id="q2"></a>**2.** `[1.2.3]` The Program Counter stores the instruction that the CPU is currently processing.

<a id="q3"></a>**3.** `[1.2.2]` Shifting the binary number 0011 one position to the left gives 0110, which doubles the value from 3 to 6.

<a id="q4"></a>**4.** `[1.3.1]` Eight bits together form one byte.

<a id="q5"></a>**5.** `[1.3.2]` ROM is normally volatile, so it loses its contents when the power is turned off.

<a id="q6"></a>**6.** `[1.3.3]` Cache memory replaces RAM, so a computer with cache does not need RAM.

<a id="q7"></a>**7.** `[1.4.2]` A solid-state drive (SSD) stores information magnetically on spinning disks.

<a id="q8"></a>**8.** `[1.4.3]` Adding more RAM automatically gives you more space to install games.

<a id="q9"></a>**9.** `[1.5.1]` The Address Bus carries information about the memory location the CPU wants to access.

<a id="q10"></a>**10.** `[1.7.2]` With PWM, a 50 % duty cycle on a 5 V supply gives an average voltage of about 2.5 V.

<a id="q11"></a>**11.** `[1.6.1]` You close a calculator app and open a game on the same computer without changing any hardware. This is possible because the game's instructions are loaded into memory in the same way as data (the stored-program concept).

<a id="q12"></a>**12.** `[1.7.1]` A sensor turns a signal from the computer into a physical action such as movement or sound.

<a id="q13"></a>**13.** `[1.7.1 · Activity 7]` Quantization rounds each sampled value to the nearest whole number.

<a id="q14"></a>**14.** `[1.7.1]` Measuring a changing signal more times per second can show changes that fewer measurements would miss.

<a id="q15"></a>**15.** `[1.7.3]` A microcontroller is a tiny computer on a single chip that is built to run one dedicated program.

<a id="q16"></a>**16.** `[1.7.5 · Activity 11]` An ultrasonic sensor sends a sound pulse and the echo takes 1166 µs to return. The distance is therefore 343 m/s × 0.001166 s, with no further division.

<a id="q17"></a>**17.** `[1.7.5 · Activity 12]` The robot program contains the instruction "IF B is more than 20, JUMP to address 06" (address 06 is GO FORWARD, address 04 is STOP and TURN). When Register B holds exactly 20, the robot jumps to address 06 and drives forward.

<a id="q18"></a>**18.** `[1.7.1]` A bumper switch is an analog sensor, because it can report any value in a range.

<a id="q19"></a>**19.** `[1.7.2]` A microcontroller pin can safely power a wheel motor directly, so a motor driver is optional.

<a id="q20"></a>**20.** `[1.7.3]` In a microcontroller program, setup() repeats again and again, while loop() runs only once when the power comes on.

<a id="q21"></a>**21.** `[1.7.1 · Activity 8]` At 20 readings per second, averaging the last 100 readings always makes an obstacle-avoiding robot safer.

### Chapter 1 · Part B – Multiple choice

*Choose the answer(s) shown in brackets after each question.*

<a id="q22"></a>**22.** `[1.1.1]` Which list shows the three broad categories of subsystems in a computer? *(Choose ONE answer.)*

- **A.** Keyboard, mouse and monitor
- **B.** CPU, Main Memory and the Input/Output subsystem
- **C.** RAM, ROM and cache
- **D.** Data Bus, Address Bus and Control Bus

<a id="q23"></a>**23.** `[1.2.2]` Which logic operation gives 1 only when both inputs are 1? *(Choose ONE answer.)*

- **A.** NOT
- **B.** OR
- **C.** AND
- **D.** XOR

<a id="q24"></a>**24.** `[1.6.2]` In the fetch stage, where is the fetched instruction placed? *(Choose ONE answer.)*

- **A.** Program Counter
- **B.** Instruction Register
- **C.** Cache
- **D.** Data Bus

<a id="q25"></a>**25.** `[1.6.2]` During the decode stage, which component interprets the instruction and decides which operation is required? *(Choose ONE answer.)*

- **A.** ALU
- **B.** Control Unit
- **C.** Program Counter
- **D.** Address Bus

<a id="q26"></a>**26.** `[1.3.3]` Which order goes from the fastest and smallest memory to the slower and larger one? *(Choose ONE answer.)*

- **A.** RAM → Cache → Registers
- **B.** Cache → Registers → RAM
- **C.** Registers → Cache → RAM
- **D.** Registers → RAM → Cache

<a id="q27"></a>**27.** `[1.5.1]` Which statements about buses are correct? *(Choose ALL correct answers.)*

- **A.** The Data Bus carries the actual data being transferred.
- **B.** The Address Bus carries the location the CPU wants to access.
- **C.** The Control Bus carries the numbers that are being added.
- **D.** The Control Bus can indicate whether the CPU wants to read or write.

<a id="q28"></a>**28.** `[1.3.2, 1.4.2–1.4.3]` Which of these keep their information when the power is turned off? *(Choose ALL correct answers.)*

- **A.** SSD
- **B.** HDD
- **C.** RAM
- **D.** Flash memory

<a id="q29"></a>**29.** `[1.7.1]` The converter inside the Arduino Uno's microcontroller has 10 bits. How many different values can it produce? *(Choose ONE answer.)*

- **A.** 10
- **B.** 256
- **C.** 1,023
- **D.** 1,024

<a id="q30"></a>**30.** `[1.7.1]` A robot stands still 20 cm from a wall. Its readings are 20, 21, 34, 19 and 20 cm. Which reading is most likely noise? *(Choose ONE answer.)*

- **A.** 20
- **B.** 21
- **C.** 34
- **D.** 19

<a id="q31"></a>**31.** `[1.7.3]` Which part of a microcontroller keeps the robot's program when the battery is removed? *(Choose ONE answer.)*

- **A.** RAM
- **B.** Flash memory
- **C.** Analog-to-digital converter
- **D.** Timers

<a id="q32"></a>**32.** `[1.7.2]` Which of the following is an actuator? *(Choose ONE answer.)*

- **A.** Camera
- **B.** Gyroscope
- **C.** Wheel motor
- **D.** Microphone

<a id="q33"></a>**33.** `[1.7.1 · Activity 7]` An imaginary converter has 3 bits and outputs only the whole numbers 0 to 7. A sensor measures 5.7 volts. Which 3-bit code does the converter write? *(Choose ONE answer.)*

- **A.** 101
- **B.** 110
- **C.** 111
- **D.** 011

<a id="q34"></a>**34.** `[1.7.3]` Which statements about a microcontroller are correct? *(Choose ALL correct answers.)*

- **A.** It contains a CPU, memory and connection pins on one chip.
- **B.** It is designed to run many different user programs at the same time.
- **C.** It is often used inside appliances and vehicles as part of an embedded system.
- **D.** A screen and a keyboard are normally its main way of communicating with the world.
- **E.** In some devices it must save battery power or react within strict time limits.

<a id="q35"></a>**35.** `[1.7.5 · Activity 11]` An ultrasonic sensor reports an echo time of 2332 µs. The speed of sound is 343 m/s. What is the distance to the wall? *(Choose ONE answer.)*

- **A.** 20 cm
- **B.** 40 cm
- **C.** 80 cm
- **D.** 160 cm

<a id="q36"></a>**36.** `[1.7.5 · Activity 12]` The robot program drives forward when Register B (the distance in cm) is more than 20, and stops and turns otherwise. The sensor reports an echo time of 1749 µs. The program divides the echo time by 58 and ignores decimals. What does the robot do? *(Choose ONE answer.)*

- **A.** It drives forward, because the distance is 30 cm.
- **B.** It stops and turns, because the distance is 30 cm.
- **C.** It drives forward, because the distance is 1749 cm.
- **D.** It stops and turns, because the distance is 20 cm.

<a id="q37"></a>**37.** `[1.7.4]` Which order describes one pass of the loop that a simple robot repeats? *(Choose ONE answer.)*

- **A.** act → sense → decide
- **B.** sense → decide → act
- **C.** decide → sense → act
- **D.** sense → act → decide

<a id="q38"></a>**38.** `[1.7.1 · Activity 8]` A robot drives at 30 cm per second and reads its distance sensor 10 times per second. How far does it drive between two readings? *(Choose ONE answer.)*

- **A.** 0.3 cm
- **B.** 3 cm
- **C.** 30 cm
- **D.** 300 cm

<a id="q39"></a>**39.** `[1.7.2 · Activity 10]` A motor driver uses an H-bridge. IN1 = 1 and IN2 = 0 make the motor turn forward. What happens with IN1 = 0 and IN2 = 1? *(Choose ONE answer.)*

- **A.** The motor turns forward faster.
- **B.** The motor turns backward.
- **C.** The motor stops.
- **D.** The microcontroller restarts.

<a id="q40"></a>**40.** `[1.7.2]` A robot gripper must turn to exactly 90° and stay there. Which actuator fits best? *(Choose ONE answer.)*

- **A.** DC motor
- **B.** Servo motor
- **C.** Speaker
- **D.** Ultrasonic sensor

<a id="q41"></a>**41.** `[1.7.3]` Which parts are found inside a typical microcontroller chip? *(Choose ALL correct answers.)*

- **A.** CPU
- **B.** Flash memory that keeps the program without power
- **C.** Analog-to-digital converter
- **D.** A graphics card with gigabytes of memory
- **E.** Input/output pins

<a id="q42"></a>**42.** `[1.7.2 · Activity 10]` Both wheels turn forward. The left wheel runs at 100 % and the right wheel at 50 %. What does the robot do? *(Choose ONE answer.)*

- **A.** It drives straight ahead.
- **B.** It curves to the left.
- **C.** It curves to the right.
- **D.** It spins on the spot.

<a id="q43"></a>**43.** `[1.7.5 · Activity 13]` A parking sensor uses distance (cm) = echo time (µs) ÷ 58. Which echo time matches a wall 100 cm away? *(Choose ONE answer.)*

- **A.** 1740 µs
- **B.** 2900 µs
- **C.** 5800 µs
- **D.** 58,000 µs

### Chapter 1 · Part C – Open-ended

*Write a developed answer (normally more than 100 words), using examples, a diagram or worked steps. Each question is worth 10 points.*

<a id="q44"></a>**44.** `[1.5.1, 1.6]` Explain the Fetch–Decode–Execute cycle using the example of a program that adds 5 + 3. Describe what the Program Counter, the Instruction Register, the Control Unit, the ALU and the buses (Address Bus, Control Bus and Data Bus, see Section 1.5.1) do at each stage, and explain why the cycle repeats.

<a id="q45"></a>**45.** `[1.3–1.4]` A student says: "Why does a computer need registers, cache, RAM and an SSD? One big memory would be simpler." Write a reply that explains the role of each type, compares their speed and size, explains the difference between volatile RAM and nonvolatile SSD storage, and uses the example of a document that is saved versus one that is not saved when the power suddenly fails.

<a id="q46"></a>**46.** `[1.7.2]` A robot's wheel motor must be controlled by a microcontroller. Explain how the microcontroller controls the speed (PWM and duty cycle) and the direction (H-bridge) of the motor, and why a motor driver is needed. Include a calculation of the average voltage for a 75 % duty cycle on a 6 V supply, and explain what happens if a student connects the motor directly to a microcontroller pin.

<a id="q47"></a>**47.** `[1.7.5 · Activity 11]` A student programs an obstacle-avoiding robot. The robot should stop and turn when a wall is 20 cm away or closer. The student's program measures the echo time in seconds and calculates distance = 343 × echo time. The echo times it measures are correct, but the robot keeps hitting walls. (a) Explain what is wrong with the calculation. (b) Calculate how far from the wall the robot really is when it finally turns. (c) Explain how to fix the program and describe one extra change that would make the robot safer.

<a id="q48"></a>**48.** `[1.7.3 and 1.7.4 · Activities 9 and 12]` A company wants to build an automatic night light. It should switch a lamp on when the room becomes dark and off when it becomes bright. (a) Name the sensor, the actuator and the computing part you would use, and say what each one does. (b) Describe how the sense–decide–act loop works for this device, including what the program compares and why the loop repeats. (c) Explain why a microcontroller is a better choice for this job than the processor of a laptop.

<a id="q49"></a>**49.** `[1.7.1–1.7.3 · Activities 8 and 10]` A student builds an obstacle-avoiding robot that drives at 30 cm per second. (1) The program reads the distance sensor only twice per second. (2) The wheel motor is connected directly to a microcontroller pin. (3) To remove noise, the program averages the last 50 readings. The robot often crashes and sometimes restarts. Explain the problem caused by each design choice, use a calculation for at least one of them, and suggest a fix for each.

## Chapter 2 – Networks

*Study Guide: [Chapter 2 – Networks](../03-Study-guide/02-Networks.md)*

### Chapter 2 · Part A – True / False

*Write True or False. If a statement is false, correct it.*

<a id="q50"></a>**50.** `[2.1.1]` A LAN usually covers a room, a building or a small campus.

<a id="q51"></a>**51.** `[2.1.1]` In a peer-to-peer network, devices share resources directly without a central server.

<a id="q52"></a>**52.** `[2.1.3]` A hub sends incoming data only to the port where the receiver is connected.

<a id="q53"></a>**53.** `[2.2]` The OSI model has seven layers, and the TCP/IP model has four layers.

<a id="q54"></a>**54.** `[2.3.1]` The World Wide Web and the Internet are the same thing.

<a id="q55"></a>**55.** `[2.3.2]` TCP starts a connection with three messages: SYN, SYN-ACK and ACK.

<a id="q56"></a>**56.** `[2.3.3]` 192.168.1.300 is a valid IPv4 address.

<a id="q57"></a>**57.** `[2.3.3]` DHCP gives devices IP addresses and other network settings automatically.

<a id="q58"></a>**58.** `[2.3.5]` Every router knows the complete path from the sender to the final destination.

<a id="q59"></a>**59.** `[2.4.3]` Authentication guarantees that data has not been changed during transmission.

<a id="q60"></a>**60.** `[2.3.6]` When you open a news website, a database server sends the web page to your browser using HTTPS on port 443.

### Chapter 2 · Part B – Multiple choice

*Choose the answer(s) shown in brackets after each question.*

<a id="q61"></a>**61.** `[2.1.1]` Which of the following are typical connections for a PAN? *(Choose ALL correct answers.)*

- **A.** Bluetooth
- **B.** USB
- **C.** Undersea cables
- **D.** Fibre between cities

<a id="q62"></a>**62.** `[2.1.3]` Which device sends data only to the port of the receiving device, using MAC addresses? *(Choose ONE answer.)*

- **A.** Hub
- **B.** Switch
- **C.** Modem
- **D.** Access point

<a id="q63"></a>**63.** `[2.2]` In the TCP/IP model, which OSI layers are combined into the Application layer? *(Choose ONE answer.)*

- **A.** Physical and Data Link
- **B.** Network and Transport
- **C.** Session, Presentation and Application
- **D.** Transport and Session

<a id="q64"></a>**64.** `[2.3.2]` Which protocol gives reliable, ordered delivery and resends lost data? *(Choose ONE answer.)*

- **A.** IP
- **B.** UDP
- **C.** TCP
- **D.** ICMP

<a id="q65"></a>**65.** `[2.3.2]` Rover's report is sent with TCP as 5 numbered packets, and packet 3 is lost. What happens? *(Choose ONE answer.)*

- **A.** The whole message is dropped
- **B.** Only packet 3 is sent again
- **C.** The phone ignores the missing word
- **D.** A router rebuilds packet 3 itself

<a id="q66"></a>**66.** `[2.3.3]` Which of these are private IPv4 addresses? *(Choose ALL correct answers.)*

- **A.** 10.0.0.5
- **B.** 8.8.8.8
- **C.** 172.20.4.1
- **D.** 172.40.4.1

<a id="q67"></a>**67.** `[2.3.4]` In the address https://mail.google.com, which part is the subdomain? *(Choose ONE answer.)*

- **A.** https
- **B.** mail
- **C.** google
- **D.** .com

<a id="q68"></a>**68.** `[2.3.4]` What does DNS give your computer when you type a domain name? *(Choose ONE answer.)*

- **A.** The web page itself
- **B.** The IP address of the server
- **C.** A new MAC address
- **D.** A password

<a id="q69"></a>**69.** `[2.3.5]` A network has these links: Home–R1, Home–R2, R1–R3, R1–R4, R2–R4, R3–Server, R4–Server. Router R3 stops working. Which paths can still reach the server? *(Choose ALL correct answers.)*

- **A.** Home → R1 → R3 → Server
- **B.** Home → R2 → R4 → Server
- **C.** Home → R3 → Server
- **D.** Home → R1 → R4 → Server

<a id="q70"></a>**70.** `[2.4.4]` Someone changes Rover's report from "12 cm" to "2 cm" on the way. Which security property was broken? *(Choose ONE answer.)*

- **A.** Privacy
- **B.** Authentication
- **C.** Integrity
- **D.** Non-repudiation

<a id="q71"></a>**71.** `[2.1.2]` A university must connect two buildings 2 km apart with a very fast link that is not disturbed by electrical noise from nearby machines. Which transmission medium fits best? *(Choose ONE answer.)*

- **A.** Twisted-pair copper cable
- **B.** Fibre-optic cable
- **C.** Wi-Fi radio waves
- **D.** Infrared

### Chapter 2 · Part C – Open-ended

*Write a developed answer (normally more than 100 words), using examples, a diagram or worked steps. Each question is worth 10 points.*

<a id="q72"></a>**72.** `[2.3.2]` Compare TCP and UDP. Then decide which protocol is better for (a) Rover's obstacle report and (b) a live video call. Justify both decisions.

<a id="q73"></a>**73.** `[2.3]` Explain step by step what happens from the moment you type https://www.example.com into a browser until the page appears on the screen. Use the terms DNS, IP address, TCP handshake, HTTPS, router and server.

<a id="q74"></a>**74.** `[2.4]` Rover sends its reports to a phone through home Wi-Fi. Write a simple security plan for this system. Explain how firewalls, privacy (encryption), authentication, integrity and non-repudiation each protect Rover's reports, and give one real risk for each idea.

## Chapter 3 – Behaviorist AI

*Study Guide: [Chapter 3 – Behaviorist AI](../03-Study-guide/03-Behaviorist-AI.md)*

### Chapter 3 · Part A – True / False

*Write True or False. If a statement is false, correct it.*

<a id="q75"></a>**75.** `[3.1]` In classical conditioning, Pavlov's dogs learned to salivate at the sound of a bell after the bell had been paired with food many times.

<a id="q76"></a>**76.** `[3.1]` Negative reinforcement is a kind of punishment.

<a id="q77"></a>**77.** `[3.1]` In Skinner's operant conditioning, a consequence that follows an action changes how often the action is repeated.

<a id="q78"></a>**78.** `[3.2]` A reactive agent builds a detailed map of the room and plans its whole route before it moves.

<a id="q79"></a>**79.** `[3.2]` An ultrasonic sensor calculates distance as (343 m/s × echo time) ÷ 2, because the sound travels to the obstacle and back.

<a id="q80"></a>**80.** `[3.3]` Behaviors are ranked 1, 2 and 3, and rank 1 is given to the most important behavior. When the rank-1 and rank-3 behaviors are both active, the rank-3 behavior controls the motors.

<a id="q81"></a>**81.** `[3.3]` Hysteresis uses two thresholds, for example entering Avoid below 20 cm and leaving it only above 30 cm, to stop the robot from switching back and forth.

<a id="q82"></a>**82.** `[3.4]` In Brooks's subsumption architecture, higher layers switch off the lower layers completely.

<a id="q83"></a>**83.** `[3.5]` In the case-study robot, the Avoid behavior runs on the robot itself and does not depend on Wi-Fi.

<a id="q84"></a>**84.** `[3.6]` In reinforcement learning, the reward is a number chosen by the designer, and the robot does not feel pleasure or pain.

### Chapter 3 · Part B – Multiple choice

*Choose the answer(s) shown in brackets after each question.*

<a id="q85"></a>**85.** `[3.1]` A car's seat-belt warning sound stops when you buckle up, so you buckle up more quickly next time. Which type of consequence is this? *(Choose ONE answer.)*

- **A.** Positive reinforcement
- **B.** Negative reinforcement
- **C.** Positive punishment
- **D.** Negative punishment

<a id="q86"></a>**86.** `[3.2]` Which three parts make up the sense–act loop of a robot? *(Choose ONE answer.)*

- **A.** Sensor, controller, actuator
- **B.** Keyboard, monitor, printer
- **C.** Map, plan, route
- **D.** Router, switch, modem

<a id="q87"></a>**87.** `[3.2]` An ultrasonic sensor measures an echo time of 1,166 µs. About how far away is the obstacle? *(Choose ONE answer.)*

- **A.** 10 cm
- **B.** 20 cm
- **C.** 40 cm
- **D.** 2 m

<a id="q88"></a>**88.** `[3.3]` The robot has Avoid (rank 1: distance < 20 cm), Go to light (rank 2) and Wander (rank 3). The distance is 12 cm and bright light is ahead. Which behavior controls the motors? *(Choose ONE answer.)*

- **A.** Wander
- **B.** Go to light
- **C.** Avoid
- **D.** No behavior, because two rules conflict

<a id="q89"></a>**89.** `[3.3]` Which of these situations make the Avoid behavior (distance < 20 cm) active? *(Choose ALL correct answers.)*

- **A.** Distance 15 cm, no light
- **B.** Distance 80 cm, bright light
- **C.** Distance 12 cm, bright light
- **D.** Distance 25 cm, no light

<a id="q90"></a>**90.** `[3.3]` A robot near stairs has a cliff sensor. Which behavior should get rank 1? *(Choose ONE answer.)*

- **A.** Wander
- **B.** Go to light
- **C.** Cliff stop
- **D.** Avoid obstacles

<a id="q91"></a>**91.** `[3.4]` In Brooks's subsumption architecture for a mobile robot, which behavior is in the lowest layer (Level 0)? *(Choose ONE answer.)*

- **A.** Explore
- **B.** Wander
- **C.** Avoid obstacles
- **D.** Plan a route

<a id="q92"></a>**92.** `[3.5]` The robot moves at 0.3 m/s. If a stop decision is made on a phone and takes 1 second to arrive over Wi-Fi, how far does the robot travel before it reacts? *(Choose ONE answer.)*

- **A.** 1.5 cm
- **B.** 6 cm
- **C.** 20 cm
- **D.** 30 cm

<a id="q93"></a>**93.** `[3.5]` Which design ideas protect the case-study robot when the network is slow or fails? *(Choose ALL correct answers.)*

- **A.** Avoid runs locally on the robot
- **B.** Remote drive commands expire after a timeout
- **C.** A remote DRIVE command is allowed to override Avoid
- **D.** A remote STOP command is allowed to win, because stopping is safe

<a id="q94"></a>**94.** `[3.6]` A robot updates its estimate with: `new = old + 0.5 × (reward − old)`. The estimate for 'late' is −5 and the robot gets a reward of +1. What is the new estimate? *(Choose ONE answer.)*

- **A.** −4
- **B.** −2
- **C.** 0.5
- **D.** 1

### Chapter 3 · Part C – Open-ended

*Write a developed answer (normally more than 100 words), using examples, a diagram or worked steps. Each question is worth 10 points.*

<a id="q95"></a>**95.** `[3.1–3.2]` Explain why the term "Behaviorist AI" is an analogy. Compare classical conditioning (Pavlov) and operant conditioning (Skinner) with a robot that uses behavior rules, and describe at least one important difference between an animal and a robot.

<a id="q96"></a>**96.** `[3.3]` A robot has three behaviors: Avoid (rank 1: IF distance < 20 cm THEN stop and turn right), Go to light (rank 2) and Wander (rank 3: always active). Trace what the robot does at distances of 80 cm (no light), 45 cm (light), 15 cm (light) and 70 cm (light). Then explain what goes wrong if the engineer gives Go to light a higher priority than Avoid, and why safety behaviors usually get rank 1.

<a id="q97"></a>**97.** `[3.5–3.7]` Evaluate the robot design in which the robot sends sensor data to a phone over Wi-Fi and the phone decides when to stop. Use the latency calculation (robot speed 0.3 m/s, 20 cm safety distance) to support your answer. Then propose a better design and describe one limit of purely reactive robots.

---

## Answer Key

*Check your answers only after you have tried the questions. Each answer links back to its question.*

### Answers – Chapter 1 – Hardware

#### Chapter 1 · Part A – True / False

**1. True.** The ALU performs arithmetic operations (add, subtract, multiply, divide), logic operations (NOT, AND, OR, XOR) and shift operations. [↩ Q1](#q1)

**2. False.** The Program Counter holds the address of the next instruction to fetch. The Instruction Register holds the instruction the CPU is currently processing. [↩ Q2](#q2)

**3. True.** 0011 represents 3 and 0110 represents 6. A left shift by one position multiplies the value by two, as long as the result fits in the available bits. [↩ Q3](#q3)

**4. True.** A bit is a single 0 or 1, and eight bits form one byte. For example, 00000101 represents 5. [↩ Q4](#q4)

**5. False.** ROM is nonvolatile, so it keeps its contents when the power is turned off. RAM is the memory that is normally volatile. [↩ Q5](#q5)

**6. False.** Cache does not replace RAM. It works together with RAM and keeps copies of data and instructions the CPU is likely to need soon. [↩ Q6](#q6)

**7. False.** An SSD stores information electronically using flash memory and has no spinning disks. An HDD is the device that stores information magnetically on spinning disks. [↩ Q7](#q7)

**8. False.** RAM helps the computer work with running programs. Space for installing games depends on secondary storage (SSD/HDD). [↩ Q8](#q8)

**9. True.** The Address Bus carries the location, the Data Bus carries the actual data, and the Control Bus carries signals such as read or write. [↩ Q9](#q9)

**10. True.** Average voltage = duty cycle × supply voltage = 0.50 × 5 V = 2.5 V. This is the *average voltage*. The motor runs slower than at 100 %, but its speed is not exactly half, because friction and the load on the wheel also matter. [↩ Q10](#q10)

**11. True.** In a stored-program computer, programs are kept in memory like data, so the same hardware can run a different program simply by loading new instructions. Older machines had to be rewired to change their task. [↩ Q11](#q11)

**12. False.** A device that turns a computer signal into a physical action is an actuator. A sensor does the opposite: it measures the world and turns the measurement into a signal. [↩ Q12](#q12)

**13. True.** Quantization rounds each sample to the nearest whole number, for example 2.2 becomes 2 and 5.7 becomes 6. [↩ Q13](#q13)

**14. True.** Samples taken between measurements are never recorded, so a rapidly changing signal needs more samples per second than a smooth one. [↩ Q14](#q14)

**15. True.** A microcontroller combines a CPU, memory and connection pins on one chip and runs one dedicated program. [↩ Q15](#q15)

**16. False.** The sound travels to the wall and back, so the time must be divided by 2: 343 × 0.001166 ÷ 2 = 0.2 m = 20 cm. Without the division the result (0.4 m) is twice too large. [↩ Q16](#q16)

**17. False.** 20 is not more than 20, so the jump does not happen. The program continues to address 04 and the robot stops and turns. [↩ Q17](#q17)

**18. False.** A bumper switch is a digital sensor: it is either pressed (1) or not pressed (0). A light sensor is an example of an analog sensor. [↩ Q18](#q18)

**19. False.** A pin supplies only a tiny current (about 20 mA is recommended on an Arduino Uno), while a motor can need hundreds of milliamps. A motor driver must switch the battery current. [↩ Q19](#q19)

**20. False.** It is the other way round: setup() runs once when the power comes on, and loop() repeats forever. [↩ Q20](#q20)

**21. False.** 100 readings at 20 per second take 5 seconds. The average then describes the past, and the robot can drive 150 cm in that time. Averaging a few readings helps; averaging too many makes the robot react too late. [↩ Q21](#q21)

#### Chapter 1 · Part B – Multiple choice

**22. B.** The CPU processes instructions, main memory temporarily stores the information in use, and the I/O subsystem lets us interact with the computer. Keyboard, mouse and monitor are devices; RAM, ROM and cache are types of memory; buses connect the subsystems. [↩ Q22](#q22)

**23. C.** AND gives 1 only when both inputs are 1. OR gives 1 when at least one input is 1, XOR gives 1 when the inputs are different, and NOT changes a single input. [↩ Q23](#q23)

**24. B.** The Program Counter holds the address of the instruction to fetch; the fetched instruction itself is placed in the Instruction Register. [↩ Q24](#q24)

**25. B.** The Control Unit interprets the instruction and coordinates the other parts. The ALU only performs the calculation later, in the execute stage. [↩ Q25](#q25)

**26. C.** Registers are inside the CPU and are the fastest and smallest; cache is small and fast; RAM is much larger but slower. [↩ Q26](#q26)

**27. A, B, D.** The Control Bus carries signals that coordinate operations, such as read or write, not the numbers being added. Numbers travel on the Data Bus. [↩ Q27](#q27)

**28. A, B, D.** SSD, HDD and flash memory are nonvolatile. RAM is normally volatile and loses its contents without power. [↩ Q28](#q28)

**29. D.** 2¹⁰ = 1,024 different values, from 0 to 1023. 1,023 is the largest value, not the number of values. [↩ Q29](#q29)

**30. C.** The robot is not moving, and all the other readings are close to 20 cm, so 34 cm is unwanted variation (noise) (Activity 8). [↩ Q30](#q30)

**31. B.** Flash memory stores the program and keeps it without power. RAM holds variables while the program runs and loses them when the battery is removed. [↩ Q31](#q31)

**32. C.** A wheel motor changes the world by moving the robot. A camera, a gyroscope and a microphone all measure the world, so they are sensors. [↩ Q32](#q32)

**33. B (110).** 5.7 rounds to 6, and 6 = 4 + 2 is written 110 in 3 bits. A (101) is 5, which is what you get by rounding down instead of to the nearest value. C (111) is 7. D (011) is 3. [↩ Q33](#q33)

**34. A, C, E.** A is the definition. C and E describe typical embedded systems. B describes a general-purpose computer, and D is wrong because a microcontroller usually has no screen or keyboard and talks to the world through sensors and actuators. [↩ Q34](#q34)

**35. B.** 343 × 0.002332 = 0.8 m, and 0.8 ÷ 2 = 0.4 m = 40 cm. Choice C (80 cm) comes from forgetting to divide by 2. A and D do not match the calculation. [↩ Q35](#q35)

**36. A.** 1749 ÷ 58 = 30 (decimals ignored). 30 is more than 20, so the robot drives forward. B reverses the rule. C ignores the division. D confuses 30 with the threshold. [↩ Q36](#q36)

**37. B.** The robot first measures (sense), then compares and chooses (decide), then moves (act), and then repeats because the world has changed. [↩ Q37](#q37)

**38. B.** Time between readings = 1 ÷ 10 = 0.1 s, and 30 cm/s × 0.1 s = 3 cm. C (30 cm) is the distance for one whole second. [↩ Q38](#q38)

**39. B.** Swapping IN1 and IN2 reverses the current through the motor, so it turns backward. With both at 0 it would stop. [↩ Q39](#q39)

**40. B.** A servo motor turns to a chosen angle and holds it. A DC motor spins continuously; a speaker and a sensor are not suitable. [↩ Q40](#q40)

**41. A, B, C, E.** A microcontroller has a CPU, flash, RAM, an ADC, timers and pins on one chip. D describes a laptop or PC, not a microcontroller. [↩ Q41](#q41)

**42. C.** The left wheel travels faster, so the robot turns toward the slower right side. Equal speeds would drive straight (A). [↩ Q42](#q42)

**43. C.** 100 cm × 58 = 5800 µs. A (1740 µs) matches 30 cm, B (2900 µs) matches 50 cm, and D is ten times too large. [↩ Q43](#q43)

#### Chapter 1 · Part C – Open-ended

**44.** The Fetch–Decode–Execute cycle [↩ Q44](#q44)

*Key points:*

- Fetch: the Program Counter holds the address of the next instruction. The address travels on the Address Bus, the Control Bus signals a read, and the instruction comes back on the Data Bus. It is placed in the Instruction Register, and the CPU normally moves on to the next instruction.
- Decode: the Control Unit interprets the instruction in the Instruction Register and decides which operation is required (for example LOAD, ADD or STORE).
- Execute: LOAD 5 into Register A and LOAD 3 into Register B; for ADD, the Control Unit tells the ALU to add, and the ALU produces 8 in Register C; STORE writes 8 to memory address 20 (address on the Address Bus, write signal on the Control Bus, value on the Data Bus).
- Why it repeats: a program is a sequence of instructions stored in memory. After one instruction is completed, the CPU fetches the next one, until an instruction such as HALT stops the program. Jump instructions can change which instruction comes next.
- Good answers use the LOAD / ADD / STORE / HALT program from Section 1.6.3 and show the cycle as a loop.

**Marking guide (10 points):** 2 points for each key point above (up to 10). Other well-reasoned answers can earn full marks.

**45.** Why a computer needs registers, cache, RAM and an SSD [↩ Q45](#q45)

*Key points:*

- Registers: tiny storage inside the CPU, the fastest and smallest; they hold the values being used right now (for example 5 and 3 before the ALU adds them).
- Cache: small, fast memory holding copies of data and instructions the CPU is likely to need soon; it works with RAM and does not replace it.
- RAM: much larger but slower working memory for running programs; normally volatile.
- SSD: long-term storage for programs and files; much larger and generally slower than RAM; nonvolatile.
- Why not one big memory: faster memory costs more and cannot easily be made very large, so computers combine small fast memory with large slower storage.
- Example: a document saved to the SSD can be opened again after a power failure; unsaved changes that exist only in RAM are lost.

**Marking guide (10 points):** 1 point for each key point above (up to 6). Up to 4 more points for a clear, well-organised answer that uses a correct example or calculation. Other well-reasoned answers can earn full marks.

**46.** Controlling a wheel motor [↩ Q46](#q46)

*Key points:*

- PWM: the digital pin switches fully on and off very quickly, and the motor reacts to the average. The duty cycle is the fraction of time the pin is on; more on-time means more speed, although the speed is not exactly proportional to the average voltage (friction and load).
- Calculation: average voltage = duty cycle × supply voltage = 0.75 × 6 V = 4.5 V (on an Arduino, an analogWrite value of about 191).
- H-bridge: four switches around the motor; closing one diagonal pair sends the current one way, the other pair reverses it. IN1 = 1, IN2 = 0 → forward; IN1 = 0, IN2 = 1 → backward; IN1 = 0, IN2 = 0 → stop.
- Motor driver: a pin can supply only a tiny current (about 20 mA recommended on an Arduino Uno), but a motor needs hundreds of milliamps; the driver switches the large battery current using the small control signals.
- Direct connection: the motor gets too little power to turn, and the attempt can overload the pin and disturb the microcontroller's power supply, so it may keep restarting.

**Marking guide (10 points):** 2 points for each key point above (up to 10). Other well-reasoned answers can earn full marks.

**47.** [↩ Q47](#q47)

*Key points:*

- (a) The program forgets to divide by 2. The echo time covers the path to the wall and back, so 343 × echo time gives twice the real distance.
- (b) The program believes the wall is twice as far away as it is. It turns only when the calculated distance is 20 cm or less, which means the real distance is about 10 cm.
- (c) Fix: distance = 343 × echo time ÷ 2. A further safety change: raise the threshold (for example to 30 cm), so the robot has room to turn, or check the sensor more often.

**Marking guide (10 points):** (a) 3 points, (b) 4 points, (c) 3 points. Give part marks when the idea is right but the calculation or explanation is incomplete.

*Sample answer:* The student forgot that the sound pulse travels to the wall and then back to the sensor. The measured echo time therefore covers the distance twice. Multiplying the speed of sound by the echo time gives the length of the whole round trip, not the distance to the wall. Because the program does not divide by 2, it always believes that the wall is twice as far away as it really is. The robot turns only when its calculated distance falls to 20 cm, and that happens when the wall is really only about 10 cm away. At that point the robot may not have enough room to stop and turn, so it hits the wall. To fix the program, the calculation must be distance = 343 m/s × echo time ÷ 2. For example, an echo time of 1166 µs gives 343 × 0.001166 ÷ 2 = 0.2 m, which is 20 cm. To make the robot safer, the student could also raise the threshold to 30 cm, so that the robot reacts earlier and has more space to turn. Other valid improvements, such as measuring more often, should also be accepted if they are explained.

**48.** [↩ Q48](#q48)

*Key points:*

- (a) Sensor: a light sensor measures how bright the room is. Computing part: a microcontroller runs the program. Actuator: the lamp (or a switch for the lamp) turns light on and off.
- (b) Sense: measure the brightness and convert it into a number. Decide: compare the number with a threshold. Act: switch the lamp on or off. Repeat: the light level changes during the day and when the lamp itself is on, so the loop must keep checking.
- (c) The job is one dedicated task that needs little computing power. A microcontroller is small, cheap, uses little power, has pins to connect a sensor and a lamp directly, and needs no screen, keyboard or large operating system.

**Marking guide (10 points):** (a) 3 points, (b) 4 points, (c) 3 points. Give part marks when the idea is right but the calculation or explanation is incomplete.

*Sample answer:* I would use a light sensor as the sensor, a microcontroller as the computing part, and the lamp, switched through a small driver circuit, as the actuator. The light sensor measures how bright the room is and turns the brightness into an electrical signal. The microcontroller converts that signal into a number by sampling and rounding it, and then runs a program that compares the number with a threshold. If the number is below the threshold, the room is dark, so the program tells the lamp to switch on. If the number is above the threshold, the program switches the lamp off. This is the sense–decide–act loop. The loop must repeat all the time because the brightness changes during the day, and the lamp itself changes how bright the room is. A microcontroller suits this job better than a laptop processor because the task is simple and never changes. A microcontroller is small, cheap and uses very little power, so the light can stay on all year. It has connection pins for the sensor and the lamp, and it does not need a screen, a keyboard or a large operating system. A laptop processor is designed for many different programs and would be a waste of money and energy here.

**49.** [↩ Q49](#q49)

*Key points:*

- (1) Two readings per second means 0.5 s between readings, so the robot drives 30 cm/s × 0.5 s = 15 cm "blind", most of its 20 cm safety distance. Fix: read the sensor much more often, for example 20 times per second (1.5 cm between readings).
- (2) A microcontroller pin cannot supply the current a motor needs. The motor barely turns and the overload can disturb the microcontroller's supply, so it restarts. Fix: use a motor driver (H-bridge) that switches the battery current.
- (3) Averaging 50 readings at 2 per second covers 25 seconds, so the distance is badly out of date. Fix: average only a few readings (for example 3), or use two thresholds (hysteresis).

**Marking guide (10 points):** (1) 3 points, (2) 4 points, (3) 3 points. Give part marks when the idea is right but the calculation or explanation is incomplete.

*Sample answer:* The first problem is the sampling rate. If the sensor is read only twice per second, there are 0.5 seconds between readings. At 30 cm per second the robot drives 30 × 0.5 = 15 cm without any new information, which is most of its 20 cm safety distance. A wall that was 30 cm away at one reading can be only 15 cm away at the next, or the robot can hit it before it reacts. The fix is to read the sensor far more often; at 20 readings per second the robot moves only 1.5 cm between readings. The second problem is the motor connection. A microcontroller pin can only supply a very small current, about 20 milliamps on an Arduino Uno, but a wheel motor needs much more. The motor gets too little power and the overloaded pin can pull down the microcontroller's supply, which explains why it restarts. The motor must be connected through a motor driver with an H-bridge, which switches the battery current and also allows forward and backward driving. The third problem is the averaging. At two readings per second, 50 readings cover 25 seconds, so the average describes where the wall was long ago. The robot reacts to the past instead of the present. A better solution is to average only the last three readings, or to use two thresholds so that small noise near the limit does not make the robot switch back and forth.

### Answers – Chapter 2 – Networks

#### Chapter 2 · Part A – True / False

**50. True.** A LAN is a local network, such as home Wi-Fi or a school computer lab. [↩ Q50](#q50)

**51. True.** In P2P all devices are equal; in client–server, central servers provide services. [↩ Q51](#q51)

**52. False.** A hub copies data to all ports. A switch is the device that sends data only to the correct port, using MAC addresses. [↩ Q52](#q52)

**53. True.** OSI: Physical to Application (7). TCP/IP: Link, Internet, Transport, Application (4). [↩ Q53](#q53)

**54. False.** The Internet is the whole infrastructure (cables, routers, servers, protocols). The Web is only one service that runs on it, using HTTP/HTTPS. [↩ Q54](#q54)

**55. True.** This is the TCP three-way handshake (Figure 2.6). [↩ Q55](#q55)

**56. False.** Each of the four numbers in an IPv4 address must be between 0 and 255, so 300 is not allowed. [↩ Q56](#q56)

**57. True.** DHCP also gives the subnet mask, default gateway and DNS server, using the DORA steps. [↩ Q57](#q57)

**58. False.** Each router only decides the next hop, using its routing table. The packet reaches the destination hop by hop. [↩ Q58](#q58)

**59. False.** Authentication checks who a user or device is. Protecting data from being changed is integrity. [↩ Q59](#q59)

**60. False.** A web server sends web pages (HTTPS, port 443). A database server stores organised data, for example the articles, and the web or application server asks it for that data. [↩ Q60](#q60)

#### Chapter 2 · Part B – Multiple choice

**61. A, B.** A PAN connects personal devices around one person, usually with Bluetooth or USB. Undersea cables and city-to-city fibre are used for WANs and GANs. [↩ Q61](#q61)

**62. B.** A switch (Layer 2) uses MAC addresses. A hub copies data to every port. [↩ Q62](#q62)

**63. C.** OSI layers 5, 6 and 7 together match the TCP/IP Application layer (Figure 2.5). [↩ Q63](#q63)

**64. C.** TCP is connection-oriented and reliable. UDP is fast but does not resend; IP addresses and moves packets; ICMP reports errors. [↩ Q64](#q64)

**65. B.** TCP uses the numbers to find the missing piece and asks for only that packet again (Quick check 5). [↩ Q65](#q65)

**66. A, C.** Private ranges are 10.x.x.x, 172.16–172.31.x.x and 192.168.x.x. 172.40.4.1 is outside 172.16–172.31, and 8.8.8.8 is public. [↩ Q66](#q66)

**67. B.** https is the protocol, mail is the subdomain, google is the second-level domain and .com is the TLD. [↩ Q67](#q67)

**68. B.** DNS works like a phone book: it translates the domain name into the server's IP address. [↩ Q68](#q68)

**69. B, D.** Any path through R3 is broken, and there is no direct Home–R3 link. Both paths through R4 still work, which shows why several paths make the network reliable. [↩ Q69](#q69)

**70. C.** Integrity means data is not changed on the way. Hashes and digital signatures help the receiver detect such changes. [↩ Q70](#q70)

**71. B.** Fibre-optic cable carries light, so it is fast over long distances and is not affected by electrical interference. Twisted-pair Ethernet is limited to about 100 m per cable; Wi-Fi and infrared have a short range and can be disturbed or blocked. [↩ Q71](#q71)

#### Chapter 2 · Part C – Open-ended

**72.** Compare TCP and UDP [↩ Q72](#q72)

*Key points:*

- TCP: connection-oriented, three-way handshake (SYN, SYN-ACK, ACK), numbering, error checking, resending, correct order; slower because of overhead.
- UDP: connectionless, no handshake, no resending; fast and lightweight.
- (a) Rover's report: TCP, because every word matters – a missing "12" or "LEFT" would make the report wrong or dangerous.
- (b) Live video: UDP, because speed matters more than perfect delivery; a late frame is useless, so resending it would only add delay.
- Good answers mention reliability vs. speed as a trade-off.

**Marking guide (10 points):** 2 points for each key point above (up to 10). Other well-reasoned answers can earn full marks.

**73.** From typing a web address to seeing the page [↩ Q73](#q73)

*Key points:*

- Browser reads the domain parts (protocol, subdomain, second-level domain, TLD).
- Device asks a DNS server; DNS returns the IP address of the web server.
- TCP connection is opened with the three-way handshake (SYN, SYN-ACK, ACK).
- Browser sends an HTTPS request (encrypted) to the server, normally port 443.
- Data is split into packets; routers forward them hop by hop using IP addresses and routing tables.
- Web server processes the request and sends the page back in packets.
- Browser receives the packets, TCP puts them in order, and the page is shown.
- The device's own IP address may have been given earlier by DHCP.

**Marking guide (10 points):** 1 point for each key point above (up to 8). Up to 2 more points for a clear, well-organised answer that uses a correct example or calculation. Other well-reasoned answers can earn full marks.

**74.** A security plan for Rover [↩ Q74](#q74)

*Key points:*

- Firewall: allow only the needed traffic (for example, Rover's address to the app's port 443) and block unknown ports from the Internet.
- Privacy: send reports over HTTPS/TLS so other people on the Wi-Fi cannot read them.
- Authentication: Rover and the phone prove their identity (certificate, token, password), so a fake device cannot pretend to be Rover.
- Integrity: hashes or digital signatures show if "12 cm" was changed to "2 cm".
- Non-repudiation: digital signatures and logs prove which device sent which report.
- Conclusion: one measure is not enough; combining them gives defence in depth.

**Marking guide (10 points):** 1 point for each key point above (up to 6). Up to 4 more points for a clear, well-organised answer that uses a correct example or calculation. Other well-reasoned answers can earn full marks.

### Answers – Chapter 3 – Behaviorist AI

#### Chapter 3 · Part A – True / False

**75. True.** The bell (at first a neutral stimulus) became a signal that predicts food, so it started to cause salivation by itself. [↩ Q75](#q75)

**76. False.** Negative reinforcement makes a behavior more likely by removing something unpleasant (for example, a seat-belt warning sound stops). Punishment makes a behavior less likely. [↩ Q76](#q76)

**77. True.** For example, a rat that receives food after pressing a lever presses the lever more and more often. [↩ Q77](#q77)

**78. False.** A reactive agent chooses its action using only current sensor information, like a reflex. Building a map and planning is the approach of symbolic ("think first") systems. [↩ Q78](#q78)

**79. True.** The echo time covers the trip to the wall and back again, so the distance to the wall is half of what the sound covers. [↩ Q79](#q79)

**80. False.** Rank 1 is the highest priority, so the rank-1 behavior controls the motors. The highest-priority active behavior always wins; a larger number means a lower priority. [↩ Q80](#q80)

**81. True.** With one threshold, noisy readings around 20 cm make the behavior flicker. With two thresholds, the behavior changes only once. [↩ Q81](#q81)

**82. False.** Lower layers keep running. Higher layers only suppress (replace an input signal) or inhibit (block an output) at the points where they are wired in. [↩ Q82](#q82)

**83. True.** Safety is local: Avoid uses only the robot's own sensor and microcontroller, because network messages can be delayed or lost. [↩ Q83](#q83)

**84. True.** The link to behaviorism is an analogy. The reward is simply a number that the learning algorithm tries to make as large as possible over time. [↩ Q84](#q84)

#### Chapter 3 · Part B – Multiple choice

**85. B.** Something unpleasant (the sound) is removed, and the behavior becomes more likely, which is negative reinforcement. [↩ Q85](#q85)

**86. A.** The sensor measures, the controller (microcontroller) applies a rule, and the actuator (for example a motor) acts. The action changes the world, and the robot senses again. [↩ Q86](#q86)

**87. B.** 343 m/s × 0.001166 s ≈ 0.40 m for the trip there and back; half of that is about 0.20 m = 20 cm. [↩ Q87](#q87)

**88. C.** Avoid, Go to light and Wander are all active, and the highest-priority active behavior (Avoid) wins. The robot stops and turns right. [↩ Q88](#q88)

**89. A, C.** A behavior is active when its condition is true. Avoid depends only on the distance being below 20 cm; light does not matter for it. [↩ Q89](#q89)

**90. C.** Falling down the stairs is the most harmful failure, so Cliff stop gets the highest rank; Avoid moves to rank 2. [↩ Q90](#q90)

**91. C.** Level 0 avoids obstacles, Level 1 wanders and Level 2 explores. Planning a route is not a layer in this design. [↩ Q91](#q91)

**92. D.** 0.3 m/s × 1 s = 0.3 m = 30 cm, which is more than the 20 cm safety distance. A decision on the robot itself (about 50 ms) means only 1.5 cm. [↩ Q92](#q92)

**93. A, B, D.** A remote DRIVE must never beat Avoid, because driving into an obstacle is not safe. The other three ideas make the robot fail safe. [↩ Q93](#q93)

**94. B.** −5 + 0.5 × (1 − (−5)) = −5 + 0.5 × 6 = −5 + 3 = −2. [↩ Q94](#q94)

#### Chapter 3 · Part C – Open-ended

**95.** Behaviorism and Behaviorist AI [↩ Q95](#q95)

*Key points:*

- Behaviorism studies observable behavior: stimulus in, response out, without looking inside the "black box".
- **Classical conditioning:** two events become linked (bell + food → bell alone causes salivation).
- **Operant conditioning:** consequences change how often an action is repeated (reinforcement and punishment).
- A behavior-based robot also links situations (sensor conditions) to responses (actions) without a model of the world.
- **Difference:** the robot's rules are written by an engineer (or learned from reward numbers); the robot does not feel, want or understand anything.
- So the name borrows an idea from psychology; it does not apply psychology to machines.

**Marking guide (10 points):** 1 point for each key point above (up to 6). Up to 4 more points for a clear, well-organised answer that uses a correct example or calculation. Other well-reasoned answers can earn full marks.

**96.** Priorities and conflicts [↩ Q96](#q96)

*Key points:*

- **80 cm, no light:** only Wander is active → moves forward.
- **45 cm, light:** Go to light and Wander active → Go to light wins.
- **15 cm, light:** Avoid, Go to light and Wander active → Avoid wins (stops and turns right).
- **70 cm, light:** Go to light wins again.
- If Go to light outranks Avoid, the robot drives towards the light even when an obstacle (for example a glass wall) is closer than 20 cm and crashes.
- Safety behaviors prevent the most harmful failure, so they get the highest rank; ranking is a design decision that must be explained.

**Marking guide (10 points):** 1 point for each key point above (up to 6). Up to 4 more points for a clear, well-organised answer that uses a correct example or calculation. Other well-reasoned answers can earn full marks.

**97.** Safety in a networked robot [↩ Q97](#q97)

*Key points:*

- Network messages can be delayed, lost or disconnected.
- 0.2 s delay → 6 cm; 1 s delay → 30 cm, which is more than the 20 cm safety distance, so the robot would hit the obstacle.
- **Better:** keep Avoid on the robot (about 50 ms → 1.5 cm); use the network for telemetry and non-critical commands.
- Remote commands should expire (timeout); a remote STOP may win, a remote DRIVE must not beat Avoid; the robot should fail safe.
- **Limit of reactive robots:** no memory or planning, so they can get trapped (for example circling the edge of a room or stuck in a corner); hybrid systems add planning on top of reactive safety.

**Marking guide (10 points):** 2 points for each key point above (up to 10). Other well-reasoned answers can earn full marks.

---

## Appendix: old question numbers

Stage 2 numbered each chapter from 1 again, so "Q13" was ambiguous. Use this table to update references in the slides and videos (for example, the echo-time question that was "Chapter 3, Q13" in Stage 2 is now **Q87**).

| Source | Old numbers → new numbers |
|---|---|
| Stage 2 Test Bank, Chapter 1 (Hardware) | 1 → 1, 2 → 2, 3 → 3, 4 → 4, 5 → 5, 6 → 6, 7 → 7, 8 → 8, 9 → 9, 10 → 10, 11 → 22, 12 → 23, 13 → 24, 14 → 25, 15 → 26, 16 → 27, 17 → 28, 18 → 29, 19 → 30, 20 → 31, 21 → 44, 22 → 45, 23 → 46 |
| Networks Test Bank V2.0 | 1 → 50, 2 → 51, 3 → 52, 4 → 53, 5 → 54, 6 → 55, 7 → 56, 8 → 57, 9 → 58, 10 → 59, 11 → 61, 12 → 62, 13 → 63, 14 → 64, 15 → 65, 16 → 66, 17 → 67, 18 → 68, 19 → 69, 20 → 70, 21 → 72, 22 → 73, 23 → 74 |
| Stage 2 Test Bank, Chapter 3 (Behaviorist AI) | 1 → 75, 2 → 76, 3 → 77, 4 → 78, 5 → 79, 6 → 80, 7 → 81, 8 → 82, 9 → 83, 10 → 84, 11 → 85, 12 → 86, 13 → 87, 14 → 88, 15 → 89, 16 → 90, 17 → 91, 18 → 92, 19 → 93, 20 → 94, 21 → 95, 22 → 96, 23 → 97 |
| Section 1.7 draft (Merey) | S7-TF1 → 12, S7-TF2 → 13, S7-TF3 → 14, S7-TF4 → 15, S7-TF5 → 16, S7-TF6 → 17, S7-TF7 → 18, S7-TF10 → 19, S7-TF11 → 20, S7-TF12 → 21, S7-MC1 → 32, S7-MC2 → 33, S7-MC3 → 34, S7-MC4 → 35, S7-MC5 → 36, S7-MC6 → 37, S7-MC7 → 38, S7-MC8 → 39, S7-MC9 → 40, S7-MC10 → 41, S7-MC11 → 42, S7-MC12 → 43, S7-OE1 → 47, S7-OE2 → 48, S7-OE3 → 49 |

New in Stage 3 (to cover sections that had no question): Q11 [1.6.1], Q60 [2.3.6], Q71 [2.1.2].

Two draft questions from Section 1.7 (S7-TF8 and S7-TF9) were not included because they repeat Q29 (10-bit values) and Q10 (PWM average voltage).
