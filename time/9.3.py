from datetime import *
days=input("please enter day of birth:")
month=input("please enter month of birth:")
year=input("please enter year of birth:")



date_string= days+" " + month + " " + year
datetime_object=datetime.strptime(date_string,"%d %b %Y")

print(datetime_object.strftime("%d-%m-%Y"))