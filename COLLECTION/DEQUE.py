from collections import deque

a=['m','a','d','h','u','s','u','d','h','a','n']
d=deque(a)
print(d)

d.append('vagale')
d.appendleft('vagale')
print(d)
d.pop()
print(d)
d.pop()
print(d)