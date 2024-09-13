# tkinter와 lotto 모듈을 이용하여 
# 로또번호 생성기를 작성하시오.
# entry에 원하는 수를 입력하면 
# 수량 만큼 message창에 출력되도록



import tkinter as tk
from tkinter import messagebox
import lotto 

app = tk.Tk()
# title
app.title("lotto 생성기")
# Label (단순 텍스트 출력)
lbl = tk.Label(app, text="수량:")
lbl.grid(row=0, column=0) # row는 행, column은 열 
# Entry (입력창)
txt = tk.Entry(app)
txt.grid(row=0, column=1)
def fn_click():
    num = txt.get() # entry 값을 가져옴.
    print()
    set_lotto = lotto.lotto_maker(int(num))
    lo_str = ""
    for lo in set_lotto:
        lo_str += str(lo) + "\n"
    messagebox.showinfo("행운의 번호", lo_str)    
# button 
btn = tk.Button(app, text="확인", command=fn_click)
btn.grid(row=1, column=0,columnspan=2, sticky="ew")
app.mainloop() # 실행