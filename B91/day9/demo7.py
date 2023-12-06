food1={'Idly','Roti','Poori','Dose'}
food2={'Coffee','Tea','Milk','Dose'}
food3=food1.intersection(food2)
print(food1) # I R P D
print(food2) #C T M D
print(food3) #D

food3=food1.union(food2)
print(food1) # I R P D
print(food2) #C T M D
print(food3) #I R P D C T M


food3=food1.difference(food2)
print(food1) # I R P D
print(food2) #C T M D
print(food3) #I R P

food3=food1.update(food2)
print(food1) # I R P D C T M
print(food2) #C T M D
print(food3) #None
