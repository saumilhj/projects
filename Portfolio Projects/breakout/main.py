from turtle import Screen, Turtle
from brick import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.tracer(0)
screen.title("Breakout")
screen.bgcolor(0, 0, 0)
screen.setup(width=980, height=500)

hit_pad = Paddle()
bricks = Brick()
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(fun=hit_pad.move_left, key="Left")
screen.onkeypress(fun=hit_pad.move_right, key="Right")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if len(bricks.bricks) == 0:
        game_on = False
    if ball.xcor() >= 460 or ball.xcor() <= -460:
        ball.bounce_x()
    if ball.ycor() >= 230:
        ball.bounce_y()
    if ball.ycor() - hit_pad.ycor() == 20 and (-60 <= ball.xcor() - hit_pad.xcor() <= 60):
        ball.bounce_y()
    for brick in bricks.bricks:
        if 20 <= brick.ycor() - ball.ycor() <= 25 or -25 <= brick.ycor() - ball.ycor() <= -20:
            if -55 <= brick.xcor() - ball.xcor() <= 55:
                brick.ht()
                ball.bounce_y()
                bricks.bricks.remove(brick)
                score.inc_score()
    if ball.ycor() <= -260:
        ball.restart()


game_over = Turtle()
game_over.penup()
game_over.goto(x=-200, y=0)
game_over.color("white")
game_over.write("GAME OVER !", font=("Courier", 60, "normal"))
screen.exitonclick()
