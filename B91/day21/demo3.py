class Cat:
    pass


obj1=Cat()
obj2=obj1
obj3=Cat()

print(id(obj1)) #123
print(id(obj2))#123
print(id(obj3))#456

