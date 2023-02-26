import random
from turtle import Turtle, Screen

screen = Screen()
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
all_turtle = []
is_race_on = False

screen.setup(width=900, height=600)
user_bet = screen.textinput(title='make your bet', prompt='Which turtle will win the race? choose a rainbow color ')
if user_bet:
    is_race_on = True

x_co = -380
y_co = 275

for turtle_indx in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_indx])
    new_turtle.goto(x=x_co, y=y_co)
    y_co -= 80
    all_turtle.append(new_turtle)


while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 360:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won! {winning_color} is the winner')
            else:
                print(f' You have lost! {winning_color} is the winner')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
