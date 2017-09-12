#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import paramiko

def depoly_monitor(ip):

    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, 2092, 'lmx')

        stdin, stdout, stderr = client.exec_command('ls -l')
        print(stdout.readlines())

        with client.open_sftp() as sftp:
            sftp.put('monitor.py', 'monitor.py')
            sftp.chmod('monitor.py', 0o755)


def main():
    with open('hosts') as f:
        for line in f:
            depoly_monitor(line.strip())


if __name__ == '__main__':
    main()
