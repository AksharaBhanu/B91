url="http://aksharatraining.com"
print(url.startswith('http'))
print(url.startswith('akshara'))

print(url.endswith('com'))
print(url.endswith('org'))

#it contains akshara?-->True
print(url.__contains__('akshara'))
print(url.find('akshara')) #starting index
print('akshara' in url)
#it contains bhanu?-->False
print(url.__contains__('bhanu'))
print(url.find('bhanu')) #-1 if it is not present
print('bhanu' in url)
