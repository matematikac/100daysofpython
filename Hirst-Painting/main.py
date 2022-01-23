import colorgram
import turtle
import random

#pravi listu sa objektima Color klase, ciji je atribut Rgb, a u kome se na laze intovi kao tuple: (r,g,b)
colors = colorgram.extract('images.jpg',100)


list_of_colors = [] # lista u koja se sastoji od elemenata oblika: (r, g, b)
for element in colors:
    red = element.rgb.r
    green = element.rgb.g
    blue = element.rgb.b
    x = (red, green, blue)
    list_of_colors.append(x)

turtle.colormode(255)
tim = turtle.Turtle()
size_of_point = 20
distance_between_point = 50
def draw_a_line():
    for _ in range(20):
        tim.pendown()
        tim.dot(size_of_point, random.choice(list_of_colors))
        tim.penup()
        tim.forward(distance_between_point)
number_of_rows = 20
distance_between_rows = 30
y_coordinate = -100
while number_of_rows > 0:
    tim.penup()
    y_coordinate += distance_between_rows
    tim.setpos(-250, y_coordinate)
    draw_a_line()
    number_of_rows -= 1
# tim.penup()
# d = 10
#
# for element in list_of_colors:
#     tim.setpos(-350 , -350 + d)
#     tim.pendown()
#     tim.dot(5, element)
#     tim.penup()
#     d += 10
screen = turtle.Screen()
screen.exitonclick()