import datetime
#
# tday=datetime.date.today()
# print(tday.weekday())
# print(tday.isoweekday())
day=int(input("enter day:"))
day=day-1
if day==5 or day==6:
    day=day=5
elif day==0:
    day=day+6



today=datetime.datetime(day,1,1)
print(today.strftime("%A"))