from turtle import Turtle


FONT =('Courier', 30, 'bold')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.color("red")
        self.score_r = 0
        self.score_l = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(' {}   :   {}'.format(self.score_l, self.score_r), font=FONT, align='center')

    def winner(self):
        self.goto(0, 0)
        if self.score_r > self.score_l:
            self.write("          GAME OVER \nTHE WINNER IS THE RIGHT PLAYER", font=FONT, align='center')
        else:
            self.write("          GAME OVER \nTHE WINNER IS THE LEFT PLAYER", font=FONT, align='center')