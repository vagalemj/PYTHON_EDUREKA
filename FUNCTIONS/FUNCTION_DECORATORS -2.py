def function1(function):
    def wrapper():
        print('hello')
        function()
        print('welcome to python')
    return wrapper
@function1
def function2():
    print('version 3.11')

print(function2())
