import pandas as pd
import numpy as np
import sys
import io

# Logger to capture terminal output
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self): pass

sys.stdout = Logger("sales_analysis_log.txt")

# Create the CSV data in-memory for the script to run without external files
csv_data = """Date,Product,Quantity,Price
1/1/2025,A,10,50
1/2/2025,B,5,30
1/3/2025,C,12,40
1/4/2025,A,7,50"""

# 1. Load the CSV into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))
print("--- Loaded DataFrame ---")
print(df)

# 2. Add a new column "Total" (Quantity * Price)
df['Total'] = df['Quantity'] * df['Price']
print("\n--- DataFrame with 'Total' Column ---")
print(df)

# 3. Using NumPy for calculations
total_array = df['Total'].to_numpy()

total_sales = np.sum(total_array)
avg_daily_sales = np.mean(total_array)
std_dev_sales = np.std(total_array)

print("\n--- Sales Statistics (NumPy) ---")
print(f"Total Sales: {total_sales}")
print(f"Average Daily Sales: {avg_daily_sales:.2f}")
print(f"Standard Deviation of Daily Sales: {std_dev_sales:.2f}")