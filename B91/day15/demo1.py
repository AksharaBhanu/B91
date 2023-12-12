all_fruits=['apple','banana','mango','chiku']


for fruit in all_fruits:                 #object is not iterable
    print(fruit)
print('-'*10)
#1. check if the 2nd  item(all_fruits)  is collection or not (object is not iterable-STOP)
#2. create variable fruit (1st item)
#3. automatically calculate number of iteration (size of the collection)
#4. take each element from the colletion in respective iteration and store it in temp var
#5. execute the loop body

#use tuple set frozenset dict in for

all_fruits=('apple','banana','mango','chiku')
for fruit in all_fruits:                 #object is not iterable
    print(fruit)
print('-'*10)

all_fruits={'apple','banana','mango','chiku'}
for fruit in all_fruits:                 #object is not iterable
    print(fruit)
print('-'*10)

all_fruits=frozenset(all_fruits)
for fruit in all_fruits:                 #object is not iterable
    print(fruit)
print('-'*10)

all_fruits={'fruit1':'Apple','fruit2':'Mango'}
for fruit in all_fruits:                 #object is not iterable
    print(fruit)
print('-'*10)

all_items=all_fruits.items()
for item in all_items:
    print(item)
print('-'*10)

all_keys=all_fruits.keys()

for key in all_keys:
    print(key)
print('-' * 10)

all_values=all_fruits.values()
for value in all_values:
    print(value)
print('-'*10)