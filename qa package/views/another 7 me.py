a=int(input("Please enter number:"))
b=int(input("Please enter number:"))
c=0
d=0
while a>b:
    c=a//b
    d=a-c*b
    print(a//b)
    print(d)
    break
if b>a:
    print("wrong enter a>b!")
    a = int(input("Please enter number:"))
    b = int(input("Please enter number:"))
    c = a // b
    d = a - c * b
    print(a//b)
    print(d)