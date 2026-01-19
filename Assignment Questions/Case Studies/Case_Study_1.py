# ================== IMPORTS ==================
from abc import ABC, abstractmethod
import json
import csv
import time
from functools import wraps

# ================== DECORATORS ==================
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        role = input("Enter role (admin/user): ")
        if role.lower() != "admin":
            print("Access Denied: Admin privileges required")
            return None
        return func(*args, **kwargs)
    return wrapper

def performance_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Execution Time: {end - start:.6f} seconds")
        return result
    return wrapper

# ================== DESCRIPTORS ==================
class MarksDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        for mark in value:
            if mark < 0 or mark > 100:
                raise ValueError("Invalid Marks: Marks should be between 0 and 100")
        obj.__dict__[self.name] = value

class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj.__dict__['_salary'] = value

# ================== ABSTRACT BASE CLASS ==================
class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up resources for {self.name}")

# ================== STUDENT CLASS ==================
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    @log_execution
    @performance_timer
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

# ================== FACULTY CLASS ==================
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")

# ================== COURSE CLASS ==================
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

# ================== ITERATOR ==================
class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.courses):
            raise StopIteration
        course = self.courses[self.index]
        self.index += 1
        return course

# ================== GENERATOR ==================
def student_generator(students):
    print("Fetching Student Records...")
    for sid, student in students.items():
        yield f"{sid} - {student.name}"

# ================== FILE HANDLING ==================
def save_students_json(students):
    data = []
    for s in students.values():
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Student data successfully saved to students.json")

def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students.values():
            avg, grade = s.calculate_performance()
            writer.writerow([s.pid, s.name, s.department, round(avg, 2), grade])
    print("CSV Report (students_report.csv) generated")

# ================== UI HELPER FUNCTIONS ==================
def input_marks_subject_wise():
    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = int(input(f"Enter marks for Subject {i}: "))
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a valid number")
    return marks

def display_students_table(students):
    if not students:
        print("No students registered yet")
        return
    print("\nRegistered Students")
    print("-" * 60)
    print(f"{'ID':<10}{'Name':<25}{'Courses'}")
    print("-" * 60)
    for s in students.values():
        course_names = ", ".join(c.name for c in s.courses) if s.courses else "Not Enrolled"
        print(f"{s.pid:<10}{s.name:<25}{course_names}")

def display_faculty_table(faculty_members):
    if not faculty_members:
        print("No faculty registered yet")
        return
    print("\nAvailable Faculty")
    print("-" * 40)
    print(f"{'ID':<10}{'Name'}")
    print("-" * 40)
    for f in faculty_members.values():
        print(f"{f.pid:<10}{f.name}")

def display_courses_table(courses):
    if not courses:
        print("No courses available yet")
        return
    print("\nAvailable Courses")
    print("-" * 60)
    print(f"{'Code':<10}{'Course Name':<30}{'Credits'}")
    print("-" * 60)
    for c in courses.values():
        print(f"{c.code:<10}{c.name:<30}{c.credits}")

def display_students_for_comparison(students):
    if not students:
        print("No students registered yet")
        return
    print("\nAvailable Students")
    print("-" * 40)
    print(f"{'ID':<10}{'Name'}")
    print("-" * 40)
    for s in students.values():
        print(f"{s.pid:<10}{s.name}")

# ================== MAIN SYSTEM ==================
students = {}
faculty_members = {}
courses = {}

while True:
    print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll Student\n5 Calculate Performance\n6 Compare Students\n7 Generate Reports\n8 Exit")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ").strip()
            if not sid:
                print("Student ID cannot be empty")
                continue
            if sid in students:
                raise Exception("Student ID already exists")
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue
            dept = input("Department: ").strip()
            if not dept:
                print("Department cannot be empty")
                continue
            while True:
                try:
                    sem = int(input("Semester: "))
                    if sem < 1 or sem > 8:
                        print("Semester should be between 1 and 8")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid semester number")
            marks = input_marks_subject_wise()
            students[sid] = Student(sid, name, dept, sem, marks)
            print("Student Created Successfully")
            display_students_table(students)

        elif choice == "2":
            fid = input("Faculty ID: ").strip()
            if not fid:
                print("Faculty ID cannot be empty")
                continue
            if fid in faculty_members:
                raise Exception("Faculty ID already exists")
            name = input("Name: ").strip()
            if not name:
                print("Name cannot be empty")
                continue
            dept = input("Department: ").strip()
            if not dept:
                print("Department cannot be empty")
                continue
            while True:
                try:
                    sal = int(input("Salary: "))
                    if sal < 0:
                        print("Salary cannot be negative")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid salary")
            faculty_members[fid] = Faculty(fid, name, dept, sal)
            print("Faculty Created Successfully")
            display_faculty_table(faculty_members)

        elif choice == "3":
            code = input("Course Code: ").strip()
            if not code:
                print("Course Code cannot be empty")
                continue
            if code in courses:
                raise Exception("Course Code already exists")
            name = input("Course Name: ").strip()
            if not name:
                print("Course Name cannot be empty")
                continue
            while True:
                try:
                    credits = int(input("Credits: "))
                    if credits < 0:
                        print("Credits cannot be negative")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid credit value")
            display_faculty_table(faculty_members)
            fid = input("Faculty ID: ").strip()
            if fid not in faculty_members:
                raise Exception("Faculty ID not found")
            courses[code] = Course(code, name, credits, faculty_members[fid])
            print("Course Added Successfully")

        elif choice == "4":
            display_courses_table(courses)
            sid = input("Student ID: ").strip()
            if sid not in students:
                raise Exception("Student ID not found")
            code = input("Course Code: ").strip()
            if code not in courses:
                raise Exception("Course Code not found")
            students[sid].enroll(courses[code])
            print("Enrollment Successful")

        elif choice == "5":
            sid = input("Student ID: ").strip()
            if sid not in students:
                raise Exception("Student ID not found")
            avg, grade = students[sid].calculate_performance()
            print(f"Average: {avg:.2f}, Grade: {grade}")

        elif choice == "6":
            display_students_for_comparison(students)
            s1_id = input("First Student ID: ").strip()
            if s1_id not in students:
                raise Exception("First Student ID not found")
            s2_id = input("Second Student ID: ").strip()
            if s2_id not in students:
                raise Exception("Second Student ID not found")
            s1 = students[s1_id]
            s2 = students[s2_id]
            print(f"{s1.name} > {s2.name} :", s1 > s2)

        elif choice == "7":
            if not students:
                print("No students to generate reports")
                continue
            generate_csv_report(students)
            save_students_json(students)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print(f"Error: {e}")