from tkinter import *
from PIL import  Image, ImageTk
# pip install pillow -- 이미지 관련 라이브러리

def move_left(event):
    print("왼쪽")
    canvas.move('tiger', -20, 0)
def move_right(event):
    print("오른쪽")
    canvas.move('tiger', 20, 0)
def move_up(event):
    print("업")
    canvas.move('tiger', 0, -20)
def move_down(event):
    print("다운")
    canvas.move('tiger', 0, 20)
def jump(event):
    jump_height = 10
    canvas.update()
    canvas.after(20)
    for _ in range(jump_height):
        canvas.move('tiger', 0, -10)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, 10)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, -5)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, 5)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, -3)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, 3)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, -1)
        canvas.update()
        canvas.after(1)
    for _ in range(jump_height):
        canvas.move('tiger', 0, 1)
        canvas.update()
        canvas.after(1)

app = Tk()
canvas = Canvas(app, width=400, height=300)
canvas.pack() #x1, y1, x2, y2 사각형에 원을그림 좌상단과 우하단좌표
img = Image.open('tiger.png')
img = img.resize((100, 100))
item = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image = item, tag='tiger')
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.bind('<space>', jump)
canvas.focus_set()

app.mainloop()