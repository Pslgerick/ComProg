# import turtle
# import random

# window = turtle.Screen()
# arthur = turtle.Turtle()
# window.colormode(255)
# arthur.speed(0)
# arthur.width(2)
# window.bgcolor(50, 0, 70)
# arthur.pencolor(255,255,0)

# def shape(angle, side, limit):
#     reverseDirection = 200
#     arthur.forward(side)

#     if side % (reverseDirection * 2) == 0:
#         angle = angle + 2
#         print('side')

#     elif side % reverseDirection == 0:
#         angle = angle - 2
#         print('side')
    
#     arthur.right(angle)
#     side = side + 2
#     if side < limit:
#         shape(angle, side, limit)

# angle = 119
# side = 0
# limit = 400
# shape(angle, side, limit)

# turtle.done()
# from tkinter import *
# from tkinter import font as tkFont
# root = Tk()
# window = Tk()
# tkont.BOLD == 'bold'

# def click(args):
#     if args == 1:
#         print('Number 1')
#     if args == 2:
#         print('Number 2')
#     if args == 3:
#         print('Number 3')
# font1 = tkFont.Font(family = 'Calibri', size = 36, )
# btn1 = Button(text = '#1', font = font1)
# btn2 = Button(text = '#2', font = font1)
# btn3 = Button(text = '#3', font = font1)
# root.columnconfigure((0,2), weight=1)
# root.columnconfigure((0,2), weight=1)
# btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS', command = lambda:click(1))
# btn2.grid(row=0, column=1, columnspan=1, sticky='EWNS', command = lambda:click(2))
# btn.grid(row=1, column=0, columnspan=1, sticky='EWNS', command = lambda:click(3))
# window.mainloop()
# try:  # Python-2
#     from Tkinter import *
#     import tkFont
# except ImportError:  # Python-3
#     from tkinter import *
#     from tkinter import font as tkFont
#     root = Tk()
# tkFont.BOLD == 'bold'


# def click(args):
#     if args == 1:
#         print("Button 1 is pressed!")
#     if args == 2:
#         print("Button 2 is pressed!")
#     if args == 3:
#         print("Button 3 is pressed!")
#     if args == 4:
#         print("Button 4 is pressed!")
#     if args == 5:
#         print("Button 5 is pressed!")
#     if args == 6:
#         print("Button 6 is pressed!")
# window = Tk()
# helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
# btn1 = Button(text='btn1', font=helv36)
# btn2 = Button(text='btn2', font=helv36)
# btn3 = Button(text='btn3', font=helv36)
# btn4 = Button(text='btn4', font=helv36)
# btn5 = Button(text='btn5', font=helv36)
# btn6 = Button(text='btn6', font=helv36)
# root.rowconfigure((0,1), weight=1)  # make buttons stretch when
# root.columnconfigure((0,2), weight=1)  # when window is resized
# btn1.grid(row=0, column=0, columnspan=1, sticky='EWNS', command = lambda:click(1))
# btn2.grid(row=0, column=1, columnspan=1, sticky='EWNS', command = lambda:click(2))
# btn3.grid(row=1, column=0, columnspan=1, sticky='EWNS', command = lambda:click(3))
# btn4.grid(row=1, column=1, columnspan=1, sticky='EWNS', command = lambda:click(4))
# btn5.grid(row=0, column=3, columnspan=1, sticky='EWNS', commnad = lambda:click(5))
# btn6.grid(row=1, column=3, columnspan=1, sticky='EWNS', command = lambda:click(6))
# window.mainloop()
from tkinter import *
from tkinter import ttk

def test():
    name = userName.get()
    text = "Hello {0}! Pleased to meet you.".format(name)
    greeting.set(text)

window = Tk()

greeting = StringVar()
userName = StringVar()

name = Entry(window, textvariable=userName)
name.grid(column=1, row=1, sticky=NW)

button = Button(window, text="greeting", command=test)
button.grid(column=2, row=1, sticky=NW)

label = Label(window, textvariable=greeting)
label.grid(column=1, row=2, sticky=NW)

#creating a rectangle
canvas = Canvas(window)
canvas.grid(column=1, row=2)
#attributes are x,y coordinates of two points
x = canvas.create_rectangle(5,5,115,115)    

mainloop()