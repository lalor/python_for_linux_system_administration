from __future__ import print_function
import threading

def say_hi():
    print("hello, world")

def main():
    for i in range(5):
       thread = threading.Thread(target=say_hi)
       thread.start()

if __name__ == '__main__':
    main()
