from fabric.api import run, sudo
from fabric.api import env

env.hosts= ['10.166.224.14', '10.166.224.14']
env.port= 2902
env.user='lmx'

def hostname():
    run('hostname')

def ls(path='.'):
    run('ls {}'.format(path))

def tail(path='/etc/passwd', line=10):
    sudo('tail -n {0} {1}'.format(line, path))
