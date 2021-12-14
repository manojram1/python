user=int(input("Enter the length of set:"))
print("Enter the elements one by one:")
new_user=[ ]
for i in range(user):
    new=input()
    new_user.append(new)

my_user=set(new_user)
move=input('Enter the element to remove from set:')
my_user.discard(move)
print("Orginal set",set(new_user))
print("Removed element set",my_user)







