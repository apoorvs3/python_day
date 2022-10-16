from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('ping-pong')
screen.tracer(0)

r_paddle = Paddle('RIGHT')
l_paddle = Paddle('LEFT')


screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
