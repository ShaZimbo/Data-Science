""" Scoreboard to track progress """
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):
    """ Class to track the score """
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 280)

    def display(self):
        """ Display level """
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        """ Increase level """
        self.level += 1
        self.clear()
        self.display()

    def game_over(self):
        """ Game over screen """
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
