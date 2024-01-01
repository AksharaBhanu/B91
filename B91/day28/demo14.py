#create a tuple by taking all names from list1 in upper case
list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj','Bhanu']

t1=tuple([n.upper() for n in list1])
print(t1)

def to_upper(n):
    return n.upper()

t2=tuple(map(to_upper,list1))
print(t2)