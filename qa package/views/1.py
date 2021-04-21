num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))

if num1>num2:
    a=num1
    num1=num2
    num2=a

for i in range(num1+1, num2,):
    if i%2==0:
        print(i)