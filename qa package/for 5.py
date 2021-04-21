
g=int(input("enter grade:"))
c=0
s=0
while 0<=g<=100:
    if 60<=g:
        s+=g
        c+=1
    g = int(input("enter grade:"))
print(s/c)
