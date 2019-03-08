#snake and ladder
import random
p=0
d=0
snl={8:37,13:34,38:9,11:2,25:4,40:68,52:81,76:97,65:46,89:70,93:64}
#function to roll the dice
def rolldice():
	return random.randint(1,6)
#get 1 or 6 to enter the game
while True:
	r=input("press r to roll the dice,q to quit:")
	if r=='r':
		d=rolldice()
		if d==6 or d==1:
			p=d
			print("you are at:",p)
			print("congratulations,you are in the game:",p)
			break
#give the conditions at various positions
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
		if p in snl:
			if p < snl[p]:
				print("lucky!climbed a ladder at",p)
			else:
				print("eaten by a snake",p)
			p=snl[p]
			print("you are at:",p)
		elif r=='q':
			exit()
