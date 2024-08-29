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
