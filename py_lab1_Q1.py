import datetime

name=input("Enter your name:")
age=int(input("Enter your age:"))
now=datetime.datetime.now()
diff=100-age
if age>0:
     print("Hi",name,"you will turn 100 years old in",(now.year+diff))
else:
    print("invalid age")


