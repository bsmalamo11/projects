# Space Shooter Game

## Description

Space Shooter is an action-packed game built using Pygame where players control a spaceship to battle against waves of enemy ships. The objective is to defeat all enemies while avoiding their attacks and ensuring the player's spaceship doesn't get destroyed. The game features a scoring system based on levels and lives, with increasing difficulty as the player progresses.

## Features

- **Player Control**: Move the spaceship using keyboard inputs and shoot lasers to destroy enemy ships.
- **Enemy Waves**: Enemies spawn in waves with increasing difficulty, including different colors and types.
- **Health and Lives**: Track the player's health and remaining lives.
- **Sound Effects**: Includes sound effects for shooting lasers.
- **Background Music**: Optional background music can be added.
- **Health Bars**: Visual indicators for the player's health.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. **Clone the repository:**
    
    ```bash
    bashCopy code
    git clone https://github.com/yourusername/space-shooter-game.git
    cd space-shooter-game
    
    ```
    
2. **Install the required libraries:**
    
    ```bash
    bashCopy code
    pip install pygame
    
    ```
    
3. **Download Assets:**
Ensure that you have the following assets in the `assets` directory:
    - `pixel_ship_yellow.png` (Player ship)
    - `pixel_ship_red_small.png` (Red enemy ship)
    - `pixel_ship_blue_small.png` (Blue enemy ship)
    - `pixel_ship_green_small.png` (Green enemy ship)
    - `pixel_laser_yellow.png` (Player laser)
    - `pixel_laser_red.png` (Red laser)
    - `pixel_laser_blue.png` (Blue laser)
    - `pixel_laser_green.png` (Green laser)
    - `background-black.png` (Background)
    - `laser_sound_effect.wav` (Laser sound effect)

## Usage

1. **Run the game:**
    
    ```bash
    bashCopy code
    python game.py
    
    ```
    
2. **Controls:**
    - **Move Left**: `LEFT` arrow key or `A`
    - **Move Right**: `RIGHT` arrow key or `D`
    - **Move Up**: `UP` arrow key or `W`
    - **Move Down**: `DOWN` arrow key or `S`
    - **Shoot**: `SPACE` bar
3. **Objective:**
    - Destroy all enemy ships in each wave.
    - Avoid enemy attacks and keep track of your lives and health.

## Code Overview

- **`game.py`**: Main game script. Includes game logic, rendering, and event handling.
- **`Ship` class**: Base class for player and enemy ships. Manages ship properties, movement, and shooting.
- **`Player` class**: Inherits from `Ship`, specifically for the player's ship with health bar and shooting functionality.
- **`Enemy` class**: Inherits from `Ship`, specifically for enemy ships with movement and shooting functionality.
- **`Laser` class**: Handles laser properties, movement, and collision detection.

## Contributing

If you'd like to contribute to the development of this game, feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.