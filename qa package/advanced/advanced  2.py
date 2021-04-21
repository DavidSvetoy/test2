count=1
pwd=input("Enter password:")
con=input("Enter confirmation:")
while pwd!=con :
    print("Wrong password! ")
    if count==5:
        print ("too many tries")
        break
    count+=1
    con=input("Enter confirmation:")
else :
    print("Great")








