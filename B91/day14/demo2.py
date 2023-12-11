#check if the given number is odd or even
#step 1 --> accept a number

a=input('plz enter a number')
if a.isnumeric():
    n=int(a)
    if n%2==0:
        print(' Even')
    else:
        print('odd')
else:
    print('invalid input')


#step to divide it by 2 and get reminder using %

#if the reminder is 0 then print 'EVEN' else print 'ODD'

