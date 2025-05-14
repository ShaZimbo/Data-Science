""" Take the turtle on a random walk """
import random
from turtle import Turtle, Screen

SCREEN = Screen()
SCREEN.colormode(255)
tommy = Turtle()


def ranc():
    """ Function to choose color """
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return tommy.color(r, b, g)


angle = [0, 90, 180, 270]
tommy.speed(0)
tommy.shape("turtle")
tommy.pensize(10)

for _ in range(150):
    ranc()
    tommy.setheading(random.choice(angle))
    tommy.fd(20)

SCREEN.exitonclick()
