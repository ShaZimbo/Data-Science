""" Turtle crossing game """
import time
from turtle import Screen
from cars import Car
from animal import Animal
from scoreboard import Scoreboard

animal = Animal()
car = Car()
scoreboard = Scoreboard()
SCREEN = Screen()
SCREEN.tracer(0)
SCREEN.listen()
SCREEN.onkey(animal.move_up, "Up")
SCREEN.setup(600, 600)
animal.start_pos()
scoreboard.display()
PLAY = True

while PLAY:
    time.sleep(0.1)
    SCREEN.update()
    car.create_car()
    car.drive()
    if animal.ycor() > 280:
        scoreboard.increase_level()
        car.increase_speed()
        animal.start_pos()
    for vehicle in car.all_cars:
        if animal.distance(vehicle) < 20:
            PLAY = False
            scoreboard.game_over()

SCREEN.exitonclick()
