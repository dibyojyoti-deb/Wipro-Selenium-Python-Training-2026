class SalaryDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get("salary")

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance.__dict__["salary"] = value


class Employee:
    salary = SalaryDescriptor()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))

employee = Employee(name, salary)
print(employee.name)
print(employee.salary)
