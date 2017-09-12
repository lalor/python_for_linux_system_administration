def bread(f):
    def wrapper(*args, **kwargs):
        print("begin")
        f()
        print("end")
    return wrapper

@bread
def say_hi():
    print("Hi")

say_hi()
