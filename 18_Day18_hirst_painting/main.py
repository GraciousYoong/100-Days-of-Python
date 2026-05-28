from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
dot = Turtle()
dot.speed("fastest")
dot.hideturtle()

colors_list = [(235, 37, 113), (143, 26, 67), (237, 72, 37), (220, 164, 55), (15, 140, 88), (174, 162, 50), (33, 122, 186), (52, 189, 227), (173, 44, 94), (242, 219, 57), (80, 24, 74), (127, 190, 92), (250, 223, 0), (23, 169, 122), (189, 67, 41), (207, 133, 165), (147, 29, 25), (35, 181, 208), (11, 101, 56), (239, 163, 193), (243, 166, 157), (164, 213, 180), (98, 8, 6), (140, 214, 231), (8, 70, 28), (50, 140, 208)]

start_x = -250
start_y = -250

dot.penup()
dot.goto(start_x, start_y)
dot.pendown()

for row in range(10):
    for col in range(10):
        dot.dot(20, random.choice(colors_list))
        dot.penup()
        dot.forward(50)
        dot.pendown()
    dot.penup()
    dot.goto(start_x, start_y + (row + 1) * 50)
    dot.pendown()

screen.exitonclick()