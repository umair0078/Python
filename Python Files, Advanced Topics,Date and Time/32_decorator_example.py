# How long a function takes to run
import time

def timer(func):
    def modified_function():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")
    return modified_function

@timer
def greet():
    print("Hello!")
    time.sleep(2)

greet()