import pandas as pd

# Dataset
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}
df = pd.DataFrame(data)

# 1. Filter all employees from the "IT" department
it_employees = df[df["Department"] == "IT"]

# 2. Find the average salary per department
avg_salary_dept = df.groupby("Department")["Salary"].mean()

# 3. Add "Salary_Adjusted" column (increase by 10%)
df["Salary_Adjusted"] = df["Salary"] * 1.10

# Output results
print("IT Employees:")
print(it_employees)
print("\nAverage Salary per Department:")
print(avg_salary_dept)
print("\nFinal DataFrame with Salary Adjustment:")
print(df)

# Logging to file
with open("test_log.txt", "a") as f:
    f.write(f"\nEmployee Analysis:\n{df.to_string()}\n")