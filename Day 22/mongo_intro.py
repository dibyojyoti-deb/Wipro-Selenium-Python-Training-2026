import sys
from pymongo import MongoClient

# Logger to capture terminal output to a file
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger("output.txt")

# Original Code
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
collection = db["employees"]

new_employee = {
    "name": "Anuradha",
    "department": "IT",
    "salary": 75000
}

insert_result = collection.insert_one(new_employee)
print(f"\nInserted new employee with ID: {insert_result.inserted_id}")