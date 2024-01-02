#create a list2 by taking only upper case names from list1

list1=['MEGHANA','Roopa','BHANU','Jameela','Raghu','YASH','Vinay Bharadwaj']

list2=[n for n in list1 if n.isupper()]
print(list2)

def is_upper(n):
    return n.isupper()

list3=list(filter(is_upper,list1))
print(list3)


list3=list(filter(lambda n:n.isupper(),list1))
print(list3)