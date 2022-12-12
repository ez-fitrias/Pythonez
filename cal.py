from tkinter import *


# frame
root = Tk()
# output screen
# screen = Entry(root, borderwidth=5)
# buttons
num1 = Button(root, padx=25, pady=12, text='1')
num2 = Button(root, padx=25, pady=12, text='2')
num3 = Button(root, padx=25, pady=12, text='3')
num4 = Button(root, padx=25, pady=12, text='4')
num5 = Button(root, padx=25, pady=12, text='5')
num6 = Button(root, padx=25, pady=12, text='6')
num7 = Button(root, padx=25, pady=12, text='7')
num8 = Button(root, padx=25, pady=12, text='8')
num9 = Button(root, padx=25, pady=12, text='9')
num0 = Button(root, padx=25, pady=12, text='0')
ops1 = Button(root, padx=25, pady=12, text='+')
ops2 = Button(root, padx=25, pady=12, text='x')
ops3 = Button(root, padx=25, pady=12, text='-')
ops4 = Button(root, padx=25, pady=12, text=':')
ops5 = Button(root, padx=25, pady=12, text='=')
# shoving
num1.grid(column=0, row=1)
num2.grid(column=1, row=1)
num3.grid(column=2, row=1)
num4.grid(column=0, row=2)
num5.grid(column=1, row=2)
num6.grid(column=2, row=2)
num7.grid(column=0, row=3)
num8.grid(column=1, row=3)
num9.grid(column=2, row=3)
num0.grid(column=0, row=4)
ops1.grid(column=1, row=4)
ops2.grid(column=2, row=4)
ops3.grid(column=0, row=5)
ops4.grid(column=1, row=5)
ops5.grid(column=2, row=5)
# screen.grid(column=0, row=0)
# looping
root.mainloop()
