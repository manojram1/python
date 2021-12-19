f = open("test.txt", "r")
n=int(input("How many last n lines need to be displayed:"))
for line in (f.readlines() [-n:]):
     print(line,end=" ")


