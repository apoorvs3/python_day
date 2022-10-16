from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def move_right():
    tim.left(15)


def move_left():
    tim.right(15)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(move_forward, key='w')
screen.onkey(move_backward, key='s')
screen.onkey(move_right, key='a')
screen.onkey(move_left, key='d')
screen.onkey(clear, key='c')

screen.exitonclick()
