sent=input("enter sentence: ")
letter=input("enter letter: ")
new_sent=""

# hello my name is shachar my blabla
for i in sent:
    if i==letter:
        new_sent+=i.capitalize()
    else:
        new_sent+=i

print(new_sent)