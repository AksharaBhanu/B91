list1=['apple','banana','chiku','dragon fruit','grapes','orange','blue berry']
#print all the items present in list 1st to last
for item in list1:
    print(item)
print('-'*10)

count=len(list1)
for i in range(count):
    print(list1[i])
print('-'*10)

#print all the items present in list last to 1st
for item in reversed(list1):
    print(item)
print('-'*10)

count=len(list1)
for i in range(count-1,-1,-1):
    print(list1[i])
print('-'*10)

for item in list1[::-1]:
    print(item)
print('-'*10)

#print all the alternative items present in list
count=len(list1)
for i in range(0,count,2):
    print(list1[i])
print('-'*10)

for item in list1[::2]:
    print(item)
print('-'*10)

