""" Class to create board """
from turtle import Turtle, Screen


class Board(Turtle):
    """ Class to set up game board """
    def __init__(self):
        super().__init__()
        self.board = Screen()
        self.line = Turtle()
        self.board.bgcolor("black")
        self.board.setup(800, 600)
        self.board.title("Classic Pong")
        self.line.hideturtle()
        self.line.setpos(0, -280)
        self.line.seth(90)
        self.board.listen()

    def create_board(self):
        """ function to create board """
        for _ in range(30):
            self.line.color("white")
            self.line.fd(10)
            self.line.penup()
            self.line.fd(10)
            self.line.pendown()
