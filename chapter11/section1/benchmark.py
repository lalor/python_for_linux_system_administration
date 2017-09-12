from __future__ import print_function
import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print(func.__name__, time.time() - t)
        return res
    return wrapper

@benchmark
def add(a, b):
    time.sleep(1)
    return a + b

print(add(1, 2))
