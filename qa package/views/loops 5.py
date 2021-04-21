high=0
mikum=0
for i in range(7):
    num = int(input("enter number: "))
    if num>high:
        high=num
        mikum=i+1
print(mikum)