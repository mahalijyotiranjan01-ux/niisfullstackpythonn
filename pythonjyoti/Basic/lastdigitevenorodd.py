print("enter a number")
no=int(input())
last_digit = no% 10
if last_digit % 2==0:
	print ("The last digit  is even.") 
else:
	print("The last digit odd.")
