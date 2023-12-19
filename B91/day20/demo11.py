#test(0)--> End
#test(1)--> 1  End
#test(2)--> 2 1 end
def test(n):
    if n<=0:
        print('end')
    else:
        print(n)
        n=n-1
        test(n)

test(3)