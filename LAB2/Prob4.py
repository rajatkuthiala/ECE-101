def Prob4(x):
	number=[x]
	while x > 1:
		if x%2==0:
			x=x//2
			number.append(x)
		else:
			x=x*3+1
			number.append(x)
	print(*number,sep='\n')
	
