from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # using colon to tell the type of argument it is going to receive
        self.quiz = quiz_brain  # object of QuizBrain class
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.minsize(width=350, height=450)
        self.window.config(pady=20, padx=20, background=THEME_COLOR)
        self.label_score = Label(text='Score: ', fg='White', background=THEME_COLOR)
        self.label_score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(
            150, 125,  # this will give position to text
            width=280,  # to wrap question
            text='Some question text',
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        r_image = PhotoImage(file='./images/true.png')
        l_image = PhotoImage(file='./images/false.png')
        self.true_button = Button(image=r_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=l_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')      # makes white even after all questions are run
        if self.quiz.still_has_questions():
            self.label_score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='The End :)')       # to stop after last question called
            self.true_button.config(state='disabled')       # disable button after end
            self.false_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)  # notice no parentehiss
