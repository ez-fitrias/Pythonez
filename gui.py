from logging import PlaceHolder
from tkinter import *

# frame
root = Tk()

# input
entry = Entry(root, width=25, borderwidth=5, bg='light green', fg='green')
entry.insert(0, 'Enter your name')
entry.grid(column=0, row=0)


def click():
    label = Label(root, text=f'greetings,{entry.get()}!')
    label.grid(column=0, row=2)


# button
button = Button(root, bg='light blue', fg='blue', padx=50, pady=10, command=click, text='Enter')
# shoving it
button.grid(column=0, row=1)
# keep it run
root.mainloop()