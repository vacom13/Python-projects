from turtle import Turtle
START_DIR= 45 # Right half

# Ball Settings
BALL_SPEED = 20
ANIMATION_SPEED = 10
BALL_COLOR = 'white'

# Ball Setup
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.speed(ANIMATION_SPEED)
        self.penup()
        self.seth(START_DIR)

    def move(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.seth(360 - self.heading())
        self.forward(BALL_SPEED)
