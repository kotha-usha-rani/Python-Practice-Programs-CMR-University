import random
l=["r","p","s"]
while True:
	u=input("enter your choice,enter e to exit")
	if u=="e
		print("game over")
		exit()
	c=random.choice(l)
	print("computer chooses",c)
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		print("u wins!")
	elif u=="p" and c=="s":
		print("c wins!")
	elif u=="s" and c=="r":
		print("c wins!")
	elif u=="r" and c=="s":
		print("u wins!")
	elif u=="p" and c=="r":	
		print("c wins!")
	elif u=="s" and c=="p":	
		print("u wins!")
	else:
		print("wrong choice")
	
