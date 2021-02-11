import turtle
import time
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(n=0, delay=0)
r_pad = Pad((350, 0))
l_pad = Pad((-350, 0))


screen.listen()
screen.onkeypress(r_pad.go_up, "Up")
screen.onkeypress(r_pad.go_down, "Down")
screen.onkeypress(l_pad.go_up, "w")
screen.onkeypress(l_pad.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on == True:
    time.sleep(0.04)
    screen.update()
    ball.move()


# detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# detect collision with r_pad
    if (ball.distance(r_pad) < 50 and ball.xcor() > 330) or (ball.distance(l_pad) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    if(ball.xcor() < -390):
        scoreboard.r_point()
        ball.reset_position()

    if(ball.xcor() > 390):
        scoreboard.l_point()
        ball.reset_position()


screen.exitonclick()

# detect pad misses ball
