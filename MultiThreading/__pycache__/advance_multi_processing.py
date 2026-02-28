# Multiprocessing with ProcessPoopExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def sq_num(number):
    time.sleep(1)
    return f"Square: {number*number}"

numbers = [1,2,3,4,5]

if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(sq_num,numbers)

    for result in results:
        print(result)