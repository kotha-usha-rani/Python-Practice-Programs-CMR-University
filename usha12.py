d={"police":100,"ambulance":108,"firestation":101}
n=input("enter the name")
if n in d:
	print("name:",n,"number:",d[n])

for i in d:
	print(i,d[i])