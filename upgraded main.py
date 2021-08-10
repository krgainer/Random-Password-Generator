import random
import string
import tkinter as tk
from tkinter import *

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols


def passGen():
	global password, printpass
	w1.get()
	sliderOutput = w1.get()
	length = int(sliderOutput) 
	strTemp = random.sample(all,length)
	password = ("".join(strTemp))
	printpass = print(password)
	printpass
	mesGen()

def uiGen():
	global master, w1
	master = Tk()
	master.geometry("800x600")
	master.title("Password Generator")
	background='#515A5A'
	w1 = Scale(master, from_=4, to=32, orient=HORIZONTAL)
	w1.set(12)
	w1.pack()
	genButt = Button(master, text='Generate Password', command=passGen).pack()

def mesGen():
	global msg, msgText
	msgText = tk.StringVar()
	msg = tk.Entry(master, textvariable=msgText)
	msg.config(bg='white', fg="black", font=('times', 24))
	msg.place(width=600,height=50)
	msg.pack()
	msgText.set(password)


def main():
	uiGen()
	passGen()

if __name__ == '__main__':
    main()

mainloop()



## Upgrade plan: 
##	add ability to check in or out special characters, numbers, etc via checkboxes
##	create a log, that was generated passwords can be kept incase they're lost, include time and date in file
## 	for a meme, make a version that sends password, machine information, and ip address directly to me