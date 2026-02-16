import requests
import threading
import time
import sys

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

# Initialize Logger
sys.stdout = Logger("download_comparison_log.txt")

urls = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in"
]

def downloadfiles(url):
    try:
        response = requests.get(url)
        # Cleaning filename to handle empty strings from split
        name_part = url.split("/")[-1]
        if not name_part:
            name_part = url.split("//")[-1].replace(".", "_")
        filename = name_part + ".txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# --- Sequential Section ---
print("--- Starting Sequential Downloads ---")
starttime = time.time()
for url in urls:
    downloadfiles(url)
sequentialtime = time.time() - starttime
print(f"Sequential download time: {sequentialtime:.4f} seconds")

# --- Threading Section ---
print("\n--- Starting Threading Downloads ---")
threads = []
starttime1 = time.time()
for url in urls:
    thread = threading.Thread(target=downloadfiles, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish before measuring time
for thread in threads:
    thread.join()

threadingtime = time.time() - starttime1
print(f"Threading download time: {threadingtime:.4f} seconds")

# --- Faster Method Comparison ---
print("\n--- Speed Comparison ---")
if threadingtime < sequentialtime:
    difference = sequentialtime - threadingtime
    print(f"Threading was faster by {difference:.4f} seconds.")
else:
    difference = threadingtime - sequentialtime
    print(f"Sequential was faster by {difference:.4f} seconds.")