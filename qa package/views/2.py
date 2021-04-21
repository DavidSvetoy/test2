num=int(input("enter number: "))

while num<=0:
    num = int(input("הכנס מספר תקין: "))

for i in range(2,num):
    if num%i==0:
        print("לא ראשוני")
        break
else:
    print("ראשוני")