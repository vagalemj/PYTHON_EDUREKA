def function1(function):
    def wrapper(*args, **kwargs):
        print('hello')
        function(*args, **kwargs)
        print('welcome to python')
    return wrapper
def function2():
    print('version 3.11')

function2 = function1(function2)

function2()

