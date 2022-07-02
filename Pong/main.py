from turtle import Screen,Turtle
from peddle import Peddle
from ball import Ball
from time import sleep
from score_board import ScoreBoard

# Game settings

USER_1_color = 'purple'
USER_2_color = 'red'
SET_SPEED = .1

# Player Names
player_1 = input("Player 1 name: ")
player_2 = input("Player 2 name: ")

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor("black")
screen.tracer(0)

# Environment Setup
right_peddle = Peddle(350, 0)
left_peddle = Peddle(-350, 0)
environment = Turtle()
ball = Ball()

score_1 = ScoreBoard(x = -200, y= 260, color = USER_1_color)
score_2 = ScoreBoard(x=200, y=260, color = USER_2_color)
winner = ScoreBoard(x = 0, y = 0, color = 'green')

environment.left(90)
environment.color("white")
environment.penup()
environment.goto(0, -400)

while environment.ycor() <= 400:
    environment.pendown()
    environment.forward(10)
    environment.penup()
    environment.forward(10)

score_1.display_scoreboard(left_peddle.score, player_1)
score_2.display_scoreboard(right_peddle.score, player_2)


# Functions defining the change reaction
screen.listen()


screen.onkeypress(right_peddle.go_up, "Up")
screen.onkeypress(right_peddle.go_down, "Down")

screen.onkeypress(left_peddle.go_up, "w")
screen.onkeypress(left_peddle.go_down, "s")

def new_dir():
    global checker,counter, i
    score_1.display_scoreboard(left_peddle.score, player_1)
    score_2.display_scoreboard(right_peddle.score, player_2)
    if checker == 0:
        ball.seth(225)
        checker = 1
    elif checker == 1:
        ball.seth(45)
        checker = 0
    screen.update()
    sleep(.9)
    counter = 0
    i = .05

checker = 0
counter = 0
i = .05


def win_condition(USER_2_color, player):
    winner.color(USER_2_color)
    winner.write(f"THE WINNER IS {player}", align='center', font=('arial', 30, 'normal'))

sleep(5)
while True:
    if ball.xcor() >= 350:
        left_peddle.score+=1
        ball.goto(0,0)
        new_dir()
    elif ball.xcor() <= -350:
        right_peddle.score+=1
        ball.goto(0,0)
        new_dir()
    screen.update()
    if left_peddle.score == 10:
        win_condition(USER_1_color, player_1)
        break
    elif right_peddle.score == 10:
        win_condition(USER_2_color, player_2)
        break
    if ((ball.distance(right_peddle) < 50 and ball.xcor() >= 325)
            or (ball.distance(left_peddle) < 50 and ball.xcor() <= -325)):
        ball.seth(180 - ball.heading())
        counter+=1
    ball.move()
    if i > 0:
        if counter== 1:
            counter = 0
            i-=.001
    sleep(i)




screen.exitonclick()
