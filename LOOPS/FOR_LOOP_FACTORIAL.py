# Iterative approach
def factorial_iterative(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Recursive approach
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test cases
num = 5
print(f"Factorial of {num} using the iterative approach:", factorial_iterative(num))
print(f"Factorial of {num} using the recursive approach:", factorial_recursive(num))
