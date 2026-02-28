# Processes that run in parallel
#  CPU-Bound Tasks that are heavy in usage(e.g., mathematical computation, data processing)
#  Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def sq_num():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__=="__main__":
    # creating 2 processes
    p1 = multiprocessing.Process(target=sq_num)
    p2 = multiprocessing.Process(target=cube_num)
    t=time.time()

    # Start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)