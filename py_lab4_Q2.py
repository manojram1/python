from datetime import timedelta,date

current_date=date.today()
print("current date:",current_date)

subtractdate=current_date - timedelta(days=5)
print("Subtracted five days from current date:",subtractdate)