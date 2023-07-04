from collections import namedtuple     #importing namedtuple from collection library

a=namedtuple('courses','name, technology, lang')
s=a('data science','ML','python')
print(s)                                    #binds the tuple a to s
s=a._make(['data science','ML','python'])   #list
print(s)
