a=[10,20,30,40,50,60,70]
b=[n for n in a if n<50]
print(b)

def add_to_list(n):
    return n<50

b=list(filter(add_to_list,a))
print(b)


b=list(filter(lambda n:n<50,a))
print(b)