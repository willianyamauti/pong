from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


START_RP = (350, 0)
START_LP = (-350, 0)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(START_RP)
l_paddle = Paddle(START_LP)
ball = Ball()
score = Score()

screen.listen()

""" Movements """
# right paddle
screen.onkey(key='Up', fun=r_paddle.move_up)
screen.onkey(key='Down', fun=r_paddle.move_down)
# left paddle
screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key='s', fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    screen.update()
    score.update_score()
    ball.move()
    time.sleep(ball.move_speed)

    # detect screen collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    # the second condition avoid the ball not recognising the collision with the paddle(.distance calculates the
    # distance between the center of two objects)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()
        ball.speed_up()


    # detect point for l_paddle
    if ball.xcor() >380:
        ball.reset_pos()
        score.l_point()

    # detect point for l_paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
