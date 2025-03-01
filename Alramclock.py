# Import Required Libraries
from tkinter import *
import datetime
import time
import winsound
from threading import Thread

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")

# Use Threading
def Threading():
    # Fetch values from Tkinter variables before starting the thread
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    t1 = Thread(target=alarm, args=(set_alarm_time,))
    t1.start()

def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break  # Exit loop after playing the alarm sound

# Add Labels, Frame, Button, OptionMenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = [f"{i:02d}" for i in range(24)]  # Generates '00' to '23'
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = [f"{i:02d}" for i in range(60)]  # Generates '00' to '59'
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = [f"{i:02d}" for i in range(60)]  # Generates '00' to '59'
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
