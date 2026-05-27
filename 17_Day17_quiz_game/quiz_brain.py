class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0

    def new_question(self):
        for question in self.question_list:
            current_question = self.question_list[self.question_number]
            user_input = input(f"Q.{self.question_number + 1}: {current_question.text}(True or False)? ")
            self.question_number += 1
            self.check_answer(user_input, current_question.answer)
            print("\n")
    
    def check_answer(self, user_input, question_answer):
        if user_input.lower() == question_answer.lower():
            print("You got it right!")
            self.current_score += 1
        else:
            print("Sorry, you got it wrong!")
        print(f"The correct answer was {question_answer}.")
        print(f"Your current score is {self.current_score}/{self.question_number}.")
    
            