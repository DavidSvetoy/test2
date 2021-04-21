y=0
d=0
for i in range(6):
    x=int(input("enter num:"))

    if x%2==0:
        y=x+y
        d+=1
if d!=0:
    print(y)
    print(y/d)
