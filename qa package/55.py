sum=0
count_less_20=0
count=0

# 0,1,2,3,4
for i in range(5):
    price = int(input("enter price: "))
    sum+=price
    count+=1
    if price<20:
        count_less_20+=1
    if sum>=200:
        print("too expensive!!! I'm leaving.")
