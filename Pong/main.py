import turtle
from paddle import Paddle
from ball import Ball
from score_bord import Score
import time


screen = turtle.Screen()
screen.setup(width = 800, height = 600)
screen.title("                                                                                                          Pong Game")
screen.bgcolor("blue")
screen.tracer(0)
#tracer(0): brise sve tragove sa ekrana koji ce nastati izvrsavanjem koda do update() koji onda postavlja novu sliku
# novu sliku update() postavlja u definisanom vremenu (time.sleep(sekunde))
paddle_r = Paddle((360,0))
paddle_l = Paddle((-360,0))
ball = Ball()
score = Score()

net = turtle.Turtle()
net.color("white")
net.hideturtle()
net.penup()
net.goto(10,250)
net.setheading(270)
net.shapesize(0.5,1)
for _ in range (14):
    net.pendown()
    net.forward(20)
    net.penup()
    net.forward(20)

screen.listen()
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330 or ball.distance(paddle_l) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 370:
        score.score_l += 1
        score.refresh_score()
        ball.refresh()
    if ball.xcor() < -370:
        score.score_r += 1
        score.refresh_score()
        ball.refresh()

    if score.score_r == 3 or score.score_l == 3:
        score.winner()
        is_game_on = False

screen.exitonclick()