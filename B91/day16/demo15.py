#prepare a new list which contains only dose
food=['masala Dose','set dose','vade','onion dose','paper dose','rava Dose','idly']
all_dose=[item.upper() for item in food  if 'dose' in item.lower()]
print(all_dose)
