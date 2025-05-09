import random
from turtle import Turtle, Screen, colormode

colormode(255)


def ranc():
    """ Function to choose color """
    rgb_colors = [
        (236, 35, 108), (145, 28, 66),
        (239, 75, 35), (7, 148, 95), (220, 171, 45),
        (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0),
        (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98),
        (44, 170, 114), (211, 132, 166), (206, 57, 35)
    ]
    rand_rgb = random.choice(rgb_colors)
    return rand_rgb


dot = Turtle()
dot.ht()
dot.speed("fastest")
dot.up()
dot.setpos(-212.13, -212.13)
for _ in range(1, 11):
    for d in range(10):
        dot.dot(20, ranc())
        dot.fd(50)
    dot.setpos(-212.13, -212.13)
    dot.lt(90)
    dot.fd(50*_)
    dot.rt(90)

SCREEN = Screen()
SCREEN.exitonclick()

# import colorgram

# color_range = colorgram.extract('spot_painting.jpg', 20)

# colors = []

# for color in color_range:
#     rgb = color.rgb
#     colors.append((rgb.r, rgb.g, rgb.b))
