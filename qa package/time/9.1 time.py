import datetime
name=input("enter name:")
age=int(input("please enter age:"))
till=100-age
current=datetime.date.today()
r=current.year+till
print(r)
print(current)
print(f"{name} will be 100 in the year of {r}")