from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
from threading import Timer

THEME_COLOR = "#375362"
#-------------------------UI-------------------#

class Ui():
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.font = ("Arial",14, "bold italic")
        self.window = Tk()

        self.window.config(padx=50, pady=50,background=THEME_COLOR)
        self.score_lable = Label(text=f'Score: {self.quiz.score}',font=('Arial',15,'bold'),background=THEME_COLOR,fg='white')
        self.score_lable.grid(row=0,column=1,columnspan=2)
        
        self.image_true = PhotoImage(file='images/true.png')
        self.image_false = PhotoImage(file='images/false.png')
        self.true_button = Button(image=self.image_true,command=self.correct_true).grid(row=2,column=0,)
        self.false_button = Button(image=self.image_false,command=self.wrong_false).grid(row=2,column=1)


        self.canvas =  Canvas(width=300, height=414,background='white',highlightthickness=0)
        self.question_text = self.canvas.create_text(150,207,width=290,text='', font=self.font) 
        self.canvas.grid(row=1, column=0,pady=50,columnspan=2)

        self.next_question()
        self.window.mainloop()

    def correct_true(self):
        self.my_answer = 'True'
        self.check_ans()
        
        
    def wrong_false(self):
        self.my_answer = 'False' 
        self.check_ans()
        
    
    def next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=question_text)
    
    def check_ans(self):
        if self.quiz.check_answer(self.my_answer):
            self.canvas.config(background='Green')
            
        else:
            self.canvas.config(background='Red') 
        self.score_lable.config(text=f"Score: {self.quiz.score}")
        Timer(1,self.after_each_ans).start()

    def after_each_ans(self): 
        self.canvas.config(background='white')
        try:
            self.next_question()
        except IndexError:
            self.window.quit()





