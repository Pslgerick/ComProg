from tkinter import *
import math

class calc:

	def click(self,argi):
		try:
			if self.e.get() == "Syntax ERROR" or self.e.get()== "Enter Value First":
				self.e.delete(0,END)

		except SyntaxError or NameError:
			self.e.delete(0,END)

		else:
			self.e.insert(END, argi)

	def operation(self):
		self.input = self.e.get()
		self.display = self.input.replace('÷','/')
		self.display = self.display.replace('x','*')
		self.display = self.display.replace('^', "**")

	def button_equal(self):
		self.operation()

		try:
			self.value= eval(self.display)
			
			if isinstance (self.value, float):
				if self.value - int(self.value) == 0:
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

			
# Driver Code
root = Tk()
obj=calc(root) 
root.mainloop()
