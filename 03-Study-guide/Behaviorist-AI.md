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


---

<!--
==========================================================================
PART 2 starts here. It is a separate section, written separately from
Part 1 above. Do not edit Part 1 when changing Part 2.
Part 2 authors: [add names]
Keep only the references in the References list that your team actually
read and used. Delete any you did not.
==========================================================================
-->

# **Part 2: From Behaviorism to Layered Behavior**

**Status:** Drafted. Needs review by a team member who did not write it.

Part 1 explained reactive agents, the sense-act loop and simple behavior rules. Part 2 continues from there. It explains where the word "behaviorist" comes from, how several behaviors can be combined using priorities, how this differs from AI that builds a model of the world first, and how reward-based learning connects to behaviorism.

## **Part 2 Goals**

To explain the ideas behind Behaviorist AI, show how layered behaviors and priorities work in a simple robot, and connect them to hardware and networks.

## **Learning Objectives (Part 2)**

By the end of this part, students will be able to:

- Explain behaviorism in psychology, with Pavlov and Skinner as examples.
- Explain why "Behaviorist AI" is an analogy and not a direct application of psychology.
- Explain how behavior-based AI differs from AI that builds an internal model of the world first.
- Describe Brooks's subsumption architecture in simple words.
- Use behavior priorities to predict what a simple robot will do.
- Connect reward-based learning with the idea of behaviorism.
- For a simple robot, point out which hardware senses, which network link carries the data, and which behavior rule decides the action.
- State briefly the limits of behavior-based AI and some ethical questions it raises.

## **A. Behaviorism in Psychology**

**Behaviorism** is an approach in psychology that studies what living things do, meaning their **observable behavior**, instead of guessing about thoughts inside the mind.

Two famous examples:

- **Ivan Pavlov**, a Russian physiologist, noticed that dogs began to salivate at the sound of a bell after the bell had repeatedly been followed by food. The dogs learned to connect the bell with the food. This is called **classical conditioning**.
- **B. F. Skinner**, an American psychologist, studied how the **consequences** of an action change future behavior. An action followed by a reward becomes more likely. An action followed by a punishment becomes less likely. This is called **operant conditioning**.

The idea to remember: behavior can be shaped through interaction with the environment.

## **B. From Psychology to AI: What "Behaviorist AI" Means**

In this guide, **Behaviorist AI** means **behavior-based AI**: intelligence that shows up in how a system responds to its environment, not in a detailed model built in advance. Some authors prefer the names *behavior-based AI* or *reactive robotics*.

It shares two ideas with behaviorism:

1. It focuses on **observable behavior**.
2. It treats intelligence as coming from **direct interaction with the environment**.

> **Important:** this is an **analogy**. Behavior-based robots were developed as an engineering approach. They were not built by applying Skinner's theories. The closest link to behaviorism is **reward-based learning** (Section G).

## **C. Two Ways to Build an Intelligent Robot**

**Model-first (sense, plan, act):** the robot senses, builds an **internal model** (a map or description of the world), makes a plan, and then acts. Early robots such as *Shakey*, built at SRI, worked in this way. This approach belongs to **symbolic AI**, which represents knowledge as symbols and reasons about them.

**Behavior-based (sense, act):** the robot connects sensors directly to actions through simple behaviors, and repeats this continuously (the sense-act loop from Part 1).

| | **Model-first** | **Behavior-based** |
|---|---|---|
| **Steps** | Sense, build model, plan, act | Sense, act, repeat |
| **Needs a model of the world?** | Yes | No. The world itself is used as the "model" |
| **Speed of reaction** | Slower, because planning takes time | Fast |
| **Strength** | Reasoning and long-term goals | Works in changing environments |
| **Weakness** | Fails if the model is out of date | Weak at long-term planning |

**Example:** a model-first robot draws a map of a room and plans a route. If someone moves a chair, its map is wrong until it updates the map. A behavior-based robot simply senses the chair and turns.

## **D. Conflicting Rules and Priorities**

In Part 1 (Section 8), the table of rules contains rules that can be true **at the same time**. For example, "Obstacle in front" and "Obstacle on the left" can both match.

When more than one behavior wants to control the motors, the robot needs a way to choose. The simplest way is a **priority**: each behavior gets a rank, and the **highest-priority active behavior controls the robot**.

Behaviors that protect the robot (such as avoiding collisions) usually get the **highest priority**.

## **E. Subsumption Architecture (Brooks)**

**Rodney Brooks**, a roboticist at MIT, proposed the **subsumption architecture** in the 1980s. Its main ideas are:

- Behavior is organized in **layers**.
- Each layer is a complete, simple behavior that connects **sensors to actuators**.
- Layers are built **step by step**. First the robot learns to survive (avoid obstacles), then to wander, then to pursue goals.
- A higher layer can **interfere with** (*subsume*) the signals of lower layers, but the lower layers keep running by themselves. The robot still avoids obstacles even while a higher layer is steering.
- There is **no central world model**. Each layer reacts directly to what the sensors report.

Because each layer works alone, the system is **robust** and each layer can be **tested separately**.

```text
Higher layers (goals, exploring)
        ↓  can interfere with
Middle layers (wandering)
        ↓  can interfere with
Lowest layer (avoid obstacles)
        ↓
      Motors
```

To keep our example simple, the next section uses a **priority list**. Brooks's real design is more detailed, but the key idea is the same: simple behaviors, combined, with no master plan.

## **F. Worked Example: A Robot with Priorities**

Take the obstacle-avoiding robot from Part 1 and add a **light sensor** and two more behaviors. The behaviors, from highest to lowest priority:

| **Priority** | **Behavior** | **Rule** |
|---|---|---|
| 1 (highest) | Avoid | If distance < 20 cm: stop and turn right |
| 2 | Go to light | If bright light is detected ahead: move toward the light |
| 3 (lowest) | Wander | Always active: move forward |

```text
Ultrasonic sensor ──► [1 Avoid]        ──┐
Light sensor      ──► [2 Go to light]  ──┼──► Highest-priority active behavior ──► Motors
(always active)   ──► [3 Wander]       ──┘
```

**Tracing four moments:**

| **Moment** | **Distance** | **Light ahead?** | **Active behaviors** | **Winner** | **Robot does** |
|---|---|---|---|---|---|
| 1 | 80 cm | No | Wander | Wander | Moves forward |
| 2 | 45 cm | Yes | Go to light, Wander | Go to light | Moves toward the light |
| 3 | 15 cm | Yes | Avoid, Go to light, Wander | **Avoid** | Stops and turns right |
| 4 | 70 cm | Yes | Go to light, Wander | Go to light | Moves toward the light |

At moment 3 the robot wants to reach the light, but the Avoid behavior wins because it protects the robot. This is the reason safety behaviors get the highest priority.

## **G. Reward-Based Learning (Brief Introduction)**

In Part 1, a person writes the behavior rules. In **reinforcement learning (RL)**, the robot adjusts its behavior from **experience**. It tries actions, receives a **reward** (a number, positive or negative) after each one, and learns over many attempts which action in which situation leads to more reward.

**Example:** a robot gets +1 for each second it moves without bumping and -10 for each bump. At first it turns randomly. After many trials it learns to turn **before** it gets too close to a wall.

**Link to behaviorism:** this resembles Skinner's operant conditioning, because consequences shape future behavior. It is an analogy again. In RL the reward is only a number that the designer chooses, and the robot does not "feel" anything.

## **H. Limits of Behavior-Based AI (Brief Introduction)**

- **No long-term planning or memory.** A robot with only reactive rules does not know the layout of a room. It can get stuck, for example turning right at one wall, then right at the next, and spinning in a dead end.
- **Many behaviors are hard to predict.** As more behaviors are added, their interactions become harder to understand.
- **Poor at tasks that need reasoning**, such as playing chess or answering questions.

**Symbolic AI** is stronger at reasoning, planning and explaining decisions, but it needs an accurate model, can be slow, and can fail when the world changes. Many real robots therefore **combine both**: a reactive layer for fast safety behavior and a planning layer for goals.

## **I. Ethical Questions (Brief Introduction)**

- **Safety and responsibility:** if a robot's rules fail and someone is hurt, who is responsible? This is one reason safety behaviors get top priority and need careful testing.
- **Badly designed rewards:** a learning robot rewarded only for "not bumping" might learn to never move. Designers must check what the robot really learns.
- **Human control:** can a person stop the robot at any time?
- **Explainability:** simple rules are easy to inspect, but learned behavior is harder to explain.

## **J. Putting It Together: Hardware, Network and Behavior**

Imagine the obstacle-avoiding robot has a microcontroller with **Wi-Fi** and sends its distance readings to a phone app.

| **Question** | **Answer** |
|---|---|
| Which hardware senses? | The ultrasonic sensor (distance) and the light sensor |
| Which network link carries the data? | The Wi-Fi link between the robot and the phone. Readings travel as packets, and IP addresses identify the robot and the phone (see the Networks part of this guide) |
| Which behavior rule decides the action? | The Avoid rule: if distance < 20 cm, stop and turn right |

**Design note:** the Avoid rule runs **on the robot itself**, not over the network. A delayed or lost Wi-Fi packet could make the robot stop too late. The network carries monitoring data and optional commands, while the safety behavior stays local.

## **K. Practice Activity**

Use the robot and priority table from Section F.

**Question 1.** For each situation, state which behaviors are active, which one wins, and what the robot does.

| **Situation** | **Distance** | **Light ahead?** |
|---|---|---|
| a | 80 cm | No |
| b | 80 cm | Yes |
| c | 12 cm | Yes |
| d | 12 cm | No |

**Question 2.** Suppose *Go to light* had a **higher** priority than *Avoid*. What would the robot do in situation c, and why is this a problem?

**Question 3.** In the Wi-Fi example (Section J), name: (i) the hardware that senses, (ii) the network link, and (iii) the behavior rule that decides to stop.

### **Answer Key**

**Question 1:**

- **a:** Only Wander is active, so the robot moves forward.
- **b:** Go to light and Wander are active. Go to light has the higher priority, so the robot moves toward the light.
- **c:** Avoid, Go to light and Wander are all active. Avoid has the highest priority, so the robot stops and turns right.
- **d:** Avoid and Wander are active. Avoid wins, so the robot stops and turns right.

**Question 2:** The robot would keep driving toward the light and hit the obstacle. This shows why behaviors that protect the robot must have the highest priority.

**Question 3:** (i) the ultrasonic sensor; (ii) the Wi-Fi link carrying packets between the robot and the phone; (iii) the Avoid rule ("distance < 20 cm: stop and turn right"), which runs on the robot.

## **Terminology (Part 2)**

- **Behaviorism** - an approach in psychology that studies observable behavior.
- **Classical conditioning** - learning to connect two events that occur together (Pavlov).
- **Operant conditioning** - learning in which consequences, such as rewards and punishments, change future behavior (Skinner).
- **Internal model (world model)** - a map or description of the world that a system builds and uses to plan.
- **Symbolic AI** - AI that represents knowledge as symbols and reasons about them.
- **Behavior-based AI** - AI in which intelligence comes from simple behaviors that respond directly to the environment.
- **Subsumption architecture** - Brooks's layered way of organizing behaviors.
- **Layer** - one complete, simple behavior in a layered system.
- **Priority** - the rank that decides which active behavior controls the robot.
- **Reward** - a number given to a learning system after an action, showing how good the result was.
- **Reinforcement learning (RL)** - learning from experience by trying actions and receiving rewards.
- **Hybrid system** - a system that combines reactive behavior with planning.

## **Conclusion (Part 2)**

Behaviorist AI borrows the focus on observable behavior from psychology, but it is an engineering approach. By layering simple behaviors and giving them priorities, a robot can act sensibly without a model of the world, with safety behaviors always coming first. Reward-based learning adds the ability to improve from experience. Behavior-based AI is fast and robust but weak at long-term planning, which is why it is often combined with symbolic methods.

## **References**

1. Brooks, R. A. (1986). A robust layered control system for a mobile robot. *IEEE Journal of Robotics and Automation, 2*(1), 14-23.
2. Brooks, R. A. (1991). Intelligence without representation. *Artificial Intelligence, 47*(1-3), 139-159.
3. Murphy, R. R. *Introduction to AI Robotics.* MIT Press.
4. Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
5. Brookshear, J. G., Smith, D., & Brylow, D. (2012). *Computer Science: An Overview* (11th ed.). Pearson. (Chapter 11, Artificial Intelligence.)
