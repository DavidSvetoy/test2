d=int(input("enter day:"))
m=int(input("enter month:"))
y=int(input("enter year:"))
print(f"{d}/{m}/{(y%100)//10}{(y%100)%10}")
