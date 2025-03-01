from question_model import Question
from quiz_brain import QuizBrain
import json



print('Lista de perguntas por tópico: \n'
      '1 - Test concepts \n'
      '2 - Python code \n'
      '3 - Functional test pyramid \n'
      '4 - No Functional test pyramid \n')
inserted_value = input('Insira o valor referente a lista de perguntas desejada:')
data_types = {'1':'data.json','2':'python_data.json',
              '3':'functional_test_pyramid.json','4':'no_functional_test_pyramid.json'}
with open(data_types.get(inserted_value), encoding="utf8") as file:
    question_data = json.load(file)

question_bank = [Question(q.get("text"), q.get("answer"), q.get("options")) for q in question_data]
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f'Correct: {quiz.correct_answers}')
print(f'Incorrect: {quiz.incorrect_answers}')
