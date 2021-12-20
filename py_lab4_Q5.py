from datetime import date

date1 = date(year = 2001, month = 2, day = 28)
date2 = date(year = 2000, month = 2, day = 28)
date3 = date1 - date2
print("Difference between given two dates:",date3)