
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
def max(a,b,c):
	if a>b and a>c:
		print ("maximum is :",a)
	elif b>a and b>c:
		print ("maximum is :",b)
	else:
		print ("maximum is :",c)
max(a,b,c)