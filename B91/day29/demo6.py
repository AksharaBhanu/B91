#create a list2 by taking only +ve numbers from list
list1=[10,-20,30,-40,50]

list2=[n for n in list1 if n>0]
print(list2)


def is_positive(n):
    return n>0

list3=list(filter(is_positive,list1))
print(list3)


list3=list(filter(lambda n:n>0,list1))
print(list3)