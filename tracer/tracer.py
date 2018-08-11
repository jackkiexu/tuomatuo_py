# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      tracer
   Description :
   Author :         xjk
   date：           8/10/18
-------------------------------------------------
   Change Activity: 8/10/18:
-------------------------------------------------
"""
__author__ = 'xujiankang'

from flask import Flask
app = Flask(__name__)


@app.route('/jack')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()