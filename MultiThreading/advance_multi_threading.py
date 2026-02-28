# Multithreading with Thread Pool Executer

from concurrent.futures import ThreadPoolExecutor
import time

def print_num(num):
    time.sleep(1)
    return f"Number: {num}"

nums=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_num,nums)

for result in results:
    print(result)