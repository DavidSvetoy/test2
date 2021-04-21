from random import randint

num=randint(1,9)
a=int(input("הכנס מספר: "))

while num!=a:
    if a>num:
        print("גדול מידי")
        a = int(input("הכנס שוב מספר: "))
    else:
        print("קטן מידי")
        a = int(input("הכנס שוב מספר: "))
else:
    print("צדקת!")