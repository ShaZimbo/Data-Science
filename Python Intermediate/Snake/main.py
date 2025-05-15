""" Classic Snake Game """
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN = Screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

PLAY = True
while PLAY:
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.f_move()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if (
        snake.head.xcor() < -290
        or snake.head.xcor() > 290
        or snake.head.ycor() < -290
        or snake.head.ycor() > 290
    ):
        scoreboard.game_over()
        PLAY = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            scoreboard.game_over()
            PLAY = False

SCREEN.exitonclick()
