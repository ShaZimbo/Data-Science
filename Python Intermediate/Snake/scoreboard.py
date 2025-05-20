""" Class to track Snake score """
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    """ Class to track the score """
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_high_score.txt", "r", encoding="utf-8") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update()

    def update(self):
        """ update scoreboard """
        self.clear()
        self.write(f"Score: {self.score}\tHigh Score: {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """ function to increase score """
        self.score += 1
        self.update()

    def reset(self):
        """ reset scoreboard retaining high score """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_high_score.txt", "w", encoding="utf-8") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()
