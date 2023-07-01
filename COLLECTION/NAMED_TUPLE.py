from collections import namedtuple

a=namedtuple('courses','name, technology, lang')
s=a('data science','ML','python')
print(s)        #binds the tuple a to s
