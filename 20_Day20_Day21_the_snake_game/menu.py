from turtle import Turtle

ALIGNMENT = "center"
FONT_TITLE = ("Courier", 24, "bold")
FONT_OPTION = ("Courier", 20, "normal")
FONT_HINT = ("Courier", 14, "normal")

SELECTED_COLOR = "#E3DD34"
UNSELECTED_COLOR = "#E0EFF0"

class Menu(Turtle):
    def __init__(self):
        super().__init__()
        self.options = ["Normal", "Hard"]
        self.index = 0
        self.hideturtle()
        self.penup()
        self.draw()

    @property
    def difficulty(self):
        return self.options[self.index].lower()

    def draw(self):
        self.clear()

        self.color(UNSELECTED_COLOR)
        self.goto(0, 60)
        self.write("SELECT DIFFICULTY.", align=ALIGNMENT, font=FONT_TITLE)

        for i, option in enumerate(self.options):
            self.goto(0, 30 - i * 30)
            if i == self.index:
                self.color(SELECTED_COLOR)
                self.write(f"> {option}  ", align=ALIGNMENT, font=FONT_OPTION)
            else:
                self.color(UNSELECTED_COLOR)
                self.write(f"  {option}  ", align=ALIGNMENT, font=FONT_OPTION)

        self.color(UNSELECTED_COLOR)
        self.goto(0, -30)
        self.write("Up/Down to choose, ENTER to start", align=ALIGNMENT, font=FONT_HINT)

    def select_up(self):
        self.index = (self.index - 1) % len(self.options)
        self.draw()

    def select_down(self):
        self.index = (self.index + 1) % len(self.options)
        self.draw()
