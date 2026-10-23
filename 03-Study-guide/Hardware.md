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
