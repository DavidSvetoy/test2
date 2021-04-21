list1=[1,2,3,4,5,6,7,8,9,10]

list2=list1[-3:]

print(list1[::-1])

print(list1[1::2])

list3=list1[::2]
print(list3)

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
num3=int(input("enter number 3: "))
list4=list1[:4]+[num1,num2]+list1[6:]+[num3]
# list1[4:5]=[num1,num2]
# list1.append(num3)
print(list4)

list5=[]
for i in list1:
    list5+=[i*2]
print(list5)

list6=list1[:1]+list1[-1:]
print(list6)