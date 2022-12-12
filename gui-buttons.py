from tkinter import *
from turtle import bgcolor, color


def click():
    # mylabel = Label(root, text='"see,i`am,your new programmer"')
    mylabel = Label(root, text=entry.get())
    mylabel.grid(column=3, row=3)


# frame
root = Tk()
# content
test = Label(root, text='jfvjnfsmksjdt')
mylabel = Label(root, text='Hello world!')  # .grid(column=0, row=0)
mylabel1 = Label(root, text='it`s me,zidane')  # .grid(column=1, row=1)
mylabel2 = Label(root, text='your new programmer')  # .grid(column=2, row=2)
mylabel3 = Label(root, text=':) :) :) :) :) :) :)')  # .grid(column=4, row=2)
mylabel4 = Label(root, text=':) :) :) :) :) :) :)')  # .grid(column=5, row=1)
mylabel5 = Label(root, text=':) :) :) :) :) :) :)')  # .grid(column=6, row=0)
mylabel6 = Label(root, text=' ')  # .grid(column=3, row=2)
# buttons
mybutton = Button(root, text='Enter(fill the coulumn with something!)', padx=50, pady=10, fg='green', background='light blue', command=click) # if want to disable it use state=DISABLED
# entry(input)
entry = Entry(root, width=25, borderwidth=5, bg='grey')
# shoving the content, column = x, row = y
# test.pack() this can be used,it places the text in the middle and always in the middle
# while with grid you can set a fixed position
mylabel.grid(column=0, row=0)
mylabel1.grid(column=1, row=1)
mylabel2.grid(column=2, row=2)
mylabel3.grid(column=4, row=2)
mylabel4.grid(column=5, row=1)
mylabel5.grid(column=6, row=0)
mylabel6.grid(column=3, row=2)
mybutton.grid(column=3, row=1) # can also use .pack
entry.grid(column=3, row=0)
# keep it running
root.mainloop()
