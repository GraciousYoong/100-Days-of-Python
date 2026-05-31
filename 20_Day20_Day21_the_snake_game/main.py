from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1C1924")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def restart():
    global game_is_on

    snake.reset()
    food.refresh()
    scoreboard.reset()

    game_is_on = True

game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(restart," ")

while True:
    time.sleep(0.1)
    if game_is_on:
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.score_increase()

        if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            game_is_on = False
            scoreboard.game_over()
    
        for segment in snake.snake_segments[1::]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    screen.update()
