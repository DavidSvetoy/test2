sent=input("enter sentence: ")
new_sent=""
list1=sent.split()

for i in list1:
    new_sent+=i.capitalize()+" "

print(new_sent)