import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print(a)

a.append(6)  # adding single element at the end of the array
print(a)

a.extend([8, 9, 10])  # adding multiple element at the end of the array
print(a)

a.insert(0, 0)  # inserting value in specific location of the array
print(a)
