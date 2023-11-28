from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700,height=600)
user_bet = screen.textinput(title='Make your bet!', prompt='Who gonna win it?')
colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'pink']
turtle_names = ['red_t', 'blue_t', 'green_t', 'yellow_t', 'black_t', 'purple_t', 'pink_t']
y_positions = [-78,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("you won!")
                is_race_on = False
            else:
                print("You've lost!")
                is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




# j_red = Turtle(shape="turtle")
# j_red.color(colors[0])
#
#
# j = Turtle(shape="turtle")
# j.goto(x=-200, y=200)


screen.exitonclick()

