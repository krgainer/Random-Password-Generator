import tkinter as tk
from tkinter import *
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols

master = Tk()
w1 = Scale(master, from_=4, to=32, orient=HORIZONTAL)
w1.get()
w1.set(12)
w1.pack()
w2 = Button(master, text='Show').pack()
#w2 = Button(master, text='Show', command=sliderOutput).pack()


sliderOutput = w1.get()
length = int(sliderOutput) 
strTemp = random.sample(all,length)
password = ("".join(strTemp))
printpass = print(password)

w2 = Button(master, text='Show', command=printpass).pack()

msg = tk.Entry(master, text = password)
msg.config(bg='darkgrey', font=('times', 24, 'italic'))
msg.pack()


##GUI
# master = Tk()
# w1 = Scale(master, from_=4, to=32, orient=HORIZONTAL)
# w1.get()
# Button(master, text='Show', command=sliderOutput).pack()
# w1.pack()
# w1.set(12) 


mainloop()


