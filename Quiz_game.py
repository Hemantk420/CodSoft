import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from quiz_data import quiz_data
import random


################################___________________FUNCTION______________________#######################################
score = 0
question_order = list(range(len(quiz_data)))
random.shuffle(question_order)

def show_question():
    question_index = question_order[current_question]
    question=quiz_data[question_index]
    qs_label.config(text=question["question"])
    choices=question["Choices"]
    random.shuffle(choices)
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="", background='#FFD39D')

    next_btn.config(state="disabled")
def check_answer(choice):
    question_index = question_order[current_question]
    question = quiz_data[question_index]
    selected_choice=choice_btns[choice].cget("text")
    if selected_choice==question["Answer"]:

        global score
        score+=1

        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)),background='#FFD39D')
        feedback_label.config(text="Correct!", foreground="green",font=('arial',14))
    else:
        feedback_label.config(text="\tIncorrect!\n\n# The correct answer is: "+question["Answer"], foreground="red",font=('arial',14))
        print(question["Answer"])

    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")
def next_question():
    global current_question,score
    current_question+=1
    if current_question<len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed","Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))

        btn = messagebox.askretrycancel('Quiz Game', 'Do you want to retry!', parent=root)
        if btn>0:
            score = 0
            current_question = 0
            show_question()
        else:
            root.destroy()

####################################_____GUI________###################################################

root=tk.Tk()
root.title("Quiz App")
root.maxsize(450,550)
root.minsize(450,550)
root.config(bg='#FFD39D')

qs_label = tk.Label( root, anchor="center", wraplength=400, font=('arial',16,'bold'),foreground='brown4', background='#FFD39D')
qs_label.pack(pady=25)

choice_btns = []

for i in range(4):
    button = tk.Button( root, command=lambda i=i: check_answer(i), width=20,font=('arial',14,'bold'), foreground="#FFD39D",bg='brown4')
    button.pack(pady=10)

    choice_btns.append(button)

feedback_label=ttk.Label( root, anchor="center", padding=10)
feedback_label.pack(pady=10)

fm = Frame(root,width=380,bg='#FFD39D')
fm.pack(padx=10,pady=10,ipady=20)

score=0
score_label=ttk.Label( fm, text="Score: 0/{}".format(len(quiz_data)), anchor="center", padding=2, font=('arial',14,'bold'),background='#FFD39D')
score_label.place(x=150,y=10)

next_btn=tk.Button( fm, text="Next",padx=15, command=next_question, state="disabled",font=('arial',14), foreground='#FFD39D', background='brown4')
next_btn.place(x=290)

cancel_btn=tk.Button( fm, text="Cancel",font=('arial',14), foreground='#FFD39D', background='brown4',command=exit)
cancel_btn.place(x=10)

current_question=0
show_question()
root.mainloop()