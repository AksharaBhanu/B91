list1=[10,20,30]
list2=[n*2 for n in list1]
print(list2)

def double_it(n):
    return n*2

list3=list(map(double_it,list1))
print(list3)

list3=list(map(lambda n:n*2,list1))
print(list3)
