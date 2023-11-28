import turtle
from turtle import Turtle

class Paddles(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4, outline=20)

    def move_to_start_left(self):
        self.penup()
        self.goto(450,0)
        self.setheading(90)

    def move_to_start_right(self):
        self.penup()
        self.goto(-450, 0)
        self.setheading(90)

    def move_up(self):
        self.forward(100)

    def move_down(self):
        self.backward(100)



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')

    # def move_ball(self):
    #     self.