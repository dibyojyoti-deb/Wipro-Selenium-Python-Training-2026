import pandas as pd
import numpy as np

# Dataset
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

# 1. Convert to Pandas DataFrame
df = pd.DataFrame(students)

# 2. Calculate statistics using NumPy
scores = df['score'].to_numpy()
mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)

print(f"Mean: {mean_score}")
print(f"Median: {median_score}")
print(f"Standard Deviation: {std_dev:.2f}\n")

# 3. Add 'above_average' column
df['above_average'] = df['score'] > mean_score

# Display Final DataFrame
print(df)

# Optional: Log results to file as per previous instructions
with open("test_log.txt", "a") as f:
    f.write(f"\nData Analysis Results:\n{df.to_string()}\n")