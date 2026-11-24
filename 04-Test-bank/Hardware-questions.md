# Part A – True / False

*Write True or False. If a statement is false, correct it.*

1. [1.2.2] The ALU performs arithmetic, logic and shift operations on data.

2. [1.2.3] The Program Counter stores the instruction that the CPU is currently processing.

3. [1.2.2] Shifting the binary number 0011 one position to the left gives 0110, which doubles the value from 3 to 6.

4. [1.3.1] Eight bits together form one byte.

5. [1.3.2] ROM is normally volatile, so it loses its contents when the power is turned off.

6. [1.3.3] Cache memory replaces RAM, so a computer with cache does not need RAM.

7. [1.4.2] A solid-state drive (SSD) stores information magnetically on spinning disks.

8. [1.4.3] Adding more RAM automatically gives you more space to install games.

9. [1.5.1] The Address Bus carries information about the memory location the CPU wants to access.

10. [1.7.2] With PWM, a 50 % duty cycle on a 5 V supply gives an average voltage of about 2.5 V.

# Part B – Multiple Choice

11. [1.1.1] Which list shows the three broad categories of subsystems in a computer? *(Choose ONE answer.)*

    - A. Keyboard, mouse and monitor
    - B. CPU, Main Memory and the Input/Output subsystem
    - C. RAM, ROM and cache
    - D. Data Bus, Address Bus and Control Bus

12. [1.2.2] Which logic operation gives 1 only when both inputs are 1? *(Choose ONE answer.)*

    - A. NOT
    - B. OR
    - C. AND
    - D. XOR

13. [1.6.2] In the fetch stage, where is the fetched instruction placed? *(Choose ONE answer.)*

    - A. Program Counter
    - B. Instruction Register
    - C. Cache
    - D. Data Bus

14. [1.6.2] During the decode stage, which component interprets the instruction and decides which operation is required? *(Choose ONE answer.)*

    - A. ALU
    - B. Control Unit
    - C. Program Counter
    - D. Address Bus

15. [1.3.3] Which order goes from the fastest and smallest memory to the slower and larger one? *(Choose ONE answer.)*

    - A. RAM → Cache → Registers
    - B. Cache → Registers → RAM
    - C. Registers → Cache → RAM
    - D. Registers → RAM → Cache

16. [1.5.1] Which statements about buses are correct? *(Choose ALL correct answers.)*

    - A. The Data Bus carries the actual data being transferred.
    - B. The Address Bus carries the location the CPU wants to access.
    - C. The Control Bus carries the numbers that are being added.
    - D. The Control Bus can indicate whether the CPU wants to read or write.

17. [1.3.2, 1.4.2–1.4.3] Which of these keep their information when the power is turned off? *(Choose ALL correct answers.)*

    - A. SSD
    - B. HDD
    - C. RAM
    - D. Flash memory

18. [1.7.1] The converter inside the Arduino Uno's microcontroller has 10 bits. How many different values can it produce? *(Choose ONE answer.)*

    - A. 10
    - B. 256
    - C. 1,023
    - D. 1,024

19. [1.7.1] A robot stands still 20 cm from a wall. Its readings are 20, 21, 34, 19 and 20 cm. Which reading is most likely noise? *(Choose ONE answer.)*

    - A. 20
    - B. 21
    - C. 34
    - D. 19

20. [1.7.3] Which part of a microcontroller keeps the robot's program when the battery is removed? *(Choose ONE answer.)*

    - A. RAM
    - B. Flash memory
    - C. Analog-to-digital converter
    - D. Timers

# Part C – Open-ended

*Write a developed answer (normally more than 100 words), using examples, a diagram or worked steps.*

21. [1.5.1, 1.6] Explain the Fetch–Decode–Execute cycle using the example of a program that adds 5 + 3. Describe what the Program Counter, the Instruction Register, the Control Unit, the ALU and the buses (Address Bus, Control Bus and Data Bus, see Section 1.5.1) do at each stage, and explain why the cycle repeats.

22. [1.3–1.4] A student says: "Why does a computer need registers, cache, RAM and an SSD? One big memory would be simpler." Write a reply that explains the role of each type, compares their speed and size, explains the difference between volatile RAM and nonvolatile SSD storage, and uses the example of a document that is saved versus one that is not saved when the power suddenly fails.

23. [1.7.2] A robot's wheel motor must be controlled by a microcontroller. Explain how the microcontroller controls the speed (PWM and duty cycle) and the direction (H-bridge) of the motor, and why a motor driver is needed. Include a calculation of the average voltage for a 75 % duty cycle on a 6 V supply, and explain what happens if a student connects the motor directly to a microcontroller pin.

---

# Answer Key

## Part A – True / False

**1. True.** The ALU performs arithmetic operations (add, subtract, multiply, divide), logic operations (NOT, AND, OR, XOR) and shift operations.

**2. False.** The Program Counter holds the address of the next instruction to fetch. The Instruction Register holds the instruction the CPU is currently processing.

**3. True.** 0011 represents 3 and 0110 represents 6. A left shift by one position multiplies the value by two, as long as the result fits in the available bits.

**4. True.** A bit is a single 0 or 1, and eight bits form one byte. For example, 00000101 represents 5.

**5. False.** ROM is nonvolatile, so it keeps its contents when the power is turned off. RAM is the memory that is normally volatile.

**6. False.** Cache does not replace RAM. It works together with RAM and keeps copies of data and instructions the CPU is likely to need soon.

**7. False.** An SSD stores information electronically using flash memory and has no spinning disks. An HDD is the device that stores information magnetically on spinning disks.

**8. False.** RAM helps the computer work with running programs. Space for installing games depends on secondary storage (SSD/HDD).

**9. True.** The Address Bus carries the location, the Data Bus carries the actual data, and the Control Bus carries signals such as read or write.

**10. True.** Average voltage = duty cycle × supply voltage = 0.50 × 5 V = 2.5 V.

## Part B – Multiple Choice

**11. B.** The CPU processes instructions, main memory temporarily stores the information in use, and the I/O subsystem lets us interact with the computer. Keyboard, mouse and monitor are devices; RAM, ROM and cache are types of memory; buses connect the subsystems.

**12. C.** AND gives 1 only when both inputs are 1. OR gives 1 when at least one input is 1, XOR gives 1 when the inputs are different, and NOT changes a single input.

**13. B.** The Program Counter holds the address of the instruction to fetch; the fetched instruction itself is placed in the Instruction Register.

**14. B.** The Control Unit interprets the instruction and coordinates the other parts. The ALU only performs the calculation later, in the execute stage.

**15. C.** Registers are inside the CPU and are the fastest and smallest; cache is small and fast; RAM is much larger but slower.

**16. A, B, D.** The Control Bus carries signals that coordinate operations, such as read or write, not the numbers being added. Numbers travel on the Data Bus.

**17. A, B, D.** SSD, HDD and flash memory are nonvolatile. RAM is normally volatile and loses its contents without power.

**18. D.** 2¹⁰ = 1,024 different values, from 0 to 1023. 1,023 is the largest value, not the number of values.

**19. C.** The robot is not moving, and all the other readings are close to 20 cm, so 34 cm is unwanted variation (noise) (Activity 8).

**20. B.** Flash memory stores the program and keeps it without power. RAM holds variables while the program runs and loses them when the battery is removed.

## Part C – Open-ended

*Other well-reasoned answers are also acceptable.*

**21. The Fetch–Decode–Execute cycle**

- Fetch: the Program Counter holds the address of the next instruction. The address travels on the Address Bus, the Control Bus signals a read, and the instruction comes back on the Data Bus. It is placed in the Instruction Register, and the CPU normally moves on to the next instruction.
- Decode: the Control Unit interprets the instruction in the Instruction Register and decides which operation is required (for example LOAD, ADD or STORE).
- Execute: LOAD 5 into Register A and LOAD 3 into Register B; for ADD, the Control Unit tells the ALU to add, and the ALU produces 8 in Register C; STORE writes 8 to memory address 20 (address on the Address Bus, write signal on the Control Bus, value on the Data Bus).
- Why it repeats: a program is a sequence of instructions stored in memory. After one instruction is completed, the CPU fetches the next one, until an instruction such as HALT stops the program. Jump instructions can change which instruction comes next.
- Good answers use the LOAD / ADD / STORE / HALT program from Section 1.6.3 and show the cycle as a loop.

**22. Why a computer needs registers, cache, RAM and an SSD**

- Registers: tiny storage inside the CPU, the fastest and smallest; they hold the values being used right now (for example 5 and 3 before the ALU adds them).
- Cache: small, fast memory holding copies of data and instructions the CPU is likely to need soon; it works with RAM and does not replace it.
- RAM: much larger but slower working memory for running programs; normally volatile.
- SSD: long-term storage for programs and files; much larger and generally slower than RAM; nonvolatile.
- Why not one big memory: faster memory costs more and cannot easily be made very large, so computers combine small fast memory with large slower storage.
- Example: a document saved to the SSD can be opened again after a power failure; unsaved changes that exist only in RAM are lost.

**23. Controlling a wheel motor**

- PWM: the digital pin switches fully on and off very quickly, and the motor reacts to the average. The duty cycle is the fraction of time the pin is on; more on-time means more speed.
- Calculation: average voltage = duty cycle × supply voltage = 0.75 × 6 V = 4.5 V (on an Arduino, an analogWrite value of about 191).
- H-bridge: four switches around the motor; closing one diagonal pair sends the current one way, the other pair reverses it. IN1 = 1, IN2 = 0 → forward; IN1 = 0, IN2 = 1 → backward; IN1 = 0, IN2 = 0 → stop.
- Motor driver: a pin can supply only a tiny current (about 20 mA recommended on an Arduino Uno), but a motor needs hundreds of milliamps; the driver switches the large battery current using the small control signals.
- Direct connection: the motor gets too little power to turn, and the attempt can overload the pin and disturb the microcontroller's power supply, so it may keep restarting.
