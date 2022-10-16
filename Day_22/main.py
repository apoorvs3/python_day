from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor('Black')
screen.title('ping-pong')
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle()
# r_paddle.set_position((350, 0))
# l_paddle.set_position((-350, 0))


screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
