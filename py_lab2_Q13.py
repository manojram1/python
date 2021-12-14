my_list=int(input("Enter the length of list:"))
print("Enter the list elements one by one:")
list=[]
sub_list=[[]] 
for x in range(my_list):
       data=input()
       list.append(data)
def generate_sub_lists():
      for i in range(len(list)+1):
        for j in range(i+1,len(list)+1):
              sub=list[i:j]
              sub_list.append(sub)
generate_sub_lists()                  
print("The sublists of the given list is",sub_list)


