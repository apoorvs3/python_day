import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv('50_states.csv')
score = 0


def check(answer):
    states = data['state'].tolist()
    if answer in states:
        answer_matcher(answer)


def answer_matcher(answer):
    global score
    x = data[data['state'] == answer]['x']
    y = data[data['state'] == answer]['y']
    x_cor = x.values[0]
    y_cor = y.values[0]
    answer_turtle = turtle.Turtle()
    answer_turtle.penup()
    answer_turtle.hideturtle()
    answer_turtle.goto(x_cor, y_cor)
    answer_turtle.write(answer)
    score += 1


game_is_on = True
answers = []
while game_is_on:
    answer_state = screen.textinput(title=f'{score}/50 states correct', prompt='What\'s is another states name?')
    print(answer_state.title())
    if answer_state.title() in answers:
        continue
    answers.append(answer_state.title())
    check(answer_state.title())
    if score>50:
        game_is_on = False

screen.exitonclick()
