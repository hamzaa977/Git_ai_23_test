print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")
class Calculator:

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b

    def multiply(self,a,b):
        if isinstance(a, float) and isinstance(b, float):
            return a*b
        return a * b

    def divide(self, a, b):
        if b==0:
            raise ValueError("Cannot divide by zero")
        return a/b
    
    def power(self, a, b):
    # Fix the power function here
    # Hint: how should negative exponents be handled?
        if b < 0:
            return 1 / (a ** abs(b))
        return a ** b

    def factorial(self, n):
        # """Calculate the factorial of n"""
        # TODO: Implement this function
        # The factorial of n is the product of all positive integers less than or equal to n
        # For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
        # Edge cases: factorial(0) = 1, factorial of negative numbers should raise ValueError
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
        
    def fibonacci(self, n):
        # """Return the nth Fibonacci number"""
        # The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
        # fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, fibonacci(3) = 2, etc.
        # Edge case: fibonacci of negative numbers should raise ValueError
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b