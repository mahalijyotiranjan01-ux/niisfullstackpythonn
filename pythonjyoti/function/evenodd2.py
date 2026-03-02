def check():
	print("print a number")
	no=int(input())
	if no%2==0:
		return True
	else:
		return False
if check():
	print("even number")
else:
	print("odd number")	
