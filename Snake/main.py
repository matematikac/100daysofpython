import turtle
import time
from snake import Snake
from food import Food
from score_bord import ScoreBord


screen = turtle.Screen()
screen.setup(width = 600, height = 600)
screen.title("                                                        My Snake Game")
screen.bgcolor("black")
screen.tracer(0) # brise sve tragove sa ekrana i koristi se zajedno sa update() koji onda postavlja novu sliku

snake = Snake()
food = Food()
score = ScoreBord()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if food.distance(snake.head) < 15:
        food.refresh()
        score.record()
        snake.add_snake_body()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()

    for sn in snake.snake[1:]:
        if sn.distance(snake.head) < 10:
            is_game_on = False
            score.game_over()
screen.exitonclick()