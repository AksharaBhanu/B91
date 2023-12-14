#Write a code to print rectangle pattern
for i in range(4,0,-1):
    for j in range(1,i+1):
        print('* ',end=' ')
    print('')

for i in range(1,5):
    for j in range(5,i,-1):
        print('* ',end=' ')
    print('')