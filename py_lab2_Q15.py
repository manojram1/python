import random

char="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ12345!@#$%^&*()"
while 1:
   password_len=int(input("Length of the password:"))
   password_count=int(input("How many password would you like:"))
   for x in range(0,password_count):
     password=""
     for x in range(0,password_len):
               password_char=random.choice(char)
               password+=password_char
     print("Generated new password:",password)
