age=int(input("enter age:"))

if 0<=age<=18:
    print("child")
if 19<=age<=60:
  print("adult")
if 61<=age<=120:
    print("senior")
elif 121<=age or age<=-1:
    print("Invalid age")