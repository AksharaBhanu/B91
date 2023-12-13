#print the smallest number in the list without using min function
a=[50,10,10,20]
# print(min(a))
small=a[0]
for new in a:
    if new < small:
        small=new

print(small)