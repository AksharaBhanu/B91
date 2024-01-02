list1=['Meghana','Roopa','Bhanu','Jameela','Raghu','Yash','Vinay Bharadwaj']

list3=sorted(list1,key=lambda n:len(n))
print(list3) #small name to big name

list4=sorted(list1,key=lambda n:len(n),reverse=True)
print(list4) #big name to small name