from decorator import decorator_question


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 1
        self.score = 0
        self.question_list = q_list
        self.correct_answers = []
        self.incorrect_answers = []


    def still_has_questions(self):
        if self.question_number <= len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print('Correct!')
            self.correct_answers.append(self.question_number)
            return True
        else:
            print('Incorrect!')
            self.incorrect_answers.append(self.question_number)
            return False

    @decorator_question
    def next_question(self):
        question = self.question_list[self.question_number - 1]
        print(f'Q {self.question_number} : {question.q_text}')
        print('Options: \n')
        for option_number, option_value in question.option_dict.items():
            print(f'{option_number} : {option_value}\n')
        user_answer = input(f'Answer:')
        if self.check_answer(user_answer, question.q_answer):
            self.score += 1
        print(f'The correct answer was: {question.q_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}\n')
        self.question_number += 1

