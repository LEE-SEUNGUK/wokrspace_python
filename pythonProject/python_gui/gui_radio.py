from tkinter import *

def sel():
    selection = "선택 항목 : " + str(var.get())
    label_answer.config(text=selection)

window = Tk()

# 문제 출력
label_question = Label(window, text="1.가장 배우기 쉬운 언어는?")
label_question.pack()

# 정수형 변수 생성
var = IntVar()
Radiobutton(window, text="python", variable=var, value=1,
command=sel).pack(anchor=W)

Radiobutton(window, text="Pascal", variable=var, value=2,
command=sel).pack(anchor=W)

Radiobutton(window, text="Scratch", variable=var, value=3,
command=sel).pack(anchor=W)

label_answer = Label(window, text="")
label_answer.pack()

window.mainloop()