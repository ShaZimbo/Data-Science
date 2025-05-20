""" Create cars for turtle crossing """
from turtle import Turtle
import random

colors = ["pink", "purple", "blue", "green", "yellow", "orange", "red"]
CAR_SPEED = 5


class Car:
    """ create cars """
    def __init__(self):
        self.all_cars = []
        self.move = CAR_SPEED

    def create_car(self):
        """ Create cars """
        cars = random.randint(1, 6)
        if cars == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(colors))
            y_cor = random.randint(-240, 240)
            new_car.setpos(320, y_cor)
            self.all_cars.append(new_car)

    def drive(self):
        """ set cars to drive on road """
        for car in self.all_cars:
            car.bk(self.move)

    def increase_speed(self):
        """ increase speed on level completion """
        self.move += self.move
