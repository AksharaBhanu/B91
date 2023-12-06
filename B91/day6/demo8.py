food=['idly','vade','dose']
drinks=['coffee','tea','milk']
food.append(drinks)

print(food)
print(food[0])
print(food[1])
print(food[2])
print(food[3])

v1=food[0]
print(type(v1))
v2=food[3]
print(type(v2))

#note: if we use append or insert 2 list then it will created nested list

childList=food[3]
print(childList[0])

print(food[3][0])