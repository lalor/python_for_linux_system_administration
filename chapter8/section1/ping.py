from __future__ import print_function
import subprocess
import threading

def is_reacheable(ip):
    if subprocess.call(["ping", "-c", "1", ip]):
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))

def main():
    with open('ips.txt') as f:
        lines = f.readlines()
        threads = []
        for line in lines:
            thr = threading.Thread(target=is_reacheable, args=(line,))
            thr.start()
            threads.append(thr)

        for thr in threads:
            thr.join()

if __name__ == '__main__':
    main()
