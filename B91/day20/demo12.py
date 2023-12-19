def test(n):
    if n>0:
        print(n)
        n=n-1
        test(n)

test(10)