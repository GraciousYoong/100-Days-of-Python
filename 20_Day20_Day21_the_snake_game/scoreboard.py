from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        
        try:
            with open("data.txt") as f:
                self.high_score = int(f.read())
        except:
            self.high_score = 0

        self.color("#E0EFF0")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=("Courier", 20, "bold"))

        self.goto(0, -20)
        self.write("Press SPACE to Restart", align=ALIGNMENT, font=("Courier", 14, "normal"))
        
    def update_scoreboard(self):
        self.write(
            f"Score: {self.current_score}         High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT
        )

    def score_increase(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.clear()
        if self.current_score > self.high_score:
            self.high_score = self.current_score

            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))

        self.current_score = 0
        self.goto(0, 270)
        self.update_scoreboard()