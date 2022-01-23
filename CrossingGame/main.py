import turtle
from player import Player
from carr import Carr
from score import Score
import time

# screen set up
screen = turtle.Screen()
screen.setup (width=800, height=600)
screen.title("                                                                                         Turtle Crossing Game")
screen.tracer(0)
screen.bgcolor('black')
# creating a player
tim = Player()

screen.listen()
screen.onkey(tim.move,'Up')

score = Score()
# build first five cars, and than in while loop building more cars
cars = []
for _ in range(5):
    car = Carr()
    cars.append(car)
# starting game; ind for building more cars during while loop; and game_speed for increasing speed of a game when entering next level
is_game_on = True
ind = 0
game_speed = 1
while is_game_on:
    screen.update()
    time.sleep(game_speed)
    for c in cars:
        c.drive()
    if cars[0].xcor() < 200 and ind == 0:
        ind += 1
        for _ in range(5):
            car = Carr()
            cars.append(car)
    if cars[0].xcor() < 0 and ind == 1:
        ind += 1
        for _ in range(5):
            car = Carr()
            cars.append(car)
    if cars[0].xcor() < -150 and ind == 2:
        ind += 1
        for _ in range(5):
            car = Carr()
            cars.append(car)
    if cars[0].xcor() < -350 and ind == 3:
        ind += 1
        for _ in range(5):
            car = Carr()
            cars.append(car)
# entering next level and increase game speed
    if tim.ycor() > 260:
        game_speed *= 0.75
        tim.refresh()
        score.level += 1
        score.clear()
        score.score_board()
# detecting collision and update number of lives
    for c in cars:
        if c.distance(tim) < 30:
            tim.refresh()
            score.lives -= 1
            score.clear()
            score.score_board()
# condition for game over and exit the while loop
    if score.lives == 0:
        is_game_on = False
        score.game_over()

screen.exitonclick()