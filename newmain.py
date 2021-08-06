import random
import string
import tkinter as tk
from tkinter import *

def generate():
	global password, printpass
	w1.get()
	sliderOutput = w1.get()
	length = int(sliderOutput) 
	strTemp = random.sample(all,length)
	password = ("".join(strTemp))
	printpass = print(password)
	printpass

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

master = Tk()
master.title("Password Generator")
background='#515A5A'
w1 = Scale(master, from_=4, to=32, orient=HORIZONTAL)
w1.set(12)
w1.pack()

generate()

genButt = Button(master, text='Generate', command=generate).pack()

msg = tk.Entry(text=password)
msg.config(bg='white', fg="black", font=('times', 24,))
msg.pack()

mainloop()


