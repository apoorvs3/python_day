import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00 : 00')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:  # long brake
        timer_label.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:  # 2, 4, 6, 8
        timer_label.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    :param count: count is in seconds
    :return: None, works on GUI
    """
    global reps, timer
    count_minute = math.floor(count / 60)
    count_sec = int(count % 60)
    # this ladder for beautification of our clock only
    if count_sec == 0:
        count_sec = '00'
    elif count_sec < 10:
        count_sec = f'0{int(count_sec)}'
    if count_minute < 10:
        count_minute = f'0{int(count_minute)}'
    # labelling reconfiguring
    canvas.itemconfig(timer_text, text=f'{count_minute} : {count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text='✓')
        else:
            check_mark.config(text='')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Poodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_mark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

window.mainloop()
