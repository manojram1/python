with open("test.txt","r") as f:
   content=f.readlines()
   for x in content:
      variable= x.strip()
      print(variable,end=" ")
    


