import math
import time
import sys
from multiprocessing import Pool, cpu_count

# Remove the limit for integer string conversion to allow processing massive factorials
sys.set_int_max_str_digits(0)

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [50000, 60000, 55000, 45000, 70000]

    # --- Sequential Section ---
    print("--- Starting Sequential Calculations ---")
    starttime1 = time.time()
    seq_results = []
    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
        print(f"Sequential: Factorial {num} calculated")
    seqtime = time.time() - starttime1
    print(f"Sequential time: {seqtime:.4f} seconds")

    # --- Multiprocessing Section ---
    print("\n--- Starting Multiprocessing Calculations ---")
    starttime2 = time.time()
    
    # Pool(cpu_count()) uses all available CPU cores
    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)
    
    for num in numbers:
        print(f"Multiprocessing: Factorial {num} calculated")
    
    paralleltime = time.time() - starttime2
    print(f"Parallel time: {paralleltime:.4f} seconds")

    # --- Speed Comparison ---
    print("\n--- Speed Comparison ---")
    if paralleltime < seqtime:
        print(f"Multiprocessing was faster by {seqtime - paralleltime:.4f} seconds.")
    else:
        print(f"Sequential was faster by {paralleltime - seqtime:.4f} seconds.")