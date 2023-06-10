from snake import Snake
from food import Food
from score_board import ScoreBoard
from turtle import Screen, mode, Turtle
import time
score_board = ScoreBoard()


def left():
    if snake.head.heading() != 90:
        snake.head.setheading(270)


def right():
    if snake.head.heading() != 270:
        snake.head.setheading(90)


def up():
    if snake.head.heading() != 180:
        snake.head.setheading(0)


def down():
    if snake.head.heading() != 0:
        snake.head.setheading(180)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("snake game")
mode("logo")


game_is_on = True

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)

while game_is_on:
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        score_board.write_gg()
        break
    for x in range(2, len(snake.snake_segments)-1):
        if snake.snake_segments[x].distance(snake.head) < 20:
            score_board.write_gg()
            game_is_on = False

    snake.move_snake()
    screen.update()
    time.sleep(0.1)
    score_board.write_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.refresh_score()
        snake.add_seg()
screen.exitonclick()


















