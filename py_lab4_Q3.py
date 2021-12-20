from datetime import date

user=int(input("Enter the timestamp value:"))
timestamp = date.fromtimestamp(user)
print("Date =", timestamp)


