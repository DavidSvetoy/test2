grade=input("enter grades: ")
list1=grade.split()
count_pass=0
count_lo=0
for i in list1:
     if int(i)>=60:
         count_pass+=1
     else:
         count_lo+=1
print("over:", count_pass)
print("lo over:", count_lo)