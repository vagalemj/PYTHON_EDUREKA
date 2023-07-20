list1=[10,20,30,'madhu']
list2=[10,40,50]
list3=[10,20,30]

x = list1

print(x in list1)

print(10 in list1)

print(x[0] in list1)

print('madhu' in list1)

y = list2

print(y in list2)

print(50 in list2)

print(10 in(list1 and list2 or list3))

#print(10 in(list1 or list2 or list3))

print(list1 in list2)

print(list1 in list3)

print(list1 == list3)