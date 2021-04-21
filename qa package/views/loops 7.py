a=int(input("Please enter number:"))
b=int(input("Please enter number:"))
biggestnumber=0
lowestnumber=0
divnum=0

if a>b:
    biggestnumber=a
    lowestnumber=b
if b>a:
    biggestnumber=b
    lowestnumber=a
for i in range(lowestnumber,biggestnumber+1,lowestnumber):
    divnum+=1
print(f'the divide number is {divnum} and the remainder is {biggestnumber-(lowestnumber*divnum)}')





