#create a list2 by taking all names from list1 in upper case
list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj']
list2=[]

for n in list1:
    v=n.upper()
    list2.append(v)

print(list2)

list3=[n.upper() for n in list1]
print(list3)

def to_upper(n):
    return n.upper()

list4=list(map(to_upper,list1))
print(list4)