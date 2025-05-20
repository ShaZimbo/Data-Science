""" Classic Snake Game """
from time import sleep
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

snake = Snake()
food = Food()
scoreboard = Scoreboard()
SCREEN = Screen()
SCREEN.tracer(0)
SCREEN.setup(600, 600)
SCREEN.bgcolor("black")
SCREEN.title("Classic Snake Game")


PLAY = True
while PLAY:
    SCREEN.listen()
    SCREEN.onkey(snake.go_up, "Up")
    SCREEN.onkey(snake.go_down, "Down")
    SCREEN.onkey(snake.go_rt, "Right")
    SCREEN.onkey(snake.go_lt, "Left")
    sleep(0.1)
    SCREEN.update()
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
        scoreboard.reset()
        play_again = (
            SCREEN.textinput("Continue?",
                             "Would you like to play again (y/n)?").lower()
            )
        if play_again == "n":
            PLAY = False
        else:
            snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            scoreboard.reset()
            play_again = (
                SCREEN.textinput("Continue?",
                                 "Would you like to play again (y/n)?").lower()
                )
            if play_again == "n":
                PLAY = False
            else:
                snake.reset()

SCREEN.exitonclick()
