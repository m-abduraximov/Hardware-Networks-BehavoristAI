
# Chapter 2: Hardware

## Goals

To help students understand the basic parts of a computer, how they work together, and how computers store, process, and exchange information.

## Learning Objectives

By the end of this chapter, students will be able to:

- Identify the main hardware components of a computer, including CPU, memory, storage, input/output devices, and buses, and explain their basic roles.
- Explain the functions of the ALU, Control Unit, and Registers inside the CPU.
- Understand how computers store information using bits, bytes, and memory addresses.
- Explain the differences between RAM, ROM, Cache Memory, and Secondary Storage.
- Describe how input/output devices and controllers allow a computer to communicate with other devices.
- Explain how the Data Bus, Address Bus, and Control Bus transfer information between computer components.
- Explain the stored-program concept in simple words.
- Describe the Fetch–Decode–Execute cycle and how the CPU follows instructions.
- Trace how different hardware components work together when executing a simple program.

---

## Table of Contents

1. **[Introduction to Computer Hardware](#1-introduction-to-computer-hardware)**
   - [1.1 Main Computer Subsystems](#11-main-computer-subsystems)
   - [1.2 How the Subsystems Work Together](#12-how-the-subsystems-work-together)
2. **[Central Processing Unit (CPU)](#2-central-processing-unit-cpu)**
   - [2.1 What Is the CPU?](#21-what-is-the-cpu)
   - [2.2 The Arithmetic Logic Unit (ALU)](#22-the-arithmetic-logic-unit-alu)
   - [2.3 Registers](#23-registers)
   - [2.4 The Control Unit](#24-the-control-unit)
3. **[Main Memory](#3-main-memory)**
   - [3.1 How Does Computer Memory Work?](#31-how-does-computer-memory-work)
   - [3.2 RAM and ROM](#32-ram-and-rom)
   - [3.3 Memory Hierarchy and Cache](#33-memory-hierarchy-and-cache)
4. **[Input/Output Subsystem and Storage](#4-inputoutput-subsystem-and-storage)**
   - [4.1 Input and Output Devices](#41-input-and-output-devices)
   - [4.2 Secondary Storage](#42-secondary-storage)
   - [4.3 Memory vs. Storage](#43-memory-vs-storage)
5. **[Subsystem Interconnection](#5-subsystem-interconnection)**
   - [5.1 Buses](#51-buses)
   - [5.2 Input/Output Controllers](#52-inputoutput-controllers)
6. **[Program Execution](#6-program-execution)**
   - [6.1 Stored-Program Concept](#61-stored-program-concept)
   - [6.2 Fetch–Decode–Execute Cycle](#62-fetchdecodeexecute-cycle)
   - [6.3 Worked Example: Adding Two Numbers](#63-worked-example-adding-two-numbers)

**[Key Terminology](#key-terminology)**

---

## 1. Introduction to Computer Hardware

### Goal

To introduce the three main subsystems of a computer before studying them separately.

### 1.1 Main Computer Subsystems

If we divide a computer into parts, we will get three broad categories or subsystems which make a computer work. These are the **Central Processing Unit (CPU)**, the **Main Memory**, and the **Input/Output subsystem**.

Each of these subsystems has its own responsibility. The CPU is responsible for processing instructions and performing calculations, while the main memory temporarily stores information which the computer is currently using. The Input/Output subsystem allows us to interact with the computer by receiving information or showing the results.

#### Example: Using a Calculator

For example, imagine that you are using a calculator on your computer. When you type a number on your keyboard, the computer receives this information through an input device. After that, the CPU processes the information and the result appears on your monitor.

During this process, the computer also uses its main memory to keep the information it needs.

### 1.2 How the Subsystems Work Together

Although each subsystem has its own responsibility, they cannot do everything independently.

For example, the CPU is capable of performing calculations, but without memory it would not have the instructions and data needed to perform them. The same can be said about input and output devices, because without them it would be much harder for us to interact with the computer.

*_[DIAGRAM 1 — Three Main Computer Subsystems: Show a keyboard connected to the computer's input system, a CPU connected to Main Memory, and an output connection to a monitor. Use arrows to demonstrate how information moves between the components.]_*

### Activity 1: Follow a Keyboard Input

Imagine that you type the number 7 on a keyboard and a calculator app shows 7 on the screen.

**Try to answer the following questions:**

1. Which device gives information to the computer?
2. Where can the computer temporarily store this information?
3. Which device shows the result?
4. What would happen if the computer could receive keyboard input but had no working output device? Explain your answer.

<details>
<summary><b>Suggested Answers</b></summary>

1. Keyboard.
2. RAM.
3. Monitor.
4. The computer could still receive and process information, but the user would not be able to see the result on the screen. Other output methods might still work if available.

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

*_[IMAGE 1 — CPU Structure: Insert the existing CPU image (IMG_0072.jpg) if it clearly shows ALU, Control Unit, and Registers. Otherwise use a simplified labelled diagram. Check the relative image path in the final GitHub repository.]_*

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

A logical shift moves bits in one direction and fills empty positions with zeros.

An arithmetic right shift works with signed binary numbers and normally keeps the sign bit.

One interesting thing about shifting is that it can also change the value of a binary number. For example, shifting a number one position to the left can multiply its value by two, while shifting to the right can divide it by two.

However, this depends on the type of shift and whether the number can fit within the available bits.

#### Example: Left Shift

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

For example, imagine that a system has two conditions which must be satisfied before it performs an action.

The AND operation can be used to check whether both conditions are true. If even one of them is false, the result will be 0.

*_[IMAGE 2 — Logic Operations: Insert an image showing NOT, AND, OR, and XOR with binary inputs and outputs. A visual truth table would work well here.]_*

### 2.3 Registers

Registers are small independent storage locations inside the CPU that can temporarily store information.

Several registers are needed for the processor to work properly.

You may wonder why the CPU needs registers if a computer already has RAM. The reason is that registers are much faster and allow the CPU to access the information it is currently working with very quickly.

However, there are fewer registers than memory locations in RAM.

#### Data Registers

Older computers often used a small number of registers to store input data and operation results.

Modern computers can use more registers inside the CPU to speed up their work, because the processor can keep frequently used values close to where calculations are performed.

Data registers are labelled as **R₁ … Rₙ** in the figure above.

For example, if the CPU needs to calculate 5 + 3, the two numbers can be stored in separate data registers before being used by the ALU.

After the calculation, the result can be stored in another register.

#### Instruction Register

Nowadays, memory stores not only data but also programs.

The CPU is responsible for fetching instructions from memory one by one, decoding them, and executing them.

The **Instruction Register (IR)** temporarily stores the instruction which the CPU is currently processing.

#### Program Counter

The last register we will discuss is the **Program Counter (PC)**.

Its main responsibility is to keep the address of the next instruction that the CPU should fetch from memory.

Normally, after fetching an instruction, the CPU moves to the next one. However, some instructions can change this order, for example when a program needs to jump to another part of its code.

### 2.4 The Control Unit

Not a single CPU will work properly without a **Control Unit**.

As the name suggests, it controls and coordinates the operation of different CPU components. It does this by sending control signals to other components and making sure that instructions are carried out correctly.

However, the Control Unit does not perform calculations itself. This responsibility belongs to the ALU.

#### Worked Example: Adding 5 + 3

To understand how these components work together, let's imagine that our CPU needs to calculate:

> **5 + 3 = ?**

The process can be divided into several steps:

1. **Registers:** First, the numbers 5 and 3 are available in two data registers.
2. **Control Unit:** The Control Unit coordinates the operation and tells the ALU which calculation needs to be performed.
3. **ALU:** The ALU performs the addition and produces the result 8.
4. **Registers:** Finally, the result can be stored in another register and later transferred to memory.

This is a simplified example, but it shows us how the ALU, registers, and Control Unit work together to perform even a simple calculation.

*_[DIAGRAM 2 — CPU Adding 5 + 3: Show two data registers containing 5 and 3, arrows leading to the ALU, and an output register containing 8. The Control Unit should be shown separately with arrows coordinating the operation.]_*

### Activity 2: Understanding CPU Components

Now that we have discussed the main parts of the CPU, try to identify which component is responsible for each task.

#### Part A: Who Am I?

Match each statement with the **ALU, Data Register, Instruction Register, Program Counter, or Control Unit**.

1. I keep the instruction that the CPU is currently working on.
2. I perform an AND operation on two bit patterns.
3. I temporarily hold a number while the CPU is using it.
4. I keep the address of the next instruction to fetch.
5. I coordinate what other parts of the CPU do.

#### Part B: Find the Mistake

A student writes:

> "The Control Unit adds two numbers, and the ALU decides which instruction should be executed next."

**What is wrong with this explanation?**

Try to rewrite it in one or two sentences.

<details>
<summary><b>Suggested Answers</b></summary>

**Part A**

1. Instruction Register.
2. ALU.
3. Data Register.
4. Program Counter.
5. Control Unit.

**Part B**

The ALU performs calculations, while the Control Unit coordinates CPU operations. The Program Counter stores the address of the next instruction to fetch.

</details>

---

## 3. Main Memory

### Goal

To understand how computers store information, how memory locations work, and why different types of memory are needed.

### Learning Objectives

By the end of this section, students will be able to:

- Explain the purpose of main memory.
- Understand how data is stored using bits and bytes.
- Explain what a memory address is.
- Describe the difference between RAM and ROM.
- Explain why computers use cache memory.
- Compare registers, cache, and RAM.

### 3.1 How Does Computer Memory Work?

A computer needs a place to keep the information it is currently working with.

This is the responsibility of **Main Memory**.

Main memory stores data and program instructions which the CPU needs while programs are running.

However, computers do not store information in the same way that we write words or numbers on paper.

Instead, they represent information using binary digits called **bits**.

A bit can have only two possible values:

- **0**
- **1**

Eight bits together form one **byte**.

For example, the binary number `00000101` represents the decimal number 5.

Computers use combinations of bits to represent numbers, letters, instructions, and other information.

#### Memory Addresses

Imagine that memory consists of many small storage locations.

Each location has its own address, which allows the computer to find the information stored there.

A memory address can be compared to a house address. If you want to send something to a particular house, you need to know where it is located.

The same idea applies to computer memory.

For example:

| Memory Address | Value |
|----------------|-------|
| 00 | 12 |
| 01 | 4 |
| 02 | 9 |
| 03 | 12 |

In this simplified example, address 02 contains the value 9.

If the CPU needs this value, it can request the information stored at that address.

**Important:** The address tells the computer where the information is stored. The value is the actual information at that location.

*_[DIAGRAM 3 — Memory Addresses: Create a row of numbered memory locations, each containing a different value. Use an arrow to highlight address 02 and its value 9.]_*

### 3.2 RAM and ROM

Although both RAM and ROM are types of memory, they have different responsibilities.

#### Random Access Memory (RAM)

**RAM** is the working memory of a computer.

It temporarily stores information which programs are currently using.

For example, when you open a browser, the computer uses RAM to hold the information needed while the browser is running.

One important characteristic of RAM is that it is usually **volatile**.

This means that the information stored in RAM is lost when the computer loses power.

However, this does not mean that every file disappears when you turn off your computer. Files that have been saved to secondary storage can remain there.

#### Read-Only Memory (ROM)

**ROM** is a type of nonvolatile memory.

Traditionally, ROM is used to store instructions that do not need to change during normal computer operation.

For example, computers need firmware that helps initialize hardware when the system starts.

Some firmware is stored in nonvolatile memory, such as flash memory, which can be updated.

Unlike ordinary RAM, this type of memory keeps its information even when the computer is turned off.

#### RAM vs. ROM

| RAM | ROM |
|-----|-----|
| Used for temporary working information | Traditionally used for firmware or fixed instructions |
| Normally volatile | Nonvolatile |
| Can be read and written during normal operation | Traditionally read-only, although modern firmware storage may be updated |
| Used while programs are running | Helps store instructions needed for specific system functions |

#### Common Misconception

> **"If RAM loses information when the computer turns off, all my files will disappear."**

This is incorrect.

RAM is temporary working memory. Files saved to nonvolatile storage, such as an SSD, can remain available after the computer is turned off.

### 3.3 Memory Hierarchy and Cache

A computer needs memory that is fast, large, and affordable. However, faster memory usually costs more and cannot always store large amounts of information.

Because of this, computers use different types of memory, each of which has its own responsibility.

The three main types we will discuss are:

- **Registers:** Small storage locations inside the CPU. They are extremely fast but can hold only a small amount of information.
- **Cache Memory:** Small and fast memory that stores copies of data and instructions which the CPU is likely to use soon.
- **Main Memory (RAM):** Memory that stores information and instructions which programs are currently using. It has much more space than registers or cache, but it is generally slower.

#### Memory Hierarchy

The usual order from fastest and smallest to slower and larger is:

```text
        Registers
            ↓
          Cache
            ↓
           RAM
```

*_[DIAGRAM 4 — Memory Hierarchy: Show Registers at the top, Cache in the middle, and RAM at the bottom. Add arrows showing that memory generally becomes larger but slower as we move down.]_*

#### Example: Understanding Memory Hierarchy

Imagine that you are studying for an exam.

The information you are currently using is like something you are holding in your hand. This can be compared to a **Register**.

The notes you often check are placed on your desk, so you can easily reach them. This is similar to **Cache Memory**.

Your notebook contains much more information, but finding something inside it takes more time. This can be compared to **RAM**.

This example is simplified, but it shows why computers keep frequently used information closer to the CPU.

#### How Does Cache Work?

Let's imagine that the CPU needs some information which is stored in RAM.

The process can be divided into several steps:

1. The CPU needs a particular piece of data.
2. The processor checks whether this information is already available in cache.
3. If the data is there, the CPU can access it quickly.
4. If it is not there, the system retrieves the needed information from RAM.
5. A copy may also be placed in cache so the CPU can access it faster next time.

This is one of the reasons why cache memory helps computers work faster.

**Important:** Cache does not replace RAM. It works together with RAM to reduce the time needed to access frequently used information.

#### Common Misconception

> **"Cache memory and RAM are basically the same thing."**

Although both store information, they have different responsibilities.

Cache is much smaller and faster. It keeps copies of data that the CPU is likely to need soon, while RAM stores a much larger amount of information used by running programs.

---

## 4. Input/Output Subsystem and Storage

### Goal

To understand how computers receive information, display results, and store files for future use.

### Learning Objectives

By the end of this section, students will be able to:

- Explain the difference between input and output devices.
- Identify common examples of input/output hardware.
- Understand the purpose of secondary storage.
- Explain the difference between RAM and SSD/HDD.
- Describe how a computer uses memory and storage when running a program.

### 4.1 Input and Output Devices

The **Input/Output subsystem (I/O)** is the third major subsystem of a computer.

Its main responsibility is to allow the computer to receive information from the outside world and send information back.

There are two main categories of devices:

#### Input Devices

Input devices allow users to send information into a computer.

Some common examples are:

- Keyboard
- Mouse
- Microphone
- Camera

#### Output Devices

Output devices allow a computer to display information or perform an output action.

Some common examples are:

- Monitor
- Speakers
- Printer

#### Example: Typing a Sentence

Imagine that you are writing a document on your computer.

When you press a key on your keyboard, the computer receives information through an input device.

After that, the computer processes the information, and the letter appears on your monitor, which is an output device.

However, not every device belongs to only one category.

For example, a **touchscreen** can work as both an input and an output device. It displays information while also allowing users to interact with the computer by touching the screen.

*_[IMAGE 3 — Input and Output Devices: Insert a labelled illustration showing a keyboard, microphone, mouse, monitor, speakers, and touchscreen. Divide them into Input, Output, and Both categories.]_*

### 4.2 Secondary Storage

Computers need to store programs, pictures, documents, and other files even after they are turned off.

This is the main responsibility of **Secondary Storage**.

Unlike RAM, secondary storage can keep information without a continuous power supply.

There are several types of storage devices.

#### Hard Disk Drive (HDD)

A **Hard Disk Drive (HDD)** stores information magnetically on spinning disks.

HDDs are commonly used when large storage capacity is needed. They contain moving mechanical parts.

#### Solid-State Drive (SSD)

A **Solid-State Drive (SSD)** stores information electronically using flash memory.

Unlike HDDs, SSDs do not have spinning disks.

SSDs are generally faster than HDDs, especially when accessing many small files or loading programs.

#### Optical Storage

Another type of storage is optical storage, such as **CDs and DVDs**.

These devices use laser technology to read information stored on discs.

Although they are less common in modern computers, they are still an example of how information can be stored using different technologies.

*_[IMAGE 4 — Types of Secondary Storage: Show HDD, SSD, and optical disc side by side with labels.]_*

### 4.3 Memory vs. Storage

RAM and secondary storage may seem similar because both are used to keep information.

However, they have different responsibilities.

**RAM** holds information that a program is currently using.

**Secondary Storage** keeps programs and files so that they can be opened again later.

One important difference is that RAM is normally **volatile**, which means it loses its contents when power is turned off.

SSDs and HDDs are **nonvolatile**, meaning they can keep stored information even without power.

| RAM | SSD / HDD |
|-----|-----------|
| Temporary working memory | Long-term storage |
| Normally loses information without power | Keeps information without power |
| Used by running programs | Used to save programs and files |
| Generally faster to access | Generally slower than RAM |

#### Example: Playing a Video Game

Imagine that you have a game installed on your computer.

The game files are stored on an SSD or HDD.

When you open the game, the computer loads the necessary information into RAM.

During gameplay, the CPU works with the instructions and data that are currently needed.

When you close the game, the files remain on your storage device, so you can open it again later.

This example shows why computers need both RAM and secondary storage.

#### Common Misconception

> **"If my computer has more RAM, I can store more games and files."**

This is not exactly how it works.

RAM helps your computer work with running programs, while SSDs and HDDs are responsible for keeping your files.

For example, increasing RAM does not automatically increase the amount of space available for installing games.

### Activity 3: What Happens When Power Is Off?

Imagine that two students are writing documents on their computers.

**Student A** has saved the document to an SSD before the computer suddenly loses power.

**Student B** has been writing for an hour but has not saved the latest changes when the computer loses power.

**Questions:**

1. Why might Student B lose the latest changes?
2. Why can Student A open the saved document again?
3. Which type of memory is normally volatile?
4. Compare the two situations. What is the main difference between saving a document and keeping it open in RAM?

<details>
<summary><b>Suggested Answers</b></summary>

1. Because unsaved changes may exist only in volatile memory.
2. Because the saved document is stored on a nonvolatile SSD.
3. RAM.
4. Saving a document writes information to nonvolatile storage, while RAM temporarily holds information used by running programs.

Some programs can automatically recover unsaved work, but this should not be taken for granted.

</details>

---

## 5. Subsystem Interconnection

### Goal

To understand how the CPU, memory, and input/output devices communicate and exchange information.

### Learning Objectives

By the end of this section, students will be able to:

- Explain what a bus is.
- Identify the roles of the Data Bus, Address Bus, and Control Bus.
- Understand the basic purpose of input/output controllers.
- Describe how information moves between computer components.

### 5.1 Buses

A computer consists of many different components, but these components need a way to communicate with each other.

For this purpose, computers use communication connections called **Buses**.

In a simplified computer model, a bus can be considered as a path through which information travels between different hardware components.

There are three important types of buses which we will discuss:

#### Data Bus

The **Data Bus** carries the actual data being transferred between components.

For example, if the CPU needs a number from memory, the data bus carries that number.

#### Address Bus

The **Address Bus** carries information about the location which the CPU wants to access.

Imagine that the CPU needs a specific value stored in memory. It needs to know where this value is located.

The address bus helps identify this location.

#### Control Bus

The **Control Bus** carries signals that coordinate different operations.

For example, it can indicate whether the CPU wants to read information from memory or write new information into it.

#### Example: Reading Information from Memory

Let's imagine that the CPU needs a number stored at memory address 12.

The process can be explained using three main steps:

1. **Address Bus:** The CPU identifies the memory location it wants to access.
2. **Control Bus:** A control signal indicates that the CPU wants to read the information.
3. **Data Bus:** The requested data is transferred from memory to the CPU.

This is a simplified explanation, but it shows that different buses have different responsibilities.

*_[DIAGRAM 5 — CPU and Memory Communication: Show CPU on the left and Main Memory on the right, connected by three labelled paths: Address Bus, Data Bus, and Control Bus. Use arrows to show the direction of communication in the reading example.]_*

**Important:** Modern computers can use more complicated communication systems. However, this simplified model helps us understand the main purpose of buses.

### 5.2 Input/Output Controllers

Different input and output devices do not always work in the same way or at the same speed as the CPU.

For this reason, computers use **Input/Output Controllers**.

A controller helps the computer communicate with a device and manages the transfer of information.

#### Example: USB Controller

For example, when you connect a keyboard or an external storage device to your computer through USB, a USB controller helps manage communication between the device and the computer.

USB is a common connection system used by many different devices.

We do not need to study every USB version or connector type.

The important thing is to understand that controllers help different hardware components communicate and work together.

### Activity 4: Follow the Data

Imagine that the CPU wants to read the number stored at memory address 15.

The memory contains the following information:

| Memory Address | Value |
|----------------|-------|
| 14 | 20 |
| 15 | 8 |
| 16 | 12 |

**Questions:**

1. Which bus carries the address 15?
2. Which bus carries the signal telling memory to read information?
3. Which bus transfers the requested value back to the CPU?
4. What number will the CPU receive?
5. What would happen if the CPU requested address 16 instead of 15? Explain your answer.

<details>
<summary><b>Suggested Answers</b></summary>

1. Address Bus.
2. Control Bus.
3. Data Bus.
4. The CPU receives 8.
5. The CPU would receive 12 instead of 8 because address 16 contains a different value.

</details>

---

## 6. Program Execution

### Goal

To understand how computers follow instructions and how the CPU, registers, memory, and buses work together during program execution.

### Learning Objectives

By the end of this section, students will be able to:

- Explain the stored-program concept.
- Describe the Fetch–Decode–Execute cycle.
- Identify the roles of the Program Counter and Instruction Register.
- Explain how a computer follows a simple program.
- Understand how the main CPU components work together during execution.

### 6.1 Stored-Program Concept

Modern general-purpose computers can store both program instructions and data in memory.

This is known as the **Stored-Program Concept**.

In simple words, a computer does not need completely different hardware for every task. Instead, it can follow different sets of instructions depending on which program is running.

#### Example: Different Programs on One Computer

Imagine that you have a computer which you use for studying, playing games, and browsing the internet.

When you open a calculator, the computer follows instructions that allow it to perform calculations.

When you open a game, it follows a completely different set of instructions.

Although the programs are different, the same computer can execute them.

This is possible because computers can store different programs and follow their instructions.

#### Program Instructions vs. Data

Although instructions and data can both be stored in memory, they have different purposes.

- **Program Instructions:** Tell the computer what operation needs to be performed.
- **Data:** The information which the computer works with.

For example, if a calculator needs to calculate 5 + 3, the numbers 5 and 3 are data, while the instruction to add them is part of the program.

This difference is important because it helps us understand what the CPU actually does when executing a program.

### 6.2 Fetch–Decode–Execute Cycle

Now that we understand that computers store programs in memory, the next question is:

**How does the CPU actually follow these instructions?**

The answer is a repeating process called the **Fetch–Decode–Execute Cycle**.

This process consists of three main steps.

#### Step 1: Fetch

During the Fetch stage, the CPU retrieves the next instruction from memory.

The **Program Counter (PC)** holds the address of the instruction that needs to be fetched.

After the instruction is fetched, it is placed in the **Instruction Register (IR)**.

#### Step 2: Decode

After receiving the instruction, the CPU needs to understand what it should do.

During the Decode stage, the **Control Unit** interprets the instruction and determines which operation is required.

For example, it may identify that the CPU needs to add two numbers.

#### Step 3: Execute

During the Execute stage, the CPU performs the required operation.

Depending on the instruction, this may involve:

- Performing a calculation using the ALU.
- Reading or writing data.
- Moving information between registers.
- Performing another required operation.

After the instruction is completed, the CPU continues with the next instruction.

However, some instructions, such as jumps, can change which instruction comes next.

#### Fetch–Decode–Execute Diagram

*_[DIAGRAM 6 — Fetch–Decode–Execute Cycle: Draw a circular diagram containing Fetch → Decode → Execute → Fetch. Show the Program Counter and Instruction Register next to Fetch, the Control Unit next to Decode, and the ALU as an example of a component used during Execute.]_*

#### Common Misconception

> **"The CPU executes an instruction first and only after that understands what it means."**

This is incorrect.

The CPU must first **Fetch** an instruction from memory, then **Decode** it to determine what operation is required, and finally **Execute** it.

The cycle repeats as the CPU continues processing instructions.

### 6.3 Worked Example: Adding Two Numbers

We have already discussed how the CPU can perform calculations using the ALU, registers, and Control Unit.

Now we will look at the same example from another perspective.

Instead of focusing only on CPU components, we will see how a simple program is executed.

Imagine that the computer needs to calculate:

> **5 + 3 = 8**

The numbers and program instructions are available in memory.

A simplified sequence of operations would look like this:

1. The CPU fetches an instruction telling it to load the first number.
2. The value 5 is placed in a register.
3. The CPU follows another instruction and loads 3 into a second register.
4. The CPU fetches and decodes an addition instruction.
5. The ALU adds 5 and 3, producing the result 8.
6. The result is placed in another register and can later be stored in memory.
7. If the program needs to display the result, the computer sends the information to an output device.

This example shows that a computer does not calculate using only one component.

The CPU, memory, registers, ALU, and Control Unit all have different responsibilities.

#### Example: A Simple Program

The following is an imaginary program written in plain English instead of real machine code.

| Address | Instruction |
|---------|-------------|
| 00 | LOAD 5 into Register A |
| 01 | LOAD 3 into Register B |
| 02 | ADD A and B, put result in Register C |
| 03 | STORE Register C at memory address 20 |
| 04 | HALT |

In this example, the computer follows instructions one by one.

First, it loads the values 5 and 3 into registers.

After that, the ALU performs the addition and places the result in Register C.

Finally, the result is stored at memory address 20, and the program stops.

**HALT** is an instruction that tells the processor to stop executing this program.

*_[DIAGRAM 7 — A Simple Program: Show the instruction table on the left, CPU with registers and ALU in the centre, and a memory location containing the result 8 on the right. Use numbered arrows to show the steps of execution.]_*

### Activity 5: Be the CPU

Now imagine that you are the CPU executing the program above.

#### Part A: Follow the Instructions

Try to answer the following questions:

1. What value is stored in Register A after the first instruction?
2. What value is stored in Register B after the second instruction?
3. What result does the ALU produce?
4. At which memory address is the result stored?
5. Which instruction stops the program?

#### Part B: Predict the Result

Now imagine that we change some instructions in our program.

6. What would happen if the second instruction loaded **7 instead of 3** into Register B?
7. What would happen if we kept the original values 5 and 3, but replaced the ADD instruction with **SUBTRACT A minus B**?
8. Would changing the addition instruction also change the memory address where the result is stored? Explain your answer.

<details>
<summary><b>Suggested Answers</b></summary>

**Part A**

1. Register A = 5.
2. Register B = 3.
3. The ALU produces 8.
4. Memory address 20.
5. HALT.

**Part B**

6. The result would become 12 because 5 + 7 = 12.
7. The result would become 2 because 5 - 3 = 2.
8. No. The result would still be stored at memory address 20 because the STORE instruction has not changed.

</details>

---

## Key Terminology

The following terms summarize the main concepts introduced in this chapter.

### Computer Components

| Term | Definition |
|------|------------|
| **Hardware** | The physical parts of a computer. |
| **Subsystem** | A group of components with a particular role. |
| **CPU** | The main processing component that executes program instructions. |
| **ALU** | The part of the CPU that performs arithmetic and logic operations. |
| **Control Unit** | Coordinates CPU operations by sending control signals. |
| **Register** | A small and fast storage location inside the CPU. |
| **Data Register** | A register used to temporarily store values needed by the CPU. |
| **Instruction Register** | Holds the instruction currently being processed. |
| **Program Counter** | Holds the address of the next instruction to fetch. |

### Memory and Storage

| Term | Definition |
|------|------------|
| **Main Memory** | Memory used to hold instructions and data needed while programs run. |
| **RAM** | Temporary working memory that normally loses its contents without power. |
| **ROM** | Nonvolatile memory traditionally used for instructions that do not change during normal use. |
| **Cache Memory** | Small and fast memory holding copies of frequently or recently needed information. |
| **Memory Hierarchy** | The organization of memory into different levels based on speed, capacity, and cost. |
| **Memory Address** | A number identifying a memory location. |
| **Bit** | A binary digit, 0 or 1. |
| **Byte** | Eight bits. |
| **Volatile Memory** | Memory that loses its stored information without power. |
| **Nonvolatile Memory** | Memory that can keep information without power. |
| **Secondary Storage** | Hardware that keeps data after power is turned off. |
| **HDD** | A storage device that uses spinning magnetic disks. |
| **SSD** | A storage device that uses flash memory without spinning disks. |

### Operations and Communication

| Term | Definition |
|------|------------|
| **Arithmetic Operations** | Operations used to perform calculations with numbers. |
| **Logic Operations** | Operations that work with bits using rules such as NOT, AND, OR, and XOR. |
| **Shift Operations** | Operations that move bits to the left or right. |
| **Input Device** | Hardware used to send information to a computer. |
| **Output Device** | Hardware used to present results from a computer. |
| **I/O Controller** | Hardware that helps a device communicate with the computer. |
| **Bus** | A communication path between computer components. |
| **Data Bus** | Carries data between components. |
| **Address Bus** | Carries the address of the location or device being accessed. |
| **Control Bus** | Carries signals that coordinate operations, such as reading or writing. |

### Program Execution

| Term | Definition |
|------|------------|
| **Program** | A set of instructions for a computer. |
| **Stored-Program Concept** | The idea that program instructions and data can be stored in memory. |
| **Program Instructions** | Instructions that tell the computer which operations to perform. |
| **Data** | Information that a computer processes or works with. |
| **Fetch** | The process of retrieving an instruction from memory. |
| **Decode** | The process of determining what an instruction requires. |
| **Execute** | The process of carrying out an instruction. |
| **Fetch–Decode–Execute Cycle** | A repeating process through which the CPU follows program instructions. |
| **HALT** | An instruction used to stop program execution. |



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
