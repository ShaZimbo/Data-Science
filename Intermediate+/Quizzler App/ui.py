""" User interface for Quizzler """
from tkinter import Tk, Label, Canvas, Button, PhotoImage
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
current_dir = os.path.dirname(__file__)
TRUE_IMAGE = os.path.join(current_dir, "images", "true.png")
FALSE_IMAGE = os.path.join(current_dir, "images", "false.png")


class QuizInterface:
    """ Quiz UI Setup"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
            font=("Ariel", 14, "bold"),
            bg=THEME_COLOR,
            fg="white",
            pady=20
            )
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(
            height=250, width=300, highlightthickness=10, bg="white"
            )
        self.canvas.create_image(125, 150)
        self.question_t = self.canvas.create_text(150, 125, width=280,
                                                  text="Welcome to Quizzler",
                                                  font=("Ariel", 18, "italic"),
                                                  fill=THEME_COLOR
                                                  )
        self.canvas.grid(column=0, row=1, columnspan=2)
        true_img = PhotoImage(file=TRUE_IMAGE)
        false_img = PhotoImage(file=FALSE_IMAGE)
        self.true = Button(
            image=true_img, highlightthickness=0, command=self.check_true
            )
        self.false = Button(
            image=false_img, highlightthickness=0, command=self.check_false
            )
        self.true.grid(column=0, row=2, pady=20)
        self.false.grid(column=1, row=2, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """ Retrieve next question and update UI"""
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_t, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_t,
                text="You've completed the quiz!"
                )
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_true(self):
        """ If true button pressed, check if it matches """
        self.feedback(self.quiz.check_answer("True"))

    def check_false(self):
        """ If false button pressed, check if it matches """
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, check):
        """ Give visual feedback on answer """
        if check:
            self.canvas.configure(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}"
                                         f"/{self.quiz.question_number}")
        else:
            self.canvas.configure(bg="red")
            self.score_label.config(text=f"Score: {self.quiz.score}"
                                         f"/{self.quiz.question_number}")
        self.window.after(
            750,
            self.get_next_question
            )
