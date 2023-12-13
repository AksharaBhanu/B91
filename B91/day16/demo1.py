print('start')
for i in range(1,7):
    print(i,'Hi')
    if i>2 and i<5:
        continue #skip remaining code of the for loop and goto next iteration
    print(i,'bye')
print('end')