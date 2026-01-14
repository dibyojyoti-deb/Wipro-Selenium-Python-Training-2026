def number_generator(n):
    """
    Generator that yields numbers from 1 to N
    """
    for i in range(1, n + 1):
        yield i


def square_generator(n):
    """
    Generator that yields squares of numbers from 1 to N
    """
    for i in range(1, n + 1):
        yield i ** 2

def fibonacci_generator(n):
    """
    Generator that yields first N Fibonacci numbers
    """
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    n = 10
    
    print(f"Numbers up to {n}:")
    for num in number_generator(n):
        print(num, end=" ")
    print("\n")
    
    print(f"Squares up to {n}:")
    for square in square_generator(n):
        print(square, end=" ")
    print("\n")
    
    print(f"First {n} Fibonacci numbers:")
    for fib in fibonacci_generator(n):
        print(fib, end=" ")
    print()