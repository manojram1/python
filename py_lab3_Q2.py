
f = open("test.txt", "r")
n=int(input("How many 1st n lines need to be displayed:"))
if n<=0:
    print("Enter the positive integer value")
else:
    for i in range(1,n+1):
        lines=f.readline()
        print(lines)
f.close()


