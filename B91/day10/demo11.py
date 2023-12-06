a='abc'
all_methods=dir(a)
methods = [method for method in all_methods if callable(getattr(a, method))]

# Print the methods
print("Methods in MyClass:")
for method in methods:
    print(method)

# print(a.isalpha()) #contains only letter -yes-true
# print(a.isnumeric())#contains only digits -no-false
# print(a.isalnum())#contains  letter or digits-true
# print('-----------')
# b='abc123'
# print(b.isalpha())#contains only letter -no-false
# print(b.isnumeric())#contains only digits -no-false
# print(b.isalnum())#contains  letter or digits-yes-true
# print('-----------')
# c='123'
# print(c.isalpha())#contains only letter -no-false
# print(c.isnumeric())#contains only digits -yes-true
# print(c.isalnum())#contains  letter or digits-yes-true

