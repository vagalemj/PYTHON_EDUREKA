from collections import UserString

a = 'Welcome to MJ world'      # string sentences with single Quotes
b=UserString(a)

print(b)

c = "I'm MJV"          # string sentences with double Quotes
d=UserString(c)

print(d)

print(len(d))
print(len(b))       #length of the strings