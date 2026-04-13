#Factorial using Recursion

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Fibonacci using Recursion

def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example
print(fibonacci(6))  # Output: 8