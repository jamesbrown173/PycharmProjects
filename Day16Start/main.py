#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("CornflowerBlue")
# timmy.shapesize(2)
# for _ in range (5):
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Country", ["China", "Japan", "Uk", "Vietnam"])
table.add_column("Number", [32, 32, 29, 20])
table.align = "l"
print(table)








