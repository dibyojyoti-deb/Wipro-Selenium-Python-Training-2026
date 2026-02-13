from pymongo import MongoClient
import sys

class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self): pass

sys.stdout = Logger("mongodb_terminal_log.txt")

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["company_db"]
    collection = db["employees"]
    print("--- MongoDB: Connected Successfully ---\n")

    # 1. Insert a new employee
    new_emp = {"name": "Suresh", "department": "IT", "salary": 55000}
    res = collection.insert_one(new_emp)
    print(f"Inserted document ID: {res.inserted_id}")

    # 2. Find all in "IT"
    print("\nEmployees in IT Department:")
    for emp in collection.find({"department": "IT"}):
        print(emp)

    # 3. Update salary of 'Suresh'
    collection.update_one({"name": "Suresh"}, {"$set": {"salary": 58000}})
    print("\nUpdated Suresh's salary to 58000.")

    client.close()
except Exception as e:
    print(f"Error: {e}")