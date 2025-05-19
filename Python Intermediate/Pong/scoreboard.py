""" Class to track score """
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """ Class to track the score """
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(pos)

    def increase_score(self):
        """ function to increase score """
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """ function to advise the game has ended """
        self.color("red")
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
