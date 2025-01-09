import time

def timer(func):
    def count_time():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return count_time()


@timer
def number():
    for i in range(100000000):
        pass