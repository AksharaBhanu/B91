#prepare a new list which contains only dose
food=['masala dose','set dose','vade','onion dose','paper dose','rava dose','idly']
all_dose=[]

for item in food:
    if 'dose' in item:
        all_dose.append(item)

print(all_dose)

print('set dose' in food) #yes True
print('dose' in food) #no False

a='set dose'
print('dose' in a) #yes True
print('idly' in a) #no False
