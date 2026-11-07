# Behaviorist AI

## Part A – True / False

Write True or False. If a statement is false, correct it.

1. **[3.1]** In classical conditioning, Pavlov's dogs learned to salivate at the sound of a bell after the bell had been paired with food many times.
2. **[3.1]** Negative reinforcement is a kind of punishment.
3. **[3.1]** In Skinner's operant conditioning, a consequence that follows an action changes how often the action is repeated.
4. **[3.2]** A reactive agent builds a detailed map of the room and plans its whole route before it moves.
5. **[3.2]** An ultrasonic sensor calculates distance as (343 m/s × echo time) ÷ 2, because the sound travels to the obstacle and back.
6. **[3.3]** In the priority convention used in this guide, rank 1 is the lowest priority.
7. **[3.3]** Hysteresis uses two thresholds, for example entering Avoid below 20 cm and leaving it only above 30 cm, to stop the robot from switching back and forth.
8. **[3.4]** In Brooks's subsumption architecture, higher layers switch off the lower layers completely.
9. **[3.5]** In the case-study robot, the Avoid behavior runs on the robot itself and does not depend on Wi-Fi.
10. **[3.6]** In reinforcement learning, the reward is a number chosen by the designer, and the robot does not feel pleasure or pain.

---

## Part B – Multiple Choice

11. **[3.1]** A car's seat-belt warning sound stops when you buckle up, so you buckle up more quickly next time. Which type of consequence is this? *(Choose ONE answer.)*
    - **A.** Positive reinforcement
    - **B.** Negative reinforcement
    - **C.** Positive punishment
    - **D.** Negative punishment

12. **[3.2]** Which three parts make up the sense–act loop of a robot? *(Choose ONE answer.)*
    - **A.** Sensor, controller, actuator
    - **B.** Keyboard, monitor, printer
    - **C.** Map, plan, route
    - **D.** Router, switch, modem

13. **[3.2]** An ultrasonic sensor measures an echo time of 1,166 µs. About how far away is the obstacle? *(Choose ONE answer.)*
    - **A.** 10 cm
    - **B.** 20 cm
    - **C.** 40 cm
    - **D.** 2 m

14. **[3.3]** The robot has Avoid (rank 1: distance < 20 cm), Go to light (rank 2) and Wander (rank 3). The distance is 12 cm and bright light is ahead. Which behavior controls the motors? *(Choose ONE answer.)*
    - **A.** Wander
    - **B.** Go to light
    - **C.** Avoid
    - **D.** No behavior, because two rules conflict

15. **[3.3]** Which of these situations make the Avoid behavior (distance < 20 cm) active? *(Choose ALL correct answers.)*
    - **A.** Distance 15 cm, no light
    - **B.** Distance 80 cm, bright light
    - **C.** Distance 12 cm, bright light
    - **D.** Distance 25 cm, no light

16. **[3.3]** A robot near stairs has a cliff sensor. Which behavior should get rank 1? *(Choose ONE answer.)*
    - **A.** Wander
    - **B.** Go to light
    - **C.** Cliff stop
    - **D.** Avoid obstacles

17. **[3.4]** In Brooks's subsumption architecture for a mobile robot, which behavior is in the lowest layer (Level 0)? *(Choose ONE answer.)*
    - **A.** Explore
    - **B.** Wander
    - **C.** Avoid obstacles
    - **D.** Plan a route

18. **[3.5]** The robot moves at 0.3 m/s. If a stop decision is made on a phone and takes 1 second to arrive over Wi-Fi, how far does the robot travel before it reacts? *(Choose ONE answer.)*
    - **A.** 1.5 cm
    - **B.** 6 cm
    - **C.** 20 cm
    - **D.** 30 cm

19. **[3.5]** Which design ideas protect the case-study robot when the network is slow or fails? *(Choose ALL correct answers.)*
    - **A.** Avoid runs locally on the robot
    - **B.** Remote drive commands expire after a timeout
    - **C.** A remote DRIVE command is allowed to override Avoid
    - **D.** A remote STOP command is allowed to win, because stopping is safe

20. **[3.6]** A robot updates its estimate with: `new = old + 0.5 × (reward − old)`. The estimate for 'late' is −5 and the robot gets a reward of +1. What is the new estimate? *(Choose ONE answer.)*
    - **A.** −4
    - **B.** −2
    - **C.** 0.5
    - **D.** 1

---

## Part C – Open-ended

Write a developed answer (normally more than 100 words), using examples, a diagram or worked steps.

21. **[3.1–3.2]** Explain why the term "Behaviorist AI" is an analogy. Compare classical conditioning (Pavlov) and operant conditioning (Skinner) with a robot that uses behavior rules, and describe at least one important difference between an animal and a robot.

22. **[3.3]** A robot has three behaviors: Avoid (rank 1: IF distance < 20 cm THEN stop and turn right), Go to light (rank 2) and Wander (rank 3: always active). Trace what the robot does at distances of 80 cm (no light), 45 cm (light), 15 cm (light) and 70 cm (light). Then explain what goes wrong if the engineer gives Go to light a higher priority than Avoid, and why safety behaviors usually get rank 1.

23. **[3.5–3.7]** Evaluate the robot design in which the robot sends sensor data to a phone over Wi-Fi and the phone decides when to stop. Use the latency calculation (robot speed 0.3 m/s, 20 cm safety distance) to support your answer. Then propose a better design and describe one limit of purely reactive robots.



# Behaviorist AI

## Part A – True / False

1. **True.** The bell (at first a neutral stimulus) became a signal that predicts food, so it started to cause salivation by itself.
2. **False.** Negative reinforcement makes a behavior more likely by removing something unpleasant (for example, a seat-belt warning sound stops). Punishment makes a behavior less likely.
3. **True.** For example, a rat that receives food after pressing a lever presses the lever more and more often.
4. **False.** A reactive agent chooses its action using only current sensor information, like a reflex. Building a map and planning is the approach of symbolic ("think first") systems.
5. **True.** The echo time covers the trip to the wall and back again, so the distance to the wall is half of what the sound covers.
6. **False.** Rank 1 is the highest priority. The highest-priority active behavior controls the motors; a larger number means a lower priority.
7. **True.** With one threshold, noisy readings around 20 cm make the behavior flicker. With two thresholds, the behavior changes only once.
8. **False.** Lower layers keep running. Higher layers only suppress (replace an input signal) or inhibit (block an output) at the points where they are wired in.
9. **True.** Safety is local: Avoid uses only the robot's own sensor and microcontroller, because network messages can be delayed or lost.
10. **True.** The link to behaviorism is an analogy. The reward is simply a number that the learning algorithm tries to make as large as possible over time.

---

## Part B – Multiple Choice

11. **B.** Something unpleasant (the sound) is removed, and the behavior becomes more likely, which is negative reinforcement.
12. **A.** The sensor measures, the controller (microcontroller) applies a rule, and the actuator (for example a motor) acts. The action changes the world, and the robot senses again.
13. **B.** 343 m/s × 0.001166 s ≈ 0.40 m for the trip there and back; half of that is about 0.20 m = 20 cm.
14. **C.** Avoid, Go to light and Wander are all active, and the highest-priority active behavior (Avoid) wins. The robot stops and turns right.
15. **A, C.** A behavior is active when its condition is true. Avoid depends only on the distance being below 20 cm; light does not matter for it.
16. **C.** Falling down the stairs is the most harmful failure, so Cliff stop gets the highest rank; Avoid moves to rank 2.
17. **C.** Level 0 avoids obstacles, Level 1 wanders and Level 2 explores. Planning a route is not a layer in this design.
18. **D.** 0.3 m/s × 1 s = 0.3 m = 30 cm, which is more than the 20 cm safety distance. A decision on the robot itself (about 50 ms) means only 1.5 cm.
19. **A, B, D.** A remote DRIVE must never beat Avoid, because driving into an obstacle is not safe. The other three ideas make the robot fail safe.
20. **B.** −5 + 0.5 × (1 − (−5)) = −5 + 0.5 × 6 = −5 + 3 = −2.

---

## Part C – Open-ended

### 21. Behaviorism and Behaviorist AI

- Behaviorism studies observable behavior: stimulus in, response out, without looking inside the "black box".
- **Classical conditioning:** two events become linked (bell + food → bell alone causes salivation).
- **Operant conditioning:** consequences change how often an action is repeated (reinforcement and punishment).
- A behavior-based robot also links situations (sensor conditions) to responses (actions) without a model of the world.
- **Difference:** the robot's rules are written by an engineer (or learned from reward numbers); the robot does not feel, want or understand anything.
- So the name borrows an idea from psychology; it does not apply psychology to machines.

### 22. Priorities and conflicts

- **80 cm, no light:** only Wander is active → moves forward.
- **45 cm, light:** Go to light and Wander active → Go to light wins.
- **15 cm, light:** Avoid, Go to light and Wander active → Avoid wins (stops and turns right).
- **70 cm, light:** Go to light wins again.
- If Go to light outranks Avoid, the robot drives towards the light even when an obstacle (for example a glass wall) is closer than 20 cm and crashes.
- Safety behaviors prevent the most harmful failure, so they get the highest rank; ranking is a design decision that must be explained.

### 23. Safety in a networked robot

- Network messages can be delayed, lost or disconnected.
- 0.2 s delay → 6 cm; 1 s delay → 30 cm, which is more than the 20 cm safety distance, so the robot would hit the obstacle.
- **Better:** keep Avoid on the robot (about 50 ms → 1.5 cm); use the network for telemetry and non-critical commands.
- Remote commands should expire (timeout); a remote STOP may win, a remote DRIVE must not beat Avoid; the robot should fail safe.
- **Limit of reactive robots:** no memory or planning, so they can get trapped (for example circling the edge of a room or stuck in a corner); hybrid systems add planning on top of reactive safety.
