from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")

class Score(Turtle):
    def __init__(self, cor_x, cor_y):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(cor_x, cor_y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.current_score}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()