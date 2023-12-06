a={'fruit':'Apple','food':'mini meals','snacks':'pani puri'}
#read the data
print(a['fruit'])
# print(a['Fruit']) #KeyError: 'Fruit'
print(a.get('fruit'))
print(a.get('Fruit'))# return None

#read all the keys
all_keys=a.keys()
print(all_keys) #list of keys

#read all the values
all_values=a.values()
print(all_values) #list of values

K_V=a.items()
print(K_V) #k+v as tuples in list

