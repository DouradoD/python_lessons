from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q.get("text"), q.get("answer")) for q in question_data]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()