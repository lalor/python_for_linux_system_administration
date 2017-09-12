#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import os
import shutil
import tarfile
import subprocess


def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def unpackage_mongo(package, package_dir):
    unpackage_dir = os.path.splitext(package)[0]
    if os.path.exists(unpackage_dir):
        shutil.rmtree(unpackage_dir)

    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)

    t = tarfile.open(package, 'r:gz')
    t.extractall('.')

    shutil.move(unpackage_dir, package_dir)


def create_datadir(data_dir):
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    os.mkdir(data_dir)


def format_mongod_command(package_dir, data_dir, logfile):
    mongod = os.path.join(package_dir, 'bin', 'mongod')
    mongod_format = """{0} --fork --dbpath {1} --logpath {2}"""
    return mongod_format.format(mongod, data_dir, logfile)


def start_mongod(cmd):
    returncode, out = execute_cmd(cmd)
    if returncode != 0:
        raise SystemExit('execute {0} error :{1}'.format(cmd, out))
    else:
        print("execute command ({0}) successful".format(cmd))


def main():
    package = 'mongodb-linux-x86_64-debian71-3.4.0.tgz'
    cur_dir = os.path.abspath('.')
    package_dir = os.path.join(cur_dir, 'mongo')
    data_dir = os.path.join(cur_dir, 'mongodata')
    logfile = os.path.join(data_dir, 'mongod.log')

    if not os.path.exists(package):
        raise SystemExit("{0} not found".format(package))

    unpackage_mongo(package, package_dir)
    create_datadir(data_dir)
    start_mongod(format_mongod_command(package_dir, data_dir, logfile))


if __name__ == '__main__':
    main()
