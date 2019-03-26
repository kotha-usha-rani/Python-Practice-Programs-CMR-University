#  find the largest among three numbers 
#define maximum
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
#conditions
if (a > b) and (a > c): 
	print("largest = a") 
elif (b > a) and (b > c): 
	print("largest = b") 
else: 
	print("largest = c") 
        