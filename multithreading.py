import threading

def print_numbers():
    for i in range(10):
        print(i)

# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)

t1.start()
t2.start()

t1.join()
t2.join()