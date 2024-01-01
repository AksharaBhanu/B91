#create a list2 by taking names from list1 which starts with 's'
list1=['surya','raghavendra','monisha','sandeep','sravani']

list2=[n for n in list1 if n.startswith('s')]
print(list2)

def start_s(n):
    return n.startswith('s')

list3=list(filter(start_s,list1))
print(list3)