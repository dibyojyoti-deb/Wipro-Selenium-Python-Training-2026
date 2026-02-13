import mysql.connector
import sys

# Logger to capture terminal output to a specific file
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# Renamed the output file here
sys.stdout = Logger("database_log.txt")

# Database configuration
host = "localhost"
user = "root"
password = "bushan10"
database = "feb2026"

# Establishing connection
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("connected to the database successfully")

# Executing query
query = "SELECT * FROM employee"
cursor.execute(query)

result = cursor.fetchall()

# Printing results
for row in result:
    print(row)

# Closing connection
cursor.close()
conn.close()