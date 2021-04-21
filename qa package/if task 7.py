day=int(input("Please enter day:"))
month=int(input("Please enter month:"))
year=int(input("Please enter year:"))

if 1<=day<=31 and 1<=month<=12 and 1950<=year<=2021:
    print(f"{day}/{month}/{year//10%10}{year%10}")
else:
    print("Error")