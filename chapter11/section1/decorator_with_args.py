from __future__ import print_function

def times(length=1):
    def bread(func):
        def wrapper(*args, **kwargs):
            for i in range(length):
                func(*args, **kwargs)
        return wrapper
    return bread

@times(5)
def sandwich(name):
    print(name)

sandwich('Helo, World')
