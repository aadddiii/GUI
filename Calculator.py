from tkinter import *

root = Tk()
root.title("calculator")

#functions
def click(number):
	num_1 = input_1.get ()
	input_1.delete(0, END)
	num_2 = f'{num_1}{number}'
	input_1.insert(0, num_2)

def clear():
	input_1.delete(0, END)

def add():
	global fxn
	fxn = "add"
	global sub_1
	sub_1 = int(input_1.get())
	input_1.delete(0, END)

def minus():
	global fxn
	fxn = "min"
	global sub_1
	sub_1 = int(input_1.get())
	input_1.delete(0, END)

def mult():
	global fxn
	fxn = "mult"
	global sub_1
	sub_1 = int(input_1.get())
	input_1.delete(0, END)

def div():
	global fxn
	fxn = "div"
	global sub_1
	sub_1 = int(input_1.get())
	input_1.delete(0, END)


def equal():
	sub_2 = int(input_1.get())

	if fxn == "add":
		input_1.delete(0, END)
		res = sub_1 + sub_2
		input_1.insert(0, res)

	if fxn == "min":
		input_1.delete(0, END)
		res = sub_1 - sub_2
		input_1.insert(0, res)

	if fxn == "mult":
		input_1.delete(0, END)
		res = sub_1 * sub_2
		input_1.insert(0, res)

	if fxn == "div":
		input_1.delete(0, END)
		res = sub_1 / sub_2
		input_1.insert(0, int(res))


#buttons and input
button_clear = Button(root, text="C", padx=20, pady=20, command=clear)
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda:click(0))
button_equal = Button(root, text="=", padx=20, pady=20, command=equal)
button_add = Button(root, text="+", padx=19, pady=20, command=add)

button_1 = Button(root, text="1", padx=20, pady=20, command=lambda:click(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda:click(2))
button_3 = Button(root, text="3", padx=21, pady=20, command=lambda:click(3))
button_minus = Button(root, text="-", padx=21, pady=20, command=minus)

button_4 = Button(root, text="4", padx=20, pady=20, command=lambda:click(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda:click(5))
button_6 = Button(root, text="6", padx=21, pady=20, command=lambda:click(6))
button_mult = Button(root, text="*", padx=21, pady=20, command=mult)

button_7 = Button(root, text="7", padx=20, pady=20, command=lambda:click(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda:click(8))
button_9 = Button(root, text="9", padx=21, pady=20, command=lambda:click(9))
button_div = Button(root, text="/", padx=21, pady=20, command=div)

input_1 = Entry(root, borderwidth=3, width=36)

#display
button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mult.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

input_1.grid(row=0, column=0, columnspan=4)


root.mainloop()
