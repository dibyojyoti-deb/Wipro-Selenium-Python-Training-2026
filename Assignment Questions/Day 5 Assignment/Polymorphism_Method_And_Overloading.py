# Base class demonstrating method overriding
class Calculator:
    def calculate(self, a, b):
        print(f"Calculator Result (Addition): {a + b}")


# Derived class overriding the method
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print(f"AdvancedCalculator Result (Multiplication): {a * b}")


# Custom class for operator overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print(f"Result after operator overloading: {self.value}")


def main():
    print("=== Method Overriding & Polymorphism Demo ===")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\n--- Using Calculator (Base Class) ---")
    calc = Calculator()
    calc.calculate(a, b)   # Polymorphism

    print("\n--- Using AdvancedCalculator (Derived Class) ---")
    adv_calc = AdvancedCalculator()
    adv_calc.calculate(a, b)   # Overridden behavior

    print("\n=== Operator Overloading Demo (+) ===")
    x = int(input("Enter first value for object 1: "))
    y = int(input("Enter first value for object 2: "))

    obj1 = Number(x)
    obj2 = Number(y)

    result = obj1 + obj2   # Operator overloading
    result.display()


if __name__ == "__main__":
    main()
