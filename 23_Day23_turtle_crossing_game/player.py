from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#f8f9fa")
        self.penup()
        self.setheading(90)
        self.reset()
        self.can_move = True

    def reset(self):
        self.goto(STARTING_POSITION)
        self.can_move = True
    
    def move_front(self):
        if self.ycor() < FINISH_LINE_Y:
            if self.can_move:
                self.forward(MOVE_DISTANCE)

    def move_back(self):
        if self.ycor() > -FINISH_LINE_Y:
            if self.can_move:
                self.forward(-MOVE_DISTANCE)