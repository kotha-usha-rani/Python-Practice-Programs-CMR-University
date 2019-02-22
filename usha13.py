import random
d={8:37,13:34,38:9,11:2,25:4,40:68,52:81,76:97,65:46,89:70,93:64}
p=random.choice([2,8,11,34,38,89,93,52])
print("you got",p)
if p in d:
	if p>d[p]:
		print("snake")
	else:
		print("laddder")
	print("you can go to",d[p])