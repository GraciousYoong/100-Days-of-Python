from turtle import Turtle
import random

COLORS = ["#0b7285", "#ff6b6b", "#ffd43b"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.speed("fast")
            self.all_cars.append(new_car)

    def reset(self):
        for car in self.all_cars:
            car.goto(1000, 1000)
            car.hideturtle()
        self.all_cars.clear()
    
    def move(self):
        for car in self.all_cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
