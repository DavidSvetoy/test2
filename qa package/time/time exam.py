import datetime
tday=datetime.date.today()
print(tday)
birth= datetime.date(2000,2,1)
since=tday-birth
print(since.total_days())