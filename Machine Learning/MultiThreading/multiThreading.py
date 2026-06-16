# Multithreading
# when to use multithreading
# I/O-nound tasks: Tasks that spend more time waiting for I/O operations(e.g. file operations, network request).
# Concurrent execution: when you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

# create 2 threads
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)

t=time.time()
# Start the thread
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)