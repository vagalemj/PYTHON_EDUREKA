def funcmj():
    print('First function')
    def func1():
        print('First child function')
    def func2():
        print('Second child function')
    
    func1()
    func2()

print(funcmj())