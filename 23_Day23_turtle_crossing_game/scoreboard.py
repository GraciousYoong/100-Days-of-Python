from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#f8f9fa")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"LEVEL {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -25)
        self.write("Press SPACE to restart", align="center", font=("Courier", 16, "normal"))

    # def win(self):
    #     self.goto(0, 0)
    #     self.write("YOU WIN!", align="center", font=FONT)
    #     self.goto(0, -25)
    #     self.write("Press SPACE to play again", align="center", font=("Courier", 16, "normal"))

    def reset(self):
        self.clear()
        self.level = 1
        self.update_scoreboard()