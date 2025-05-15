""" Class to create snake """
from turtle import Turtle, Screen
from time import sleep

MOVE_DISTANCE = 10
SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ Class to create snake and actions """
    def __init__(self):
        self.screen = Screen()
        self.create_screen()
        self.segments = []
        self.create_snake(SIZE)
        self.head = self.segments[0]
        self.move()

    def create_snake(self, size):
        """ function to create snake """
        for _ in range(size + 1):
            self.add_segment((-_ * 10, 0))

    def add_segment(self, pos):
        """ create a segment of the snake """
        segment = Turtle("square")
        segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        segment.penup()
        segment.color("white")
        segment.setpos(pos)
        self.segments.append(segment)

    def extend(self):
        """ add a segment to the snake """
        last_seg_pos = self.segments[-1].pos()
        self.add_segment(last_seg_pos)

    def create_screen(self):
        """ screen set up"""
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.title("Classic Snake Game")
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")
        self.screen.onkey(self.go_rt, "Right")
        self.screen.onkey(self.go_lt, "Left")

    def move(self):
        """ function to play the snake game """
        self.screen.update()
        sleep(.1)
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def go_up(self):
        """ function to go up """
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def go_down(self):
        """ function to go up """
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def go_rt(self):
        """ function to turn right """
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def go_lt(self):
        """ function to turn left """
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
