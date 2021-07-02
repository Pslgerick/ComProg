from tkinter import *
from tkinter import font as tkFont


gui = Tk()
gui.title('Simple Calculator')
gui.configure(background='gray49')


entry = Entry(gui, text = "Hello")

entry.grid(row = 0, column = 0, columnspan=5,ipadx=80, ipady=15, pady = 20)
font_num = tkFont.Font(family= 'Times', size = 12, weight=tkFont.BOLD)

def click(num):
    pass

def clear():
    pass

def button_add():
    pass

def button_equal():
    pass 
    
def button_subtract():
    pass

def button_multiply():
    pass

def button_divide():
    pass

def delete():
    pass

#Labeled the buttons
num_1 = Button(gui, text = '1', padx = 30, pady = 30, font = font_num , bg = 'gray86', command= lambda: click(1) )
num_2 = Button(gui, text = '2', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(2) )
num_3 = Button(gui, text = '3', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(3) )
num_4 = Button(gui, text = '4', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(4) )
num_5 = Button(gui, text = '5', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(5) )
num_6 = Button(gui, text = '6', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(6) )
num_7 = Button(gui, text = '7', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(7) )
num_8 = Button(gui, text = '8', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(8) )
num_9 = Button(gui, text = '9', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(9) )
num_0 = Button(gui, text = '0', padx = 30, pady = 30, font = font_num, bg = 'gray86', command= lambda: click(0) )
dot = Button(gui, text = '.', padx = 31, pady = 30, font = font_num, bg = 'gray86', command= lambda: click('.') ) #no function yet

#operators
btn_add = Button(gui, text = '+', padx = 30, pady = 30, font = 'Times', bg = 'SeaGreen2', command=button_add )
btn_subtract = Button(gui, text = '-', padx = 30, pady = 30, font = 'Times', bg = 'SeaGreen2', command=button_subtract )
btn_divide = Button(gui, text = '/', padx = 31, pady = 30, font = 'Times', bg = 'SeaGreen2', command=button_divide)
btn_multiply = Button(gui, text = '*', padx = 30, pady = 30, font = 'Times', bg = 'SeaGreen2', command=button_multiply )
btn_equal = Button(gui, text = '=', padx = 70, pady = 30, font = 'Times', bg = 'gold', command=button_equal)
delete = Button(gui, text = 'DEL', padx = 20, pady = 30, font = 'Times', bg = 'yellow' ) #no function yet
clear = Button(gui, text = 'CLR', padx = 18, pady = 30, font = 'Times', bg = 'yellow', command=clear)

btn_exit = Button(gui, text = 'OFF', padx = 18, pady = 30, font = 'Times', bg = 'red', command=quit )


#arrange the button in windows
#For numbers
num_7.grid(row = 1, column = 0)
num_8.grid(row = 1, column = 1)
num_9.grid(row = 1, column = 2)

num_4.grid(row = 2, column = 0)
num_5.grid(row = 2, column = 1)
num_6.grid(row = 2, column = 2)

num_1.grid(row = 3, column = 0)
num_2.grid(row = 3, column = 1)
num_3.grid(row = 3, column = 2)

num_0.grid(row = 4, column = 0)
dot.grid(row = 4, column=1)

#For the operators
btn_multiply.grid(row = 2, column = 3)
btn_divide.grid(row =2, column= 4)

btn_add.grid(row = 3, column= 3)
btn_subtract.grid(row = 3, column=4)

delete.grid(row = 1, column=3)
clear.grid(row = 1, column= 4)

btn_equal.grid(row = 4, column= 2, columnspan=2)

btn_exit.grid(row = 4, column = 4)




gui.mainloop()