f=open("abc.txt","w")
n=int(input("How many lines:"))
List=[]
for i in range(n):
    s=input("Enter the characters:")
    List.append(s)
f.writelines(List)
f.close()

