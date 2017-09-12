from __future__ import print_function
import ipdb

def sum_nums(n):
    s=0
    for i in range(n):
        ipdb.set_trace()
        s += i
        print(s)

if __name__ == '__main__':
    sum_nums(5)
