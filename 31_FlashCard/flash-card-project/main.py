import random
import time
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn= {}
try:
    french_dict = pd.read_csv('./data/word_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = french_dict.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['French'])
    canvas.itemconfig(language, text='French')
    canvas.itemconfig(language_image, image=card_front_image)
    window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('./data/word_to_learn.csv', index=False)
    next_card()


def flip_card():
    global current_card
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(card_word, text=current_card['English'])
    canvas.itemconfig(language_image, image=card_back_image)


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas containing French word
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
language_image = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 136, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 276, font=("Ariel", 60, "bold"))
next_card()
canvas.grid(column=0, row=0, columnspan=2)

# Image with tick mark
right_image = PhotoImage(file='./images/right.png')
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

# Image with cross mark
left_image = PhotoImage(file='./images/wrong.png')
unknown_button = Button(image=left_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

window.mainloop()
