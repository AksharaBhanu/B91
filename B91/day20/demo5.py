def test():
    return 10,20,30   #in same return statement we can return multiple values--packing

a=test()
print(a)
print(type(a))

print(a[0])
print(a[1])
print(a[2])

x,y,z=a #unpacking
print(x)
print(y)
print(z)