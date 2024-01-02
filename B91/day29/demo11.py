#create a list2 by taking all names from list1 in upper case
list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj']
list2=[n.upper() for n in list1]
print(list2)

def to_upper(n):
    return n.upper()

list3=list(map(to_upper,list1))
print(list3)

list3=list(map(lambda n:n.upper(),list1))
print(list3)

