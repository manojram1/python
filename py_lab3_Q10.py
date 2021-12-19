f=open("test.txt","r")
wrd=input("Enter the word to be searched:")
s=f.read()
lst=s.split()
count=0
for i in lst:
    if(i==wrd):
        count+=1
print("word {} occurs {} times.".format(wrd,count))
f.close()

