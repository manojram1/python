number=int(input("Enter the number:"))
print("The divisors of",number)
def divisor(num):
    for i in range(1,num+1):
        if num % i == 0:
          print(i,end=" ")
divisor(number)








