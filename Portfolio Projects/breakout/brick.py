from turtle import Turtle
import random

COLORS = ["teal", "cyan", "red", "blue", "gold", "lime",
          "dark violet", "indigo", "firebrick", "aquamarine"]


class Brick():

    def __init__(self):
        self.bricks = []
        self.generate_bricks()

    def generate_bricks(self):
        for j in range(0, 90, 25):
            for i in range(-420, 430, 105):
                brick = Turtle()
                brick.penup()
                brick.shape("square")
                brick.color(random.choice(COLORS))
                brick.shapesize(stretch_len=5, stretch_wid=1)
                brick.goto(x=i, y=j)
                self.bricks.append(brick)
