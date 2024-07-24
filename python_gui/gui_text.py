from tkinter import *


def add_text(event=None):
    user_input = entry.get()
    text.insert(END, user_input + "\n")
    entry.delete(0, END)

app = Tk()
app.geometry("400x300")
app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

entry = Entry(app, width=50)
entry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
entry.bind('<Return>', add_text)

text =Text(app, relief=SUNKEN) #외곽선 음영
text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

button = Button(app, text="추가", command=add_text)
button.grid(row=0, column=1, padx=10, pady=10)

app.mainloop()