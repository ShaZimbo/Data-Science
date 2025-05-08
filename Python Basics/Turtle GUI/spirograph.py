""" Create a spirograph """
import random
from turtle import Turtle, Screen, colormode

degrees = [0, 90, 180, 270]
colormode(255)
tommy = Turtle()


def ranc():
    """ Function to choose color """
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return tommy.color(r, b, g)


times = 50
tommy.speed(0)
tommy.shape("turtle")
for m in range(times):
    tommy.circle(100)
    tommy.lt(360/times)
    ranc()

SCREEN = Screen()
SCREEN.exitonclick()
