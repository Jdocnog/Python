from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # self.canvas.create_rectangle(20, 125, 300, 375, fill="white")
        self.questionText = self.canvas.create_text(
            150,
            125,
            width= 280,
            text=f"Question goes here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        # self.canvas.create_text(230, 50, text=f"Score: {self.score}", fill="white")
        self.scoreLabel = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.scoreLabel.grid(row=0, column=1)

        self.trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=self.trueImage, highlightthickness=0, command=self.true_button_press)
        self.trueButton.grid(row=2, column=0)

        self.falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=self.falseImage, highlightthickness=0, command=self.false_button_press)
        self.falseButton.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=q_text)

            self.scoreLabel.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.questionText, text=f"You've reached the end of the quiz, "
                                                           f"you got {self.quiz.score} questions correct out of 10")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")

    def true_button_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
