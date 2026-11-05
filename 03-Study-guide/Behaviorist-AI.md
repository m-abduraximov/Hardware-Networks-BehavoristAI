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
   
