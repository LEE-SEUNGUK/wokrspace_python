from tkinter import *

def update_label(*args):
    selection = "선택 항목 : " + str(option_var.get())
    label_option_answer.config(text=selection)

window = Tk()

# 문제 출력
label_question = Label(window, text="1.가장 배우기 쉬운 언어는?")
label_question.pack()

# Select Box 추가
options = ["python", "Pascal", "Scratch"]
option_var = StringVar(window)
option_var.set(options[0]) # 기본값 설정
option_menu = OptionMenu(window, option_var,
*options)

option_menu.pack()
label_option_answer = Label(window, text="")
label_option_answer.pack()
option_var.trace_add("write", update_label)
window.mainloop()