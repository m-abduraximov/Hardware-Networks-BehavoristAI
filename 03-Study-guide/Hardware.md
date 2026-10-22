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
- Explain the difference between a sensor and an actuator, and give examples of each.
- Explain what a microcontroller is and how it differs from a normal computer.
- Describe the sense–decide–act loop of a simple robot: a sensor measures, the microcontroller decides, an actuator acts.
- Trace how an obstacle-avoiding robot uses an ultrasonic sensor, a microcontroller and motors (the running example of this project).

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

**Sensors, Actuators and Microcontrollers**

**1. The big idea**
A robot does three things: it senses, it decides, and it acts. Each step uses a different hardware part:
Step
Hardware part
Meaning
Sense
Sensor
A device that measures something in the real world and turns it into an electrical signal
Decide
Microcontroller
A tiny computer on one chip that reads signals and decides what to do
Act
Actuator
A device that turns an electrical signal into physical action (movement, sound, light)
Compare with a normal computer: a sensor works like an input device, an actuator like an output device, and the microcontroller like the CPU.

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
This is the running example of our whole project. The robot has an ultrasonic sensor at the front, a microcontroller, and two motors that drive the wheels.
flowchart LR
    A[Ultrasonic sensor<br/>measures distance] --> B[Microcontroller<br/>applies the rule]
    B --> C[Motors<br/>move the wheels]
    C -. robot moves, distance changes .-> A
The rule: if the distance is less than 20 cm, stop and turn. Otherwise, drive forward.
Step by step:
The sensor sends an ultrasonic pulse and starts a timer.
The pulse hits a wall and bounces back, and the timer stops.
The microcontroller converts the echo time into distance. The sound travels there and back, so we divide by 2:
distance = speed of sound × echo time ÷ 2 (the speed of sound in air is about 343 m/s).
Echo time 0.0058 s gives 343 × 0.0058 ÷ 2 ≈ 0.995 m, about 1 m. That is more than 20 cm, so the motors keep driving forward.
A moment later the echo time is 0.001 s, which gives 343 × 0.001 ÷ 2 ≈ 0.17 m, about 17 cm. That is less than 20 cm, so the microcontroller stops the motors and turns the robot away.
The loop starts again.



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
