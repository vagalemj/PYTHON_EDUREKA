from collections import deque

a = ['m', 'a', 'd', 'h', 'u', 's', 'u', 'd', 'h', 'a', 'n']
d = deque(a)  # inserting and deleting
print(d)

d.append('vagale')  # append to last position of list
d.appendleft('vagale')  # append to first position of list
print(d)
d.pop()  # deletes the value of the list -> last position
print(d)
d.pop()
print(d)
d.pop()
