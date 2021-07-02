# importing Tkinter and math
from tkinter import *
import math


# calc class
class calc:

	def operation(self):

		"""replace x with * and ÷ with /"""
		self.input = self.e.get()
		self.newtext=self.input.replace('/','/')
		self.newtext=self.newtext.replace('x','*')


	def equals(self):
		"""when the equal button is pressed"""
		self.operation()
		try:
			# evaluate the input using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)

	def squareroot(self):
		"""squareroot method"""
		self.operation()
		try:
			# evaluate the input using the eval function
			self.value= eval(self.newtext)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqrtval=math.sqrt(self.value)
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)

	def clear(self):
			"""when clear button is pressed,clears the text input area"""
			self.e.delete(0,END)

	def button_delete(self):
			self.txt=self.e.get()[:-1]
			self.e.delete(0,END)
			self.e.insert(0,self.txt)

	def action(self,argi):
			"""pressed button's value is inserted into the end of the text area"""
			self.e.insert(END,argi)

	def __init__(self,master):
			"""Constructor method"""
			master.title('Calulator')
			master.geometry()
			self.e = Entry(master,font=("Crimson",12,'bold'))
			self.e.grid(row=0,column=0,columnspan=5,ipadx=15, ipady=5, pady = 15)
			self.e.focus_set() #Sets focus on the input text area

			# Generating Buttons
			Button(master,text="=",width=18,height=4,fg="black",
				bg="#eeeee4",command=lambda:self.equals()).grid(
									row=4, column=3,columnspan=2)

			Button(master,text='AC',width=8,height=4,
						fg="black", bg="#eeeee4",
			command=lambda:self.button_delete()).grid(row=1, column=3)

			Button(master,text='CLR',width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.clear()).grid(row=1, column=4)

			Button(master,text="+",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action('+')).grid(row=3, column=3)

			Button(master,text="x",width=8,height=4,
					fg="black",bg="#eeeee4",
					command=lambda:self.action('x')).grid(row=2, column=3)

			Button(master,text="-",width=8,height=4,
					fg="black",bg="#eeeee4",
					command=lambda:self.action('-')).grid(row=3, column=4)

			Button(master,text="÷",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action('/')).grid(row=2, column=4)

			Button(master,text="%",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action('%')).grid(row=4, column=2)

			Button(master,text="7",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action('7')).grid(row=1, column=0)

			Button(master,text="8",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(8)).grid(row=1, column=1)

			Button(master,text="9",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(9)).grid(row=1, column=2)

			Button(master,text="4",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(4)).grid(row=2, column=0)

			Button(master,text="5",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(5)).grid(row=2, column=1)

			Button(master,text="6",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(6)).grid(row=2, column=2)

			Button(master,text="1",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(1)).grid(row=3, column=0)

			Button(master,text="2",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(2)).grid(row=3, column=1)

			Button(master,text="3",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(3)).grid(row=3, column=2)

			Button(master,text="0",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action(0)).grid(row=4, column=0)

			Button(master,text=".",width=8,height=4,
				fg="black",bg="#eeeee4",
				command=lambda:self.action('.')).grid(row=4, column=1)

# Driver Code
root = Tk()

obj=calc(root) # object instantiated

root.mainloop()