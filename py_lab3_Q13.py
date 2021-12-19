f=open("test.txt","r")
data=f.read()
f.close()

with open("abc.txt","a") as file:
  file.write(data)
print("copy completed")