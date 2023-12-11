#accept age and gender and print if the person is eligible for marriage
age=int(input('plz enter ur age'))
gender=input('plz enter the gender (M/F)').upper()

if gender=='M':
    if age>=21:
        print('Yes boy u can')
    else:
        print('No kid')
elif gender=='F':
    if age >=18:
        print('Yes madam')
    else:
        print('No baby')
else:
    print('invalid')

if (gender=='M' and  age>=21 ) or (gender=='F' and age >=18):
    print('yes')
else:
    print('No')
