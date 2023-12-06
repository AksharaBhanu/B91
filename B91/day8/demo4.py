#diff way of creating list and tuple
a=[]
print(a)
print(type(a))

a=[10,20,30]
print(a)
print(type(a))

a=list()
print(a)
print(type(a))

a=list(range(5))
print(a)
print(type(a))

a=[1]*3
print(a)
print(type(a))

#diif way of creating tuple
a=()
print(a)
print(type(a))

a=(10,20,30)
print(a)
print(type(a))

a=tuple()
print(a)
print(type(a))

a=tuple(range(5))
print(a)
print(type(a))

# a=(1)*3   #this is not a tuple , here * represents multiplication and () is a maths expression
# print(a)
# print(type(a))

b=[10,20,30]
a=tuple(b) #converting list to tuple
print(a)
print(type(a))

c=list(a) #converting tuple to list
print(c)
print(type(c))

a=("Bhanu") * 3
print(a)
print(type(a))