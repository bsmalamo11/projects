# Voice Control Humanoid Robot

## Overview

The **Voice Control Humanoid Robot** is a versatile robotic system controlled via serial commands. The robot can move forward, backward, turn left, turn right, and stop based on commands received through the serial interface. It utilizes ultrasonic distance measurement to avoid obstacles, ensuring smooth operation.

## Components

- **AFMotor Library**: Controls DC motors for movement.
- **Servo Library**: Manages servo motor for directional changes.
- **Ultrasonic Sensor**: Measures distance to avoid obstacles.

## Hardware

- **Motors**: Four DC motors for movement.
- **Servo**: Controls the direction of the robot.
- **Ultrasonic Sensor**: Measures the distance to obstacles.
- **Arduino Board**: Microcontroller to run the code.

## Pin Configuration

- **trig**: Connected to analog pin A4.
- **echo**: Connected to analog pin A5.

## Functions

- **`setup()`**: Initializes serial communication, pin modes, and attaches the servo.
- **`forward()`**: Moves the robot forward.
- **`backward()`**: Moves the robot backward.
- **`left()`**: Turns the robot left.
- **`right()`**: Turns the robot right.
- **`Stop()`**: Stops all motor movements.
- **`loop()`**: Reads commands from the serial interface and executes corresponding movements.
- **`ultrasonic()`**: Measures distance using the ultrasonic sensor.

## Command List

The robot responds to the following commands via serial input:

- `move forward#`: Moves the robot forward until an obstacle is detected.
- `move backward#`: Moves the robot backward.
- `turn left#`: Turns the robot left.
- `turn right#`: Turns the robot right.
- `stop#`: Stops all movements.

## Usage

1. **Upload the Code**: Load the provided Arduino sketch onto your Arduino board.
2. **Connect Serial Monitor**: Open the serial monitor in the Arduino IDE.
3. **Send Commands**: Type the commands as listed above and observe the robot's response.

## Notes

- Ensure all components are correctly wired as per the pin configuration.
- Adjust the `max_distance` in the code if necessary to suit your environment.
- The robot uses a delay mechanism to ensure smooth turning; adjust delay times if needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- AFMotor Library
- Servo Library
- Ultrasonic Sensor Documentation

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
