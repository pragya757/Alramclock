# Alarm Clock using Python (Tkinter & Multithreading)

**Overview**

This is a simple alarm clock application built using Python, Tkinter, and Multithreading. The user can set the alarm time using dropdown menus, and when the time matches the system's current time, an alarm sound will play.

# Features

Graphical User Interface (GUI): Built with Tkinter.
Multithreading Support: Ensures the GUI remains responsive while the alarm runs in the background.
Customizable Time Selection: Users can select hours, minutes, and seconds.
Plays Alarm Sound: A sound file (sound.wav) is played when the alarm time is reached.

# Screenshot
![Screenshot 2025-03-02 001341](https://github.com/user-attachments/assets/dffe88e9-8fc5-41e7-9bdd-d5d3588516e9)


# Requirements

Make sure you have Python installed (Python 3.6 or later recommended). You will also need the following Python libraries:
**pip install tk**

# Code Structure

alarm_clock.py: The main script containing the GUI and alarm logic.
sound.wav: The alarm sound file (provide your own).
README.md: Documentation file.

# Troubleshooting

If you get an error like RuntimeError: main thread is not in main loop, ensure that Tkinter variables are accessed only in the main thread.
If the sound doesn’t play, make sure sound.wav exists in the directory and is a valid sound file.
If the alarm doesn't stop after ringing, modify the alarm function to control sound playback.
