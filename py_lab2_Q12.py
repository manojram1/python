my_list=int(input("Enter the length of list:"))
print("Enter the list elements one by one:")
list=[]
for i in range(my_list):
       data=input()
       list.append(data)

string=''.join(list)
print("converted string",string)




