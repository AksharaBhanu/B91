#create a list which contains even number from 1 to 10
a=[]
for i in range(1,11):
    if i % 2==0:
        a.append(i)

print(a)

b=[i for i in range(1,11) if i %2==0]
print(b)

