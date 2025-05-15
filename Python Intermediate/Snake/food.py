""" Class to create food with random locations """
from turtle import Turtle
import random


class Food(Turtle):
    """ Class to add food for snake """

    def __init__(self):
        super().__init__()

        self.color("DeepPink")
        self.penup()
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.shape("circle")
        self.speed("fastest")
        self.f_move()

    def f_move(self):
        """ function to move food """
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(rand_x, rand_y)
