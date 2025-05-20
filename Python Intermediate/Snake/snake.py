""" Class to create snake """
from turtle import Turtle
START_POS = (0, 0)
MOVE_DISTANCE = 10
SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ Class to create snake and actions """
    def __init__(self):
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

    def move(self):
        """ function to play the snake game """
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def reset(self):
        """ function to reset snake """
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake(SIZE)
        self.head = self.segments[0]
        self.move()

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
