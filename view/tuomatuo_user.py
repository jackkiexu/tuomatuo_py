# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      tuomatuo_user
   Description :
   Author :         xjk
   date：           8/11/18
-------------------------------------------------
   Change Activity: 8/11/18:
-------------------------------------------------
"""
__author__ = 'xujiankang'

from flask import Flask, request
from core import app, db


@app.route('/jack2', methods=['GET', 'POST'])
def jack2():
    print 'request.data', request.data
    print 'request.args', request.args
    print 'request.headers', request.headers
    print 'request.form', request.form
    print 'request.json', request.json

    return 'jack'