list1=['cat','dog','cow','rat']
print(list1)
list1.insert(1,'goat')
print(list1)

list1.insert(5,'donkey')
print(list1)

#IQ: add an element at the end of the list without using append
n=len(list1)
list1.insert(n,'Tiger')
print(list1)

list1.insert(100,'lion')
print(list1)
print(list1[7])