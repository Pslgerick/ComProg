from tkinter import *
import math

class calc:

	def click(self,argi):
		self.e.insert(END, argi)

	def operation(self):
		self.input = self.e.get()
		self.display = self.input.replace('/','/')
		self.display = self.display.replace('x','*')

	def button_equal(self):
		self.operation()

		try:
			self.value= eval(self.display)

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
