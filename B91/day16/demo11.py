a=[]
print(a,type(a))

a=list()
print(a,type(a))

a=[10,20,30]
print(a,type(a))

a=list(range(4))
print(a,type(a))

food1=['idly','vade','dose','poori']
food2=[item for item in food1]
print(food1,id(food1))
print(food2,id(food2))

a=[10,20,30,40,50,60,70,80,90,100]
b=[i for i in a] #add all the elements from list a to list b
print(a)
print(b)

c=[i for i in a if i>50] # add all the elements which are >50 from list a to list c
print(c)

a=[10,20,30,40,50,60,70,80,90,100]
c=[]
for i in a:
    if i>50:
        c.append(i)

print(c)

a=range(1,11)
b=[i for i in a if i>5]
print(b)


b=[i for i in range(1,11) if i>5]
print(b)