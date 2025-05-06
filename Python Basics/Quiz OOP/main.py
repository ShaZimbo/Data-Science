""" Quiz functions """
from art import ART
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    Q_TEXT = question["question"]
    Q_ANSWER = question["correct_answer"]
    new_q = Question(Q_TEXT, Q_ANSWER)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

print(ART)
while quiz.more_questions():
    quiz.next_question()

print(f"You have completed the quiz.\n"
      f"Your final score is {quiz.score}/{quiz.question_number}")
