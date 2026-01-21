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
        if not kwargs.get("silent", False):
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
        if not kwargs.get("silent", False):
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
                raise ValueError("Marks should be between 0 and 100")
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

# ================== STUDENT CLASS ==================
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.course = None

    def enroll(self, course):
        if self.course:
            raise Exception(
                f"Student '{self.name}' already enrolled in '{self.course.name}'"
            )
        self.course = course

    @log_execution
    @performance_timer
    def calculate_performance(self, silent=False):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def get_details(self):
        print(f"{self.pid:<6} {self.name:<20} {self.department:<18} {self.semester}")

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)

# ================== FACULTY CLASS ==================
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary
        self.assigned_course = None

    def get_details(self):
        assigned = self.assigned_course.code if self.assigned_course else "None"
        print(f"{self.pid:<6} {self.name:<20} {self.department:<18} {assigned}")

# ================== COURSE CLASS ==================
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

# ================== DISPLAY TABLE HELPERS ==================
def display_students(students):
    print("\nAvailable Students")
    print("--------------------------------")
    print("ID     Name                 Department         Sem")
    for s in students.values():
        s.get_details()

def display_faculty(faculty_members):
    print("\nAvailable Faculty")
    print("--------------------------------")
    print("ID     Name                 Department         Course")
    for f in faculty_members.values():
        f.get_details()

def display_courses(courses):
    print("\nAvailable Courses")
    print("--------------------------------")
    print("Code   Name                 Credits  Faculty")
    for c in courses.values():
        print(f"{c.code:<6} {c.name:<20} {c.credits:<8} {c.faculty.name}")

# ================== FILE HANDLING ==================
def save_students_json(students):
    with open("students.json", "w") as f:
        json.dump([
            {
                "id": s.pid,
                "name": s.name,
                "department": s.department,
                "semester": s.semester,
                "marks": s.marks
            } for s in students.values()
        ], f, indent=4)
    print("Student data successfully saved to students.json")

def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students.values():
            avg, grade = s.calculate_performance(silent=True)
            writer.writerow([s.pid, s.name, s.department, round(avg, 1), grade])
    print("CSV Report generated")

# ================== INPUT HELPER ==================
def input_marks_subject_wise():
    marks = []
    for i in range(1, 6):
        while True:
            try:
                m = int(input(f"Enter marks for Subject {i}: "))
                if 0 <= m <= 100:
                    marks.append(m)
                    break
                else:
                    print("Marks should be between 0 and 100")
            except ValueError:
                print("Invalid number")
    return marks

# ================== ADMIN HELPERS ==================
@admin_only
def create_faculty(fid, name, dept, sal):
    return Faculty(fid, name, dept, sal)

@admin_only
def create_course(code, name, credits, faculty):
    if faculty.assigned_course:
        raise Exception(
            f"Faculty '{faculty.name}' already assigned to '{faculty.assigned_course.code}'"
        )
    course = Course(code, name, credits, faculty)
    faculty.assigned_course = course
    return course

# ================== MAIN SYSTEM ==================
students = {}
faculty_members = {}
courses = {}

while True:
    print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Enroll Student\n5 Calculate Performance\n6 Compare Students\n7 Generate Reports\n8 Exit")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            if sid in students:
                raise Exception("Student ID already exists")
            students[sid] = Student(
                sid,
                input("Name: "),
                input("Department: "),
                int(input("Semester: ")),
                input_marks_subject_wise()
            )
            print("Student Created Successfully")

        elif choice == "2":
            fid = input("Faculty ID: ")
            faculty = create_faculty(
                fid,
                input("Name: "),
                input("Department: "),
                int(input("Salary: "))
            )
            if faculty:
                faculty_members[fid] = faculty
                print("Faculty Created Successfully")

        elif choice == "3":
            display_faculty(faculty_members)
            fid = input("Faculty ID: ")
            course = create_course(
                input("Course Code: "),
                input("Course Name: "),
                int(input("Credits: ")),
                faculty_members[fid]
            )
            if course:
                courses[course.code] = course
                print("Course Added Successfully")

        elif choice == "4":
            display_students(students)
            display_courses(courses)
            students[input("Student ID: ")].enroll(
                courses[input("Course Code: ")]
            )
            print("Enrollment Successful")

        elif choice == "5":
            display_students(students)
            s = students[input("Student ID: ")]
            avg, grade = s.calculate_performance()
            print(f"{s.name} | Average: {avg:.1f} | Grade: {grade}")

        elif choice == "6":
            display_students(students)
            s1 = students[input("First Student ID: ")]
            s2 = students[input("Second Student ID: ")]

            print("\nComparing Students Performance")
            print("--------------------------------")
            if s1 > s2:
                print(f"{s1.name} is performing better than {s2.name}")
            else:
                print(f"{s2.name} is performing better than {s1.name}")

        elif choice == "7":
            generate_csv_report(students)
            save_students_json(students)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print(f"Error: {e}")
