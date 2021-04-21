sent=input("enter sentence: ")
word=input("enter word: ")
list1=[]
# hello my name is shachar my blabla my
# 0123456789012345678901234567890123456
# my
# list[6,25]

list1+=[sent.find(word)]
for i in range(len(sent)-1):
    a=sent.find(word,list1[-1]+1)
    if a==-1:
        break
    else:
        list1+=[a]
print(list1)