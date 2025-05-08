""" Create shapes with an increasing number of corners """
import random
from turtle import Turtle, Screen, colormode

colormode(255)
tommy = Turtle()


def ranc():
    """ Function to choose color """
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return tommy.color(r, b, g)


tommy.speed(0)
tommy.shape("turtle")

for t in range(3, 11):
    ranc()
    for m in range(t):
        tommy.rt(360/t)
        tommy.fd(100)

SCREEN = Screen()
SCREEN.exitonclick()
