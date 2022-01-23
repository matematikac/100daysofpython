import turtle
import random


START_POSITION = [(0, 0),(-20, 0),(-40, 0)]
STEP_FORWARD = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in START_POSITION:
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color(random.choice(["red","white"]))
            new_turtle.goto(position)
            self.snake.append(new_turtle)

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.snake[0].forward(STEP_FORWARD)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def add_snake_body(self):
#uzima poslednjeg clana liste(koji je: len(self.snake)-1, sto je isto sto i [-1]) i uzima njegovu poziciju
#koja ce biti pozicija novog clana liste snake
        position = self.snake[-1].position()
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color(random.choice(["red","white"]))
        new_turtle.goto(position)
        self.snake.append(new_turtle)