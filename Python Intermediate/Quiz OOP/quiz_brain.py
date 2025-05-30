""" Class to ask questions and check answers"""


class QuizBrain:
    """ Gets next question, checks answer and checks if the quiz has ended """
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def more_questions(self):
        """ Checks if there are more quiz questions """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """ Prints the next question """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:"
                            f" {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """ Checks user answer and tracks score"""
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
