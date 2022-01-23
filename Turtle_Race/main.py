import turtle

tim = turtle.Turtle()
turtle.colormode(255)

def move_forward():
    tim.color('red')
    tim.forward(30)
def move_backwards():
    tim.color('blue')
    tim.backward(50)
def turn_left():
    tim.left(90)
def turn_right():
    tim.right(90)
def clear_drawing():
    screen.resetscreen()
screen = turtle.Screen()
screen.listen()
screen.onkey(key = "w",fun = move_forward)
screen.onkey(move_backwards,"s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right,"d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()