import array as arr

a = arr.array('d', [2.5, 8.4, 3.0, 4.0, 4.5, 6.7, 1.1, 2.3])

b=0         #initializing the iterator

while b<len(a):     #specify the condition
    print(a[b])
    b=b+1       #increment your iterator


#while b<a[4]:     #specify the condition
#    print(a[b])
#    b=b+1           #increment your iterator

