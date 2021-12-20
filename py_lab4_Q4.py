import datetime

date= datetime.date(2015,6,16)
print(date)
week_number = date.strftime("%U")
print("Week number from given date:", week_number)


