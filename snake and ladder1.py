import random

i=0
while i<2:
	d=6

	r=input("press r to roll,q to quit:")
	if r=="r":
		print("you got:",d)
		d=d/3
	r=input("press r to roll,q to quit:")
	if r=="r":
		print("you got:",d)	
		d=d+1
	i=i+1
	print("hurray,you won!")
								
