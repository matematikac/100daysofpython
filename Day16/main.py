#
# #
# # import another_module
# #
# # print(another_module.another)
# import turtle
# timmy = turtle.Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# # timmy.color("red")
# # timmy.forward(200)
# # timmy.right(120)
# # timmy.forward(200)
# # timmy.right(120)
# # timmy.forward(200)
# # timmy.color("blue")
# # timmy.right(60)
# # timmy.forward(200)
# # timmy.right(120)
# # timmy.forward(200)
# timmy.color('red', 'yellow')
#
# # timmy.begin_fill()
# # while True:
# #     timmy.forward(200)
# #     timmy.right(120)
# #     if abs(timmy.pos()) < 1:
# #         break
# # timmy.end_fill()
# #timmy.done()
# my_screen = turtle.Screen()
#
# #print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

x = prettytable.PrettyTable()
# for element in "Milos+Sanja":
#     x.add_column("ljubav",element)
#x.add_row("12345678901")
# x.add_column("manchester",[1, 2, 3, 4])
# x.add_row(["milos","sanja"])
x.add_column("volim","Sanja")

table = prettytable.PrettyTable()
table.add_column("Names",["Pera","Zika","Mika"])
table.add_column("Business",["elektricar","moler","jebac"])
table.style ="bold_borderline"
print()
print (table)