class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.total_score = 0
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(answer, current_question.answer)
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it!")
            self.total_score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.total_score}/{self.question_number}")