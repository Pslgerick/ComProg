from tkinter import *
import math
from tkinter import font as tkFont

class calc:

	def click(self,argi):
		self.e.insert(END, argi)

	def operation(self):
		self.input = self.e.get()
		self.display = self.input.replace('÷','/')
		self.display = self.display.replace('x','*')

	def button_equal(self):
		self.operation()

		try:
			self.value= eval(self.display)
			if isinstance (self.value, float):
				if self.value -int(self.value) ==0:
					self.value = round(self.value)

		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Syntax ERROR')

		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)

	def clear(self):
			self.txt=self.e.get()[:-1]
			self.e.delete(0,END)
			self.e.insert(0,self.txt)
			

	def button_delete(self):
			self.e.delete(0,END)
			
			
	def __init__(self,master):
			"""Constructor method"""
			master.title('Calulator')
			master.geometry()
			self.e = Entry(master,font=("Crimson",12,'bold'))
			self.e.grid(row=0,column=0,columnspan=5,ipadx=15, ipady=5, pady = 15)
			self.e.focus_set() #Sets focus on the input text area

			# Number Buttons
			num_0=Button(master,text="0",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(0))
			num_1=Button(master,text="1",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(1))
			num_2=Button(master,text="2",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(2))
			num_3=Button(master,text="3",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(3))
			num_4=Button(master,text="4",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(4))
			num_5=Button(master,text="5",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(5))
			num_6=Button(master,text="6",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(6))
			num_7=Button(master,text="7",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(7))
			num_8=Button(master,text="8",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(8))
			num_9=Button(master,text="9",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(9))
			dot=Button(master,text=".",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click('.'))

			# For Numbers
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

			# Operation Buttons
			btn_add=Button(master,text="+",width=8,height=4, fg="black",bg="SeaGreen2", command=lambda:self.click('+'))
			btn_multiply=Button(master,text="x",width=8,height=4, fg="black",bg="SeaGreen2", command=lambda:self.click('x'))
			btn_subtract=Button(master,text="-",width=8,height=4, fg="black",bg="SeaGreen2", command=lambda:self.click('-'))
			btn_divide=Button(master,text="÷",width=8,height=4, fg="black",bg="SeaGreen2",command=lambda:self.click('÷'))
			btn_exit=Button(master,text="OFF",width=8,height=4, fg="black",bg="red", command=quit)
			btn_equal=Button(master,text="=",width=18,height=4,fg="black", bg="gold",command=lambda:self.button_equal())
			delete=Button(master,text='DEL',width=8,height=4, fg="black", bg="yellow", command=lambda:self.button_delete())
			clear=Button(master,text='AC',width=8,height=4, fg="black",bg="yellow", command=lambda:self.clear())

			#For Operations
			btn_multiply.grid(row = 2, column = 3)
			btn_divide.grid(row =2, column= 4)
			btn_add.grid(row = 3, column= 3)
			btn_subtract.grid(row = 3, column=4)
			delete.grid(row = 1, column=3)
			clear.grid(row = 1, column= 4)
			btn_equal.grid(row = 4, column= 2, columnspan=2)
			btn_exit.grid(row = 4, column = 4)
			

# Driver Code
root = Tk()
obj=calc(root) 
root.mainloop()
