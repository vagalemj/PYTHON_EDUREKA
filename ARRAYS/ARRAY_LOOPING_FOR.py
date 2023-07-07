import array as arr

a = arr.array('i', [2, 5, 8, 4, 3, 0, 4, 0, 4, 5, 6, 7, 1, 1, 2, 3])

print(a)
print('===============================')

for x in a:         # FOR LOOP
    print('for loop: ',x)

print('===============================')

for x in a[2:9]:         # FOR LOOP (range)
    print('for loop range: ',x)
