""" Class to create paddles """
from turtle import Turtle


class Paddle(Turtle):
    """ class to create paddles """
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(pos)

    def move_up(self):
        """ move paddle up """
        new_y = self.ycor() + 20
        self.setpos(self.xcor(), new_y)

    def move_down(self):
        """ move paddle down """
        new_y = self.ycor() - 20
        self.setpos(self.xcor(), new_y)
