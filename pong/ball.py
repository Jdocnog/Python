from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.l_score = 0
        self.r_score = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_speed(self):
        self.x_move = 10
        self.y_move = 10

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move < 0:
            self.x_move -= 2
            self.y_move -= 2
        else:
            self.x_move += 2
            self.y_move += 2

    def reset_ball(self):
        self.bounce_x()
        self.goto(0, 0)
