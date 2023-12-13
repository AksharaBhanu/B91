#check if the given item is present in the list or not without using in operator
food=['idly','vade','dose','poori']
# print('dose' in food)
# print('pongal' in food)
item_to_search='poori'
found=False
for item in food:
    if item==item_to_search:
        found=True
        break

print(found)
