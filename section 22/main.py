from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 25 and ball.xcor() > 320 or ball.distance(l_paddle) < 25 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_positioning()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_positioning()
        scoreboard.r_point()


screen.exitonclick()