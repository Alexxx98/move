import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from pydub import AudioSegment
from pydub.playback import play
import os


SIT_TIME = "01:00:00"
MOVE_TIME = "0:10:00"

TIME_FORMAT = "%H:%M:%S"

FINISH_TIME = datetime.strptime("00:00:00", TIME_FORMAT)
SECOND = timedelta(seconds=1)

done = False

def main():

    root = tk.Tk()
    root.geometry("360x240")
    root.resizable(False, False)
    root.title("Move")

    time_label = ttk.Label(root, text=SIT_TIME, font=("Arial", 32, "bold"))

    time_label.pack()
    time_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    style = ttk.Style()

    style.configure("Custom.TButton", font=("Arial", 16, "bold"), justify="center")

    start_button = ttk.Button(
        root, text="Start", command=lambda: [start_counting(SIT_TIME, time_label), make_undone()], style="Custom.TButton"
        )
    stop_button = ttk.Button(
        root, text="Stop", command=time_stop, style="Custom.TButton"
        )

    start_button.grid(row=0, column=0, padx=25, pady=150)
    stop_button.grid(row=0, column=1, padx=0, pady=150)

    root.mainloop()


def start_counting(start_time, label):
    datetime_start_time = datetime.strptime(start_time, TIME_FORMAT)

    if datetime_start_time <= FINISH_TIME and not done:
        label.config(text=SIT_TIME)
        return move()

    elif datetime_start_time > FINISH_TIME:
        datetime_start_time -= SECOND
        start_time = datetime_start_time.strftime(TIME_FORMAT)

        label.config(text=start_time)
        label.after(1000, lambda: start_counting(start_time, label))


def time_stop():
    pass


def make_undone():
    global done
    done = False


def move():
    global done

    window = tk.Tk()
    window.geometry("360x240")
    window.resizable(False, False)
    window.title("Move")

    time_label = ttk.Label(window, text=MOVE_TIME, font=("Arial", 32, "bold"))

    time_label.pack()
    time_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    move_label = ttk.Label(window, text="Move", font=("Arial", 32, "bold"))

    move_label.pack()
    move_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    start_time = MOVE_TIME

    def timer(start_time, label):
        datetime_start_time = datetime.strptime(start_time, TIME_FORMAT)

        if datetime_start_time <= FINISH_TIME:
            return

        datetime_start_time -= SECOND
        start_time = datetime_start_time.strftime(TIME_FORMAT)

        label.config(text=start_time)
        label.after(1000, lambda: start_counting(start_time, label))

    if not done:
        window.after(1000, lambda: timer(start_time, time_label))
        done = True
    window.mainloop()


if __name__ == "__main__":
    main()
