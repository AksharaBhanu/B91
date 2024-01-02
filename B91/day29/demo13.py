#create a set by taking all names from list1 in upper case
list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj','Bhanu']
set2=set()

for n in list1:
    v=n.upper()
    set2.add(v)

print(set2)

set3=set(list([n.upper() for n in list1]))
print(set3)

def to_upper(n):
    return n.upper()

set4=set(map(to_upper,list1))
print(set4)

set4=set(map(lambda n:n.upper(),list1))
print(set4)