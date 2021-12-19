f=open("test.txt","r") 
content=f.readlines()
list=[x.strip() for x in content]
print(list)
f.close()



