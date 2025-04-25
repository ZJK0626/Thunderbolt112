# Thunderbolt112

**Author:** Junke Zhao

---

## About the Game

**Thunderbolt112** is the final project for CMU's course [15-112: Fundamentals of Programming].  
Inspired by classic arcade games like *Space Invaders* and *Thunderbolt*, this game challenges players to control a plane, defeat enemies, dodge attacks and obstacles, and reach the final destination.

---

## How to Run

1. Ensure you have **Python 3.0 or above** installed.
2. Install the required `cmu_graphics` library by following the instructions [here](https://www.cs.cmu.edu/~112/notes/hw7.html).
3. Run the game script to start playing!

---

## Features

- 🎨 **Well-Designed User Interface**
- 🚀 **3 Levels** with increasing difficulty and win/lose conditions
- ✈️ **2 Types of Player-Controlled Planes**
- 👾 **6 Types of Enemies** with unique movement and attack patterns
- 💥 **3 Types of Enemy Bullets**:
  - Straight line
  - Sinusoidal path
  - Zigzag path
- 🖱️ **Smooth Mouse-Following Movement** with acceleration and deceleration
- 🔥 **Collision Detection**: Different effects depending on the colliding objects

---

## How to Play

1. Click **Start Game** to choose your character and level.
2. **Unlock new levels** by completing current ones and achieving the score goals.
3. **Control your plane** by moving your mouse — the plane follows your mouse's track.
4. **Life Points**: Both players and enemies have life points. Getting hit reduces life points.
5. **Obstacles**: Avoid crashing into obstacles — some are breakable, others are indestructible.
6. **Victory and Defeat**:
   - Destroy enemies by depleting their life points.
   - If your life points drop to zero, the game is over.

---

## Enemy Types

| Enemy          | Description |
|----------------|-------------|
| **Small Plane** | Basic enemy. Fires straight bullets at the player. Low attack power. |
| **Sine Plane** | Moves in a sinusoidal pattern, firing targeted bullets. Moderate attack power. |
| **Zigzag** | Flies toward the player while firing zigzagging bullets. |
| **Solar Pirate** | Boss of Level 1. Fires 3 bullets at once. High life points. |
| **Galaxy Pirate** | Boss of Level 2. Alternates between two attack modes: five-way fire and targeted double shots. |
| **Cosmic Pirate** | Boss of Level 3. The ultimate challenge! |

---

## Item Types

| Item            | Effect |
|-----------------|--------|
| **Blue Meteorite** | Breakable obstacle. No bullets. |
| **Red Meteorite** | Indestructible obstacle. No bullets. |
| **Dropped Item L** | Restores 20 life points. |
| **Dropped Item B** | Increases attack power by 5 points. |
| **Dropped Item A** | Increases shooting frequency by 1.5×. |

---

## References

- **Art Resources**: Created using [DALL·E](https://chat.openai.com/)

---
