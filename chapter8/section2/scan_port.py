from __future__ import print_function
from socket import *

def conn_scan(host, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((host, port))
        print(host, port, 'is avaliable')
    except Exception as e:
        print(host, port, 'is not avaliable')
    finally:
        conn.close()

def main():
    host = "10.166.224.14"
    for port in range(20, 5000):
        conn_scan(host, port)

if __name__ == '__main__':
    main()
