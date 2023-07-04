from collections import OrderedDict

a=OrderedDict()
a[1] = 'm'
a[2] = 'a'
a[3] = 'd'
a[4] = 'h'
a[5] = 'u'

print(a)        #ordred dictionary

print(a.keys())

print(a.popitem())  #deletes the last dictionary item

print(a)

a[1] = 's'

print(a)