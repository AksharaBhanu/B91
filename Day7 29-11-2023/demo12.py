#how to create list?
a=[]
print(a)
print(type(a))

a=[1,2,3]
print(a)
print(type(a))

b=list() #special function (constructor)
print(b)
print(type(b))

c=list(range(1,4))
print(c)
print(type(c))

c=list(range(10))
print(c)
print(type(c))

c=list(range(1,10,2))
print(c)
print(type(c))

c=list(range(10,0,-1))
print(c)
print(type(c))

d=[1,2,3,4]*3
print(d)

e=['Dinga'] *3
print(e)