""" Flash Cards """
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_TITLE = "French Flash Cards"
COUNT = 0
CARDS_FILE = "./Flash Card Project/data/french_words.csv"
STUDY_FILE = "./Flash Card Project/data/to_learn.csv"
Q_CARD = ""
A_CARD = ""
to_learn_list = []
FLIP_TIMER = None


# ---------------------------- IMPORT WORDS --------------------------- #
def get_q_card():
    """ get next card """
    global Q_CARD, FLIP_TIMER
    try:
        words = pd.read_csv(STUDY_FILE)
    except FileNotFoundError:
        words = pd.read_csv(CARDS_FILE)

    window.after_cancel(FLIP_TIMER)
    if COUNT < len(words):
        Q_CARD = words["French"].iloc[COUNT]
        canvas.itemconfig(topic_text, text="French", fill="black")
        canvas.itemconfig(q_text, text=Q_CARD, fill="black")
        canvas.itemconfig(canvas_image, image=front_image)
    FLIP_TIMER = window.after(3000, get_a_card)


def get_a_card():
    """ get next card """
    global A_CARD, COUNT
    try:
        words = pd.read_csv(STUDY_FILE)
    except FileNotFoundError:
        words = pd.read_csv(CARDS_FILE)

    if COUNT < (len(words)):
        A_CARD = words["English"].iloc[COUNT]
        canvas.itemconfig(topic_text, text="English", fill="white")
        canvas.itemconfig(q_text, text=A_CARD, fill="white")
        canvas.itemconfig(canvas_image, image=back_image)
        COUNT += 1


# ---------------------------- SAVE TO LEARN -------------------------- #
def next_card():
    """ move on to next card """
    global COUNT
    try:
        words = pd.read_csv(STUDY_FILE)
    except FileNotFoundError:
        words = pd.read_csv(CARDS_FILE)

    if COUNT < len(words):
        get_q_card()
    else:
        canvas.itemconfig(topic_text, text="Done!")
        canvas.itemconfig(q_text, text="No more cards.")
        if to_learn_list:
            df = pd.DataFrame(to_learn_list)
            df.to_csv(STUDY_FILE, index=False)


def to_learn():
    """ add items to learn to new csv """
    global to_learn_list
    to_learn_list.append({"French": Q_CARD, "English": A_CARD})
    next_card()


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
FLIP_TIMER = window.after(3000, get_a_card)

canvas = Canvas(
    width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR
    )
front_image = PhotoImage(file="./Flash Card Project/images/card_front.png")
back_image = PhotoImage(file="./Flash Card Project/images/card_back.png")
canvas_image = canvas.create_image(400, 268, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
topic_text = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"), fill="black"
    )
q_text = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"), fill="black"
    )

# Buttons
yes_img = PhotoImage(file="./Flash Card Project/images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=next_card)
yes_button.grid(column=0, row=1, pady=20)
no_img = PhotoImage(file="./Flash Card Project/images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=to_learn)
no_button.grid(column=1, row=1, pady=20)

next_card()

window.mainloop()
