n=int(input("Enter the value of longest words:"))

f=open("test.txt","r")
s=f.read()
lst=s.split()
print("Longest words in the file:")
for i in lst:
     if (len(i)>n):
      print(i)
f.close()
