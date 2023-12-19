def test(n):
    if n<=0:
        print('end')
    else:
        p=n
        n = n - 1
        test(n)
        print(p)

test(10)