from tkinter import *
from tkinter import messagebox
from python_base.luck import make_lotto
# pip install pyinstaller
# pyinstaller --onefile -w gui01.py
# -- onefile 하나의 파일로 생성
# -- windowed or -w 콘솔 창 없이 GUI 실행

print(make_lotto())

app = Tk()
app.geometry('215x100')
app.title('로또번호 생성')
def get_lotto():
    lotto = ''
    cnt_lotto = ''
    msg = txt.get() # entry 값 가져옴
    for i in range(int(msg)):
        a = make_lotto()
        mylist = str(a)
        lotto = "".join(mylist)
        cnt_lotto += lotto + '\n'
    messagebox.showinfo('생성 완료', cnt_lotto)

lbl = Label(app, text='수량')
lbl.grid(row = 0, column = 0, padx=10, pady=10)
txt = Entry(app)
txt.grid(row = 0, column = 1, padx=10, pady=10 )
btn = Button(app, text = '생성', command=get_lotto)
btn.grid(row = 1, column = 0, columnspan = 2, sticky='ew', padx=10, pady=10)
app.mainloop()