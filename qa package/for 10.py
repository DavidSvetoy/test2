c=0
num=int(input("enter number: "))
while num>0:
    if num%7==0 or num%3==0:
        c+=1
    num=int(input("enter number: "))
print(c)