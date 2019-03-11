	
a=int(input("enter a"))
try:
	b=a/(a-3)
	if a==3:
		raise ZeroDivisionError
	elif a>3:
		raise NameError
except ZeroDivisionError:
	print("division by 0 is not allowed")

except NameError:
	print("type error")
else:
	print(b)