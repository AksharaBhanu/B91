a={'fruit':'Apple','food':'mini meals','snacks':'pani puri'}
#write to dict
a['fruit']='Mango'
print(a)
a['FRUIT']='Papaya'
print(a)
a.setdefault('food','Full meals') #add only if does not exists
print(a)
a.setdefault('Dinner','Full meals')
print(a)

b={'breakfast':'Idly','lunch':'salad'}
a.update(b)
print(a)