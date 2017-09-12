#!/usr/bin/python
from fabric.api import (local, put, abort, run, cd, task, execute, settings,
                        env, runs_once, lcd, sudo)
from fabric.contrib.console import confirm
from fabric.colors import green

env.user = 'lmx'
env.port = 2092
env.hosts = open('hosts').readlines()

@task
@runs_once
def test():
    with settings(warn_only=True), lcd("redis-3.2.8"):
        result = local("make test", capture=True)
        if result.failed and not confirm("Tests failed. Continue anyway?"):
            abort("Aborting at user request.")
        else:
            green("All tests passed without errors!")

    with lcd("redis-3.2.8"):
        local("make clean")
    local("tar -czf redis-3.2.8.tar.gz redis-3.2.8")

@task
def deploy():
    put("redis-3.2.8.tar.gz",  "/tmp/redis-3.2.8.tar.gz")
    with cd("/tmp"):
        run("tar xzf redis-3.2.8.tar.gz")
        with cd("redis-3.2.8"):
            sudo("make install")

@task
def clean_file():
    with cd("/tmp"):
        sudo("rm -rf redis-3.2.8.tar.gz")
        sudo("rm -rf redis-3.2.8")

@task
def clean_local_file():
    local("rm -rf redis-3.2.8.tar.gz")

@task
def install():
    execute(test)
    execute(deploy)
    execute(clean_file)
    execute(clean_local_file)
