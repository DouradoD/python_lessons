def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print('Incorrect!')
        return False


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q {self.question_number} : {question.q_text} (True/False)')
        if check_answer(user_answer, question.q_answer):
            self.score += 1
        print(f'The correct answer was: {question.q_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}\n')

