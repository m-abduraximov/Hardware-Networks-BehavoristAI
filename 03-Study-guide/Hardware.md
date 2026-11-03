
# Chapter 2: Hardware

## Goals

To help students understand the basic parts of a computer, how they work together, and how hardware allows a robot to interact with the real world.

## Learning Objectives

By the end of this part, students will be able to:

- Identify the main hardware components of a computer, including CPU, memory, storage, input/output devices, and buses, and explain their basic roles.
- Explain the stored-program concept in simple words.
- Describe the fetch–decode–execute cycle and how the CPU follows instructions.
- Explain the role of controllers and how different hardware components work together.
- Describe how sensors, actuators, and microcontrollers help a robot receive information, process it, and perform actions.
- Briefly introduce GPUs, AI accelerators, and the history of computer hardware.
- Explain the difference between a sensor and an actuator, and give examples of each.
- Explain what a microcontroller is and how it differs from a normal computer.
- Describe the sense–decide–act loop of a simple robot.
- Trace how an obstacle-avoiding robot uses an ultrasonic sensor, a microcontroller, and motors.

---

## 1. Introduction to Computer Hardware

### Goal

To introduce the three main subsystems of a computer before studying them separately.

### 1.1 Main Computer Subsystems

If we divide a computer into parts, we will get three broad categories or subsystems which make a computer work. These are the **Central Processing Unit (CPU)**, the **Main Memory**, and the **Input/Output subsystem**.

Each of these subsystems has its own responsibility. The CPU is responsible for processing instructions and performing calculations, while the main memory temporarily stores information which the computer is currently using. The Input/Output subsystem allows us to interact with the computer by receiving information or showing the results.

#### Example: Using a Calculator

*[ADDED — Practical example]*

For example, imagine that you are using a calculator on your computer. When you type a number on your keyboard, the computer receives this information through an input device. After that, the CPU processes the information and the result appears on your monitor.

During this process, the computer also uses its main memory to keep the information it needs.

### 1.2 How the Subsystems Work Together

Although each subsystem has its own responsibility, they cannot do everything independently.

For example, the CPU is capable of performing calculations, but without memory it would not have the instructions and data needed to perform them. The same can be said about input and output devices, because without them it would be much harder for us to interact with the computer.

*[ADDED — Diagram: Show a keyboard connected to the computer, with CPU and Main Memory connected by arrows, and a monitor displaying the result.]*

#### Activity 1: Follow a Keyboard Input

*[ADDED — Activity for reinforcing the material]*

Imagine that you type the number 7 on a keyboard and a calculator app shows 7 on the screen.

**Try to answer the following questions:**

1. Which device gives information to the computer?
2. Where can the computer temporarily store this information?
3. Which device shows the result?
4. Why do we need more than just the CPU to complete this task?

<details>
<summary><b>Suggested Answers</b></summary>

1. Keyboard.
2. RAM.
3. Monitor.
4. Because the computer also needs memory and input/output devices to receive, store, and display information.

</details>

---

## 2. Central Processing Unit (CPU)

### Goal

To understand what the CPU does and how its main parts work together to process instructions.

### Learning Objectives

Students will be able to identify the ALU, registers, and control unit, explain their roles, and follow a simple CPU operation.

### 2.1 What Is the CPU?

The **CPU** can be considered as the brain of your computer.

In general, the CPU carries out instructions and performs calculations like adding or subtracting numbers. Modern processors can perform billions of operations every second, which allows computers to complete different tasks in a very short time.

However, the CPU does not work independently. It needs instructions and data from memory and also interacts with other hardware components.

In general, the CPU consists of three main parts:

- **Arithmetic Logic Unit (ALU)**
- **Control Unit (CU)**
- **Registers**

Each of these components has its own responsibility, and together they allow the processor to execute instructions.

![CPU](../Material%20for%20Research/IMG_0072.jpg)

---

### 2.2 The Arithmetic Logic Unit (ALU)

The **ALU** is the mathematical brain of a computer.

It is responsible for performing arithmetic, logic, and shift operations on data. These operations are performed using electronic circuits inside the processor.

#### Arithmetic Operations

Arithmetic operations are responsible for handling numerical calculations in a computer, like adding, subtracting, multiplying, and dividing numbers.

For example, when a computer needs to calculate **5 + 3**, the ALU can perform this operation and produce the result **8**.

However, depending on the processor, some complicated calculations may require several operations instead of just one.

#### Shift Operations

Shift operations are used to move bits from left to right or from right to left.

There are two important types of shifts:

- **Logical Shift**
- **Arithmetic Shift**

A logical shift moves bits to one direction and fills empty positions with zeros.

An arithmetic right shift works with signed binary numbers and normally keeps the sign bit.

One interesting thing about shifting is that it can also change the value of a binary number. For example, shifting a number one position to the left can multiply its value by two, while shifting to the right can divide it by two.

However, this depends on the type of shift and whether the number can fit within the available bits.

#### Example: Left Shift

*[ADDED — Example]*

Imagine that we have a binary number `0011`, which represents 3.

After shifting it one position to the left, we get:

```text
0011 → 0110
```

Now the number represents 6 instead of 3.

In this case, the shift has the same effect as multiplying the original number by two.

#### Logic Operations

A computer stores our information in the form of bits, which are values of **0 and 1**.

Logic operations help a computer work with these bits. There are four main logic operations which we will discuss:

- **NOT:** Changes 0 to 1 or 1 to 0.
- **AND:** Gives 1 only when both inputs are 1.
- **OR:** Gives 1 when at least one input is 1.
- **XOR:** Gives 1 when the two inputs are different.

With the help of these operations, a computer can process and change binary data.

#### Example: Using AND

*[ADDED — Example]*

For example, imagine that a system has two conditions which must be satisfied before it performs an action.

The AND operation can be used to check whether both conditions are true. If even one of them is false, the result will be 0.

*[ADDED — Image: Truth table showing NOT, AND, OR, and XOR. Use an image instead of a large Markdown table.]*

---

### 2.3 Registers

Registers are small independent storage locations inside the CPU that can temporarily store information.

Several registers are needed for the processor to work properly.

*[ADDED — Explanation]*

You may wonder why the CPU needs registers if a computer already has RAM. The reason is that registers are much faster and allow the CPU to access the information it is currently working with very quickly.

However, there are fewer registers than memory locations in RAM.

#### Data Registers

Older computers often used a small number of registers to store input data and operation results.

Modern computers can use more registers inside the CPU to speed up their work, because the processor can keep frequently used values close to where calculations are performed.

Data registers are labelled as **R₁ … Rₙ** in the figure above.

*[ADDED — Example]*

For example, if the CPU needs to calculate 5 + 3, the two numbers can be stored in separate data registers before being sent to the ALU.

After the calculation, the result can be stored in another register.

#### Instruction Register

Nowadays, memory stores not only data but also programs.

The CPU is responsible for fetching instructions from memory one by one, decoding them, and executing them.

The **Instruction Register (IR)** temporarily stores the instruction which the CPU is currently processing.

#### Program Counter

The last register we will discuss is the **Program Counter (PC)**.

Its main responsibility is to keep the address of the next instruction that the CPU should fetch from memory.

Normally, after fetching an instruction, the CPU moves to the next one. However, some instructions can change this order, for example when a program needs to jump to another part of its code.

*[ADDED — Diagram: Program Counter pointing to an instruction in Main Memory, with that instruction being transferred to the Instruction Register.]*

---

### 2.4 The Control Unit

Not a single CPU will work properly without a **Control Unit**.

As the name suggests, it controls and coordinates the operation of different CPU components. It does this by sending control signals to other components and making sure that instructions are carried out correctly.

However, the Control Unit does not perform calculations itself. This responsibility belongs to the ALU.

#### Worked Example: Adding 5 + 3

*[ADDED — Worked example]*

To understand how these components work together, let's imagine that our CPU needs to calculate:

> **5 + 3 = ?**

The process can be divided into several steps:

1. **Registers:** First, the numbers 5 and 3 are available in two data registers.

2. **Control Unit:** The Control Unit coordinates the operation and tells the ALU which calculation needs to be performed.

3. **ALU:** The ALU performs the addition and produces the result 8.

4. **Registers:** Finally, the result can be stored in another register and later transferred to memory.

This is a simplified example, but it shows us how the ALU, registers, and Control Unit work together to perform even a simple calculation.

*[ADDED — Diagram: Two data registers containing 5 and 3, arrows leading to the ALU, and an output register containing 8. Show the Control Unit coordinating the operation with control arrows.]*

---

### Activity 2: Understanding CPU Components

*[ADDED — Combined activity]*

Now that we have discussed the main parts of the CPU, try to identify which component is responsible for each task.

#### Part A: Who Am I?

Match each statement with the **ALU, Data Register, Instruction Register, Program Counter, or Control Unit**.

1. I keep the instruction that the CPU is currently working on.
2. I perform an AND operation on two bit patterns.
3. I temporarily hold a number while the CPU is using it.
4. I keep the address of the next instruction to fetch.
5. I coordinate what other parts of the CPU do.
6. I perform 12 + 8.

#### Part B: Find the Mistake

A student writes:

> "The Control Unit adds two numbers, and the ALU decides which instruction should be executed next."

**What is wrong with this explanation?**

Try to rewrite it in one or two sentences.

<details>
<summary><b>Suggested Answers</b></summary>

**Part A:**

1. Instruction Register.
2. ALU.
3. Data Register.
4. Program Counter.
5. Control Unit.
6. ALU.

**Part B:**

The ALU performs calculations, while the Control Unit coordinates CPU operations. The Program Counter stores the address of the next instruction to fetch.

</details>

---

## Key Terminology

| Term | Definition |
|------|------------|
| **Hardware** | The physical parts of a computer. |
| **Subsystem** | A group of components with a particular role. |
| **Input** | Information received by a computer. |
| **Output** | Information sent or displayed by a computer. |
| **CPU** | The main processing component that executes program instructions. |
| **ALU** | The part of the CPU that performs arithmetic and logic operations. |
| **Arithmetic Operations** | Operations used to perform calculations with numbers. |
| **Logic Operations** | Operations that work with bits using rules such as NOT, AND, OR, and XOR. |
| **Shift Operations** | Operations that move bits to the left or right. |
| **Bit** | The smallest unit of digital information, represented by 0 or 1. |
| **Register** | A small and fast storage location inside the CPU. |
| **Data Register** | A register used to temporarily store values needed by the CPU. |
| **Instruction Register** | Holds the instruction currently being processed. |
| **Program Counter** | Holds the address of the next instruction to fetch. |
| **Control Unit** | Coordinates CPU operations by sending control signals. |
| **Main Memory** | Holds data and instructions that a computer is currently using. |
| **RAM** | Temporary working memory used while programs are running. |
| **Input/Output Subsystem** | Hardware that allows computers to receive information and provide results. |


**Sensors, Actuators and Microcontrollers**

**1. The big idea**

A robot does three things: it senses, it decides, and it acts. Each step uses a different hardware part.
To sense, the robot uses a sensor. A sensor is a device that measures something in the real world, such as distance, light or sound, and turns it into an electrical signal.
To decide, the robot uses a microcontroller. It is a tiny computer on one chip that reads the signals from the sensors and decides what to do.
To act, the robot uses an actuator. An actuator is a device that turns an electrical signal into physical action, such as movement, sound or light.
Compare with a normal computer: a sensor works like an input device, an actuator works like an output device, and the microcontroller works like the CPU.

**2. Sensors and actuators**

Sensors measure the world. Examples: an ultrasonic sensor (distance), a light sensor (brightness), a microphone (sound), a camera (images).
Actuators change the world. Examples: a motor (movement), a speaker (sound), an LED (light), a vibration motor (shaking).

**3. The microcontroller and the sense–act loop**

A microcontroller is a small computer on a single chip. It has a processor, a little memory and pins for connecting sensors and actuators. It does not run Windows or games: it repeats one small program again and again:
Read the sensors.
Apply the rules in the program.
Send commands to the actuators.
Go back to step 1.
This repeating cycle is called the sense–act loop. Part 3 (Behaviorist AI) builds on it.


**4. Worked example: the obstacle-avoiding robot**

Our project uses an obstacle-avoiding robot to demonstrate how hardware components work together. The robot has an ultrasonic sensor to detect obstacles, a microcontroller to process information and make decisions, and two motors to control its wheels.

How the system works
The robot follows a continuous sense–decide–act cycle:

1. Sense: The ultrasonic sensor sends out a sound pulse and measures how long it takes for the echo to return after bouncing off an obstacle.
2. Decide: The microcontroller uses the echo time to calculate the distance and compares it with a safety threshold of 20 cm.
3. Act: If the obstacle is closer than 20 cm, the robot stops and turns away. If the distance is 20 cm or greater, it continues moving forward.

Calculating the distance

To calculate the distance, the microcontroller uses the speed of sound and the echo time. Because the sound travels to the obstacle and back, the measured time must be divided by two.

Distance = (Speed of sound × Echo time) ÷ 2

The speed of sound in air is approximately 343 m/s.

For example, if the echo time is 0.0058 seconds:

Distance = (343 × 0.0058) ÷ 2 = 0.9947 m

This is approximately 99.5 cm. Since the obstacle is farther than 20 cm, the robot continues moving forward.

When the echo time decreases to 0.001 seconds, the calculation becomes:

Distance = (343 × 0.001) ÷ 2 = 0.1715 m

This is approximately 17.2 cm. Since the obstacle is now closer than 20 cm, the microcontroller instructs the motors to stop and turn the robot away.

After turning, the sensor measures the distance again, and the cycle repeats. This example demonstrates how a robot combines sensing, decision-making, and movement to respond to its surroundings.



**Terminology**
- Bit values - 0 is false and 1 is true
- NOT -  it changes a bit to its opposite value so 0 becomes 1 also 1 becomes 0. It also works only with one bit
- AND - it gives 1 only when both bits are 1.
- OR - it gives value 1 when at least one is 1. XOR- it gives 1 when the two bits are different.
- Sensor – a device that measures something in the real world (distance, light, sound, touch) and turns it into an electrical signal. Works like an input device.
- Actuator – a device that turns an electrical signal into physical action (movement, sound, light). Examples: motor, speaker, LED. Works like an output device.
- Microcontroller – a small computer on a single chip with a processor, a little memory and pins for connecting sensors and actuators. It runs one program again and again.
- Signal – a changing electrical value that carries information.
- Ultrasonic sensor – a sensor that sends out a sound too high for humans to hear and measures how long the echo takes to come back, to find the distance to an object.
- Sense–act loop – the cycle a robot repeats all the time: read sensors, apply rules, command actuators, repeat.
