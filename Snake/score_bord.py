from turtle import Turtle


class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("orange")
        self.goto(-40,275)
        self.record()

    def record(self):
        self.clear()
        self.write(" score: {}".format(self.score), move=False, align='center', font=("Courier", 15, 'normal'))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=("Courier", 15, 'normal'))