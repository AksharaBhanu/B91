age=20
print(age>18 and age<100) #T & T
print(age>20 and age<100) #F & T
print(age>18 and age<10) #T & F
print(age>30 and age<10) #F & F


print(age>18 or age<100) #T & T
print(age>20 or age<100) #F & T
print(age>18 or age<10) #T & F
print(age>30 or age<10) #F & F

print(not(age>18))
print(not(age>100))