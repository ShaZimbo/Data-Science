from tkinter import Tk, Canvas, PhotoImage, Button, Label, messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 7
LONG_BREAK_MIN = 15
CHECK_MARK = ""
REPS = 0
TIMER = None


def bring_to_front():
    """ force window to front """
    window.lift()
    window.attributes('-topmost', True)
    window.focus_force()
    window.after(1000, lambda: window.attributes('-topmost', False))


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """ reset settings """
    global REPS
    global CHECK_MARK
    global TIMER
    window.after_cancel(TIMER)
    CHECK_MARK = ""
    tick_label.config(text=CHECK_MARK)
    REPS = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_timer():
    """ timer settings """
    global REPS
    global CHECK_MARK
    REPS += 1
    if REPS % 8 == 0:
        bring_to_front()
        ok = messagebox.showinfo("Break", "Start long break")
        if ok:
            count_down(LONG_BREAK_MIN * 60)
            CHECK_MARK = ""
            tick_label.config(text=CHECK_MARK)
            timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        bring_to_front()
        ok = messagebox.showinfo("Break", "Start short break")
        if ok:
            count_down(SHORT_BREAK_MIN * 60)
            tick_label.config(text=CHECK_MARK)
            timer_label.config(text="Break", fg=PINK)
    else:
        bring_to_front()
        ok = messagebox.showinfo("Work", "Start working")
        if ok:
            count_down(WORK_MIN * 60)
            timer_label.config(text="Work", fg=GREEN)
            CHECK_MARK += "✔"
            tick_label.config(text=CHECK_MARK)
            window.attributes("-topmost", False)


# ---------------------------- COUNTDOWN MECHANISM -------------------- #
def count_down(count):
    """ display count down """
    global TIMER
    count_minute = math.floor(count / 60)
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Timer
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
    )
canvas.grid(column=1, row=1)
timer_label = Label(
    text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, "bold")
    )
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Check marks
tick_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick_label.grid(column=1, row=2)

window.mainloop()

