#create a new list from existing list without using copy method
food=['idly','vade','dose','poori']
# food2=food.copy()
food2=list()
for item in food:
    food2.append(item)

print(food2)
