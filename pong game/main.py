from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard as sb
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800 , 600)
screen.title("The Bong Game")
screen.tracer(0)

r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))
ball = Ball()
scoreboard = sb()
screen.listen()
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down , "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down , "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
       ball.reset()
       scoreboard.l_point()
       scoreboard.update_scotreboard()


    if ball.xcor() < -400:
       ball.reset()
       scoreboard.r_point()
       scoreboard.update_scotreboard()


screen.exitonclick()

