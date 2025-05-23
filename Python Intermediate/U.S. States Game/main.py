""" U.S. States Game """
import turtle
import pandas as pd

MAP = turtle.Turtle()
ANSWER = turtle.Turtle()
ANSWER.hideturtle()
ANSWER.penup()
SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")
SCREEN.listen()
SCREEN.screensize(300, 300)
SCORE = 0
IMAGE = "./U.S. States Game/blank_states_img.gif"
SCREEN.addshape(IMAGE)
MAP.shape(IMAGE)
PLAY = True
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
given_answers = []
states_to_learn = []

states = pd.read_csv("./U.S. States Game/50_states.csv")

while PLAY:
    if SCORE == 50:
        ANSWER.setpos(0, 250)
        ANSWER.color("green")
        ANSWER.write(
            f"CONGRATULATIONS! {SCORE}/50", align=ALIGNMENT, font=FONT
            )
        PLAY = False
        break
    user_answer = SCREEN.textinput(
            f"{SCORE}/50", "What is another State's name?").title()
    if user_answer == "Exit":
        ANSWER.setpos(0, 250)
        ANSWER.write(
                f"{SCORE}/50 states guessed", align=ALIGNMENT, font=FONT
                )
        for state in states["state"]:
            if state not in given_answers:
                states_to_learn.append(state)
                to_learn = pd.DataFrame({"States": states_to_learn})
                to_learn.to_csv("./U.S. States Game/states_to_learn.csv")
        PLAY = False
        break
    for state in states["state"]:
        if user_answer == state and user_answer not in given_answers:
            SCORE += 1
            given_answers.append(user_answer)
            position = states[states["state"] == user_answer]
            x_coor = position.x.item()
            y_coor = position.y.item()
            ANSWER.setpos(x_coor, y_coor)
            ANSWER.write(state, align=ALIGNMENT)
SCREEN.exitonclick()
