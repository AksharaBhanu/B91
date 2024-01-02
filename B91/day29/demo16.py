#case insensitive sorting
list1=['B','a','C','d']

def my_sort(n):
    return n.lower()

list3=sorted(list1,key=lambda n:n.lower())
print(list3)

list4=sorted(list1,key=lambda n:n.lower(),reverse=True)
print(list4)