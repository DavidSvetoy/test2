num=int(input("enter num:"))
lowestnum=1

for c in range(4):
    for i in range(2,num):
        if num/i==0:
            if num<lowestnum:
                lowestnum=num
        else:
            print(lowestnum)
            num = int(input("enter num:"))







