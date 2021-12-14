string=input("Enter the string:")
c=input("Enter a character to find repetition:")
count=0
for i in string:
    if i==c:
        count+= 1
print(c,"occurs",count,"time(s).")