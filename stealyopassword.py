import random
import string
import tkinter as tk
from tkinter import *
import requests
from requests import get

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
letters = lower + upper
all = letters + num + symbols 
noNum = letters + symbols 
noSym = letters + num 
ip = requests.get('https://checkip.amazonaws.com').text.strip()

def passGen():
	global password, printPass, length
	sliderOutput = w1.get()
	length = int(sliderOutput) 
	strTemp = genTemp()
	password = ("".join(strTemp))
	printPass = print(password)
	printPass
	mesGen()

def genTemp():
	if (numCheckVar.get() == 1) & (symCheckVar.get() == 0):
		return random.sample(noSym,length)
	elif (numCheckVar.get() == 0) & (symCheckVar.get() == 1):
		return random.sample(noNum,length)
	elif (numCheckVar.get() == 0) & (symCheckVar.get() == 0):
		return random.sample(letters,length)
	else:
		return random.sample(all,length)

def uiGen():
	global master, w1
	master = Tk()
	master.geometry("800x600")
	master.title("Password Generator")
	w1 = Scale(master, from_=4, to=48, orient=HORIZONTAL)
	w1.set(12)
	w1.pack()
	genButt = Button(master, text='Generate Password', command=passGen).pack()

def mesGen():
	global msg, msgText
	msgText = tk.StringVar()
	msg = tk.Entry(master, textvariable=msgText, width=60)
	msg.config(bg='white', fg="black", font=('hellvetica', 24))
	## msg.place(width=600,height=50)
	msg.pack()
	msgText.set(password)

def chechBoxes():
	global numCheckVar, symCheckVar
	numCheckVar = tk.IntVar()
	symCheckVar = tk.IntVar()
	checkCheckBoxBox('Numbers', numCheckVar)
	checkCheckBoxBox('Symbols', symCheckVar)

def checkCheckBoxBox(text, variable):
	numCheckbox = tk.Checkbutton(master, text=text, variable=variable)
	numCheckbox.select()
	numCheckbox.pack()

def main():
	uiGen()
	print (ip)
	chechBoxes()
	passGen()

if __name__ == '__main__':
    main()

mainloop()

	
## Upgrade plan: 
##	add ability to check in or out special characters, numbers, etc via chechBoxes
##	create a log, that was generated passwords can be kept incase they're lost, include time and date in file
## 	for a meme, make a version that sends password, machine information, and ip address directly to me
## !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~