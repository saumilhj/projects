from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.setposition(x=0, y=-220)

    def move_left(self):
        if self.xcor() >= -400:
            new_x = self.xcor() - 10
            self.goto(x=new_x, y=self.ycor())

    def move_right(self):
        if self.xcor() <= 400:
            new_x = self.xcor() + 10
            self.goto(x=new_x, y=self.ycor())
