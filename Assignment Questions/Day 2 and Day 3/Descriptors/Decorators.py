import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper


@execution_time
def compute_sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


n = int(input("Enter a number to compute sum up to: "))

result = compute_sum(n)
print(result)
