from million_dollar import extract_colors
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=900, height=600)
screen.colormode(255)
color_lis = extract_colors()
color_lis  = color_lis * 2
print(color_lis)
lulu = Turtle()
lulu.penup()
y_co = -250
lulu.setposition(-400, y_co)
lulu.hideturtle()

def create_dot():
    lulu.penup()
    lulu.forward(50)
    lulu.pendown()
    lulu.dot(20, colors)


num = 0
# lulu.forward(100)
for colors in color_lis:
    if num % 10 == 0:
        y_co += 50
        lulu.penup()
        lulu.goto(-400, y_co)
        lulu.pendown()
    create_dot()
    num += 1


screen.exitonclick()
