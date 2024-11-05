# Pomodoro Timer

A simple Pomodoro timer application built with Python's Tkinter library. This app helps you manage work and break intervals using the Pomodoro technique, a time-management method that encourages focused work sessions followed by short breaks. 

## Features
- **Work Sessions**: 25-minute work intervals.
- **Short Breaks**: 5-minute breaks after each work session.
- **Long Breaks**: 20-minute breaks after every 4 work sessions.
- **Checkmark Tracker**: Track completed work sessions with checkmarks.
- **Reset Functionality**: Reset the timer and clear progress.

## Pomodoro Technique Overview
The Pomodoro technique is a productivity method that breaks down work into focused sessions, followed by short breaks to refresh. A typical cycle is:
1. Work for 25 minutes (1 "Pomodoro")
2. Take a 5-minute break
3. Repeat steps 1 and 2 for four cycles, then take a longer break (20 minutes)

## Purpose
I developed this project to enhance my productivity, recognizing that I wasn't fully utilizing my potential. With this timer, I can stay focused during work sessions and take structured breaks, fostering both efficiency and motivation.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Taran856/pomodoro-start
    cd pomodoro-timer
    ```
2. Ensure you have Python installed (version 3.6 or above).
3. Install the Tkinter library if it's not already included:
    ```bash
    pip install tk
    ```
4. Place an image file named `tomato.png` in the same directory as the code for the timer background. 

## Usage
1. Run the code:
    ```bash
    python pomodoro_timer.py
    ```
2. The Pomodoro timer window will open.
3. Click **Start** to begin the timer. It will start with a work session and cycle through breaks based on the Pomodoro technique.
4. Click **Reset** to reset the timer to the initial state and clear all progress.

## Code Structure
- **Constants**: Define colors, font style, and time durations for work/break intervals.
- **Functions**:
    - `start_timer()`: Controls the timer mechanism, alternating between work and break sessions.
    - `count_down()`: Counts down each second, updating the timer display.
    - `reset_timer()`: Cancels the current timer, resets progress, and clears checkmarks.
- **UI Setup**: Sets up the Tkinter interface, including the timer label, start/reset buttons, and checkmark display.

## License
This project is licensed under the MIT License.

## Acknowledgements
- This project uses the Tkinter library to create the graphical user interface.
- Inspired by the popular productivity technique, the Pomodoro Technique.

## Contact
For questions or feedback, please reach out to [taranpatel1006@example.com](mailto:taranpatel1006@example.com).
