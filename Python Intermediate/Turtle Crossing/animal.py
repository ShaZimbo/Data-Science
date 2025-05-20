""" Create turtle to cross road """
from turtle import Turtle
FINISH_LINE = 280


class Animal(Turtle):
    """ create turtle """
    def __init__(self):
        super().__init__()

    def start_pos(self):
        """ go to start line"""
        self.penup()
        self.goto(0, -280)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.showturtle()

    def move_up(self):
        """ move turtle up """
        self.fd(10)
