grade=int(input("Enter grade:"))
max=grade
count=0
sum=0
while 0<=grade<=100:
    count += 1
    sum=sum+grade
    if max<grade:
        max=grade
    grade = int(input("Enter grade:"))
if count>0:
    print(max)
    print(sum/count)
    print(f'{max-sum/count}')



