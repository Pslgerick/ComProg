from tkinter import *
import math
from tkinter import font as tkFont

class calc:

	def click(self,argi):
		self.e.insert(END, argi)

	def operation(self):
		try: 
			self.input = self.e.get()
			self.display = self.input.replace('÷','/')
			self.display = self.display.replace('x','*')
			self.display = self.display.replace('^', "**")
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Syntax ERROR')
		else:
			self.e.delete(0,END)
			self.e.insert(0,'Syntax ERROR')


	def button_equal(self):
		self.operation()
		try:
			self.value= eval(self.display)
			if isinstance (self.value, float):
				if self.value -int(self.value) == 0:
					self.value = round(self.value)

		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Syntax ERROR')

		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)

	def clear(self):
			self.e.delete(0,END)
			

	def button_delete(self):
			try:
				if self.e.get() == "Syntax ERROR":
					self.e.delete(0,END)
			
			except SyntaxError or NameError:
				self.e.delete(0,END)

			else:
				self.txt=self.e.get()[:-1]
				self.e.delete(0,END)
				self.e.insert(0,self.txt) 
	
	def squareroot(self):
		"""squareroot method"""
		self.operation()
		try:
			# evaluate the expression using the eval function
			self.value= eval(self.display)

		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Enter Value First')
		else:
			self.sqrtval=math.sqrt(self.value)
			ans = self.sqrtval
			if isinstance (ans, float):
				if ans - int(ans) == 0:
					answer = round(ans)
					self.e.delete(0,END)
					self.e.insert(0,answer)
				else:
					self.e.delete(0,END)
					self.e.insert(0,ans)

	def square(self):
		"""square method"""
		self.operation()
		try:
			#evaluate the expression using the eval function
			self.value = eval(self.display)
		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Enter Value First')
		else:
			self.sqval=math.pow(self.value,2)
			ans = self.sqval
			if isinstance (ans, float):
				if ans - int(ans) == 0:
					answer = round(ans)
					self.e.delete(0,END)
					self.e.insert(0,answer)
				else:
					self.e.delete(0,END)
					self.e.insert(0,ans)

	def  cos (self):
		self.operation()
		try:
			#evaluate the expression using the eval function
			self.value = eval(self.display)
			self.rad =  math.radians(self.value)

		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Enter Value First')
		else:
			self.cosine = math.cos(self.rad)
			ans = self.cosine
			if isinstance (ans, float):
				if ans - int(ans) == 0:
					answer = round(ans)
					self.e.delete(0,END)
					self.e.insert(0,answer)
				else:
					self.e.delete(0,END)
					self.e.insert(0,ans)
	
	def  sin (self):
		self.operation()
		try:
			#evaluate the expression using the eval function
			self.value = eval(self.display)
			self.rad =  math.radians(self.value)

		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Enter Value First!')
		else:
			self.sine = math.sin(self.rad)
			ans = self.sine
			if isinstance (ans, float):
				if ans - int(ans) == 0:
					answer = round(ans)
					self.e.delete(0,END)
					self.e.insert(0,answer)
				else:
					self.e.delete(0,END)
					self.e.insert(0,ans)
	
	def  tan (self):
		self.operation()
		try:
			#evaluate the expression using the eval function
			self.value = eval(self.display)
			self.rad =  math.radians(self.value)

		except SyntaxError or NameError:
			self.e.delete(0,END)
			self.e.insert(0,'Enter Value First!')
		else:
			self.tangent = math.tan(self.rad)
			ans = self.tangent
			if isinstance (ans, float):
				if ans - int(ans) == 0:
					answer = round(ans)
					self.e.delete(0,END)
					self.e.insert(0,answer)
				else:
					self.e.delete(0,END)
					self.e.insert(0,ans)
	def __init__(self,master):
			"""Constructor method"""
			master.title('Calulator')
			master.geometry()
			self.e = Entry(master,font=("Crimson",14,'bold'))
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
			squareroot=Button(master,text="√",width=8,height=2, fg="black",bg="gray86", command=lambda:self.squareroot())
			square=Button(master,text="x²",width=8,height=2, fg="black",bg="gray86", command=lambda:self.square())
			cos=Button(master,text="cos",width=8,height=2, fg="black",bg="gray86", command=lambda:self.cos())
			sin=Button(master,text="sin",width=8,height=2, fg="black",bg="gray86", command=lambda:self.sin())
			tan=Button(master,text="tan",width=8,height=2, fg="black",bg="gray86", command=lambda:self.tan())
			exponent=Button(master,text="^",width=8,height=2, fg="black",bg="gray86", command=lambda:self.click('^'))
			# For Numbers
			num_7.grid(row = 3, column = 0)
			num_8.grid(row = 3, column = 1)
			num_9.grid(row = 3, column = 2)

			num_4.grid(row = 4, column = 0)
			num_5.grid(row = 4, column = 1)
			num_6.grid(row = 4, column = 2)

			num_1.grid(row = 5, column = 0)
			num_2.grid(row = 5, column = 1)
			num_3.grid(row = 5, column = 2)

			num_0.grid(row = 6, column = 0)
			dot.grid(row = 6, column=2)

			squareroot.grid(row = 2, column = 0)
			square.grid(row = 2, column = 1)

			cos.grid(row = 1, column = 0)
			sin.grid(row = 1, column = 1)
			tan.grid(row = 1, column = 2)
			exponent.grid(row = 2, column = 2)

			# Operation Buttons
			btn_off=Button(master,text="OFF",width=16,height=4, fg="black",bg="#F5C37E", command=quit)
			btn_add=Button(master,text="+",width=8,height=4, fg="black",bg="#F5C37E", command=lambda:self.click('+'))
			btn_multiply=Button(master,text="x",width=8,height=4, fg="black",bg="#F5C37E", command=lambda:self.click('x'))
			btn_subtract=Button(master,text="-",width=8,height=4, fg="black",bg="#F5C37E", command=lambda:self.click('-'))
			btn_divide=Button(master,text="÷",width=8,height=4, fg="black",bg="#F5C37E",command=lambda:self.click('÷'))
			pi=Button(master,text="π",width=8,height=4, fg="black",bg="gray86", command=lambda:self.click(str(math.pi)))
			btn_equal=Button(master,text="=",width=18,height=4,fg="black", bg="#F16100",command=lambda:self.button_equal())
			delete=Button(master,text='⌫',width=8,height=4, fg="black", bg="#F16100", command=lambda:self.button_delete())
			clear=Button(master,text='AC',width=8,height=4, fg="black",bg="#F16100", command=lambda:self.clear())


			#For Operations
			btn_off.grid(row=1, column=3, columnspan=2, rowspan=2)
			btn_multiply.grid(row = 4, column = 3)
			btn_divide.grid(row =4, column= 4)
			btn_add.grid(row = 5, column= 3)
			btn_subtract.grid(row = 5, column=4)
			delete.grid(row = 3, column=3)
			clear.grid(row = 3, column= 4)
			btn_equal.grid(row = 6, column= 3, columnspan=2)
			pi.grid(row = 6, column = 1)
			

# Driver Code
root = Tk()
obj=calc(root) 
root.mainloop()
