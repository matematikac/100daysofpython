from turtle import Turtle
import random


COLORS = ['blue','green','orange','white','purple','yellow']
class Carr(Turtle):
    def __init__(self):
        super().__init__()
        self.build_carr()

    def build_carr(self):
        self.penup()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.goto(300, random.randint(-220, 220))
        self.setheading(180)

    def drive(self):
        self.forward(20)
        if self.xcor() < -400:
            self.goto(380, random.randint(-220,220))