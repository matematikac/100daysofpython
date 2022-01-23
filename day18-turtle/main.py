from turtle import Turtle, Screen
from random import choice, randint
import turtle


timmy = Turtle()
timmy.shape("turtle")
timmy.speed(0)
timmy.pensize(2)
turtle.colormode(255)
angle = [0, 90, 180, 270]


def color_of_turtle():
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return timmy.color((r, g, b))


def move():
    step = 15
    color_of_turtle()
    timmy.setheading(choice(angle))
    timmy.forward(step)


# ran4dom walk
n = 150
angle = 360/n
for _ in range(n+1):
    color_of_turtle()
    timmy.circle(10)
    timmy.right(angle)
    timmy.forward(2)






screen = Screen()
screen.exitonclick()