from turtle import Screen, Turtle
from paddles import Paddles, Ball


screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong!')


paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.penup()
paddle.goto(350, 0)

def go_up():
    


# screen.listen()
# screen.onkey(paddle_left.move_up, key='Up')
# screen.onkey(paddle_left.move_down, key='Down')
# screen.onkey(paddle_right.move_up, key='w')
# screen.onkey(paddle_right.move_down, key='s')




#
# game_is_on = True
#
# paddle_left.move_to_start_left()
# paddle_right.move_to_start_right()



screen.exitonclick()