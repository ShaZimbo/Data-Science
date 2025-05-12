""" Turtle race with betting input """
from turtle import Turtle, Screen
import random

SCREEN = Screen()
SCREEN.setup(925, 350)
bet = SCREEN.textinput("Place your bet",
                       "Who will win the race?\n"
                       "pink, purple, blue, green, yellow, orange, red.\n"
                       "Enter a color:")
colors = ["pink", "purple", "blue", "green", "yellow", "orange", "red"]
turtle_stats = {}
turtle_colors = {}

COUNT = 0

for n in range(7):
    n = Turtle("turtle")
    turtle_stats[n] = 5
    turtle_colors[n] = colors[COUNT]
    n.color(colors[COUNT])
    n.pu()
    n.setpos(-450, (-150 + (50 * COUNT)))
    COUNT += 1


RACE = True

while RACE is True:
    rand_t = random.choice(list(turtle_stats.keys()))
    rand_t.fd(10)
    turtle_stats[rand_t] += 5
    for key, value in turtle_stats.items():
        if value == 450:
            RACE = False

winner = max(turtle_stats, key=turtle_stats.get)
if turtle_colors[winner] == bet:
    print(f"You win! The winner is {turtle_colors[winner]}")
else:
    print(f"You lose! The winner is {turtle_colors[winner]}")
