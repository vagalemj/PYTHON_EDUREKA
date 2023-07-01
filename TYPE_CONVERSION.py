a=[10,20,30,40]             #LIST
b={1:'madhu',2:'sudhan'}    #DICTIONARY
c=(50,60,70,80)             #TUPLE
d={90,100,110,120}          #SET
e='madhu','sudhan'          #CHARACTER

print(e+c)                  #adding char and tuple

print(tuple(a))
print(tuple(b))
print(tuple(d))
print(tuple(e))

print(list(b))
print(list(c))
print(list(d))
print(list(e))

print(set(a))
print(set(b))
print(set(c))
print(set(e))