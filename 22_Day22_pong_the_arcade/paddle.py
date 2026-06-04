from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fast")
        self.goto(x_cor, y_cor)
        self.setheading(90)

    def up(self):
        if self.ycor() < 240:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -240:
            self.forward(-MOVE_DISTANCE)