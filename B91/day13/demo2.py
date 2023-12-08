a=[10,20,30]
b=[10,20,30]
c=a
d=a.copy()
print(a)
print(b)
print(c)
print(d)

print(a is b) #are they pointing to same object or not
print(c is a)
print(d is a)

print(a is not b)
print(c is not b)