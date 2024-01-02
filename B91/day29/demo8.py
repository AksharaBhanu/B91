#create a list2 by taking short names from list1 --> 5 or less char
list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj']

list2=[n for n in list1 if len(n)<6]
print(list2)

def is_short(n):
    return len(n)<=5

list3=list(filter(is_short,list1))
print(list3)


list3=list(filter(lambda n:len(n)<=5,list1))
print(list3)