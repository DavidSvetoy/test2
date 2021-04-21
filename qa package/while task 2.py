age=int(input("Enter Age:"))

while not 0<age>120:
    if 0<=age<=18:
        print("child")
    if 18<age<=60:
        print("adult")
    if 60<age<=120:
        print("senior")
    age=int(input("Enter age:"))

print("invalid age!")






