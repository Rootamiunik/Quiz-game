from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Ui
from tkinter import messagebox

#----------Creating question and answer----------------!
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


#--------------------setup--------#
quiz = QuizBrain(question_bank)
ui = Ui(quiz_brain=quiz)
messagebox.showinfo("Finished",f"Quiz completed.\nYour score: {ui.quiz.score}\{len(question_bank)}")