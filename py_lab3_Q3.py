
f = open("test.txt", "a")
f.write("Adding additional contents to the file.")
f.close()
f = open("test.txt", "r")
print(f.read())
f.close()

 