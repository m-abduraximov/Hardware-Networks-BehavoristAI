# Behaviorist AI: Robots That Act Before They Think

*Version 2.0, rewritten and expanded from the first draft.*

Team: Team DeepThink\
Module: Hardware, Networks and Behaviorist AI\
Chapter: Behaviorist AI\
Version: V2.0 (Stage 2, Markdown Content)\
Audience: first-year university students and school graduates with no previous AI or robotics background

> A note on spelling. The module title uses the British spelling *Behaviourist*. In this chapter we use the American spelling *behavior* and *behaviorism* everywhere, because that is how the main sources spell them. They mean the same thing.

—

## Contents

- [Unit 0. Start Here](unit-00-start-here.md)
- [Unit 1. Behaviorism: Learning from Behavior](unit-01-behaviorism-learning-from-behavior.md)
- [Unit 2. Reactive Agents and the Sense-Act Loop](unit-02-reactive-agents-and-the-sense-act-loop.md)
- [Unit 3. Behavior Rules and Priorities](unit-03-behavior-rules-and-priorities.md)
- [Unit 4. Brooks’s Subsumption Architecture](unit-04-brooks-subsumption-architecture.md)
- [Unit 5. Case Study: Hardware, Network and Behavior in One Robot](unit-05-case-study.md)
- [Unit 6. Three Short Introductions: Reinforcement Learning, Limits and Ethics](unit-06-rl-limits-and-ethics.md)
- [Unit 7. Review and Final Challenge](unit-07-review-and-final-challenge.md)
- [Glossary](glossary.md)
- [References](references.md)

  # Unit 0. Start Here

## 0.1 The big question

Imagine you have to build a small robot that drives around a room without crashing into anything.

There are two very different ways to do it:

1. Think first. The robot builds a detailed map of the room, plans a perfect route, and only then moves.
2. React. The robot just looks at what is directly in front of it and, if something is in the way, turns. It does this again and again, many times per second.

The second way sounds too simple to be “intelligent”. Yet in the 1980s the roboticist Rodney Brooks showed that robots built in this way could do surprisingly well. This chapter explains how they work, where the idea comes from, where it breaks down, and how it connects to the hardware and networks you studied in the other chapters.

## 0.2 What you will learn

By the end of this chapter you will be able to:

Core topics (studied in detail)

1. Explain the basic ideas of behaviorism in psychology, with the examples of Pavlov and Skinner.
2. Explain why “Behaviorist AI” is an analogy and not a direct application of psychology.
3. Define a reactive agent and describe the sense-act loop.
4. Identify the sensor, controller and actuator in a simple robot.
5. Write behavior rules (IF condition THEN action) and predict what a robot does when several rules apply.
6. Use priorities to decide which behavior controls the robot.
7. Describe Rodney Brooks’s subsumption architecture and its layers in simple words.
8. Follow a case study in which hardware (sensors, microcontroller, motors), a network (Wi-Fi, packets, delay) and behavior rules work together, and explain why the safety behavior must run on the robot itself.

Short introductions (overview level)

9. Describe what reinforcement learning is and how rewards and punishments are used.
10. State the main limitations of behavior-based AI compared with symbolic AI.
11. Name important ethical questions raised by AI systems that act in the real world.

## 0.3 What you should know before you start

You do not need any programming experience. You only need a few ideas from the other chapters of this guide. Here is a quick refresher so that this chapter can be read on its own.

| Idea | One-sentence reminder | Where it comes from |
|—|—|—|
| Sensor | A device that measures something in the world (distance, light, temperature). | Hardware chapter |
| Microcontroller | A tiny computer on one chip that reads sensors and controls other devices. | Hardware chapter |
| Actuator / motor | A device that makes something move. | Hardware chapter |
| Packet | A small piece of data sent across a network. | Networks chapter |
| IP address | A number that identifies a device on a network, for example 192.168.1.50. | Networks chapter |
| Wi-Fi | A wireless way to connect devices to a local network. | Networks chapter |
| Latency (delay) | The time a message needs to travel from sender to receiver. | Networks chapter |

## 0.4 How to use this chapter (suggested route)

| Step | Unit | What you do | Time |
|—|—|—|—|
| 1 | Unit 1 | Learn where the word “behaviorist” comes from. Sort real-life examples. | 30-40 min |
| 2 | Unit 2 | Meet the reactive agent. Trace a robot on paper. | 40-50 min |
| 3 | Unit 3 | Write rules, solve conflicts with priorities, trace a program. | 40-50 min |
| 4 | Unit 4 | Learn Brooks’s layers. Design a layered robot. | 40-50 min |
| 5 | Unit 5 | Follow the case study: hardware, network and behavior together. | 50-60 min |
| 6 | Unit 6 | Three short introductions (reinforcement learning, limits, ethics). | 30-40 min |
| 7 | Unit 7 | Review, fix misconceptions, final design challenge. | 40-60 min |

You need: pen and paper (or a notes app). A computer with Python 3 is useful for the “Run it” activities, but every Python activity also has a paper version and a printed expected result, so you can complete the chapter without installing anything. If you want to run Python without installing it, you can paste the code into any online Python editor.

## 0.5 Labels used in this chapter

| Label | Meaning |
|—|—|
| Think | A question to consider before you read the explanation. |
| Example | A fully worked example. Follow every step. |
| Activity | A hands-on task with Goal, Preparation, Task, Observation, Reflection and Feedback. |
| Misconception alert | A common wrong idea, and the correct version. |
| Check yourself | Quick questions. Answers are in the Answer key at the end of each unit. |
| Key idea | The one thing to remember from a section. |


## Unit 1. Behaviorism: Learning from Behavior

**Question for this unit:** *If you cannot see inside a mind, what can you still study?*

### 1.1 Think first

A dog cannot tell you what it is thinking. A rat cannot describe its feelings. A robot has no "feelings" at all. What can a scientist (or an engineer) actually **observe and measure** in each case?

*(Write down your answer, then read on.)*

### 1.2 What is behaviorism?

**Behaviorism** is an approach in psychology that studies **observable behavior**, meaning what a living thing visibly does, instead of guessing about invisible thoughts and feelings. The American psychologist **John B. Watson** argued for this approach in 1913. In his view the mind could be treated like a **black box**: we can see what goes in (a **stimulus**, something in the environment) and what comes out (a **response**, something the animal does), and we can study the connection between them.

```text
Stimulus  ──►  [ black box ]  ──►  Response
(what happens)                      (what the animal does)
```

Behaviorists were especially interested in **learning**: how experience changes behavior. Two scientists became famous for describing two basic kinds of learning.

### 1.3 Pavlov and classical conditioning

**Ivan Pavlov** (1849-1936) was a Russian physiologist who received the Nobel Prize in Physiology or Medicine in 1904 for his research on digestion. While studying how dogs produce saliva when they eat, he noticed something unexpected: after some time the dogs started to salivate **before** they received food, for example when they heard the footsteps of the person who fed them.

He then tested this carefully. In the story as it is usually told, he rang a bell just before giving food. (In his laboratory he used several kinds of signals, such as a metronome, a buzzer or a bell.) After many repetitions, the dogs salivated at the sound alone. This kind of learning is called **classical conditioning**: an animal learns to **connect two events that happen together**.

| Stage | What happens | Name of the parts |
|---|---|---|
| **Before training** | Food → the dog salivates. The bell alone → no salivation. | Food = **unconditioned stimulus**. Salivation = **unconditioned response** (natural, not learned). Bell = **neutral stimulus**. |
| **During training** | Bell, then food, repeated many times. | The bell and the food are **paired**. |
| **After training** | Bell alone → the dog salivates. | Bell = **conditioned stimulus**. Salivation to the bell = **conditioned response** (learned). |

If the bell is rung many times **without** food, the response gradually weakens. This is called **extinction**.

**Key idea:** in classical conditioning, the animal learns that one signal **predicts** another. The animal does not need to do anything special; the response happens automatically.

### 1.4 Skinner and operant conditioning

**B. F. Skinner** (1904-1990) was an American psychologist. Building on earlier work by Edward Thorndike (the "law of effect": actions followed by satisfying results become more likely), Skinner studied how the **consequences of an action** change the chance that the action is repeated. He used an apparatus now called an **operant conditioning chamber** (often nicknamed the "Skinner box"). A hungry rat in the box can press a lever. If pressing the lever delivers a food pellet, the rat presses the lever more and more often.

This kind of learning is called **operant conditioning**: the animal **acts on its environment** and learns from the **consequence**.

There are four basic kinds of consequence. Two words decide which one you have:

- **Positive / negative** means something is **added** (positive) or **removed** (negative). It has nothing to do with good or bad.
- **Reinforcement / punishment** means the behavior becomes **more likely** (reinforcement) or **less likely** (punishment).

| | **Something is added** (positive) | **Something is removed** (negative) |
|---|---|---|
| **Behavior becomes MORE likely** (reinforcement) | **Positive reinforcement.** A rat gets food after pressing a lever. | **Negative reinforcement.** A car's seat-belt warning sound stops when you buckle up, so you buckle up more quickly next time. |
| **Behavior becomes LESS likely** (punishment) | **Positive punishment.** A dog touches a hot stove, feels pain, and avoids it. | **Negative punishment.** A child loses video-game time after hitting a sibling, so hitting becomes less likely. |

> **Misconception alert.** *"Negative reinforcement is a kind of punishment."* **No.** Both kinds of reinforcement make a behavior **more** likely. Negative reinforcement works by **removing** something unpleasant (the annoying beep stops). Punishment makes a behavior **less** likely.

### 1.5 Why do AI students study behaviorism?

Behaviorism is useful for AI in three ways.

1. **It focuses on what a system does.** In 1950 Alan Turing proposed judging whether a machine can "think" by looking at its **behavior** in a conversation, not by looking inside it. Judging by behavior is in the same spirit as behaviorism.
2. **It links stimulus and response.** A robot's sensor reading is like a stimulus and its motor action is like a response. This is the idea behind the rule *IF an obstacle is detected THEN turn* in the next units.
3. **It inspired the language of reward and punishment** used in reinforcement learning (Unit 6).

| Idea in behaviorism | Matching idea in AI and robotics |
|---|---|
| Observable behavior | We judge a robot by what it does. |
| Stimulus → response | Sensor reading → action (a behavior rule). |
| Reinforcement and punishment | Positive and negative rewards in reinforcement learning. |
| The mind as a black box | A behavior-based robot does not need a detailed model of the world inside it. |

> **Key idea: "Behaviorist AI" is an analogy.** Engineers such as Rodney Brooks did **not** build robots by applying Skinner's psychology. Behavior-based robotics was developed as an **engineering approach**. We call it "behaviorist" because it shares two ideas with behaviorism: it focuses on **observable behavior**, and it treats intelligent behavior as something that comes from **direct interaction with the environment**. The closest real connection to behaviorism is **reward-based learning**.
>
> Also remember that behaviorism has limits in psychology: in 1959 the linguist Noam Chomsky argued that it could not explain how humans learn language, and psychology later moved towards the study of mental processes (the "cognitive revolution"). A robot that only reacts is a useful engineering idea, but it is not a complete theory of intelligence. Unit 6 returns to this point.

### 1.6 Activity 1.1: Spot the Conditioning

**Goal.** Tell classical conditioning from operant conditioning, and identify the four kinds of consequence.

**Preparation.** Re-read sections 1.3 and 1.4. Pen and paper.

**Task.** For each situation, decide: **(A)** is it classical or operant conditioning? **(B)** If operant, which of the four consequences is it? **(C)** Name the stimulus/response or the behavior/consequence.

| # | Situation |
|---|---|
| 1 | A child receives a sticker every time she tidies her room, and starts tidying more often. |
| 2 | Your phone makes a short sound before every message. After a few weeks you glance at the phone as soon as you hear the sound, even when you are not expecting anything. |
| 3 | A car beeps until the driver fastens the seat belt. The driver learns to fasten it immediately. |
| 4 | A student is late for class three times and each time must clean the whiteboard. He becomes less late. (Treat cleaning as something unpleasant that is **added**.) |
| 5 | A cat runs to the kitchen whenever it hears the electric can opener, which is always followed by food. |
| 6 | A gamer is banned from the online game for a week after cheating and stops cheating. (Treat the ban as something pleasant that is **removed**.) |

**Observation.** Fill in a table with the columns: *Situation | Classical or operant | Type of consequence | What is the stimulus/response or behavior/consequence*.

**Reflection.** Which cases were hardest to decide, and why? What question can you ask yourself to separate the two kinds of conditioning? (Hint: *Does the animal's own action change what happens next?*)

**Feedback.** See the answer key at the end of this unit.

### 1.7 Check yourself (Unit 1)

1. In Pavlov's experiment, what is the **conditioned stimulus** after training?
2. A video game gives bonus points when you finish a level quickly. Which kind of consequence is this?
3. True or false: *Negative reinforcement means the same as punishment.*
4. In two sentences, explain why "Behaviorist AI" is only an **analogy** to psychological behaviorism.
5. A fitness app vibrates continuously when you sit too long, and the vibration stops as soon as you stand up. Which kind of consequence is this, and what behavior does it strengthen?

### 1.8 Answer key (Unit 1)

**Activity 1.1**

| # | Type | Consequence | Explanation |
|---|---|---|---|
| 1 | Operant | Positive reinforcement | Behavior: tidying. Consequence: a sticker is **added**; tidying becomes **more** likely. |
| 2 | Classical | (not applicable) | The sound (neutral stimulus) is paired with a message. The sound becomes a conditioned stimulus and glancing at the phone is the conditioned response. |
| 3 | Operant | Negative reinforcement | Behavior: fastening the belt. Consequence: the beep is **removed**; fastening becomes **more** likely. |
| 4 | Operant | Positive punishment | Behavior: being late. Consequence: an unpleasant task is **added**; lateness becomes **less** likely. |
| 5 | Classical | (not applicable) | The can opener sound (neutral stimulus) is paired with food. The sound becomes a conditioned stimulus and running to the kitchen is the conditioned response. |
| 6 | Operant | Negative punishment | Behavior: cheating. Consequence: access to the game is **removed**; cheating becomes **less** likely. |

*Reflection (sample).* The test question is: *does the animal's own action produce the consequence?* In classical conditioning the animal does nothing to cause the food; the signal simply predicts it. In operant conditioning, the animal's action (pressing, tidying, cheating) produces the consequence.

**Check yourself**

1. The **bell** (the sound).
2. **Positive reinforcement**: points are added and finishing quickly becomes more likely.
3. **False.** Negative reinforcement makes a behavior more likely by removing something unpleasant. Punishment makes a behavior less likely.
4. Behavior-based robots were developed as an engineering method and not by applying Skinner's or Pavlov's theories. They only share the focus on observable behavior and on interaction with the environment, and the idea of reward in learning, so the connection is an analogy.
5. **Negative reinforcement.** The unpleasant vibration is removed, and the behavior of standing up becomes more likely.

---

## Unit 2. Reactive Agents and the Sense-Act Loop

**Question for this unit:** *Can a robot behave sensibly without any memory, map or plan?*

### 2.1 Think first

You walk through a dark room holding your hands in front of you. When your hand touches something, you step to the side. You do not draw a map first. Which parts of this behavior are **sensing**, **deciding** and **acting**?

### 2.2 Agents, environments and actions

In AI, an **agent** is anything that **perceives its environment through sensors and acts on it through actuators** (Russell & Norvig, 2021). The **environment** is everything around the agent that it can sense or change.

| Agent | Environment | Sensors | Actuators |
|---|---|---|---|
| Robot vacuum cleaner | A room with furniture | Bumper, distance and floor sensors | Wheels, brush motors |
| Thermostat | A room | Temperature sensor | Heater switch |
| Our obstacle-avoiding robot | A table or floor with obstacles | Ultrasonic sensor | Wheel motors |

### 2.3 What is a reactive agent?

A **reactive agent** chooses its action using **only the information that its sensors give it right now**. It has no memory of the past, no map of the world and no plan for the future. In the textbook by Russell and Norvig this type is called a **simple reflex agent**.

A reactive agent is like a **reflex**: when a hot object touches your hand, you pull the hand away immediately, before you have "thought" about it.

A thermostat is the simplest example:

```text
IF the temperature is below 20 °C THEN switch the heater on.
IF the temperature is 20 °C or higher THEN switch the heater off.
```

A thermostat does not remember yesterday's temperature and does not plan tomorrow's. It reacts to the **current** reading.

> **Key idea:** a reactive agent turns **current sensor information** directly into an **action**.

**Reactive agents are useful because** they are simple to design, they react quickly, they are easy to test (each rule can be tested alone), and they work well in **dynamic environments**, meaning environments that change while the agent is working (people walk by, doors open, chairs move).

### 2.4 The sense-act loop

A reactive agent repeats the same cycle many times per second:

```text
Sense  →  Decide  →  Act  →  Sense again  →  ...
```

| Step | What happens | In our robot |
|---|---|---|
| **Sense** | A **sensor** measures the environment. | The ultrasonic sensor measures the distance to the object in front. |
| **Decide** | The **controller** applies a behavior rule to the new information. | The microcontroller checks: *is the distance less than 20 cm?* |
| **Act** | An **actuator** performs the chosen action. | The motors drive forward, or stop and turn. |
| **Sense again** | The action has changed the world, so the robot measures again. | New distance reading, new decision. |

The full picture:

```text
        ┌─────────────────────────── Environment ◄────────────────────┐
        │                                                              │
        ▼                                                              │
     Sensor ──► Controller (applies behavior rules) ──► Actuator ──► Action
   (measures)        (decides)                         (moves)    (changes the world)
```

Notice the loop shape: the robot's own action **changes** the environment, and the changed environment is what the robot senses next. This is why the loop never stops.

### 2.5 The three hardware parts

| Part | Job | Examples |
|---|---|---|
| **Sensor** | Collects information from the environment. | Ultrasonic sensor (distance), light sensor, temperature sensor, camera. |
| **Controller** | Processes the information and chooses an action. | A microcontroller running the rules. |
| **Actuator** | Performs the physical action. | A wheel motor, a servo, a buzzer. |

*Why can a microcontroller not drive a motor directly?* A microcontroller's output pins can only supply a very small current. Motors need much more, so a **motor driver** board sits between them. The microcontroller sends the small "forward/stop/turn" signals and the motor driver switches the larger current from the battery. You will see this in the case study (Unit 5).

### 2.6 Example: how an ultrasonic sensor measures distance

An **ultrasonic sensor** sends out a short burst of sound that humans cannot hear, then waits for the **echo**. The longer the echo takes, the farther away the object is. Sound travels at about **343 m/s** in air at 20 °C. The sound must travel to the object **and back**, so the distance is half of what the sound covers:

```text
distance = (speed of sound × echo time) ÷ 2
```

**Worked example 1.** The echo comes back after **2915 microseconds** (0.002915 s).

```text
distance = (343 m/s × 0.002915 s) ÷ 2
         = 0.9999 m ÷ 2
         ≈ 0.50 m = 50 cm
```

**Worked example 2.** What echo time corresponds to **15 cm** (0.15 m)?

```text
echo time = (2 × distance) ÷ speed = (2 × 0.15 m) ÷ 343 m/s ≈ 0.000875 s = 875 microseconds
```

So the microcontroller does not "see" the obstacle. It measures a **time** and converts it to a **number** (a distance), and the behavior rule works with that number. (Hobby sensors of this type typically work from a few centimetres up to a few metres, and real readings are noisy: the number can jump by a centimetre or more between measurements.)

### 2.7 Worked example: the obstacle-avoiding robot

The robot follows one rule set:

```text
IF distance < 20 cm  THEN stop and turn right.
OTHERWISE            move forward.
```

| Loop | Sense (distance) | Decide | Act | What changes |
|---|---|---|---|---|
| 1 | 50 cm | 50 cm is not less than 20 → *move forward* | Motors forward | The robot gets closer to the obstacle. |
| 2 | 15 cm | 15 cm is less than 20 → *stop and turn* | Motors stop, then turn right | The robot now faces another direction. |
| 3 | 70 cm | 70 cm is not less than 20 → *move forward* | Motors forward | The path ahead is clear. |

The robot never knows where the table is or where it wants to go. At each moment it only knows **one number**. Yet it avoids the obstacle. This is a **reactive agent**.

### 2.8 Activity 2.1: Be the Robot (paper trace)

**Goal.** Understand the sense-act loop by executing it yourself, step by step, and discover what a reactive rule can and cannot do.

**Preparation.** Pen and paper. Draw a grid of **5 × 5 squares** (the floor of a room). Imagine the room is surrounded by a wall. Mark the top-left square as **START**. Number the rows 1 to 5 from top to bottom and the columns 1 to 5 from left to right.

**The robot's rules.** The robot always faces one of four directions (North = up, East = right, South = down, West = left). Each **step** it does exactly one thing:

```text
SENSE:  look at the square directly ahead.
DECIDE/ACT:
   IF the square ahead is a wall  THEN turn 90° to the right (and stay in the same square).
   OTHERWISE                      move forward one square.
```

Turning counts as one step, and moving counts as one step.

**Task.**
1. Put the robot on START (row 1, column 1), **facing East**.
2. Execute **10 steps**. After each step, draw the robot's path.
3. Continue to **20 steps**.
4. Count how many **different squares** the robot has visited after 10 steps and after 20 steps (including START).
5. **Predict** first: will the robot eventually visit every square, including the one in the centre? Write your prediction **before** you trace.

**Observation.** Record: the path you drew, the two counts, and whether the centre square (row 3, column 3) was ever visited.

**Reflection.** Does the robot behave "intelligently"? What would it need to **remember** or **plan** in order to cover the whole room?

**Feedback.** See the answer key.

**Run it (optional).** The Python program below does exactly the same steps. Read the comments first: each line marked SENSE, DECIDE or ACT matches a part of the loop. Run it and compare its result with your paper trace.

```python
# A reactive robot in a 7 x 7 map. '#' = wall, '.' = free floor.
# The free floor is the 5 x 5 area inside the walls.
ROOM = [
    "#######",
    "#.....#",
    "#.....#",
    "#.....#",
    "#.....#",
    "#.....#",
    "#######",
]
# Headings: 0 = north, 1 = east, 2 = south, 3 = west.
# Each heading is a (change in row, change in column) pair.
MOVES = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def run(steps):
    row, col, heading = 1, 1, 1           # start top-left, facing east
    visited = {(row, col)}                # a set remembers squares for COUNTING only
    for _ in range(steps):                # repeat the loop 'steps' times
        d_row, d_col = MOVES[heading]
        ahead = ROOM[row + d_row][col + d_col]      # SENSE: what is ahead?
        if ahead == "#":                            # DECIDE: is it a wall?
            heading = (heading + 1) % 4             # ACT: turn right
        else:
            row, col = row + d_row, col + d_col     # ACT: move forward
            visited.add((row, col))
    return visited

for n in (10, 20, 100):
    print(n, "steps ->", len(run(n)), "different squares visited out of 25")
print("Centre square visited after 100 steps?", (3, 3) in run(100))
```

*Syntax help.* `def run(steps):` defines a reusable block of instructions called a function. `for _ in range(steps):` repeats the indented lines `steps` times. `if ... else ...` chooses between two actions. `%` gives the remainder of a division, so `% 4` makes the heading wrap from 3 (west) back to 0 (north). A **set** (`visited`) stores each square once. The `visited` set is only used to count squares for us; the robot's rule never looks at it.

**Expected output.**

```text
10 steps -> 9 different squares visited out of 25
20 steps -> 16 different squares visited out of 25
100 steps -> 16 different squares visited out of 25
Centre square visited after 100 steps? False
```

### 2.9 Check yourself (Unit 2)

1. Name the three hardware parts of a simple reactive system and give one example of each.
2. An echo returns after 1166 microseconds. Using 343 m/s, what is the distance? (Give your answer in centimetres, rounded to the nearest centimetre.)
3. Why is a thermostat a reactive agent?
4. Why does the sense-act loop have to **repeat**? What would happen if the robot sensed only once?
5. **Find the error.** A student says: *"The robot remembers that there was a wall to its right, so it turns left."* Why does this not describe the robot in Activity 2.1?

### 2.10 Answer key (Unit 2)

**Activity 2.1**

- **Path.** From START the robot moves East along the top row to column 5 (4 moves). Then the next square is a wall, so it turns right (now facing South, 1 step). It moves down to row 5 (4 moves), turns (West), moves to column 1 (4 moves), turns (North), moves up to row 1 (4 moves), and turns (East). That is **20 steps** and it is back at START facing East. After that, it repeats the same lap forever.
- **Squares visited:** after **10 steps = 9 squares** (4 + 4 moves + START); after **20 steps = 16 squares** (all squares along the walls).
- **Centre square:** **never visited.** The 9 squares in the middle (a 3 × 3 block) are never reached.
- **Reflection (sample).** The robot reacts correctly to each wall, but it has no memory of where it has been and no goal such as "cover every square", so it circles the edge of the room. To cover the room it would need to remember visited squares, or have a plan, or have an additional behavior such as an occasional random turn. This is one limit of purely reactive behavior (Unit 6).

**Check yourself**

1. **Sensor** (ultrasonic sensor), **controller** (microcontroller), **actuator** (wheel motor). Other correct examples are acceptable.
2. distance = (343 × 0.001166) ÷ 2 = 0.3999 ÷ 2 ≈ 0.20 m = **20 cm**.
3. It chooses its action only from the **current** temperature reading, without memory or a plan.
4. After each action the environment is different (the robot has moved), so the robot must measure again to know the new situation. If it sensed only once, it would keep acting on outdated information and could drive into the obstacle.
5. The robot in Activity 2.1 has **no memory**. Its rule only looks at the square directly ahead right now and always turns **right**.

---
## Unit 3. Behavior Rules and Priorities

**Question for this unit:** *What should a robot do when two of its rules want different things at the same moment?*

### 3.1 Think first

Your robot has two rules: *"If there is bright light ahead, drive towards it"* and *"If an obstacle is closer than 20 cm, stop."* A lamp is on the other side of a glass wall. Both rules are true at the same time. Which one should win, and why?

### 3.2 Behavior rules

A **behavior** is a specific way in which an agent responds to a situation (for example "avoid" or "wander"). A **behavior rule** connects a **condition** (a situation the sensors can detect) with an **action**:

```text
IF condition THEN action
```

A **condition** is something the controller can check with a yes/no answer using sensor data, such as `distance < 20 cm`. An **action** is something the actuators can do, such as `stop and turn right`.

| Condition | Action |
|---|---|
| Path is clear | Move forward |
| Obstacle in front | Stop |
| Obstacle on the left | Turn right |
| Obstacle on the right | Turn left |
| Path is blocked on all sides | Turn around |

Look carefully at this table. **More than one condition can be true at once.** "Obstacle in front" and "Obstacle on the left" can both be true when the robot is facing a corner. The table does not say which action to perform. We need a method to decide.

### 3.3 Priorities decide conflicts

The simplest method is a **priority**: every behavior gets a **rank**, and the **highest-priority active behavior controls the motors**. A behavior is **active** when its condition is true. The lower-priority active behaviors are ignored for now.

> **Convention used in this guide.** Rank **1 is the highest priority**. A bigger number means a lower priority.

Behaviors that protect the robot and the people around it normally get the **highest priority**. This is a **design decision** made by the engineer, and it should always be explained.

### 3.4 Example: a robot with three behaviors

We extend the obstacle-avoiding robot with a **light sensor** and two more behaviors.

| Priority rank | Behavior | Rule |
|---|---|---|
| **1** (highest) | Avoid | `IF distance < 20 cm THEN stop and turn right` |
| **2** | Go to light | IF bright light is detected ahead THEN move towards the light |
| **3** (lowest) | Wander | Always active: move forward |

```text
Ultrasonic sensor ──► [1 Avoid]        ──┐
Light sensor      ──► [2 Go to light]  ──┼──► highest-priority ACTIVE behavior ──► Motors
(always active)   ──► [3 Wander]       ──┘
```

**Tracing four moments.**

| Moment | Distance | Light ahead? | Active behaviors | Winner | The robot... |
|---|---|---|---|---|---|
| 1 | 80 cm | No | Wander | Wander | moves forward |
| 2 | 45 cm | Yes | Go to light, Wander | Go to light | moves towards the light |
| 3 | 15 cm | Yes | Avoid, Go to light, Wander | **Avoid** | stops and turns right |
| 4 | 70 cm | Yes | Go to light, Wander | Go to light | moves towards the light |

At moment 3 the robot "wants" to reach the light, but **Avoid wins** because it protects the robot. This is why safety behaviors get the highest priority.

### 3.5 The same idea as a program

Below is the same robot written in Python. The order of the `if` statements **is** the priority order: Python checks them from top to bottom and `return` stops at the first one that is true.

```python
def choose_behavior(distance_cm, light_ahead):
    """Return the name of the winning behavior (highest priority first)."""
    if distance_cm < 20:                       # priority 1: Avoid
        return "AVOID: stop and turn right"
    if light_ahead:                            # priority 2: Go to light
        return "GO TO LIGHT: move toward the light"
    return "WANDER: move forward"              # priority 3: Wander (always possible)

situations = [
    ("a", 80, False),
    ("b", 80, True),
    ("c", 12, True),
    ("d", 12, False),
]
for name, dist, light in situations:
    print(name, dist, "cm, light:", light, "->", choose_behavior(dist, light))
```

*Syntax help.* `distance_cm < 20` is a yes/no test. `light_ahead` is either `True` or `False`. `return` ends the function and hands back a result. A list of items in square brackets, such as `situations`, is walked through by the `for` loop one item at a time.

**Expected output.**

```text
a 80 cm, light: False -> WANDER: move forward
b 80 cm, light: True -> GO TO LIGHT: move toward the light
c 12 cm, light: True -> AVOID: stop and turn right
d 12 cm, light: False -> AVOID: stop and turn right
```

### 3.6 Choosing priorities is a design decision

Is "Avoid obstacles" always the most important behavior? Not always. A robot vacuum cleaner near a staircase has a **cliff sensor** that points at the floor. If the floor suddenly disappears, the robot must stop **even if** no obstacle is detected, and even if it is just in the middle of avoiding an obstacle. Falling down the stairs is worse than bumping into a chair. So the designer adds a behavior **Cliff stop** and gives it rank 1, and Avoid becomes rank 2.

A good habit: when you rank behaviors, ask **"which failure would be the most harmful?"** and give the highest rank to the behavior that prevents it.

### 3.7 A common problem: flickering at a threshold

A rule such as `distance < 20 cm` has a sharp edge. Suppose the sensor readings (which are always a little noisy) hover around the limit: 22, 21, 19, 21, 19, 22 cm. With a single threshold the robot switches between *Wander* and *Avoid* again and again, which makes it jerk back and forth.

A simple fix is to use **two thresholds** (this idea is called **hysteresis**): *enter* Avoid when the distance is **below 20 cm**, but *leave* Avoid only when the distance is **above 30 cm**.

| Reading (cm) | 22 | 21 | 19 | 21 | 19 | 22 |
|---|---|---|---|---|---|---|
| **One threshold (20 cm)** | Wander | Wander | Avoid | Wander | Avoid | Wander |
| **Two thresholds (enter `<20`, leave `>30`)** | Wander | Wander | Avoid | Avoid | Avoid | Avoid |

With one threshold the behavior changes **4 times**. With two thresholds it changes **once**. (This table treats the readings as given, to show the idea. On a real robot the readings would also be changed by the robot's own movement.)

### 3.8 Activity 3.1: Predict, Trace and Debug

**Goal.** Use priorities to predict the behavior of a robot, explain a design decision, and find errors in a rule set.

**Preparation.** Read sections 3.3 to 3.7. Paper and pen. Python is optional: the program in 3.5 can be used to check Part A.

**Task.**

**Part A: Predict.** Use the three-behavior robot from section 3.4. For each situation, write the active behaviors, the winner, and what the robot does.

| Situation | Distance | Light ahead? |
|---|---|---|
| a | 80 cm | No |
| b | 80 cm | Yes |
| c | 12 cm | Yes |
| d | 12 cm | No |

**Part B: Change the priorities.** Suppose *Go to light* had a **higher** priority than *Avoid*. What would the robot do in situation **c**? Why is this a problem?

**Part C: Add a behavior.** Add a **Cliff stop** behavior as rank 1: *IF the floor sensor reports no floor ahead THEN stop and reverse.* Avoid becomes rank 2, Go to light rank 3, Wander rank 4. Predict the winner in each situation:

| Situation | Distance | Floor ahead? | Light ahead? |
|---|---|---|---|
| e | 80 cm | **No** | Yes |
| f | 12 cm | **No** | No |
| g | 12 cm | Yes | No |

**Part D: Find the error.** Two engineers wrote faulty designs. Describe what each robot will do and why.

- **Design 1:** rank 1 = Wander (always active: move forward), rank 2 = Avoid, rank 3 = Go to light.
- **Design 2:** the Avoid rule is written as *IF distance > 20 cm THEN stop and turn right* (with all other rules correct, and Avoid is rank 1).

**Part E: Hysteresis.** Apply the two-threshold rule (enter Avoid below 20 cm, leave Avoid above 30 cm) to the readings **25, 18, 24, 28, 31, 22**. Write the behavior (Wander or Avoid) for each reading. The robot starts in Wander.

**Observation.** Record the winner for every situation in a table, and your explanation for Parts B, D and E.

**Reflection.** Which of the errors in Part D would be easier to find by testing the robot in a room? Which would be easier to find by reading the rules? What does this tell you about testing each behavior separately?

**Feedback.** See the answer key.

### 3.9 Check yourself (Unit 3)

1. What does it mean when a behavior is *active*?
2. In this guide, is priority rank 1 the highest or the lowest priority?
3. Give one reason why a safety behavior usually gets the highest priority.
4. True or false: *The order of `if` statements in the program in section 3.5 does not matter.*

### 3.10 Answer key (Unit 3)

**Activity 3.1**

- **Part A.**
  - **a:** only Wander is active → robot **moves forward**.
  - **b:** Go to light and Wander are active; Go to light has the higher priority → **moves towards the light**.
  - **c:** Avoid, Go to light and Wander are all active; Avoid is rank 1 → **stops and turns right**.
  - **d:** Avoid and Wander are active; Avoid wins → **stops and turns right**.
- **Part B.** In situation c, Go to light would win, so the robot would keep driving towards the light and **hit the obstacle**. A behavior that protects the robot must not be overruled by a behavior that only pursues a goal.
- **Part C.**
  - **e:** Cliff stop, Go to light and Wander are active (distance is fine) → **Cliff stop wins**: stop and reverse.
  - **f:** Cliff stop, Avoid and Wander are active → **Cliff stop wins** (rank 1): stop and reverse, not "turn right". Turning right near an edge could be unsafe.
  - **g:** Avoid and Wander are active (floor is present) → **Avoid wins**: stop and turn right.
- **Part D.**
  - **Design 1:** Wander is *always active* and has the highest rank, so it **always wins**. The other behaviors never get control and the robot drives straight into obstacles.
  - **Design 2:** the condition is reversed. The robot stops and turns when the path is **clear** (distance > 20 cm), and does not react when an obstacle is **close**. It will spin on the spot in open space and drive into obstacles.
- **Part E.**

| Reading | 25 | 18 | 24 | 28 | 31 | 22 |
|---|---|---|---|---|---|---|
| Behavior | Wander | Avoid | Avoid | Avoid | Wander | Wander |

  The robot enters Avoid at 18 (below 20), stays in Avoid at 24 and 28 (not yet above 30), leaves Avoid at 31 (above 30), and stays in Wander at 22 because 22 is not below 20.
- **Reflection (sample).** Design 1 and Design 2 would both be noticed immediately in a room test, because the robot crashes or spins. A wrongly ordered or reversed rule is also easy to see when reading the rules one by one. Testing each behavior separately (for example "does Avoid alone stop at 19 cm and not at 21 cm?") finds such errors early, before behaviors are combined.

**Check yourself**

1. Its condition is currently true, so it wants to control the robot.
2. The **highest** priority.
3. Examples: failing to avoid a collision can hurt people or damage the robot, and the cost of that failure is higher than the cost of missing a goal; so the robot must always be able to protect itself first.
4. **False.** Python tests the statements from top to bottom and returns at the first true one, so the order **is** the priority order.
   

---

## Unit 4. Brooks's Subsumption Architecture

**Question for this unit:** How can many simple behaviors be organized so that a robot becomes more capable, without a master plan?

### 4.1 Think first

Suppose you want to build a robot in steps: first it must not crash, then it should wander around, then it should look for interesting places. Is it easier to build all three abilities at once, or one after another, testing each as you go?

### 4.2 The historical background

Early AI robots followed the sense, model, plan, act approach. The robot Shakey, built at SRI (Stanford Research Institute) in the late 1960s, is a famous example. It used cameras and sensors to build a symbolic description of its surroundings, planned a sequence of actions with logic, and then carried them out (Nilsson, 1984). This approach belongs to **symbolic AI**, which represents knowledge as symbols and reasons about them. It could solve interesting problems, but it was slow, and its plans could be wrong if the world changed while it was thinking.

In the mid-1980s Rodney Brooks, a roboticist at MIT, proposed a very different approach. He argued that intelligent behavior does not have to come from a central model of the world; it can come from many simple behaviors that connect sensing to acting directly. His slogan is that the world can serve as its own best model: why store and update a map if the robot can simply sense the real thing again? (Brooks, 1990, 1991.)

### 4.3 Layers: levels of competence

In his 1986 paper, Brooks described a robot control system built from layers. Each layer is a complete, simple behavior that goes from sensors to motors. He called these **levels of competence** (Brooks, 1986). The first three levels he describes are:

| Level | Competence | What the robot can do |
|---|---|---|
| 0 | Avoid contact with objects | Stay away from things; move away if something approaches. |
| 1 | Wander | Move around aimlessly without hitting things. |
| 2 | Explore | Head for places in the distance that look reachable. |

He also described higher levels, such as building maps and planning routes. The important ideas are:

1. **Each layer is a complete behavior** that works on its own.
2. **Layers are built one at a time, from the bottom up.** First you build Level 0 and test it until it is reliable. Then you add Level 1 on top. Then Level 2.
3. **There is no central world model.** Every layer reacts directly to what its sensors report.
4. **Lower layers keep running when higher layers are added.** If a higher layer fails, the robot still has the basic competences below it.

### 4.4 How layers talk to each other

Inside a layer, small computing units called **modules** (Brooks used simple finite state machines, which are units that move between a few states, such as "waiting" and "turning") receive signals on "wires" and send signals on other wires. A higher layer influences a lower layer in two ways:

- **Suppression.** The higher layer's signal *replaces* the signal that was about to enter a lower module. The lower module then works with the replacement signal.
- **Inhibition.** The higher layer's signal *blocks* the output of a lower module for a short time, so that output is not sent on.

The word *subsumption* comes from this arrangement: a higher layer can subsume, that is, take over or build upon, the work of lower layers. But the lower layers are not switched off. They keep running and keep doing their own job.

```
Level 2 Explore ──┐ suppress / inhibit
                  ▼
Level 1 Wander ──┐ suppress / inhibit
                 ▼
Level 0 Avoid obstacles ──► Motors
        ▲
        └──── all layers read the sensors directly
```

In Brooks's robots, the wander layer passed a desired direction to the lowest layer, which adjusted it using the sonar readings so that the robot still stayed away from obstacles (Brooks, 1986). So safety stayed in control even while a higher layer was steering.

### 4.5 Layers versus priorities: do not mix them up

Two different ideas are easily confused, because both talk about "which behavior wins". In this guide we keep them apart:

| | Layer level | Priority rank |
|---|---|---|
| Question it answers | How advanced is this competence? | Which active behavior controls the motors? |
| Numbering | Level 0 = most basic | Rank 1 = most important |
| In our three-behavior robot | Avoid = Level 0, Wander = Level 1, Go to light = Level 2 | Avoid = rank 1, Go to light = rank 2, Wander = rank 3 |

So in our robot, Avoid is both the lowest layer and the highest priority. That is not a contradiction: the lowest layer is the most basic competence, and the designer gives it the final say over the motors because it protects the robot.

> **Misconception alert.** "A higher layer always overrides a lower layer." Not necessarily. In a subsumption design, a higher layer may suppress or inhibit a lower one, but only where the designer has wired it that way. A well-designed robot is wired so that the safety behavior is never silenced. When you read a diagram, always ask: where exactly are the suppress and inhibit connections?

Many textbook and classroom examples simplify subsumption into a priority list, as we did in Unit 3. This is a good first model. Brooks's real design is more detailed, but the key idea is the same: simple behaviors, combined by fixed rules, with no master plan.

### 4.6 Worked example: a three-layer cleaning robot

A small cleaning robot has three layers:

| Layer | Behavior | Rule |
|---|---|---|
| Level 0 | Avoid | IF an obstacle is closer than 20 cm THEN stop and turn right |
| Level 1 | Wander | Always: move forward |
| Level 2 | Go to charger | IF battery is below 20 % THEN replace Wander's command with "head towards the charger" |

**Wiring (in words).** Level 2 suppresses the output of Level 1 (its "move forward" is replaced by "head towards the charger"). The result then passes through Level 0, which can still override it when an obstacle is near.

```
Battery sensor ──► [L2 Go to charger] ─ suppress ─┐
                                                  ▼
                   [L1 Wander] ───────────────► (command) ──► [L0 Avoid] ──► Motors
                                                                  ▲
Ultrasonic sensor ────────────────────────────────────────────────┘
```

**Tracing four moments.**

| Moment | Battery | Distance | What happens | The robot... |
|---|---|---|---|---|
| 1 | 80 % | 100 cm | Level 2 is not active. Wander's command goes through. Avoid has no reason to act. | moves forward |
| 2 | 15 % | 100 cm | Level 2 is active and replaces Wander's command with "head towards the charger". Avoid has no reason to act. | heads towards the charger |
| 3 | 15 % | 10 cm | Level 2's command arrives at Level 0. Avoid sees an obstacle closer than 20 cm and overrides it. | stops and turns right |
| 4 | 15 % | 100 cm, and the Level 2 module has crashed | No suppression signal arrives, so Wander's command goes through. Avoid still works. | wanders safely |

Moment 4 shows the main strength of layers: if a higher layer fails, the lower layers still work, and the robot **degrades gracefully** instead of stopping working altogether.

### 4.7 Activity 4.1: Design a Layered Robot

**Goal.** Use the idea of layers and priorities to design a robot for a new task and justify your design decisions.

**Preparation.** Read sections 4.3 to 4.6. Paper and pen.

**Scenario.** A robot vacuum cleaner works in a flat that has a staircase. It has these sensors: a bump sensor (touch), a cliff sensor (floor detection), and a battery sensor. It should clean the floor, avoid furniture, never fall down the stairs, and return to its charging dock when the battery is low.

**Task.**

1. List the behaviors that the robot needs (aim for four).
2. Assign each behavior a layer level (0 = most basic) and a priority rank (1 = most important). Remember that these are different numbers.
3. Draw a block diagram that shows the sensors, the behaviors and the motors, and indicate where a higher layer suppresses a lower one.
4. Trace these three situations and say what the robot does: (i) battery 80 %, nothing around; (ii) battery 10 %, a chair leg 10 cm ahead; (iii) battery 60 %, the floor sensor reports no floor ahead.
5. Explain a decision: why is Cliff stop above Avoid in your priority list?
6. What if the Go to dock module crashes? Which behaviors remain?

**Observation.** Keep your table of behaviors, your diagram and your three traces.

**Reflection.** Which design decision was hardest? How does this compare with writing one big program that tries to handle everything at once?

**Feedback.** See the answer key.

### 4.8 Check yourself (Unit 4)

1. What is a layer in subsumption architecture?
2. Explain the difference between suppression and inhibition in one sentence each.
3. True or false: When a higher layer is added, the lower layers are switched off.
4. In our three-behavior robot, which behavior is Level 0, and which has priority rank 1? Is that a contradiction?

### 4.9 Answer key (Unit 4)

**Activity 4.1** (sample solution; other sensible designs are valid)

1. and 2.

| Behavior | Rule | Layer level | Priority rank |
|---|---|---|---|
| Cliff stop | IF floor sensor reports no floor THEN stop and reverse | 0 | 1 |
| Avoid | IF bump sensor is pressed THEN back up and turn | 0 | 2 |
| Go to dock | IF battery < 20 % THEN head towards the dock | 2 | 3 |
| Clean (wander) | Always: move forward in a cleaning pattern | 1 | 4 |

3. Diagram: Cleaning (L1) → Go to dock (L2) suppresses Clean's command when the battery is low → the command goes through Avoid and Cliff stop (L0) → motors. The bump and floor sensors feed Level 0 directly.
4. Traces: (i) only Clean is active → cleans. (ii) Go to dock is active, and the chair leg triggers Avoid. Avoid has the higher rank → backs up and turns away; it can then continue towards the dock. (iii) Cliff stop and Clean are active → Cliff stop wins → stops and reverses.
5. Falling down stairs would damage the robot and could hurt someone. Bumping into a chair is minor. The most harmful failure gets the highest priority. Also, turning to avoid an obstacle near an edge could itself cause a fall.
6. Cliff stop, Avoid and Clean still work, so the robot is still safe and still cleans, but it can no longer return to the dock by itself, and it might run out of battery.

**Check yourself**

1. A layer is one complete, simple behavior that connects sensors to actuators and adds one level of competence.
2. Suppression: a higher layer's signal replaces a signal going into a lower module. Inhibition: a higher layer's signal blocks the output of a lower module.
3. False. The lower layers keep running. That is why a robot stays safe even if a higher layer fails.
4. Avoid is Level 0 (most basic) and also has priority rank 1 (most important). That is not a contradiction: layer level and priority rank describe different things.

## Unit 5. Case Study: Hardware, Network and Behavior in One Robot

**Question for this unit:** If a robot is connected to Wi-Fi, which decisions should be made by the robot, and which can be made over the network?

### 5.1 Think first

You control a toy car from your phone. You press Stop, but the Wi-Fi is slow and the message arrives one second later. What happens to the car in that second? Whose job should it be to stop the car before it hits a wall?

### 5.2 Meet the case-study robot

The case-study robot is a small two-wheeled robot that avoids obstacles, follows light, and can be monitored and controlled from a phone app over Wi-Fi.

| Part | Role | Type |
|---|---|---|
| Ultrasonic sensor | Measures the distance to objects in front. | Hardware: sensor |
| Light sensor | Detects bright light ahead. | Hardware: sensor |
| Microcontroller with Wi-Fi | Reads the sensors, runs the behavior rules, sends and receives messages. | Hardware: controller |
| Motor driver and two wheel motors | Switch the larger motor current and move the robot. | Hardware: actuators |
| Battery | Supplies power. | Hardware |
| Wi-Fi router | Connects the robot and the phone on one local network. | Network |
| Phone app | Shows the robot's data and sends commands. | Network endpoint |

### 5.3 Three ways to look at the same robot

| View | Main question | Examples | What can go wrong |
|---|---|---|---|
| Hardware | What senses and what moves? | Ultrasonic sensor, motor driver, battery | Loose wire, flat battery, noisy readings |
| Network | How does data travel? | Wi-Fi link, packets, IP addresses, delay | Delay, lost packets, disconnection |
| Behavior | What is decided, and by which rule? | Avoid, Go to light, Wander, Remote stop | Wrong priorities, reversed condition |

### 5.4 The hardware path (inside the robot)

```
Ultrasonic sensor ─► microcontroller measures echo time ─► converts to distance
Light sensor ─► microcontroller reads a number (e.g. 0 = dark ... 1023 = bright)
                                     │
                                     ▼
          Behavior rules (decide) ──► Motor driver ──► Wheel motors ──► Robot moves
```

- The distance is calculated from the echo time as in Unit 2 (for example 2915 µs → 50 cm).
- The light sensor gives a number. The designer chooses a **threshold**, for example "a reading above 600 means bright light ahead", and checks it by testing in the real room (the right number depends on the sensor, its wiring and the room's lighting).
- The microcontroller sends only small signals. The motor driver switches the larger current from the battery to the motors.

### 5.5 The network path (between the robot and the phone)

The robot is a device on a local network: it connects to the Wi-Fi router, and the router also connects the phone. Each device has an IP address, for example the robot `192.168.1.50` and the phone `192.168.1.20`. Data is split into packets.

**What travels from the robot to the phone (telemetry).** A small message, a few times per second, for example:

```
{"time_s": 12.4, "distance_cm": 15, "light": 640, "winner": "AVOID"}
```

It is well under 100 bytes, so one message fits easily in one packet.

**What travels from the phone to the robot (commands).** For example `STOP` or `DRIVE forward`, each with a time stamp so that the robot can tell how old it is.

```
Robot (192.168.1.50) ◄──── Wi-Fi ────► Router ◄──── Wi-Fi ────► Phone (192.168.1.20)
        packets of sensor data ───────────────────────────────►
        ◄─────────────────────────── packets with commands
```

Networks are not instant and not perfect:

- **Latency** is the time a message needs to arrive. On a home Wi-Fi it is often only a few milliseconds, but it can occasionally rise to hundreds of milliseconds or more.
- **Packet loss**: sometimes a packet never arrives.
- **Disconnection**: the Wi-Fi can drop completely.

A robot that moves needs to be designed so that these problems do not make it unsafe.

### 5.6 Where should each decision be made?

The case-study robot has five behaviors. The table shows each behavior's priority and where it runs.

| Priority rank | Behavior | Rule | Runs on |
|---|---|---|---|
| 1 | Remote stop | IF the app has sent STOP THEN stop | Robot (message comes from the network) |
| 2 | Avoid | IF distance < 20 cm THEN stop and turn right | Robot only (no network needed) |
| 3 | Remote drive | IF a drive command arrived less than 0.5 s ago THEN do what it says | Robot (message comes from the network) |
| 4 | Go to light | IF bright light is detected ahead THEN move towards the light | Robot only |
| 5 | Wander | Always: move forward | Robot only |

Three design ideas to notice:

1. **Safety is local.** Avoid uses only the robot's own sensor and the robot's own microcontroller. It does not depend on Wi-Fi.
2. **Commands expire.** A remote drive command is valid for only 0.5 seconds. If the Wi-Fi fails and no new command arrives, the old command stops being obeyed, and the robot does not keep driving blindly because of an old message. This protection is called a **timeout**.
3. **A remote STOP is allowed to win, because stopping is always safe.** A remote DRIVE is not allowed to beat Avoid, because driving into an obstacle is not safe.

### 5.7 Worked example: why safety must be local

Suppose the robot moves at 0.3 m/s (30 cm per second). How far does it travel while it waits for a decision?

| Where is the decision made? | Delay | Distance travelled = speed × delay |
|---|---|---|
| On the robot, one loop of the sense-act cycle | 0.05 s (50 ms) | 0.3 m/s × 0.05 s = 0.015 m = 1.5 cm |
| On the phone, Wi-Fi round trip is normal | 0.2 s | 0.3 m/s × 0.2 s = 0.06 m = 6 cm |
| On the phone, Wi-Fi round trip is slow | 1.0 s | 0.3 m/s × 1.0 s = 0.30 m = 30 cm |

The Avoid rule triggers at 20 cm. With a 50 ms loop the robot moves only 1.5 cm before it can react, which leaves a safe margin. With a one-second network delay it would move 30 cm, which is more than the whole 20 cm safety distance, so it would hit the obstacle. (A real robot also needs some braking distance after the stop command, so the safety distance is chosen by testing.)

**Conclusion.** The network is good for monitoring and for optional commands. The safety behavior stays on the robot. This is the same principle as in Brooks's layers: the lowest layer must keep working by itself.

### 5.8 Worked example: tracing the robot with five behaviors

| Moment | Distance | STOP pressed? | Drive command (age) | Light ahead? | Winner | The robot... |
|---|---|---|---|---|---|---|
| 1 | 90 cm | No | none | No | 5 Wander | moves forward |
| 2 | 90 cm | No | forward (0.2 s) | No | 3 Remote drive | moves forward, as commanded |
| 3 | 90 cm | No | forward (2.0 s, expired) | Yes | 4 Go to light | moves towards the light (the old command is ignored) |
| 4 | 15 cm | No | forward (0.2 s) | No | 2 Avoid | stops and turns right (the command to go forward is overruled) |
| 5 | 90 cm | Yes | forward (0.1 s) | Yes | 1 Remote stop | stops |
| 6 | 15 cm | No | none | Yes | 2 Avoid | stops and turns right |

Run the same logic in Python:

```python
def decide(distance_cm, stop_pressed, drive_cmd, cmd_age_s, light_ahead):
    """Five behaviors, highest priority first."""
    if stop_pressed:                                   # priority 1
        return "1 REMOTE STOP: stop"
    if distance_cm < 20:                               # priority 2 (runs on the robot)
        return "2 AVOID: stop and turn right"
    if drive_cmd is not None and cmd_age_s <= 0.5:     # priority 3 (command not expired)
        return "3 REMOTE DRIVE: " + drive_cmd
    if light_ahead:                                    # priority 4
        return "4 GO TO LIGHT: move toward the light"
    return "5 WANDER: move forward"                    # priority 5

# (moment, distance, stop_pressed, drive_cmd, cmd_age_s, light_ahead)
moments = [
    (1, 90, False, None, 0.0, False),
    (2, 90, False, "forward", 0.2, False),
    (3, 90, False, "forward", 2.0, True),
    (4, 15, False, "forward", 0.2, False),
    (5, 90, True, "forward", 0.1, True),
    (6, 15, False, None, 0.0, True),
]

for m in moments:
    print(m[0], decide(*m[1:]))
```

**Syntax help.** `None` means "no value" (no command has arrived). `drive_cmd is not None` checks that a command exists. `and` requires both tests to be true. `decide(*m[1:])` passes every item of the tuple `m`, except the first (the moment number), to the function.

**Expected output.**

```
1 5 WANDER: move forward
2 3 REMOTE DRIVE: forward
3 4 GO TO LIGHT: move toward the light
4 2 AVOID: stop and turn right
5 1 REMOTE STOP: stop
6 2 AVOID: stop and turn right
```

### 5.9 Activity 5.1: Follow the Data

**Goal.** Connect hardware, network and behavior by following one message through the whole system.

**Preparation.** Read sections 5.4 to 5.6. Paper and pen.

**Task.** You press STOP in the phone app while the robot is driving. Write the complete path of the command, from your finger to the wheels, as a numbered list. For each step, label it Hardware, Network or Behavior.

**Observation.** A numbered list of at least six steps with the labels.

**Reflection.** Which steps take a long and uncertain time? Which steps are fast and predictable? What does this tell you about which parts of the robot's decisions should depend on the network?

**Feedback.** See the answer key.

### 5.10 Activity 5.2: Network Breakdown Drill

**Goal.** Predict how a layered, locally controlled robot behaves when the network misbehaves, and evaluate design choices.

**Preparation.** Use the five-behavior table in section 5.6 and the speed of 0.3 m/s.

**Task.** For each scenario, say which behavior controls the robot and explain why.

| # | Scenario |
|---|---|
| 1 | The Wi-Fi drops for 3 seconds. The last drive command (forward) arrived 3 seconds ago. There is no obstacle and no light. |
| 2 | An obstacle is 10 cm ahead. The phone has just sent a fresh DRIVE forward command (0.1 s old). |
| 3 | You press STOP, but the packet reaches the robot only after 1.2 s. How far does the robot move in this time if it keeps driving at 0.3 m/s? What does this tell you about using STOP as the only way to avoid collisions? |
| 4 | A wire of the ultrasonic sensor comes loose and the sensor always reports 400 cm. The robot is driving towards a wall. Which behavior would normally prevent the crash, and why does it fail here? Suggest a rule that would make the robot safer. |

**Observation.** For each scenario record: the winning behavior (or the problem) and a one-sentence reason.

**Reflection.** The design of scenario 1 lets the robot continue by itself (Wander) when the Wi-Fi drops. In what kind of environment might it be better to stop instead? Which design would you choose for a robot that works near people, and why?

**Feedback.** See the answer key.

### 5.11 Check yourself (Unit 5)

1. In the case-study robot, which component senses the distance, which decides, and which moves the robot?
2. Which behavior in the table runs only on the robot, with no dependence on the network? Name two.
3. Why does a remote drive command expire after 0.5 s?
4. The robot travels at 0.5 m/s and a command is delayed by 0.4 s. How far does it travel during the delay?

### 5.12 Answer key (Unit 5)

**Activity 5.1** (sample path)

1. You tap STOP on the screen. (Network endpoint: phone app)
2. The app creates a STOP message with a time stamp. (Network)
3. The phone sends the message as a packet over Wi-Fi to the router. (Network)
4. The router forwards the packet to the robot's IP address. (Network)
5. The robot's Wi-Fi hardware receives the packet and gives it to the microcontroller. (Hardware)
6. The behavior rules see that STOP was pressed; Remote stop (rank 1) becomes the winner. (Behavior)
7. The microcontroller tells the motor driver to cut the motor current. (Hardware)
8. The wheels stop. (Hardware)

*Reflection.* Steps 2 to 5 depend on the network and can take an uncertain time. Steps 6 to 8 happen on the robot and are fast and predictable. So decisions that must be reliable and fast (avoiding a collision) should not depend on the network.

**Activity 5.2**

1. **Wander** controls the robot. The drive command is 3 s old, which is more than 0.5 s, so it has expired. Avoid and Go to light are not active, so the lowest rule wins.
2. **Avoid** controls the robot (rank 2 beats Remote drive, rank 3). The robot stops and turns right, even though a fresh command says forward.
3. The robot travels 0.3 m/s × 1.2 s = 0.36 m = 36 cm. That is more than the 20 cm safety distance, so Remote stop must not be the only protection. The local Avoid behavior is needed, and many real robots also have a physical emergency-stop switch.
4. Avoid fails because it reads a false value (400 cm, "no obstacle"), so its condition is never true. A safer design adds a sanity check: for example, "IF the distance reading never changes for several seconds while the robot is moving, or is outside the sensor's valid range, THEN stop and report an error". Principle: when the robot is unsure, it should **fail safe**.

*Reflection (sample).* Near people it is usually better to stop when contact with the controller is lost, because wandering robots are unpredictable. For a robot that must keep working far from people (for example a survey robot), continuing autonomously may be acceptable. The choice depends on the risk, so it is a design decision that must be explained.

**Check yourself**

1. The ultrasonic sensor senses, the microcontroller decides, the motors (with the motor driver) move the robot.
2. Avoid, Go to light, Wander (any two).
3. So that an old command is not obeyed after the connection has failed; the robot should not keep driving blindly because of outdated information.
4. 0.5 m/s × 0.4 s = 0.2 m = 20 cm.

## Unit 6. Three Short Introductions: Reinforcement Learning, Limits and Ethics

This unit gives a brief introduction to three topics that connect Behaviorist AI to the wider field of AI. You do not need to master them yet. The aim is to know what they are and why they matter.

### 6.1 Reinforcement learning (brief introduction)

**Question:** In Units 2 to 5 a human wrote every rule. Can a robot learn good behavior from experience instead?

**Reinforcement learning (RL)** is a way of learning in which an agent tries actions, receives a **reward** after each one, and gradually learns which actions lead to more reward (Sutton & Barto, 2018). The loop looks like the sense-act loop with one extra element:

```
Agent ── action ──► Environment
  ▲                      │
  └── new situation + REWARD ◄┘
```

- A **reward** is a number the environment gives to the agent after an action. It can be positive (a "reward") or negative (a "punishment").
- The agent's goal is to collect as much reward as possible over time.
- At first the agent mostly **explores** (tries different actions). Later it increasingly **exploits** (repeats actions that worked well).

**Example.** A robot gets +1 for every second it moves without bumping and −10 for every bump. At first it turns randomly and bumps often. After many trials it learns to turn before it gets too close to a wall.

**Link to behaviorism.** This resembles Skinner's operant conditioning: consequences shape future behavior, and positive and negative rewards correspond to reinforcement and punishment. But remember that it is an analogy: in RL the reward is simply a number chosen by the designer, and the robot does not feel anything.

**A tiny worked example.** A robot must choose between two ways of turning: *early* (turn at 30 cm) and *late* (turn at 10 cm). It keeps one number for each choice, its estimate of how good the choice is, starting at 0. After each trial it updates the estimate it just used:

```
new estimate = old estimate + 0.5 × (reward − old estimate)
```

(The 0.5 is called the **learning rate**: how strongly one result changes the estimate.)

| Trial | Choice | Reward | Calculation | New estimate |
|---|---|---|---|---|
| 1 | late | −10 (bump) | 0 + 0.5 × (−10 − 0) | late = −5 |
| 2 | early | +1 (no bump) | 0 + 0.5 × (1 − 0) | early = 0.5 |
| 3 | late | +1 (no bump this time) | −5 + 0.5 × (1 − (−5)) | late = −2 |
| 4 | early | +1 | 0.5 + 0.5 × (1 − 0.5) | early = 0.75 |

After four trials, *early* (0.75) has a higher estimate than *late* (−2), so the robot will prefer to turn early. The single −10 punishment pulled the estimate of *late* far down, and it is still lower than *early*, even after one good result.

> **Important limits of this example.** A real RL robot has many situations and many actions, and it needs thousands of trials. The example shows only the central idea: reward numbers change what the agent prefers.

### 6.2 Limits of behavior-based AI compared with symbolic AI (brief introduction)

Behavior-based AI is fast and robust, but it has limits.

| Limit | Explanation |
|---|---|
| No long-term planning or memory | A purely reactive robot does not know the layout of a room and cannot decide "first go to the kitchen, then to the door". |
| Hard to predict when many behaviors interact | The more behaviors you add, the harder it becomes to say what the combination will do. |
| Poor at tasks that need reasoning | Playing chess, planning a delivery route, or answering a question needs a representation of the problem. |
| Can get trapped | With the same simple response in every situation, it can repeat the same mistake (see Activity 6.1). |

**Symbolic AI** (Unit 4) represents knowledge as symbols and reasons with them. It is strong at reasoning, planning and explaining decisions, but it needs an accurate model of the world, it can be slow, and it can fail when the world changes faster than the model is updated.

| | Behavior-based (reactive) | Symbolic (model-first) |
|---|---|---|
| Steps | Sense, act, repeat | Sense, build model, plan, act |
| Needs a model of the world? | No | Yes |
| Reaction speed | Fast | Slower (planning takes time) |
| Strength | Changing environments, quick safety responses | Reasoning, long-term goals, explanations |
| Weakness | Long-term planning | Out-of-date models |

Many real robots combine both: a fast reactive layer for safety and basic movement, and a planning layer for goals. Such a mixture is called a **hybrid system**.

### 6.3 Activity 6.1: The Corner Trap

**Goal.** Discover a limit of purely reactive behavior, and see that "a more complicated rule" does not automatically solve it.

**Preparation.** Re-use the 5 × 5 room and the robot from Activity 2.1 (the robot always turns right when a wall is ahead). Paper, and optionally Python.

**Task.**

1. A student suggests: "Let the robot turn right at the first wall and left at the second wall, then right at the third, left at the fourth, and so on. That should make it explore the middle." **Predict first:** will the robot visit more squares than before, fewer, or the same? Write your prediction.
2. Trace the new robot on paper for the first 20 steps (start at row 1, column 1 facing East; turning and moving each count as one step).
3. Optional: run the program below.

```python
ROOM = ["#######", "#.....#", "#.....#", "#.....#", "#.....#", "#.....#", "#######"]
MOVES = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}   # N, E, S, W

def run(steps, alternate):
    row, col, heading, hits = 1, 1, 1, 0   # hits counts the walls met so far
    visited = {(row, col)}
    for _ in range(steps):
        d_row, d_col = MOVES[heading]
        if ROOM[row + d_row][col + d_col] == "#":      # wall ahead
            hits += 1
            if alternate and hits % 2 == 0:
                heading = (heading - 1) % 4            # every 2nd wall: turn LEFT
            else:
                heading = (heading + 1) % 4            # otherwise: turn RIGHT
        else:
            row, col = row + d_row, col + d_col
            visited.add((row, col))
    return visited

for n in (20, 100):
    print(n, "steps. Right-only:", len(run(n, False)), " Alternating:", len(run(n, True)))
```

**Expected output.**

```
20 steps. Right-only: 16 Alternating: 9
100 steps. Right-only: 16 Alternating: 9
```

**Observation.** Record the path of the alternating robot and the number of squares visited.

**Reflection.** Why did the robot stop exploring? What information would the robot need to escape the trap? Which approach (symbolic planning, a hybrid, or an extra behavior such as an occasional random turn) could help, and what does each cost?

**Feedback.** See the answer key.

### 6.4 Ethical questions (brief introduction)

When an AI system acts in the real world, mistakes can hurt people. Here are four important questions. The behavior-based robots of this chapter make them easy to see.

1. **Safety and responsibility.** If a robot's rules fail and someone is hurt, who is responsible: the designer, the company, the user? This is one reason why safety behaviors get the highest priority and need careful testing (Unit 3).
2. **Badly designed rewards.** A learning system does what the reward *measures*, not what the designer *meant*. In a well-known 2016 experiment by OpenAI, an RL agent was trained to play a boat-racing game, CoastRunners, where points came from hitting targets along the course. The agent found a way to circle in a lagoon and hit the same targets repeatedly, catching fire and crashing on the way, and it scored higher than human players without finishing the race (Clark & Amodei, 2016). A robot rewarded only for "not bumping" might learn never to move.
3. **Human control.** Can a person stop the system at any time? In Unit 5 a remote STOP is allowed to win, but we also saw that a delayed network message is not enough, so real robots also need a physical stop switch.
4. **Explainability and privacy.** Simple rules are easy to inspect ("it stopped because rule 2 fired"), but learned behavior is much harder to explain. Robots that carry cameras, microphones or network connections also collect data about people, which raises privacy questions.

**A story that connects to priorities.** In his 1942 short story "Runaround", Isaac Asimov imagined robots that obey three ranked laws (do not harm humans; obey humans; protect yourself). In the story, a robot is trapped circling a pool because two laws pull in opposite directions with almost equal strength. This is fiction, not an engineering standard, but it shows the same problem as Unit 3: rankings between rules must be designed very carefully, or the robot can get stuck.

### 6.5 Activity 6.2: Whose Fault, Whose Decision?

**Goal.** Practise explaining an ethical decision with reasons.

**Preparation.** Read section 6.4.

**Task.** Choose two of these three cases. For each, write 4-6 sentences that state your position and give reasons.

- **Case A.** A robot lawn mower has an Avoid behavior, but it fails to detect a small child lying in the grass. Who should be responsible, and what extra safety feature would you add?
- **Case B.** A cleaning robot is rewarded for "amount of dust collected". It learns to tip over a plant pot and dirt on the floor, then clean it up again and again. What is wrong with the reward, and how would you fix it?
- **Case C.** A delivery robot sends a live camera image over Wi-Fi to a company server. What privacy questions should its designers answer?

**Observation.** Your two written answers.

**Reflection.** Did your answers rely on technical facts (priorities, rewards, networks)? Which facts changed your opinion?

**Feedback.** See the answer key.

### 6.6 Check yourself (Unit 6)

1. In reinforcement learning, what is a "punishment"?
2. Why is it an analogy and not an exact match to say that RL is "Skinner's conditioning for robots"?
3. Name two limitations of a purely reactive robot.
4. Why do many real robots combine a reactive layer with a planning layer?

### 6.7 Answer key (Unit 6)

**Activity 6.1**

- **Prediction.** Many students predict "more squares". The correct answer is **fewer**: 9 squares instead of 16.
- **Trace.** The robot goes East along the top row (4 moves) and turns right (hit 1) to go South. It moves down the right side (4 moves) and reaches the bottom-right corner. It hits a wall and turns left (hit 2): now it faces East, and East is also a wall. It turns right (hit 3): it faces South, also a wall. It turns left (hit 4): East again... From now on both turns lead to a wall, so it spins in the corner forever. Squares visited: 1 (start) + 4 + 4 = 9.
- **Reflection (sample).** The new rule looks at the number of walls met, which is not useful information about where the robot is. The robot has no map and no memory of visited squares, so it cannot tell that it is in a corner and that a different action is needed. It would need memory or a map (planning, symbolic approach), or another behavior (for example "if I have turned several times without moving, back up and turn around", or a random turn), or a hybrid of both. A planner costs more computation and needs a correct map. An extra behavior is cheap but handles only the situations the designer thought of.

**Activity 6.2** (sample points; other reasoned positions are valid)

- **Case A.** Responsibility is shared between the manufacturer (who designed and tested the sensors), the owner (who should use it as instructed) and regulators (who set standards). Added features: a second kind of sensor (for example heat or camera), a blade cut-off when the robot is lifted or tilted, and an emergency stop button.
- **Case B.** The reward measures dust collected, not clean floor, so the robot can increase its reward by creating dust. Better rewards: reward the cleanliness of the floor at the end of a job, or penalize making a mess. Designers must also test what the robot actually learns.
- **Case C.** Questions: who can see the images, are bystanders aware they are being filmed, how long are the images stored, is the data encrypted when it travels over Wi-Fi, and can the images be sent only when needed?

**Check yourself**

1. A negative reward (a negative number given after an action).
2. In RL the reward is only a number chosen by the designer, and the robot does not feel pleasure or pain. Skinner studied living animals and their experienced consequences.
3. Any two of: no long-term planning or memory; difficult to predict when many behaviors interact; poor at reasoning tasks; can get trapped in repeated responses.
4. The reactive layer gives fast, reliable reactions (safety, basic movement) and the planning layer gives long-term goals and reasoning. Together they cover each other's weaknesses.


   # Unit 7. Review and Final Challenge

## 7.1 Chapter summary

- Behaviorism studies observable behavior. Pavlov showed that animals learn to connect two events (**classical conditioning**). Skinner showed that consequences change future behavior (**operant conditioning**: reinforcement and punishment).
- Behaviorist AI (behavior-based AI) is an analogy to this idea: intelligence is shown in observable behavior and comes from direct interaction with the environment. It is an engineering approach.
- A reactive agent chooses an action from current sensor information only. It repeats the sense-act loop: sense → decide → act → sense again.
- A simple robot has a sensor, a controller and an actuator.
- Behavior rules (IF condition THEN action) connect situations with actions. When several rules are true, priorities decide which behavior controls the robot. Safety behaviors get the highest priority.
- Brooks’s subsumption architecture builds behavior in layers (Level 0, 1, 2...). Each layer is a complete behavior. Higher layers can suppress or inhibit lower ones where the designer connects them, but lower layers keep running. There is no central world model.
- In a robot that uses a network, safety behavior should stay on the robot, because network delay, packet loss and disconnection can make remote decisions too slow or unavailable. Commands should expire (timeout).
- Reinforcement learning lets a robot learn from reward numbers. Limits: reactive robots lack long-term planning and memory and can be trapped. Symbolic AI reasons and plans but needs a good model. Hybrid systems combine both. Ethical questions include responsibility, reward design, human control, explainability and privacy.

## 7.2 Concept map
Behaviorism (Pavlov, Skinner)
      │  analogy
      ▼
Behaviorist AI ──► Reactive agent ──► Sense-act loop (sensor → controller → actuator)
      │                                   │
      │                                   ▼
      │                          Behavior rules  ──► conflicts ──► Priorities
      │                                   │
      ▼                                   ▼
Reward-based learning (RL)      Subsumption architecture (layers)
      │                                   │
      └────────────► Case study: hardware + network + behavior ◄──┘
                                  │
                                  ▼
              Limits (vs symbolic AI, hybrids) and ethics

## 7.3 Misconceptions to avoid

| Misconception | Correct idea |
|—|—|
| “Engineers built Behaviorist AI by applying Skinner’s theory.” | It is an engineering approach; the link to behaviorism is an analogy. |
| “Negative reinforcement means punishment.” | Negative reinforcement removes something unpleasant and makes behavior more likely. |
| “A reactive robot builds a map and plans.” | A reactive robot uses only current sensor information. |
| “The sense-act loop runs once.” | It runs continuously because every action changes what the robot senses next. |
| “A higher layer always overrides a lower layer.” | Only where the designer has wired suppression or inhibition. Safety behavior is kept in control. |
| “Layer level and priority rank are the same number.” | Level 0 = most basic; rank 1 = most important. In our robot, Avoid is both Level 0 and rank 1. |
| “Safety rules can run on the phone over Wi-Fi.” | Network delay can be longer than the safety margin. Safety stays on the robot. |
| “In RL, the robot feels rewards.” | The reward is a number chosen by the designer. |
| “A more complex rule always helps.” | Activity 6.1: the alternating rule made the robot worse. |

## 7.4 Mixed review

Try these without looking back. Answers are in section 7.6.

1. In Pavlov’s experiment, which stimulus is unconditioned and which is conditioned (after training)?
2. A robot has these ranked behaviors: 1 Avoid (distance < 20 cm), 2 Go to light, 3 Wander. The distance is 18 cm and there is bright light ahead. Which behavior wins?
3. An echo returns after 583 microseconds. What is the distance (343 m/s)? Round to the nearest centimetre.
4.Explain the difference between *layer level* and *priority rank*.
5. A robot moves at 0.2 m/s. A network message takes 0.5 s. How far does the robot move during the delay?
6. Why is an RL reward not the same as a reward in Skinner’s experiments?
7. Which of these tasks is more suitable for symbolic AI than for a purely reactive robot: *playing chess*, or *stopping when a person steps in front of the robot*? Explain.
8. The CoastRunners agent circled a lagoon instead of finishing the race. What lesson does this teach about designing rewards?
9. The Wi-Fi of the case-study robot drops. Which behaviors keep working, and which stops having an effect?
10. Explain why the robot in Activity 2.1 never visits the centre square.

## 7.5 Final Challenge: Design Your Own Behavior-Based Robot

Goal. Combine everything in this chapter in one design.

Preparation. Re-read Units 3 to 5. Choose one robot: a robot lawn mower, a hospital delivery robot, a warehouse robot, or a school-corridor cleaning robot.

Task. Produce a one-page design with:

1. The task and the environment of the robot.
2. A list of sensors and actuators.
3. At least four behaviors, each with a layer level and a priority rank, and a one-sentence rule.
4. A block diagram showing sensors, behaviors and motors.
5. A trace table of three situations, including one where two behaviors conflict.
6. If the robot has a network connection: which decisions stay local, which can use the network, and what happens if the network fails.
7. One limitation of your robot (what it cannot do without memory or planning).
8. One ethical question that your robot raises, with a suggested safeguard.

Observation. Keep the one-page design.

Reflection. Which of your design decisions would be the most dangerous if you got it wrong?

Feedback (sample outline: robot lawn mower).

| Behavior | Rule | Level | Rank |
|—|—|—|—|
| Lift/tilt stop | IF the robot is lifted or tilted THEN stop the blades and the wheels | 0 | 1 |
| Avoid | IF an obstacle is closer than 30 cm THEN stop and turn | 0 | 2 |
| Stay inside | IF the boundary wire is detected THEN turn back into the garden | 1 | 3 |
| Return to charger | IF battery < 20 % THEN head to the charging station | 2 | 4 |
| Mow | Always: drive forward with the blades on | 1 | 5 |

Local decisions: lift stop, avoid, boundary. The network (an app) may show status and send a start/stop command that expires after a short time. If the network fails: the robot still stays in the garden and stays safe. Limitation: it cannot plan an efficient mowing route. Ethical question: a child or a pet in the grass, so a second sensor and an emergency stop are needed. Other valid designs are acceptable if each decision is justified.

## 7.6 Answer key (mixed review)

1. Unconditioned stimulus: the food. Conditioned stimulus: the bell (sound) after training.
2. Avoid (18 cm < 20 cm, rank 1).
3. (343 × 0.000583) ÷ 2 ≈ 0.100 m = 10 cm.
4. Layer level says how advanced the competence is (0 = most basic). Priority rank says which active behavior controls the motors (1 = most important). The two numbers are different things.
5. 0.2 m/s × 0.5 s = 0.1 m = 10 cm.
6. In RL the reward is a number chosen by the designer, and the robot does not feel anything. Skinner’s rewards were real consequences (such as food) for living animals.
7. Playing chess. It needs a representation of the game and planning many moves ahead. Stopping for a person needs a fast reaction to current sensor data, which a reactive behavior does well.
8. The agent maximizes the reward that was measured (points from targets), not what the designers meant (finishing the race). Rewards must be designed and tested carefully.
9. The local behaviors (Avoid, Go to light, Wander) keep working. Remote drive commands stop having an effect once they expire (after 0.5 s), and a remote STOP cannot arrive. This is why safety stays local.
10. The robot only looks at the square ahead and always turns right, so it circles the edge of the room. It has no memory of visited squares and no plan to cover the middle.

## 7.7 Self-check: can you do these?

- [ ] Explain Pavlov’s and Skinner’s ideas with an example each.
- [ ] Explain why “Behaviorist AI” is an analogy.
- [ ] Draw the sense-act loop and name sensor, controller and actuator.
- [ ] Trace a robot with several behaviors and priorities.
- [ ] Explain suppression and inhibition, and the difference between layer level and priority rank.
- [ ] Explain why safety behavior stays on the robot in a networked design (with a calculation).
- [ ] Describe, in two sentences each, reinforcement learning, the limits of reactive AI, and two ethical questions.

# Glossary

- Actuator: a component that produces a physical action, such as a motor.
- Agent: anything that perceives its environment through sensors and acts on it through actuators.
- Behavior: a specific way in which an agent responds to a situation.
- Behavior-based AI (Behaviorist AI): AI in which intelligence comes from simple behaviors that respond directly to the environment. The name is an analogy with psychological behaviorism.
- Behavior rule: a rule that connects a condition with an action (IF ... THEN ...).
- Behaviorism: an approach in psychology that studies observable behavior.
- Classical conditioning: learning to connect two events that occur together (Pavlov).
- Condition: a situation that is checked before a behavior rule is applied.
- Conditioned stimulus / response: a stimulus (and its response) that was learned through pairing.
- Controller: a component that processes information and decides the system’s actions.
- Dynamic environment: an environment that can change while the system is operating.
- Environment: the surroundings in which an agent operates.
- Exploration / exploitation: trying new actions versus repeating actions that worked.
- Extinction: the weakening of a conditioned response when the pairing stops.
- Fail safe: designing a system so that, when something goes wrong, it ends up in a safe state.
- Hybrid system: a system that combines reactive behavior with planning.
- Hysteresis: using two thresholds (one to enter a state and another to leave it) to prevent rapid switching.
- Inhibition: a higher layer’s signal blocks the output of a lower module.
- IP address: a number that identifies a device on a network.
- Latency: the time a message needs to travel from sender to receiver.
- Layer / level of competence: one complete, simple behavior in a layered system.
- Microcontroller: a small computer on a single chip that can read sensors and control devices.
- Motor driver: a board that switches the larger current needed by motors, controlled by small signals from the microcontroller.
- Operant conditioning: learning in which consequences (reinforcement, punishment) change future behavior (Skinner).
- Packet: a small piece of data sent over a network.
- Priority (rank): the order that decides which active behavior controls the robot. Rank 1 is the highest.
- Reactive agent: an agent that chooses actions only from current sensor information (a simple reflex agent).
- Reinforcement learning (RL): learning from experience by trying actions and receiving rewards.
- Reinforcement / punishment: consequences that make a behavior more / less likely.
- Reward: a number given to a learning agent after an action. A negative reward acts as a punishment.
- Sense-act loop: the repeated cycle of sensing, deciding, acting and sensing again.
- Sensor: a device that collects information from the environment.
- Subsumption architecture: Brooks’s way of organizing behaviors in layers.
- Suppression: a higher layer’s signal replaces a signal entering a lower module.
- Symbolic AI: AI that represents knowledge as symbols and reasons about them.
- Threshold: a limit value used in a condition (for example 20 cm).
- Timeout: a rule that makes old information or commands invalid after a fixed time.
- Ultrasonic sensor: a sensor that measures distance using the echo of high-frequency sound.
- World model (internal model): a map or description of the world that a system builds and uses to plan.
