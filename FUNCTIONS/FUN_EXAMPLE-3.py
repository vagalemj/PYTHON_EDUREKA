def func(n):
    def func1():
        return 'madhu'
    def func2():
        return 'sudhan'
    if n==1:
        return func1
    else:
        return func2

a=func(1)
b=func(11)

print(a())
print(b())