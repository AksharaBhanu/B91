#print the largest number in the list without using max function
a=[50,10,10,200]
# print(max(a))
big=a[0]
for new in a:
    if new > big:
        big=new

print(big)