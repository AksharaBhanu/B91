list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj']
list2=sorted(list1)
print(list2) #a to z

list3=sorted(list1,reverse=True)
print(list3) #z to a

def size(n):
   return len(n)

list3=sorted(list1,key=size)
print(list3) #small name to big name

list4=sorted(list1,key=size,reverse=True)
print(list4) #big name to small name