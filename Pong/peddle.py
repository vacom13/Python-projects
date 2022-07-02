from turtle import Turtle

# Peddle Settings
PEDDLE_SPEED = 30

#Peddle Setup
class Peddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.seth(90)
        self.shapesize(stretch_len= 5)
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 240:
            self.forward(PEDDLE_SPEED)

    def go_down(self):
        if self.ycor() > -240:
            self.backward(PEDDLE_SPEED)
