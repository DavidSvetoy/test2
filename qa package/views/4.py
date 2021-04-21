from random import randint
input("חשוב על מספר ולחץ על כל מקש בסיום")

low=0
high=100
a=randint(low,high)
print(a)
p=input("הצלחתי? ")

while p!="c":
    if p=="l":
        low=a+1
        a = randint(low, high)
    if p=="h":
        high=a-1
        a = randint(low, high)
    print(a)
    p = input("הצלחתי? ")

print("yes!")