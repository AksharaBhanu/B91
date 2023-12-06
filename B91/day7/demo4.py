i=10
j=i
i=100
print(i) #100
print(j) #10


food1=['samosa','pavbaji','aloochat','kachori','bhelpoori']
food2=food1 #it will not create another list , both food1 & food2 points to same list
print(food1)
print(food2)
food1[0]='samosa chat'

print(food1)
print(food2)

food3=food1.copy()
food1[0]='samosa'
print(food1)
print(food3)