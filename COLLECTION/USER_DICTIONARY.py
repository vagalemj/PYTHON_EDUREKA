from collections import UserDict

a = {'a': 1, 'b': 2, 'c': 3}

b = UserDict(a)     # Creating an User Dictionary
print(b)

c = UserDict()      # Creating an empty User Dictionary
print(c)