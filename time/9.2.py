# import time
# asc=time.asctime()
# print(asc)
from datetime import datetime
now=datetime.now()
year=now.strftime("%y")
month=now.strftime("%m")
day=now.strftime("%d")
nowdateisr=now.strftime("%d/%m/%y")
print(nowdateisr)
nowdateusa=now.strftime("%m/%d/%y")
print(nowdateusa)
