""" Classic Pong game """
from time import sleep
from turtle import Screen
from board import Board
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.tracer(0)
board = Board()
board.create_board()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard_r = Scoreboard((50, 240))
scoreboard_l = Scoreboard((-50, 240))

SCREEN.onkey(r_paddle.move_up, "Up")
SCREEN.onkey(r_paddle.move_down, "Down")

SCREEN.onkey(l_paddle.move_up, "w")
SCREEN.onkey(l_paddle.move_down, "s")

PLAY = True
while True:
    SCREEN.update()
    sleep(ball.game_speed)
    ball.move()
    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Paddle misses
    if ball.xcor() > 400:
        scoreboard_l.increase_score()
        ball.reset()
    if ball.xcor() < -400:
        scoreboard_r.increase_score()
        ball.reset()
    # Collision with paddle
    if (
        l_paddle.distance(ball) < 50 and ball.xcor() < -320
        or r_paddle.distance(ball) < 50 and ball.xcor() > 320
    ):
        ball.hit()
    # End of game
    if scoreboard_l.score == 10 or scoreboard_r.score == 10:
        score = Scoreboard((0, 0))
        score.game_over()
        PLAY = False
        break

SCREEN.exitonclick()
