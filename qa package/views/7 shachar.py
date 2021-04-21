num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
while num1<num2:
    print("על המספר הראשון להיות גדול מהשני")
    num1 = int(input("enter new number 1: "))
    num2 = int(input("enter new number 2: "))
a=int(num1/num2)
print(a)
print(num1-(num2*a))