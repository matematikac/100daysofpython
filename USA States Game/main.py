import turtle
import pandas


screen = turtle.Screen()
screen.title('                                                                                        U.S. States Game')
# creating that the background of our screen as a picture. It must contains extension .gif!
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
# importing our states and their positions on the map; creating the list of states
data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
# getting started our game; count is counting the number of correct answers; lives count number of lives
game_is_on = True
count = 0
lives = 3
while game_is_on:
    answer_state = screen.textinput(title='Guess the State score: {}/50'.format(count), prompt='Enter a name of USA state: ').title()
    tim = turtle.Turtle()
    tim.penup()
    tim.hideturtle()
    # checking if the answered state in the list of states, and if it is, then removing from the list of states
    if answer_state in states:
        state_data = data[data['state'] == answer_state]
        tim.goto(int(state_data['x']),int(state_data['y']))
        tim.write(state_data['state'].item())
        count += 1
        states.remove(answer_state)
    # ofter first miss the number of lives is 3, after second is 2, and than when the third miss is happened the game is over
    if lives == 1:
        tim.color('red')
        tim.goto(-150, 0)
        tim.write('GAME OVER!\nYou guess correct {} states'.format(count), font=('Courier', 15, 'italic'))
        game_is_on = False
    else:
        del tim
        lives -= 1
# creating a new csv file of a states that are not guessed, therefore they are not removed from a list of states
states_to_learn = pandas.DataFrame(states)
states_to_learn.to_csv('states_to_learn.csv')

screen.exitonclick()