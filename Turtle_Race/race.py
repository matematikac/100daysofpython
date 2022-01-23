import turtle
import random


screen= turtle.Screen()
screen.setup(width = 600, height = 600)

colors = ['blue', 'red', 'orange', 'purple']
random.shuffle(colors)

all_turtles = []
y_step = 0
for index in range(0,4):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(-280, -150 + y_step)
    y_step += 120
    all_turtles.append(new_turtle)

user_guess = screen.textinput('TURTLE RACE', 'Which turtle win the race(red/blue/orange/purple): ').lower()
race_finished = False
if user_guess:
    race_finished = True
step = [1, 5, 10, 25]
while race_finished:
    for index in range(len(all_turtles)):
        distance = random.choice(step)
        all_turtles[index].forward(distance)
        if all_turtles[index].xcor() > 250:
            race_finished = False
            if user_guess == all_turtles[index].pencolor():
                turtle.color('green')
                style = ('Courier', 30, 'italic')
                turtle.write('Race is over.\nYou WIN!', font=style, align='center')
                turtle.hideturtle()
            else:
                turtle.color('green')
                style = ('Courier', 20, 'italic')
                turtle.write(f"Race is over.\nYou lose!\nThe winner is the {all_turtles[index].pencolor()} turtle.", font=style, align='center')
                turtle.hideturtle()

screen.exitonclick()