import mysql.connector
import sys

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self): pass

sys.stdout = Logger("mysql_terminal_log.txt")

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "bushan10",
    "database": "company_db"
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("--- MySQL: Connected Successfully ---\n")

    # 1. Fetch employees with salary > 50,000
    cursor.execute("SELECT * FROM employees WHERE salary > 50000")
    print("Employees with salary > 50,000:")
    for row in cursor.fetchall():
        print(row)

    # 2. Insert a new employee
    sql_insert = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
    cursor.execute(sql_insert, ("Rajesh", "IT", 60000))
    conn.commit()
    print(f"\nInserted new employee: Rajesh")

    # 3. Update salary by 10% (e.g., for Employee ID 1)
    cursor.execute("UPDATE employees SET salary = salary * 1.10 WHERE id = 1")
    conn.commit()
    print("Updated salary for ID 1 by 10%.")

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")