# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
` Onkar and Radhika `

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Onkar` | `Fabrication ` | `Mechanics` | `Good with in hand mechanisms and workings of the sensors, also experienced in circuits and logic gates. With a decent knowledge of python coding and simple logics` |
| `Radhika` | `Coding` | `Art` | `micropython and python affinity, game logic affinity, artistiv ability` |

## 1.3 Project Title
`Whack A Mole`

## 1.4 One-Line Pitch
` A Whack-A-Mole operated by touch mat, where players whack the moles on screen with a hammer `

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`Whack-A-Mole is a tabletop game where players use a touch-sensitive mat to 
go through 5 rounds of the game and try to get the highest score.
It has playful visuals, setup and timer that create a playable atmostphere. 
The project is inherently fun and engaging due to its gameified nature. It is 
also very competitive and delightful due to its whimsical setup (the hammer), 
and leaderboard where players can track their positions.
The main technology is touch sensors and a bluetooth keyboard, where a touch on 
the mat corresponds to different mole positions.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`Its a game and playful machine all wrapped into one- the player should ideally feel delighted and a little
competitive and stressed to maintain stake in the game.Its a game that can benifit from test-retest where participants
would do better the second time, so we expect people to want to play it again.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making a game for classmates and exhibition visitors`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Whack A Mole` | `Arcade Game` | `We borrowed the concept of the game from here` |
| `Website` | `culinaryschools.org/kids-games/whack-a-mole` | `Referenced a digital HTML5 version of Whack-a-Mole to understand how the game translates to a screen` |
| `Video Game` | `Digital Whack-A-Mole games (various)` | `Inspired how a physical arcade game can be recreated digitally using clicks instead of a mallet` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`Unlike traditional digital Whack-a-Mole games that use a mouse or keyboard, our version is controlled using a custom touch-sensitive mat powered by an ESP32 microcontroller. This brings the game closer to the physical arcade experience — players tap the mat just like hitting a real mole, making it more interactive and hands-on. The combination of Python software and custom ESP32 hardware makes this a unique build that goes beyond a typical screen-based game.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`Look at the screen, Hit the same pad as on which the mole appears, the hit is recorded as "hit" or "miss", the score gets added with each hit and the level continues to the next, the next level features mole appearence in lesser interval`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Any player who wants to experience traditional arcade game` |
| Age range | `5-60` |
| Solo or multiplayer | 'Solo` |
| Expected duration of one round | `30 seconds` |
| What should the player feel? | `Player should feel the adrenaline of hitting the right mole at the right time` |
| Is explanation required before use? | `No explanation is required as the game is self explainatory` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `Player will be handed with a hammer and the screen on which the game will be displayed`
2. **Start:** `Player will have to follow with a hit on the same hole as the mole appears`
3. **First Action:** `They directly hit the pad same as the mole appearance`
4. **Main Interaction:** `The mole keeps changing it's holes within fraction of a second`
5. **System Response:** `On a successful hit, the system responds with a HIT and for the miss, it responds with a MISS, there's also a condition of bonus if the player hits a combo or hatrick`
6. **Win / Lose / End Condition:** `Each game ends with 4 levels and the final score is calculated`
7. **Reset:** `The score gets recordeed at the end of each game and the player feeds his/her name and it shows on the leaderboard`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `Just try hitting the right mole pad'

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [*] `The touch-sensitive mat connects to the computer via ESP32 and is recognized by the Python program`
- [*] ` Moles pop up randomly on the screen at set intervals`
- [*] `The player can whack a mole by tapping the corresponding zone on the mat`
- [*] `The game tracks and displays the player's score in real time`
- [*] `The game has a timer and ends after the time runs out, showing the final score`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`A working game where moles appear randomly on screen, 
the player can tap the ESP32 mat to whack them, and the 
score is displayed.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `combo availibility`
- `Sound effects when a mole is whacked or missed`
- `High score leaderboard that saves the top scores locally`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [ ] Mechanical
- [x] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [ ] Sound-based
- [ ] Light-based
- [x] Screen/UI-based
- [x] Fabricated structure
- [x] Game logic based
- [x] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`Mole appears in the game in let's say hole-1, the players hits the pad-1 with the hammer and this input is recorded by the system, it is then triggered to the game by the keyboard number key which was connected to the touchpad through esp32. This data is matched and preocessed and successful HIT is recorded and shown on the screen. This continues with changing position of the mole.`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Touchpin sensors as input]` | Input | `all the touchpins are mapped with the keyboard keys` |
| `[ESP32 / Controller]` | Processing | `ESP32 has connected bluetooth keyboard with touchpins, i.e. numbpad keys to touchpins. It records and processes each hit by the player` |
| `Computer as display` | Output | `Wack a mole game interface is shown live on the screen` |
| `6 metal sheets have been connected to 6 touchpins on the esp32` | Physical Action | `these pins are further connected to keyboard which triggers the game` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `30 inches` |
| Width | `20 inches` |
| Height | `0.5 inches` |
| Estimated weight | `400 gms` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [x] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`Simple mechaninsm of hitting the touchpad and recording of the value to show win/loss`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[NA]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `NA` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[NA]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `Fat wires` | `10 metres` | `To be used as extention of touchpins` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Write here]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `MicroPython ` | `Connecting the digital interface to the physical build, computing touch sensitivity` |
| `Python` | `Running of the game` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`There are 3 Main Codes - The micropython code that uses the bluetooth keyboard and touchpads, the game code that runs the display and scorekeeping, and the calibration code that can be run to check touch thresholds. 
Startup Behavior:
On startup, the system initializes the hardware components including the display, touchpads, and bluetooth module. It establishes a Bluetooth connection to emulate a keyboard interface. The main game code is loaded.
Input Handling:
The system receives input primarily through touchpads. Each touchpad detects user interaction based on predefined thresholds. Touch inputs are translated into keyboard interaction. During gameplay, touch inputs are interpreted as player actions.
Sensor Reading:
Touch sensors continuously read input values from the touchpads. These readings are compared against calibrated threshold values to determine whether a valid touch has occurred. The calibration code can be used to monitor and adjust these threshold values for accuracy.
Decision Logic:
The system processes touch inputs and determines the appropriate response. In-game it updates the game state, checks for valid moves, and manages scoring logic. The system ensures only valid and intentional touches trigger actions.
Output Behavior:
The display shows the game interface, scores, and feedback to the user. Outputs  include visual updates such as score changes and round changes, and indications of hits and misses.
Communication Logic:
The system uses Bluetooth to communicate between micropython and game console, acting as a wireless keyboard. It sends keypress signals based on touch input. The connection is maintained and re-established if interrupted.
Reset Behavior:
On reset or restart, the system clears all temporary states such as local scores and input buffers. It keeps track of scores on a separate file. 
`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`There are two main code flowcharts (excluding calibration):
LINK-1 - MICROPYTHON FLOWCHART - https://canva.link/57eb4on5s6tugwz
LINK-2 - GAME FLOWCHART - https://canva.link/ozaabdakyfat8a4
`

## 10.4 Pseudocode

```text
there will be two mai  pseudocodes:
1. GAME CODE------------------------------
start
IMPORT LIBABRIES
INITIALIZE game (screen, audio, assets)
REPEAT
    DISPLAY Start Screen
    WAIT until ENTER pressed

    score == 0

    FOR each round FROM 1 to 4 DO
        DISPLAY Round Info

        SET timer == round duration
        INITIALIZE moles, combo ← 0

        WHILE timer > 0 DO
            READ user input

            IF key (1–6) pressed THEN
                IF mole present at position THEN
                    REMOVE mole
                    ADD RED MOLE
                    INCREMENT score
                    INCREMENT combo
                ELSE
                    RESET combo
                ENDIF
            ENDIF

            SPAWN new moles (if limit not reached)
            REMOVE expired moles

            UPDATE display (score, time, moles)

            DECREASE timer
        END WHILE
    END FOR

    INPUT player name
    STORE (name, score) in leaderboard
    SORT leaderboard (highest score first)

    DISPLAY leaderboard

UNTIL user presses ESC

END
2. MICROPYTHON  CODE------------------------------

START

INITIALIZE 6 touch sensors
SET threshold values for each pad
SET key codes for each pad

INITIALIZE BLE keyboard AND libraries

DISPLAY "Waiting for connection"

WHILE keyboard not connected DO
    WAIT
END WHILE

DISPLAY "Connected"

INITIALIZE last_trigger[6] == 0
SET cooldown time == 200 ms

FUNCTION ReadFiltered(sensor):
    total == 0
    REPEAT 3 times:
        total ← total + sensor value
    RETURN average value
END FUNCTION

LOOP forever:
    current_time == current milliseconds

    FOR each pad i from 1 to 6 DO
        value ← ReadFiltered(pad[i])

        IF value < threshold[i] THEN
            IF (current_time - last_trigger[i]) > cooldown THEN
                SEND key[i] via BLE
                last_trigger[i] ← current_time
            ENDIF
        ENDIF
    END FOR

END LOOP

END
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [x] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` |
| `[GI Metal Sheet]` | `[6*6 inches*2]` | `[No- procured from lab]` | `[It provides a more stable diffusion of charge throughout]` |
| `[Foam board and Alluminium foil]` | `[Yes]` | `[400 Rupees]` | `[FOam board provides a stable base and foil was needed to cover the wooden mallet]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`Metal sheets were used as there were many issues in using aluminium foil as touchpads. As it was not smooth, it was reacting very strangely with the touch sensors`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Handmade paper]` | `[to cover the final project mat]` |
| `[Telesheet and aluminium foil]` | `[to cover the mallet and increase the overall stability of the structure]`|

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[0]` |
| Mechanical parts | `[0]` |
| Fabrication materials | `[500]` |
| Purchased extras | `[0]` |
| Contingency | `[0]` |
| **Total** | `[500]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Cost is fairly Bearable]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`Working to our strengths, we will divide tasks based on our strongest affinity. Descisions will be made bilaterally though discussion and any changes or new ideas will be entertained and discussed. Progress will be checked through collectively decided deadlines and milestones. If a task is delayed, the responsible party will provide valid reason and a new proposed deadlinewill be set collectively. Dicumentation will be maintained through notes and video.`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline(DD/MM/YY) | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `Radhika` | `2` | `07/04/26` | `None` | `DONE` |
| T2 | `[Complete BOM]` | `Onkar` | `1` | `09/04/26` | `T1` | `DONE` |
| T3 | `[Test electronics]` | `Onkar` | `2` | `09/04/26` | `T1` | `DONE` |
| T4 | `[Build structure]` | `Onkar` | `6` | `10/04/26` | `T1` | `DONE` |
| T5 | `[Write control code]` | `Radhika` | `12` | `10/04/26` | `T1, T3` | `DONE` |
| T6 | `[Integrate system]` | `Radhika` | `4` | `15/04/26` | `T1, T4, T5` | `DONE` |
| T7 | `[Playtest]` | `Onkar and Radhika` | `4` | `17/04/26` | `T1, T6` | `DONE` |
| T8 | `[Refine and document]` | `Onkar and Radhika` | `8` | `19/04/26` | `T1, T7` | `DONE` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `Radhika and Onkar` | `N/A` |
| Electronics | `Onkar` | `N/A` |
| Coding | `Radhika` | `N/A` |
| App | `N/A` | `N/A` |
| Mechanical build | `Onkar` | `N/A` |
| Testing | `Onkar and Radhika` | `N/A` |
| Documentation | `Radhika and Onkar` | `N/A` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [X] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [x] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [x] CAD / structure planning completed
- [x] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [x] App connected if required
- [x] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `Finalise Game and Concept` | `We brainstormed multiple ideas as went with the most appropriate one` | `We had been planning for certain ideas that didn't work out so we had to review the mehcanical and code requirements` | `finalise material` |
| Week 2 | `PLaytest(self) and finalise material ` | `We found a few vidsual changes to make to the game, decided to add music, and finalised on using a wooden hammer wrapped in foil after a lot of playtesting. ` | `We are on track` | `work on finalising` |
| Week 3 | `Finalise Code  and Mat, Playtest` | `We did this right on schedule. All physical and digital components were completed on time.` | `We got insights from playtesting for refinement.` | `Work on Refinement` |
| Week 4 | `Refine Physical Interface and Game Code` | `We ran into issues with the calibration and hammer mechanics so we spent extra time on that. ` | `Refinement still happened but on a 2-3 day offset. ` | `Ensure that all sensitivities are calibrated correctly` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`Will the sensitivity be callibrated correctly so that it trigeers the keyboard?`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `code` | `If the laptop successfully connects through ESP32, and the print statement states 'connected'` |
| `[Calibration of Force]` | `physical and code` | `A wide range of force gets detected to account for a wide range of people playing the game.` |
| `[Calibration of Sensor]` | `physical and code` | `non-touch and touch thresholds define whether there is a keypad trigger` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `Observe Behaviour for signs of confusion` |
| Is the interaction satisfying? | `Ask for feedback` |
| Do players want another turn? | `Wait for them to ask, then ask them` |
| Is the challenge balanced? | `Test with various players` |
| Is the response clear and immediate? | `Observe Behaviour for signs of confusion, observe interface for delay` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[09/04/26]` | `[We realised that there were only 7 working touchpins. We had planned for 9.]` | `Technical` | `We changed the number of touchpins and recalibrated material` | `Worked` | `Finalise Game` |
| `[11/04/26]` | `There wasn't enough competitiveness` | `Gameplay` | `Added scoreboard and rating from S-C` | `Worked` | `Finalise mehcnics and code` |
| `[13/04/26]` | `The hammer was not showing touch as well as it should` | `Mechanical` | `We made the foil composition to just one type` | `Worked` | `Playtest` |
| `[14/04/26]` | `The visuals were hard to see for some players` | `[UI]` | `Increase size of window, create new custom pixel art sprites for contrast` | `Worked` | `Finalise` |
| `[16/04/26]` | `5 rounds were very time consuming and led to fatigue` | `Gameplay` | `We reduced rounds to 4 and reduced duration. We also added music` | `Worked` | `` |
| `[18/04/26]` | `The touch sensitivity became jittery` | `Technical, Mechanical` | `Changed thresholds again, uncrossed wires and increased threshold values again` | `Worked` | `` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `Friend` | `They played 5 rounds of the game.` | `The touch sensitivity was not calibrated to the amount of force they were using so they were sometimes missing` | `They enjoyed the hitting part` | `[]` |
| `Peer` | `Played Multiple times and got multiple highscores as they got more used to it` | `Didn’t know which touchpad controlled what action` | `Simple controls` | `Add labels or visual indicators for controls` |
| `Classmate` | `Played multiple rounds quickly` | `Was unsure when a round started/ended` | `Watching score updates live` | `Add clearer round start/end indicators` |
| `Peer` | `Played a full game and watched others` | `Didn’t know which touchpad controlled what action` | `Simple controls` | `Add labels or visual indicators for controls` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.
--
Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[9-4-26]` | `[The basic circuitry bades on A1]` | `[All the other ideas had some flaw or restrictions]` |
| `v2` | `[11-4-26]` | `[The test code was done along with the game interface to be tested with kepboard and touchpads]` | `[Code could not have been put for the later part.]` |
| `v3` | `[14-4-26]` | `[The final build with the mat of metal sheets and metal mallet were created successfully for the final test run with code]` | `[Metal sheets were chosen to be used rather than foil paper as they were smoother and more sensitive to the touch]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[The final version stands with a fully functioning game coded in python itself and along with that a clean and inviting wack a mole pad has been created with tactile touchpads, hidden and clean wires, and a mallet to hit the pad with. This together is working as a good old game of WACH A MOLE]`

## 18.2 What Works Well
- `[The touchpads a re working perfectcly with the digital keyboard]`
- `[Right keys are being triggered at the right time]`
- `[The game is responding well with each hit]`

## 18.3 What Still Needs Improvement
- `[The breadboard along with circuit could be hidden well in a box so the final setum looks clean]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Player journey is written
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [x] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
