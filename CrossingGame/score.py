from turtle import Turtle


STYLE = ('Courier', 15, 'italic')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(-340,250)
        self.level = 1
        self.lives = 3
        self.score_board()

    def score_board(self):
        self.write("Level:{}\nLives:{}".format(self.level,self.lives), font=STYLE, align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",font=('Courier', 30, 'bold'), align='center')