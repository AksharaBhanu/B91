a=10
print(type(a))
print(a)

a=10,20,30   #packaing
print(type(a))
print(a)

t=(10,20,30)
a=t[0]
b=t[1]
c=t[2]

print(a)
print(b)
print(c)
print(a,b,c)

a,b,c=t  # unpacking
print(a,b,c)