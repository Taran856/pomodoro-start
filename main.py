from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"           # Color for short break text
RED = "#e7305b"            # Color for long break text
GREEN = "#9bdeac"          # Color for work session text
YELLOW = "#f7f5dd"         # Background color
FONT_NAME = "Courier"      # Font style
WORK_MIN = 25              # Duration of work sessions in minutes
SHORT_BREAK_MIN = 5        # Duration of short breaks in minutes
LONG_BREAK_MIN = 20        # Duration of long breaks in minutes
reps = 0                   # Track the number of completed sessions
check = ''                 # Checkmarks to display completed sessions
timer = None               # Timer variable for countdown

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """Reset the timer to the initial state, cancel any ongoing countdown,
    and clear checkmarks and session count."""
    global timer
    global check
    global reps

    window.after_cancel(timer)          # Cancel the active timer
    label.config(text="Timer", fg=GREEN)  # Reset label to "Timer"
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer display
    check = ""                           # Clear checkmarks
    checkmark.config(text=check)
    reps = 0                             # Reset session count

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """Starts the timer, alternating between work and break sessions
    based on the current count of completed sessions (reps)."""
    global reps

    reps += 1                             # Increment session count

    work_sec = WORK_MIN * 60              # Work session duration in seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Short break duration in seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Long break duration in seconds

    # Every 8th session is a long break
    if reps % 8 == 0:
        count_down(int(long_break_sec))
        label.config(text="BREAK", foreground=RED)

    # Every 2nd, 4th, 6th session is a short break
    elif reps % 2 == 0:
        count_down(int(short_break_sec))
        label.config(text="BREAK", foreground=PINK)

    # All other sessions are work sessions
    else:
        count_down(int(work_sec))
        label.config(text="WORK", foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """Recursive countdown function that updates the timer every second.
    When countdown reaches zero, it starts the next timer session."""
    global check
    global timer

    count_min = count // 60               # Minutes portion of countdown
    count_sec = count % 60                # Seconds portion of countdown

    if count_sec < 10:
        count_sec = "0" + str(count_sec)  # Format seconds with leading zero

    if count_min < 10:
        count_min = "0" + str(count_min)  # Format minutes with leading zero

    # Update displayed timer
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Update timer every second
    else:
        start_timer()                        # Start the next session when countdown finishes
        if reps % 2 == 0:
            check += '✔'                    # Add a checkmark for completed work sessions
            checkmark.config(text=check)     # Update checkmark display

# ---------------------------- UI SETUP ------------------------------- #

# Create the main window for the Pomodoro timer
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label for the timer header
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
label.grid(column=1, row=0)

# Canvas for displaying timer countdown on an image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button to initiate the timer
start_button = Button(text="start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button to reset the timer and checkmarks
reset_button = Button(text="reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# Label for displaying checkmarks for completed work sessions
checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

# Start the Tkinter main event loop
window.mainloop()
