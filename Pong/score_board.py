from turtle import Turtle

# Score board settings
FONT = 'arial'
FONT_SIZE = 20

# Score board setup
class ScoreBoard(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(color)
        self.goto(x, y)

    def display_scoreboard(self, score, name):
        self.clear()
        self.write(f"{name}: {score}",align= 'center', font=(FONT, FONT_SIZE,'normal'))