y=int(input("Enter year"))
if y % 400 == 0:
    print("שנה מעוברת")
elif y % 100 != 0 and y%4==0:
    print("שנה מעוברת")
else:
    print("שנה לא מעוברת")
# print(leap_year(1900))
# print(leap_year(2004))
# print(leap_year(2500))
# print(leap_year(1600))
