#n = int(input('Enter the number of rows: '))

for i in range(5):
    for j in range(5-i):
        print(' ',end=' ')
    for j in range(2 * i + 1):
        print('*',end=' ')
    print()
    
