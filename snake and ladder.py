import random

p=0
d=0
 
def rolldice():
	return random.randint(1,6)

while True:
	r=input("press r to roll the dice,q to quit:")
	if r=='r':
		d=rolldice()

		if d==6 or d==1:
			p=d
			print("you are at:",p)
			print("congratulations,you are in the game:",p)
			break

while True:

	r=input("press r to roll the dice,q to quit:")

	if r=='r':
		d=rolldice()
		p=p+d
		print("you are at:",p)

		if p==100:
			print("hurray!you won")
			exit()

		if p>100:
			p=p-d
			print("ypu need to get",100-p,"to reach home")

		if p==8:
			p=37
			print("lucky!climbed a ladder to",p)

		if p==13:
			p==34
			print("lucky!climbed a ladder to",p)

		if p==40:
			p==68
			print("lucky!climbed a ladder to",p)	

		if p==52:
			p==81
			print("lucky!climbed a ladder to",p)

		if p==76:
			p==97
			print("lucky!climbed a ladder to",p)

		if p==11:
			p==2
			print("eaten by a snake",p)

		if p==25:
			p==4
			print("eaten by a snake",p)

		if p==38:
			p==9
			print("eaten by a snake",p)

		if p==65:
			p==46
			print("eaten by a snake",p)


		if p==89:
			p==70
			print("eaten by a snake",p)

		if p==93:
			p==64
			print("eaten by a snake",p)
			break

