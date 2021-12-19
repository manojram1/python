import random

def readRandomLine():
    f=open("text.txt","r")
    lines=f.readlines()
    length=len(lines)
    r=random.randint(0,length-1)
    print(lines[r])
    f.close()
    
readRandomLine()