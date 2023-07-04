from collections import defaultdict

a=defaultdict(int)

a[1] = 'python'
a[2] = 'ajax'

print(a)

print(a[3])     #does not throw an error while when we try to access out of index value

b={1:'python', 2:'java'}
print(b[3])     #throws an error

