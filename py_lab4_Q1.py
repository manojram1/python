from datetime import datetime

current = datetime.now() 

date_time = current.strftime("%d/%m/%Y, %H:%M:%S")
print("current date and time:",date_time)

year = current.strftime("%Y")
print("current year:", year)

month = current.strftime("%B")
print("Month of year:", month)

week_number = current.strftime("%U")
print("Week number of the year:", week_number)

week = current.strftime("%A")
print("Weekday of the week:", week)

day_of_year = current.timetuple().tm_yday
print("Day of year:",day_of_year)

day_of_month = current.strftime("%d")
print("Day of the month:",day_of_month)

day_of_week = current.strftime("%w")
print("Day of week:",day_of_week)


