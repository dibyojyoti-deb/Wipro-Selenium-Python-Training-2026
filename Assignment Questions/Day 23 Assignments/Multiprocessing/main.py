import math
import time
import sys
from multiprocessing import Pool, cpu_count

# Increase the limit for integer string conversion to handle massive factorials
sys.set_int_max_str_digits(0)

# Logger to capture terminal output to a file
class Logger:
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    # Initialize Logger
    sys.stdout = Logger("factorial_analysis_log.txt")

    numbers = [50000, 60000, 55000, 45000, 70000]

    # --- Sequential Section ---
    print("--- Starting Sequential Calculations ---")
    starttime1 = time.time()
    seq_results = []
    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
        # Requirement: Print the factorial of each number
        print(f"Sequential Result for {num}: {result}")
    seqtime = time.time() - starttime1
    print(f"Sequential total time: {seqtime:.4f} seconds")

    # --- Multiprocessing Section ---
    print("\n--- Starting Multiprocessing Calculations ---")
    starttime2 = time.time()
    
    # Pool mapping for parallel execution
    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)
    
    # Requirement: Print the factorial of each number
    for num, res in zip(numbers, parallel_results):
        print(f"Parallel Result for {num}: {res}")
    
    paralleltime = time.time() - starttime2
    print(f"Parallel total time: {paralleltime:.4f} seconds")

    # --- Comparison Section ---
    print("\n--- Speed Comparison ---")
    print(f"Sequential Time: {seqtime:.4f}s")
    print(f"Parallel Time: {paralleltime:.4f}s")
    
    if paralleltime < seqtime:
        print(f"Multiprocessing was faster by {seqtime - paralleltime:.4f} seconds.")
    else:
        print(f"Sequential was faster by {paralleltime - seqtime:.4f} seconds.")