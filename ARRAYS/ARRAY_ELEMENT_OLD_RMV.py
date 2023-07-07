import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)

a.pop(4)  # removes specific index element in array
print(a)

a.pop(-9)  # removes specific index element in array (reverse) order
print(a)

a.remove(7)  # removes specific element in array
print(a)
