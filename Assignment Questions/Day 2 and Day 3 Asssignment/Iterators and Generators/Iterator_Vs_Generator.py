class OneToN:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def main():
    print("Enter the upper limit:")
    n = int(input())

    print("\nIterator Output:")
    for value in OneToN(n):
        print(value)

    print("\nGenerator Output:")
    for value in fibonacci(n):
        print(value)


main()
