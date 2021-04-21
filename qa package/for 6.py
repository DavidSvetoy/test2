g=int(input("enter grade:"))
c=0
s=0
s2=0
c2=0
while 0<=g<=100:
    if 60<=g:
        s+=g
        c+=1
    else:
        s2+=g
        c2+=1
    g = int(input("enter grade:"))
print(s2/c2)
print(s/c)