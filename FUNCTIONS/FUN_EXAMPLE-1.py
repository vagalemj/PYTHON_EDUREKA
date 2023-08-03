def func1(name):
    return f"one {name}"

def func2(name):
    return f"{name} two"

def func3(func4):
    return func4("three and four")

print(func3(func1))
print(func3(func2))

