a = 0
b = 7
while a <100:	
	a = a+1
	if (a%b == 0) or (a%10 == 7) or (a//10 == 7):
		continue
	else:
		print(a)
