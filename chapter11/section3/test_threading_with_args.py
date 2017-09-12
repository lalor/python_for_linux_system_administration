from __future__ import print_function
import threading

def say_hi(count, name):
    while count > 0:
        print("hello", name)
        count -= 1

def main():
    usernames = ['Bob', 'Jack', 'Pony', 'Jone', 'Mike']
    for i in range(5):
       thread = threading.Thread(target=say_hi, args=(50, usernames[i]))
       thread.start()

if __name__ == '__main__':
    main()
