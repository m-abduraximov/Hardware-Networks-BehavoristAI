**Goals**

To help students understand the basic parts of a computer, how they work together, and how hardware allows a robot to interact with the real world.

**Learning Objectives**

By the end of this part, students will be able to:

- ⁠Identify the main hardware components of a computer, including the CPU, memory, storage, input/output devices, and buses, and explain their basic roles.
- ⁠Explain the stored-program concept in simple words.
- Describe the fetch–decode–execute cycle and how the CPU follows instructions.
- Explain the role of controllers and how different hardware components work together.
- ⁠Describe how sensors, actuators, and microcontrollers help a robot receive information, process it, and perform actions.
- ⁠Briefly introduce GPUs, AI accelerators, and the history of computer hardware.

**Introduction:**

If we divide a computer into parts, we will get three broad categories or subsystems which make a computer work. These are central processing unit (CPU), the main memory, and the input/output subsystem. The next three sections discuss these subsystems and how they are connected

**1.1 Central Processing Unit**

CPU can be considered as a brain of your computer. In general CPU carries out instructions and performs calculations like adding subtracting but a billions times in a second. In general it
has three parts: an arithmetic logic unit also known as (ALU), a control unit, and a set of registers.

![CPU](../Material%20for%20Research/IMG_0072.jpg)

**1.2 The arithmetic logic unit (ALU)**

The ALU is the mathematical brain of a computer. It is THE thing that performs logic, shift, arithmetic operations on data. There’s a logic and arithmetic unit inside of one ALU.

Arithmetic unit:
- Its main responsibility is handling all numerical operations in a computer like adding or subtracting, multiplying and dividing. Computers use special hardware circuits to perform these calculations.

Shift Operations:
- This operations move those bits from left to right or наоборот. There is only two types logical shift and arithmetic shift. It moves bits and fills empty positions with zeros as it goes to one direction. If it shifts to the left by one position number will multiply by two while shifting to the right can divide it by two. However, this depends on the number and the type of shift.

Logic Operation:
- A computer stores our information in the form of bits which are values of 0 and 1. Logic Operations help a computer work with these bits. We have 4 main logic operations NOT, AND, OR, and XOR. With the help of these operations the computer can process and change binary data

**1.3 Register**

- These are independent cells that can temporarily store information. Several registers are needed for the processor to work.

Data register:
- Old computers used only a small number of registers to store input data and operation results. Modern computers use 10 times more inside the CPU to speed up their work, because complex operations are performed by hardware rather than software. Data registers are labeled as R₁ … Rₙ in the figure above

Instruction register
- Nowadays, memory stores not only data but also programs. The CPU is responsible for decoding instructions, fetching them from memory one by one, and storing them in the instruction register.

Program counter 
- The last register we will discuss is the program counter. It tracks the current instruction being executed. After that, the counter is increased to point to the address of the next instruction in memory.

**1.4 The control Unit**
- Not a single CPU will work without a control unit. As the name suggests, it controls the operation of each subsystem. Controlling is achieved through signals sent from the control unit to other subsystems.


**Terminology**
- Bit values - 0 is false and 1 is true
- NOT -  it changes a bit to its opposite value so 0 becomes 1 also 1 becomes 0. It also works only with one bit
- AND - it gives 1 only when both bits are 1.
- OR - it gives value 1 when at least one is 1. XOR- it gives 1 when the two bits are different.
