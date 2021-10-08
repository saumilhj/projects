from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(x=300, y=200)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update()

