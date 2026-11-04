# The Mystery Island - The Lost Treasure

## Project Overview

The Mystery Island is a single-player, terminal-based text adventure game. The player discovers an old map in an abandoned library leading to an unknown island where a legendary treasure has been hidden for centuries.

To win, the player must explore different locations, solve puzzles, avoid hazards, and collect specific items to unlock the final treasure chamber before losing all their lives. The game relies entirely on core Python concepts (functions, lists, variables, and control flow) without using classes or object-oriented programming.

## How the Game Works

The game operates on a continuous while loop managed by the main script. Here is exactly how the internal mechanics function:

1. **Initialization:** When the game starts, the player inputs their name. The system initializes three core variables: Health (3), Score (0), and Inventory (an empty list). It also creates a list to track completed locations so players cannot replay areas to farm points.

2. **The Main Menu:** The player is presented with a status screen and a menu of locations to explore (e.g., Dark Forest, Crystal Cave).

3. **Exploration & Puzzles:** Selecting a location triggers a puzzle or riddle.

4. **Resolution Check:**

   * **Correct Answer:** The scoring system adds points (e.g., +20), and the inventory system appends the location's specific item (e.g., "Map Fragment") to the inventory list. The location is marked as completed.

   * **Incorrect Answer:** The player loses 1 health point. The health system ensures the player's lives never drop below zero.

5. **Win/Lose Triggers:** After every action, the game checks for end conditions. If health reaches 0, the player loses. If the player attempts to enter the final Treasure Chamber, the game verifies that the inventory list contains all required items. If they have the items, they win the game. If not, they are sent back to the menu.

## Gameplay Flowchart

Below is the logical flow of the game's core loop:

```text
                         START GAME
                              |
                              v
                        INITIALIZATION
                  Health, Score, Inventory
                              |
+---------------------------->+<----------------------------+
|                             |                             |
|                             v                             |
|                         MAIN MENU                         |
|                     Location Selection                    |
|                             |                             |
|              +--------------+--------------+              |
|              |                             |              |
|              v                             v              |
|       ISLAND LOCATION               TREASURE CHAMBER      |
|       "Solve Puzzles"               "Final Puzzle"        |
|              |                             |              |
|       +------+------+               +------+------+       |
|       |             |               |             |       |
|       v             v               v             v       |
|    CORRECT        WRONG         ALL ITEMS    MISSING ITEMS|
|       |             |               |             |       |
|  +Score/Item    -1 Health        YOU WIN!         |       |
|       |             |               |             |       |
|       +------+------+               v             |       |
|              |                     END            |       |
|              v                                    |       |
|        CHECK HEALTH                               |       |
|              |                                    |       |
|       +------+------+                             |       |
|       |             |                             |       |
|       v             v                             |       |
| HEALTH > 0      HEALTH = 0                        |       |
|       |             |                             |       |
|       |             v                             |       |
|       |         GAME OVER                         |       |
|       |             |                             |       |
|       |             v                             |       |
|       |            END                            |       |
+-------+                                           +-------+
```

## How to Run the Game

1. Clone this repository to your local machine.

2. Ensure you have Python installed (Python 3.x recommended).

3. Open your terminal or command prompt.

4. Navigate to the project folder.

5. Run the game using the following command:
   `python main.py`

## Project File Structure

The project is modularized into the following files to separate game logic and prevent conflicts:

* **main.py**: Starts the game, displays the main menu, and controls the central `while` loop.

* **locations.py**: Contains location descriptions, choices, and exploration logic.

* **puzzles.py**: Stores riddles, hints, and answer-checking logic.

* **player.py**: Handles player name collection, health reduction limits, and status updates.

* **inventory.py**: Manages adding items to the inventory list and preventing duplicates.

* **scoring.py**: Updates points and calculates the final win/lose state based on health and items.
