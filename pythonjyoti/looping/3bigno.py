print("enter a number")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first number is biggest",no1)
	else:
		print("third number is bigger",no3)
else:
	if no2>=no3:
		print("second is bigger",no2)
	else:
		print("third is bigger",no3)