#!/usr/bin/python
#-*- coding: UTF-8 -*-

import redis
from flask import Flask

app = Flask(__name__)

@app.route('/user/<int:identify>')
def get(identify):
    r = redis.StrictRedis(host='10.166.226.152', port=6379, db=0)
    username = r.get(identify)

    if username is None:
        return "not found", 404
    else:
        return username

if __name__ == '__main__':
    app.run()
