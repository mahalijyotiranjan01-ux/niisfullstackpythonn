print("my life my rules")
sal=int(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("enter basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)
