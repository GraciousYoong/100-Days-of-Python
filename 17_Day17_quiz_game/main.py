from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    new_question = Question(question["text"],question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.new_question()

print("You have completed all the questions!")
print(f"Your final score is {quiz.current_score}/{quiz.question_number}")