#print multiplication table of given number
start=int(input('please enter starting number'))
end=int(input('please enter ending number'))
for n in range(start,end+1):
    for i in range(1,11):
        print(n,'x',i,'=',n*i)
    print('-'*10)