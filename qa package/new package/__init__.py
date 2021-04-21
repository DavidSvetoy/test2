
num: int=int(input("enter age"))
count=0
age=42
while num>=0:
    if num>age:
        count+=1
    if num>120:
        print("enter other age!")
        num = int(input("enter age"))
    else:
        num = int(input("enter age"))
print(f"error the times num was bigger than age is {count}")