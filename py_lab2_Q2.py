str1=input("Enter the string:")
d=dict()
for i in str1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("Number of characters in the string",d)



