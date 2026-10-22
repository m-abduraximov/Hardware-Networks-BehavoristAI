## **Goals**
To introduce the basic ideas of **Behaviorist AI** and explain how an intelligent system can respond to its environment through simple behaviors and rules.
## **Learning Objectives**
By the end of this part, students will be able to:
- Explain what **Behaviorist AI** means.
- Define a **reactive agent**.
- Explain how a reactive agent responds to its environment.
- Describe the **sense–act loop**.
- Explain how sensors provide information for an agent.
- Explain how simple **behavior rules** connect situations with actions.
- Describe how a robot can use reactive behavior to avoid obstacles.
- Identify the main components involved in a simple reactive behavior: **sensor, controller, and actuator**.
## **Introduction**
**Behaviorist AI** is an approach to artificial intelligence that focuses on how an intelligent system can respond to its environment through observable behaviors.

Instead of creating a complex plan before acting, a behavior-based system can react to the situation that it currently observes.

For example:

> **If an obstacle is detected, turn away from it.**

This simple rule connects a situation with an action. The system continuously observes its environment and changes its behavior when the situation changes.

A simple reactive system can therefore follow this cycle:

**Sense → Decide → Act → Sense again**

This repeated process is known as the **sense–act loop**.
## **1. Reactive Agents**
A **reactive agent** is an AI system that responds to information from its current environment.

The word *reactive* means that the system reacts to what is happening at the moment.

For example, a mobile robot can follow simple rules:

```text
If the path is clear → move forward.

If an obstacle is detected → turn.

If the path becomes clear → move forward again.
```

The agent does not need to create a complete plan for every possible situation. Instead, it uses the information currently available and selects an appropriate action.

This makes reactive agents useful in situations where the environment can change quickly.
## **2. The Sense–Act Loop**
A reactive agent needs to observe its environment repeatedly.

The **sense–act loop** describes the continuous process through which an agent receives information, chooses a response, performs an action, and observes the environment again.

The basic cycle is:

```text
Sense → Decide → Act → Sense again
```

### **Sense**

The agent receives information from its environment using a **sensor**.
### **Decide**

The system processes the information and applies a behavior rule.

For example:

```text
Obstacle detected → avoid the obstacle
```

### **Act**

The system performs the selected action.

For a mobile robot, a motor can move the wheels and change the robot's direction.

### **Sense Again**

After the robot performs an action, the environment may be different.

The robot therefore checks its sensors again and makes a new decision.

The complete process can be represented as:

```text
Environment
     ↓
   Sensor
     ↓
Information
     ↓
Behavior rule
     ↓
  Decision
     ↓
  Actuator
     ↓
Robot action
     ↓
Environment changes
     ↺
  Sense again
```

The important idea is that the process is **continuous**.
## **3. Behavior Rules**
A **behavior rule** connects a specific situation with an appropriate action.

A simple rule can be written as:

```text
If condition
THEN action
```

For example:

```text
If an obstacle is detected
THEN turn
```

Another example is:

```text
If the path is clear
THEN move forward.
```

Several simple rules can work together:

| **Situation** | **Behavior** |
|---|---|
| Path is clear | Move forward |
| Obstacle is detected | Stop and turn |
| Path becomes clear | Move forward again |

The system checks which situation is currently happening and performs the corresponding behavior.

This is one of the main ideas behind **behavior-based systems**: relatively simple behaviors can be used to produce useful actions without requiring a complex plan.
## **4. Worked Example: Obstacle-Avoiding Robot**

A simple obstacle-avoiding robot is a good example of a reactive agent.

The robot can use:

- an **ultrasonic sensor** to detect obstacles;
- a **microcontroller** to process the sensor information;
- **motors** to move the robot.

The robot follows a simple rule:

```text
If the distance is less than 20 cm
→ stop and turn.

Otherwise
→ move forward.
```

The process can be represented as:

```text
Ultrasonic sensor
       ↓
Measures distance
       ↓
Microcontroller
       ↓
Applies behavior rule
       ↓
Motors
       ↓
Robot moves
       ↓
Sensor measures again
       ↺
```
### **Step 1: The Robot Senses**

The ultrasonic sensor measures the distance to an object in front of the robot.

Suppose the sensor detects **50 cm**.

Because the distance is greater than 20 cm, the robot moves forward.
```text
50 cm > 20 cm
→ Move forward
```
### **Step 2: The Robot Senses Again**

After moving forward, the robot measures the distance again.

Suppose the new measurement is **15 cm**.

Now the obstacle is closer than the 20 cm limit.
```text
15 cm < 20 cm
→ Stop and turn
```
### **Step 3: The Robot Acts**

The microcontroller sends commands to the motors.

The robot stops and turns away from the obstacle.

### **Step 4: The Robot Checks Again**

After turning, the robot measures the distance again.

If the path is clear, it continues moving forward.

If another obstacle is detected, the same behavior rule is applied again.

The complete process is:
```text
Measure distance
      ↓
Apply the rule
      ↓
Move or turn
      ↓
Measure again
      ↺
```
This robot is a **reactive agent** because its actions depend on the information it currently receives from its environment.
## **5. Advantages and Limitations of Reactive Behavior**
Reactive behavior has several advantages.

### **Advantages**

- **Simple:** The rules are easy to understand and implement.
- **Fast:** The system can respond quickly to changes.
- **Useful in dynamic environments:** The agent can react when the environment changes.
- **Easy to test:** Individual behaviors can be tested separately.

### **Limitations**

Reactive behavior also has some limitations.

A simple rule such as:
```text
Obstacle → Turn
```
can help a robot avoid an obstacle, but it does not explain how to find the best route to a destination.

The robot may also make the same type of response repeatedly without understanding the larger situation.

For this reason, more advanced behavior-based systems can combine multiple behaviors and organize them using different priorities.
## **6. Reactive Behavior in Intelligent Systems**
Reactive behavior is useful because an intelligent system often needs to respond to changes in its environment quickly.

For example, a robot moving through an unfamiliar area cannot always predict everything that will happen.

An obstacle may appear suddenly, another object may move into the robot's path, or the available path may become blocked.

A reactive system can respond to these changes by continuously checking its sensors and applying appropriate behavior rules.

For example:
```text
IF path is clear
THEN move forward.

IF obstacle is detected
THEN stop.

IF obstacle is detected on the left
THEN turn right.

IF obstacle is detected on the right
THEN turn left.
```
These rules allow the robot to react to different situations without creating a complete plan before starting.

The main principle is:

> **Current information leads to an immediate action.**

This makes reactive behavior especially useful for systems that operate in changing or unpredictable environments.
## **7. Components of a Simple Reactive System**
A simple reactive system can be understood through three main components:

1. **Sensor**
2. **Controller**
3. **Actuator**
### **7.1 Sensor**
A sensor collects information from the environment.

For example:

- an ultrasonic sensor measures distance;
- a light sensor measures light intensity;
- a temperature sensor measures temperature;
- a camera provides visual information.

The sensor provides the information that the system needs to decide what to do.
### **7.2 Controller**
The controller processes the information received from the sensor.

It applies the appropriate behavior rule.

For example:
```text
Sensor detects obstacle
        ↓
Controller checks the rule
        ↓
Obstacle detected
        ↓
Turn
```
A microcontroller can be used as the controller in a simple robot.
### **7.3 Actuator**
An actuator performs the physical action selected by the controller.

For a mobile robot, motors are common actuators.

For example:
```text
Controller
    ↓
Turn command
    ↓
Motor
    ↓
Robot turns
```
The three components work together:
```text
Environment
     ↓
   Sensor
     ↓
 Controller
     ↓
  Actuator
     ↓
    Action
     ↓
Environment changes
     ↺
```
This creates a continuous reactive system.
## **8. Example of Multiple Behavior Rules**
A reactive agent can use more than one behavior rule.

For example, a robot may use the following rules:

| **Condition** | **Action** |
|---|---|
| Path is clear | Move forward |
| Obstacle in front | Stop |
| Obstacle on the left | Turn right |
| Obstacle on the right | Turn left |
| Path is blocked | Turn around |

The controller checks the current sensor information and selects the behavior that matches the situation.
## **9. Why Reactive Agents Are Useful**
Reactive agents are useful when a system needs to respond quickly to its surroundings.

One important advantage is that the agent does not need to calculate every possible future situation.

Instead, it can use current sensor information and simple rules.

For example, an obstacle-avoiding robot does not need to know the exact location of every object in a room.

It only needs to know whether an obstacle is currently close enough to require a response.

This can make the system:

- easier to design;
- easier to understand;
- faster to execute;
- easier to test;
- suitable for changing environments.

However, reactive behavior alone may not be enough for complex tasks that require long-term planning or reasoning.
## **Terminology**
- **Behaviorist AI** – an approach to AI that focuses on how an intelligent system responds to its environment through observable behaviors.
- **Reactive agent** – an AI system that responds to its current situation or current sensor information.
- **Behavior** – a specific way in which an agent responds to a situation.
- **Behavior rule** – a rule that connects a condition or situation to an action.
- **Environment** – the surroundings in which an intelligent system operates.
- **Sensor** – a device that collects information from the environment.
- **Controller** – a component that processes information and controls the system's actions.
- **Actuator** – a component that produces a physical action, such as a motor.
- **Sense–act loop** – the repeated process of sensing the environment, deciding what to do, performing an action, and sensing again.
- **Ultrasonic sensor** – a sensor that uses high-frequency sound and its echo to measure distance.
- **Microcontroller** – a small computer on a single chip that can process sensor information and control connected devices.
- **Obstacle** – an object or condition that blocks or makes movement difficult.
- **Reactive behavior** – behavior in which an agent responds directly to information from its current environment.
- **Condition** – a situation that is checked before a behavior rule is applied.
- **Action** – an operation performed by an intelligent system in response to a condition.
- **Dynamic environment** – an environment that can change while an intelligent system is operating.
## **Conclusion**
**Behaviorist AI** provides a simple way to understand intelligent behavior.
A **reactive agent** observes its environment, applies a suitable behavior rule, performs an action, and then observes the environment again.

The **sense–act loop** is therefore a fundamental concept:
```text
Sense → Decide → Act → Sense again
```
The obstacle-avoiding robot demonstrates how this approach can be used in practice. By combining sensors, simple rules, a controller, and actuators, the robot can respond to obstacles and change its behavior as its environment changes.

Reactive behavior is especially useful when an intelligent system needs to respond quickly to its surroundings. Although simple reactive rules may not solve complex planning problems, they provide a clear and practical foundation for building intelligent systems that can interact with changing environments.
