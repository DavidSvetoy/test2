count=int(input("enter number count: "))
a=1
b=2
sum=0

#1,2,3,5,8,13
for i in range(count//3):
    print(a)
    print(b)
    sum=a+b
    print(sum)
    a=b+sum
    b=a+sum