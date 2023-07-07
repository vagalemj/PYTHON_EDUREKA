import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print(a)

a.append(6)
print(a)

a.extend([8, 9, 10])
print(a)

a.insert(0, 0)
print(a)