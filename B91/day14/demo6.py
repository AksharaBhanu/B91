#WAP to check if the give word is palindrome or not mom dad madam
s=input('plz enter a word')
r=s[-1::-1]
if s==r:
    print(s,' is a palindrome')
else:
    print(s,' is NOT a palindrome')