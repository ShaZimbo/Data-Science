""" Class to create ball """
from turtle import Turtle


class Ball(Turtle):
    """ Class to set up game board """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("DeepPink")
        self.penup()
        self.setpos(0, 0)
        self.x_bounce = 10
        self.y_bounce = 10
        self.game_speed = 0.1

    def move(self):
        """ Coordinates ball movement """
        new_x = self.xcor() + self.x_bounce
        new_y = self.ycor() + self.y_bounce
        self.setpos(new_x, new_y)

    def bounce(self):
        """ Bounce off wall """
        self.y_bounce *= -1

    def hit(self):
        """ bounce off paddle """
        if self.xcor() < 0:
            self.x_bounce = abs(10)
            self.game_speed *= 0.9
        if self.xcor() > 0:
            self.x_bounce = -abs(10)
            self.game_speed *= 0.9

    def reset(self):
        """ resets game """
        self.x_bounce *= -1
        self.setpos(0, 0)
        self.game_speed = 0.1
