def jyoti(p,r,t):
	si=p*r*t/100
	return si
print("enter principal")
p=float(input())
print("enter rate")
r=int(input())
print("enter time period")
t=float(input())
res=jyoti(p,r,t)
print("simple intrest=",res)
