import multiprocessing
import multiprocessing.pool
import time

def timer(func):
    def count_time(*args, **kwargs,):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(end - start)
    return count_time()

def square_number(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        numbers = [1, 2, 3, 4, 5]
        result = pool.map(square_number, numbers)
        print(result)
        
        
# The time will not print in the output as the  multiprocessing.Pool runs the tasks (square_number) in separate processes, 
# and in these processes, the timer decorator is executing, but its print output isn't shown in the main process. 
# Each subprocess handles its own execution, and by default, the print statements are not returned to the main process