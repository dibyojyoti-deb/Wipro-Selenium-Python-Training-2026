class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print("-" * 20)


n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    students.append(Student(name, roll_no))

print("\nStudent Details:")
for student in students:
    student.display_details()
