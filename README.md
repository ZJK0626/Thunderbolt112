# Thunderbolt112
# Author: Junke Zhao

# About the Game
This is the Term Project of CMU's 15-112, Fundamentals of Programming.
The idea is inspired by classic arcades and video games like Space Invader and Thunderbolt.
In this game, players need to control the character(plane), to beat enemies, avoid enemies' attack and obstacles and reach to the final destination.

# How to Run:
1. This game is programming in python, so make sure to have installed Python(3.0 above).
2. This game will use library cmu_graphics, follow this guidance to install the essential library: https://www.cs.cmu.edu/~112/notes/hw7.html

# Features:
1. Well-Designed User Interface.
2. 3 levels of increasing difficulty. Including win/lose condition.
3. 2 types of player-controlled planes.
4. 6 types of enemies, each has a different moving and attacking mode.
5. 3 types of enemies' bullets：The bullets are mathematically modeled and programmed. Including straight Line, Sinusoidal, zigzag, and they always target on player's location.
6. Moving acceleration: The plane's track will always follow the mouse moving. The plane accelerates and reaches a maximum speed after the mouse is moved, and decelerates when it reaches the mouse position.
7. Collisions: The game contains collision detection, which produces different effects depending on the colliding objects.

# How to Play:
1. Click 'Start Game' to choose the level and characters you will use.
2. Initially, there will be only 1 level unlocked. As you finish existing levels and meet the score goal, new levels will be unlocked
3. Moving your mouse to control the plane, it will follow your mouse's track.
4. Both you and your enemies will have a life point. When hit by bullets, the life point will be reduced.
5. There will also be obstacles in your view, some are breakable and some are not, try not to crash on them because it will also give rise to life point reduce.
6. When enemies' life points are 0, they are eliminated. However, if your life point are 0, the game will be over.

# Enemies' Type:
1. Small plane: The most basic type of the enemy, they shoot a straight line of bullets toward the player's location. The attack power is the lowest.
2. Sine Plane: An upgraded version of the enemy, they fire bullets that are directed towards the player's position while moving along a sinusoidal curve during their movement. The attack power is modest.
3. Zigzag: Another upgraded version of the enemy, they always fly toward the players' location and fire two bullets which move along a zigzag pattern during movement.
4. Solar Pirate: The boss of level 1. It fires three bullets in three directions at once and has a relatively high life point.
5. Galaxy Pirate: The boss of level 2. Its bullets have two types. The first type is to fire five bullets in five directions at once. Another type is to fire 2 bullets toward the direction where the player is. The two attack patterns will alternate.
6. Cosmic Pirate: The boss of level 3. 

# Items' Type
1. Blue Meteorite: Obstacles that CAN be destroyed by the player's attacks. Do not fire bullets.
2. Red Meteorite: Obstacles that CANNOT be destroyed by the player's attacks. Do not fire bullets.
3. Dropped Item L: A buff item that when the player takes it, the lifePoint will recovery for 20 points.
4. Dropped Item B: A buff item that when the player takes it, the attack power will increase for 5 points.
5. Dropped Item A: A buff item that when the player takes it, the shooting frequency will increase for 1.5 times.

# Reference:
1. The Art resources are created by DALL·E: https://chat.openai.com/
