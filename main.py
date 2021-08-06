import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

length = int(input('\nPlease specify number of characters')) 

strTemp = random.sample(all,length)

password = ("".join(strTemp))

print(password)