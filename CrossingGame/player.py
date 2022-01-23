from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        self.forward(60)

    def refresh(self):
        self.goto(0, -280)