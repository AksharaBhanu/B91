#add all elements from list1 to list2 by doubling its value
list1=[10,20,30,40,50]
list2=[]
for i in list1:
    list2.append(i*2)

print(list2)

list2=[i*2 for i in list1]
print(list2)