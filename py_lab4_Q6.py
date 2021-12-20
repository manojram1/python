my_list=int(input("Enter the length of list:"))
print("Enter the numbers one by one:")
list=[]
for i in range(my_list):
       data=int(input())
       list.append(data)

new_list=sum(list)
print("Sum of numbers in the list:",new_list)

