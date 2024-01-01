#A=65  B=66 C=67  D=68
#a=97  b=98 c=99 d=100
#   66  67   97 100
list1=['B','a','C','d'] #66 97 67 100 --> 66 67 97 100 B C a d
list2=sorted(list1)
print(list2)

def my_sort(n):
    return n.lower()

list3=sorted(list1,key=my_sort)
print(list3)

list4=sorted(list1,key=my_sort,reverse=True)
print(list4)