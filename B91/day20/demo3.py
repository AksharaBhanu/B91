a='bhanu'
i=len(a)
print(i)

def my_len(a):
    count=0
    for i in a:
        count+=1
    return count

a='bhanu'
i=my_len(a)
print(i)

print(my_len('abc'))