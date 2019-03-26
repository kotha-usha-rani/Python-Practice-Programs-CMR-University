#creating a list
l=[1,3,5,7,9]
#defining a list
def listsum(List):
#initialising sum=0
    Sum = 0
    for i in List:
#procedure for calculation
        Sum = Sum + i
    return Sum
#calling a function
x=listsum([1,3,5,7,9])
print(x)
