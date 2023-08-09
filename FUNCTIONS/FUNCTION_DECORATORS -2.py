def function1(function):    #function with arguments
    def wrapper():          #inner function
        print('hello')      
        function()          #pass function again
        print('welcome to python')
    return wrapper          #return wrapper
@function1                  #Syntatic sugar (python decorator)
def function2():
    print('version 3.11')

function2()
