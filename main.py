import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

screen=Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

right_paddle=Paddle((380,0))
left_paddle=Paddle((-387,0))
ball=Ball()
score=Score()



screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


game_is_on=True

sleep_time=0.1
while game_is_on:
    screen.update()

    time.sleep(sleep_time)
    ball.move()

    ### Detecting collision with Horizontal Walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    ### Detecting collision with Paddle
    if ball.xcor()>350 and ball.distance(right_paddle) <45 or ball.xcor()< -355 and ball.distance(left_paddle) <45:
        ball.x_bounce()
        sleep_time *= 0.9

    ### Keeping Score of both Players
    if ball.xcor() > 385:
        ball.move_opposite_player()
        score.left_keep_score()

    if ball.xcor() < -390:
        ball.move_opposite_player()
        score.right_keep_score()















screen.exitonclick()






