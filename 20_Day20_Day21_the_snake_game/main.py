from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from menu import Menu
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1C1924")
screen.title("The Snake Game")
screen.tracer(0)

STARTING_SPEED = 0.1        # seconds between moves (smaller = faster)
SPEED_UP_FACTOR = 0.9       # speed factor for hard mode (0.9 = 10% faster)
MIN_SPEED = 0.03            # top speed (smaller = faster)

# Difficulty selection menu
menu = Menu()
selecting = True

def confirm_difficulty():
    global selecting
    selecting = False

screen.listen()
screen.onkey(menu.select_up, "Up")
screen.onkey(menu.select_down, "Down")
screen.onkey(confirm_difficulty, "Return")

while selecting:
    screen.update()
    time.sleep(0.05)

difficulty = menu.difficulty
menu.clear()
screen.onkey(None, "Return")

# Build the game
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_speed = STARTING_SPEED

def restart():
    global game_is_on, game_speed

    snake.reset()
    food.refresh()
    scoreboard.reset()

    game_speed = STARTING_SPEED
    game_is_on = True

game_is_on = True

# Rebind the arrow keys from menu navigation to snake controls
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(restart," ")

while True:
    time.sleep(game_speed)
    if game_is_on:
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.score_increase()

            if difficulty == "hard":
                game_speed = max(MIN_SPEED, game_speed * SPEED_UP_FACTOR)

        if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            game_is_on = False
            scoreboard.game_over()
        for segment in snake.snake_segments[1::]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    screen.update()
