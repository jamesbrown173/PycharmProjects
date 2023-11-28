import turtle
from turtle import Turtle, Screen
import random

jt =  Turtle()
st = Turtle()
turtle.colormode(255)
jt.shape("turtle")

base_degrees = 360
number_of_sides = 3
colors = ['red','blue','yellow','red','blue','yellow','red','blue','yellow']
directions = [0,90,180,270]
jt.pensize(1)
jt.speed("fastest")
color_tuple = ((random.randint(1,255)),random.randint(1,255),random.randint(1,255))

def random_color():
    color_tuple = ((random.randint(1, 255)), random.randint(1, 255), random.randint(1, 255))
    return jt.color(color_tuple)

for _ in range(0,1000):
    jt.rt(1)
    random_color()
    jt.circle(200)

screen = Screen()
screen.exitonclick()



# for _ in range(200):
#     random_color()
#     jt.forward(60)
#     jt.setheading(random.randint(0,999))

# >>>


















# color_position = 0
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         jt.forward(100)
#         jt.rt(angle)
#
# def change_color():
#     jt.color(random.choice(colors))
#
# print(random.randint)
#
# # for how_many_sides in range (0):
# #     change_color()
# #     draw_shape(how_many_sides)













# while number_of_sides < 10:
#     for _ in range(number_of_sides):
#         turn_amount = base_degrees / number_of_sides
#         jt.rt(base_degrees / number_of_sides)
#     number_of_sides += 1
#
