#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function

from fabric.api import (cd, run, task, env, roles, put, execute, hide, set_missing_host_key_policyings, sudo)
from fabric.colors import red, green, yellow
from fabric.contrib.files import exists

env.user = 'lmx'
env.port = 2092
env.roledefs = { 'web': ["10.166.224.14", "10.166.224.140"],
               'db': ["10.166.226.152"] }

def is_redis_installed():
    with settings(hide('everything'), warn_only=True):
        result = run("netstat -tl | grep -w 6379")
        return result.return_code == 0

def install_redis():
    sudo("apt-get install redis-server")

def change_redis_conf():
    sudo("sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf")

def reboot_redis():
    sudo("/etc/init.d/redis-server restart", pty=False)

@task
@roles('db')
def depoly_db():

    if is_redis_installed():
        print(yellow('redis was successfully installed'))
    else:
        install_redis()

        change_redis_conf()

        reboot_redis()

        print(green('redis has successfully installed'))

def is_python_package_installed(package):
    with settings(hide('everything'), warn_only=True):
        result = run("python -c 'import {0}'".format(package))
        return result.return_code == 0

def install_python_package(package):
    sudo('pip install {0}'.format(package))

def pip_install_if_need(package):
    if not is_python_package_installed(package):
        install_python_package(package)
        print(green('{0} has installed'.format(package)))
    else:
        print(yellow('{0} was installed'.format(package)))

def install_package():
    for package in ['gunicorn', 'flask', 'redis']:
        pip_install_if_need(package)

def kill_web_app_if_exists():
    with cd('/tmp'):
        if exists('app.pid'):
            pid = run('cat app.pid')
            print(yellow('kill app which pid is {0}'.format(pid)))
            with settings(hide('everything'), warn_only=True):
                run('kill -9 {0}'.format(pid))
        else:
            print(red('pid file not exists'))

def upload_web_app():
    put('app.py', '/tmp/app.py')

def run_web_app():
    with cd('/tmp'):
        run('gunicorn -w 1 app:app -b 0.0.0.0:5000 -D -p /tmp/app.pid --log-file /tmp/app.log', pty=False)

def restart_web_app():
    kill_web_app_if_exists()
    run_web_app()

@task
@roles('web')
def depoly_web():

    install_package()

    upload_web_app()

    restart_web_app()

@task
def depoly_all():
    execute(depoly_db)
    execute(depoly_web)
