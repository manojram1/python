from random import randint

number=randint(1,9)
gusses=1
guess=int(input("Guess a number between 1 and 9:"))

while guess!=number:
    if guess < number:
        print("your guess was too low")
        guess=int(input("Guess again:"))
        gusses=gusses+1
    elif guess > number:
        print("your guess was too high")
        guess=int(input("Guess again:"))
        gusses=gusses+1
print("your guess was correct")

       
        


