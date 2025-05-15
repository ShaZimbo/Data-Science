""" Class to track Snake score """
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    """ Class to track the score """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ function to increase score """
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ function to advise the game has ended """
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
