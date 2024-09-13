import tkinter as tk
from tkinter import messagebox
# 새로운 인스턴스 생성
root = tk.Tk()
# title
root.title("first app")
# size
root.geometry("300x350")
# Label (단순 텍스트 출력)
lbl = tk.Label(root, text="이름:")
lbl.grid(row=0, column=0) # row는 행, column은 열 
# Entry (입력창)
txt = tk.Entry(root)
txt.grid(row=0, column=1)
def fn_click():
    nm = txt.get() # entry 값을 가져옴.
    messagebox.showinfo("메세지 창", nm + "님 hello ^^.")
    print(nm)
# button 
btn = tk.Button(root, text="확인", command=fn_click)
btn.grid(row=1, column=0,columnspan=2, sticky="ew")
root.mainloop() # 실행