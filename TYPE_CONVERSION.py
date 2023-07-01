a=[10,20,30,40]             #LIST
b={1:'madhu',2:'sudhan'}    #DICTIONARY
c=(50,60,70,80)             #TUPLE
d={90,100,110,120}          #SET
e='madhu','sudhan'          #CHARACTER

print(e+c)                  #adding char and tuple

#CONVERTING

print(tuple(a))     #LIST -> TUPLE
print(tuple(b))     #DICTIONARY -> TUPLE
print(tuple(d))     #SET -> TUPLE
print(tuple(e))     #CHAR -> TUPLE

print(list(b))      #DICTIONARY -> LIST
print(list(c))      #TUPLE -> LIST
print(list(d))      #SET -> LIST
print(list(e))      #CHAR -> LIST

print(set(a))       #LIST -> SET
print(set(b))       #DICTIONARY -> SET
print(set(c))       #TUPLE -> SET
print(set(e))       #CHAR -> SET