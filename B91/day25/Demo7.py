
a=10
print(type(a)) #class int
print(id(a)) #12312324234
print(a) #10

b='Bhanu'
print(type(b)) #class str
print(id(b)) #45654645456
print(b) #Bhanu

class emp:
    def __init__(self):
        self.name='Arjun'
        self.id='A123'

    def __str__(self):
        return self.id+'-'+self.name

c=emp()
print(type(c)) #class emp
print(id(c))#678908129873912
print(c) #<__main__.emp object at 0x000002A30406FFD0>