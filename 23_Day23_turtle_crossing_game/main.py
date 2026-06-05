import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

def restart():
    global game_is_on
    player.reset()
    car_manager.reset()
    scoreboard.reset()
    game_is_on = True

screen.listen()
screen.onkey(player.move_front,"Up")
screen.onkey(player.move_back,"Down")
screen.onkey(restart, " ")

while True:
    time.sleep(0.1)
    screen.update()
    if game_is_on:
        car_manager.create_car()
        car_manager.move()
        for car in car_manager.all_cars:
            if car.distance(player) < 25:
                game_is_on = False
                player.can_move = False
                scoreboard.game_over()

        if player.ycor() > 270:
            player.reset()
            car_manager.level_up()
            scoreboard.level_up()