from tkinter import *
# pip install pillow -- 이미지 관련 라이브러리

def move_left(event):
    print("왼쪽")
    canvas.move(item, -2, 0)
def move_right(event):
    print("오른쪽")
    canvas.move(item, 2, 0)
def move_up(event):
    print("업")
    canvas.move(item, 0, -2)
def move_down(event):
    print("다운")
    canvas.move(item, 0, 2)

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack() #x1, y1, x2, y2 사각형에 원을그림 좌상단과 우하단좌표
item = canvas.create_oval(100, 150, 150, 200, fill='red')
app.bind('<Left>', move_left)
app.bind('<Right>', move_right)
app.bind('<Up>', move_up)
app.bind('<Down>', move_down)
app.mainloop()