from string import *
from itertools import product

#char digits and special char in variable
value = ascii_letters + digits + punctuation

#use can set limit of numbers 
for i in range(1,4):
	for j in product(value, repeat=i):
		word= "".join(j)
		p=open('password.txt', "a")
		p.write(word)
		p.write("\n")
