from tkinter import *

root = Tk()
root["bg"] = "light grey"
root.title("Simple Calculator")

# buttons commands
def button_click(number):
    global f_num
    global state
    if number == '+':   
        state = '+' 
        f_num = int(screen.get())
        screen.delete(0, END)
    elif number == '-':
        state = '-'
        f_num = int(screen.get())
        screen.delete(0, END)
    elif number == 'x':
        state = 'x'
        f_num = int(screen.get())
        screen.delete(0, END)
    elif number == '/':
        state = '/'
        f_num = int(screen.get())
        screen.delete(0, END)
    elif number == '=':
        if state == '+':
            s_num = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num + int(s_num))
        elif state == '-':
            s_num = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num - int(s_num))
        elif state == 'x':
            s_num = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num * int(s_num))
        elif state == '/':
            s_num = screen.get()
            screen.delete(0, END)
            screen.insert(0, f_num / int(s_num))
    elif number == 'c':
        screen.delete(0,END)
    else:
        current = screen.get()
        screen.delete(0, END)
        screen.insert(0, str(current) + str(number))


# define buttons
screen = Entry(root, width=42, borderwidth=5)
num1 = Button(root, padx=40, pady=20, text='1', command=lambda: button_click(1), bg='light grey')
num2 = Button(root, padx=40, pady=20, text='2', command=lambda: button_click(2), bg='light grey')
num3 = Button(root, padx=40, pady=20, text='3', command=lambda: button_click(3), bg='light grey')
num4 = Button(root, padx=40, pady=20, text='4', command=lambda: button_click(4), bg='light grey')
num5 = Button(root, padx=40, pady=20, text='5', command=lambda: button_click(5), bg='light grey')
num6 = Button(root, padx=40, pady=20, text='6', command=lambda: button_click(6), bg='light grey')
num7 = Button(root, padx=40, pady=20, text='7', command=lambda: button_click(7), bg='light grey')
num8 = Button(root, padx=40, pady=20, text='8', command=lambda: button_click(8), bg='light grey')
num9 = Button(root, padx=40, pady=20, text='9', command=lambda: button_click(9), bg='light grey')
num0 = Button(root, padx=40, pady=20, text='0', command=lambda: button_click(0), bg='light grey')
num00 = Button(root, padx=37, pady=20, text='00', command=lambda: button_click('00'), bg='light grey')
plus = Button(root, padx=40, pady=20, text='+', command=lambda: button_click('+'), bg='light blue')
minus = Button(root, padx=40, pady=20, text='-', command=lambda: button_click('-'), bg='light blue')
multiply = Button(root, padx=41, pady=20, text='x', command=lambda: button_click('x'), bg='light blue')
divide = Button(root, padx=40, pady=20, text='/', command=lambda: button_click('/'), bg='light blue')
clear = Button(root, padx=40, pady=20, text='C', command=lambda: button_click('c'), bg='light green')
equal = Button(root, padx=87, pady=20, text='=', command=lambda: button_click('='), bg='light green')

# place buttons/buttons layout
screen.grid(column=0, row=0, columnspan=3, padx=10, pady=10)
num1.grid(column=0, row=3)
num2.grid(column=1, row=3)
num3.grid(column=2, row=3)
num4.grid(column=0, row=2)
num5.grid(column=1, row=2)
num6.grid(column=2, row=2)
num7.grid(column=0, row=1)
num8.grid(column=1, row=1)
num9.grid(column=2, row=1)
num0.grid(column=0, row=4)
num00.grid(column=0, row=5)
clear.grid(column=0, row=6)
plus.grid(column=1, row=4)
minus.grid(column=2, row=4)
multiply.grid(column=1, row=5)
divide.grid(column=2, row=5)
equal.grid(column=1, row=6, columnspan=2)

# keep it running
root.mainloop()
