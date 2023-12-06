name="ABCDEF" #6


#print in reverse order
print(name[::-1])

#print alternative character
print(name[::2])

#print reverse alternative character
print(name[::-2])

#print all the chars except 1st and last 10--> 0 to 9 0 & 9
count=len(name)-1
print(name[1:count])
print(name[1:-1])